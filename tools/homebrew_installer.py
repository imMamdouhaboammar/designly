#!/usr/bin/env python3
"""
Homebrew Formula Generator, Validator, and Installer Adapter for Designly.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORMULA_PATH = ROOT / "Formula/designly.rb"
DIST_DIR = ROOT / "dist"

def check(cond: bool, msg: str, errors: list[str]):
    print(("PASS: " if cond else "FAIL: ") + msg)
    if not cond:
        errors.append(msg)

def get_current_version() -> str:
    pkg = ROOT / "package.json"
    if pkg.is_file():
        try:
            return json.loads(pkg.read_text(encoding="utf-8")).get("version", "5.0.1")
        except Exception:
            pass
    return "5.0.1"

def generate_release_tarball(version: str | None = None) -> Path:
    if version is None:
        version = get_current_version()
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    tar_path = DIST_DIR / f"designly-{version}.tar.gz"
    
    exclude_prefixes = {".git", "__pycache__", "dist", ".superpowers", ".planning", ".pytest_cache"}
    
    with tarfile.open(tar_path, "w:gz") as tar:
        for p in sorted(ROOT.rglob("*")):
            rel = p.relative_to(ROOT)
            parts = rel.parts
            if any(part in exclude_prefixes or part.startswith(".") and part not in [".skills.json", ".codex-plugin"] for part in parts):
                continue
            tar.add(p, arcname=f"designly-{version}/{rel.as_posix()}", recursive=False)
            
    sha256 = hashlib.sha256(tar_path.read_bytes()).hexdigest()
    print(f"Generated release tarball: {tar_path}")
    print(f"SHA256: {sha256}")
    return tar_path

def validate_formula(errors: list[str]) -> None:
    if not FORMULA_PATH.is_file():
        errors.append("Formula/designly.rb does not exist")
        print("FAIL: Formula file not found")
        return
        
    content = FORMULA_PATH.read_text(encoding="utf-8")
    check("class Designly < Formula" in content, "Formula class name is Designly", errors)
    check("desc " in content, "Formula has description", errors)
    check("homepage " in content, "Formula has homepage", errors)
    check("url " in content, "Formula has url", errors)
    check("sha256 " in content, "Formula has sha256 checksum", errors)
    check("license " in content, "Formula has license", errors)
    check("def install" in content, "Formula has install definition", errors)
    check("test do" in content, "Formula has test block", errors)
    
    # Check with ruby -c if ruby is available
    try:
        res = subprocess.run(["ruby", "-c", str(FORMULA_PATH)], capture_output=True, text=True)
        check(res.returncode == 0, f"Ruby syntax check: {res.stdout.strip() or res.stderr.strip()}", errors)
    except Exception as e:
        print(f"INFO: Ruby not available or failed: {e}")

def main() -> int:
    parser = argparse.ArgumentParser(description="Designly Homebrew Installer & Formula Tool")
    parser.add_argument("--check", action="store_true", help="Validate Homebrew formula syntax & completeness")
    parser.add_argument("--tarball", action="store_true", help="Generate distribution tarball and print SHA256")
    parser.add_argument("--update-sha", help="Update Formula with specific SHA256")
    args = parser.parse_args()

    errors = []
    print("=== Designly Homebrew Formula & Installer Adapter ===\n")

    if args.tarball:
        ver = get_current_version()
        tar_path = generate_release_tarball(ver)
        sha256 = hashlib.sha256(tar_path.read_bytes()).hexdigest()
        content = FORMULA_PATH.read_text(encoding="utf-8")
        updated = re.sub(r'archive/refs/tags/v\d+\.\d+\.\d+\.tar\.gz', f'archive/refs/tags/v{ver}.tar.gz', content)
        updated = re.sub(r'sha256 "[0-9a-fA-F]{64}"', f'sha256 "{sha256}"', updated)
        FORMULA_PATH.write_text(updated, encoding="utf-8")
        print(f"Updated Formula/designly.rb with version v{ver} and SHA256: {sha256}\n")

    validate_formula(errors)

    if errors:
        print(f"\nHomebrew Validation FAILED with {len(errors)} errors.")
        return 1

    print("\nHomebrew Adapter Validation: PASS (0 errors)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
