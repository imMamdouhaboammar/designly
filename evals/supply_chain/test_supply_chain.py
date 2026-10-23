#!/usr/bin/env python3
"""
Supply chain security and package sanity test suite for Designly.
Conforms to test-guard & api-security-best-practices.
"""
from __future__ import annotations
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PACKAGE_JSON = ROOT / "package.json"
NPMIGNORE = ROOT / ".npmignore"

FORBIDDEN_FILES = [
    ".env", ".env.local", ".env.production", "auth.json", "secrets.json",
    "credentials.json", "private.key", "id_rsa"
]

ALLOWED_PACKAGE_FILES = frozenset({
    "bin", "dist/index.js", "dist/index.d.ts", "dist/skills-sh",
    "skills", "shared", "skills.json", "README.md", "NOTICE",
})


def validate_package_files(files: object) -> list[str]:
    """Reject missing, extra, broad, or duplicated publish paths."""
    if not isinstance(files, list) or not all(isinstance(item, str) for item in files):
        return ["files must be an array of paths"]
    issues = []
    if len(files) != len(set(files)):
        issues.append("duplicate entries in package files whitelist")
    missing = ALLOWED_PACKAGE_FILES - set(files)
    extra = set(files) - ALLOWED_PACKAGE_FILES
    if missing:
        issues.append(f"missing publish paths: {', '.join(sorted(missing))}")
    if extra:
        issues.append(f"unapproved publish paths: {', '.join(sorted(extra))}")
    return issues

def check(cond: bool, msg: str, errors: list[str] | None = None):
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        if errors is not None:
            errors.append(msg)
        assert cond, msg

def test_package_json_supply_chain(errors: list[str] | None = None):
    print("\n--- Testing package.json Supply Chain Integrity ---")
    check(PACKAGE_JSON.is_file(), "package.json exists", errors)
    data = json.loads(PACKAGE_JSON.read_text(encoding="utf-8"))

    check(data.get("name") == "designly", "package name is valid", errors)
    check("version" in data and re.match(r"^\d+\.\d+\.\d+", data["version"]), "strict semver present", errors)
    
    # Check no suspicious life-cycle scripts (preinstall/postinstall)
    scripts = data.get("scripts", {})
    check("preinstall" not in scripts, "no arbitrary preinstall script", errors)
    check("postinstall" not in scripts, "no arbitrary postinstall script", errors)

    # Check strict file whitelist
    files_whitelist = data.get("files", [])
    whitelist_issues = validate_package_files(files_whitelist)
    check(not whitelist_issues, "granular publish whitelist: " + "; ".join(whitelist_issues), errors)

    # Check dependencies are zero or clean
    deps = data.get("dependencies", {})
    check(len(deps) == 0, f"runtime dependencies zero-bloat ({len(deps)} dependencies)", errors)

def test_npmignore_secrets_prevention(errors: list[str] | None = None):
    print("\n--- Testing .npmignore Secrets & Artifacts Exclusion ---")
    check(NPMIGNORE.is_file(), ".npmignore exists", errors)
    content = NPMIGNORE.read_text(encoding="utf-8")

    check(".env*" in content, ".env* ignored in npmignore", errors)
    check("auth.json" in content or "secrets" in content, "secrets ignored in npmignore", errors)
    check("evals" in content, "evals ignored in npmignore", errors)
    check(".git" in content, ".git ignored in npmignore", errors)

def test_no_secrets_in_repo(errors: list[str] | None = None):
    print("\n--- Auditing Repository for Leaked Credentials / Secrets ---")
    for root_dir, _, files in os.walk(ROOT):
        for f in files:
            for forbidden in FORBIDDEN_FILES:
                if f.lower() == forbidden.lower():
                    check(False, f"forbidden secret file found: {os.path.join(root_dir, f)}", errors)
    check(True, "zero forbidden secret files detected in repository", errors)

def main() -> int:
    errors = []
    test_package_json_supply_chain(errors)
    test_npmignore_secrets_prevention(errors)
    test_no_secrets_in_repo(errors)

    print(f"\n==========================================")
    print(f"Supply Chain Security Test Suite: {'PASS' if not errors else 'FAIL'} ({len(errors)} errors)")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
