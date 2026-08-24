#!/usr/bin/env python3
"""
Homebrew formula and installer adapter test suite.
Conforms to test-guard rules.
"""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORMULA = ROOT / "Formula/designly.rb"
INSTALLER = ROOT / "tools/homebrew_installer.py"

def check(cond: bool, msg: str, errors: list[str]):
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        errors.append(msg)

def main() -> int:
    errors = []
    print("\n--- Testing Homebrew Formula & Installer Adapter ---")

    check(FORMULA.is_file(), "Formula/designly.rb exists", errors)
    check(INSTALLER.is_file(), "tools/homebrew_installer.py exists", errors)

    # Run installer validation tool
    proc = subprocess.run([sys.executable, str(INSTALLER), "--check"], capture_output=True, text=True)
    check(proc.returncode == 0, "homebrew_installer.py --check exited 0", errors)
    check("Homebrew Adapter Validation: PASS" in proc.stdout, "formula validation passed", errors)

    print(f"\n==========================================")
    print(f"Homebrew Test Suite: {'PASS' if not errors else 'FAIL'} ({len(errors)} errors)")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
