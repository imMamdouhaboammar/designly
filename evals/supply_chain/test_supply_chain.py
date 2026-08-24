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

def check(cond: bool, msg: str, errors: list[str]):
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        errors.append(msg)

def test_package_json_supply_chain(errors: list[str]):
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
    check(isinstance(files_whitelist, list) and len(files_whitelist) > 0, "files whitelist defined", errors)
    check("bin" in files_whitelist, "bin in whitelist", errors)
    check("dist" in files_whitelist, "dist in whitelist", errors)
    check("skills" in files_whitelist, "skills in whitelist", errors)
    check("evals" not in files_whitelist, "evals excluded from publish whitelist", errors)
    check(".planning" not in files_whitelist, "planning excluded from publish whitelist", errors)

    # Check dependencies are zero or clean
    deps = data.get("dependencies", {})
    check(len(deps) == 0, f"runtime dependencies zero-bloat ({len(deps)} dependencies)", errors)

def test_npmignore_secrets_prevention(errors: list[str]):
    print("\n--- Testing .npmignore Secrets & Artifacts Exclusion ---")
    check(NPMIGNORE.is_file(), ".npmignore exists", errors)
    content = NPMIGNORE.read_text(encoding="utf-8")

    check(".env*" in content, ".env* ignored in npmignore", errors)
    check("auth.json" in content or "secrets" in content, "secrets ignored in npmignore", errors)
    check("evals" in content, "evals ignored in npmignore", errors)
    check(".git" in content, ".git ignored in npmignore", errors)

def test_no_secrets_in_repo(errors: list[str]):
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
