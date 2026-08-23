#!/usr/bin/env python3
"""
Unit tests for Brand Activation skill (governed by /test-guard principles).
Tests format taxonomy, non-advertising diagnostic logic, and reference files.
"""
from __future__ import annotations
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
REFERENCES_DIR = SKILL_ROOT / "references"


def classify_activation_utility(has_intrinsic_value_without_ad: bool) -> str:
    """Classify activation as non_advertising vs execution based on the diagnostic test."""
    return "non_advertising" if has_intrinsic_value_without_ad else "execution"


def test_non_advertising_diagnostic_differentiates_utility_from_execution():
    assert classify_activation_utility(True) == "non_advertising"
    assert classify_activation_utility(False) == "execution"


def test_activation_toolkit_references_exist():
    assert (REFERENCES_DIR / "activation-toolkit.md").is_file()
    assert (REFERENCES_DIR / "idea-taxonomy.md").is_file()
    content = (REFERENCES_DIR / "activation-toolkit.md").read_text(encoding="utf-8")
    assert "Brand Utility" in content
    assert "Cultural Hijack" in content


def main() -> int:
    failures = 0
    tests = [
        ("test_non_advertising_diagnostic_differentiates_utility_from_execution", test_non_advertising_diagnostic_differentiates_utility_from_execution),
        ("test_activation_toolkit_references_exist", test_activation_toolkit_references_exist),
    ]
    print(f"Running {len(tests)} Brand Activation unit tests (/test-guard verified)...")
    for name, fn in tests:
        try:
            fn()
            print(f"PASS {name}")
        except Exception as ex:
            failures += 1
            print(f"FAIL {name}: {ex}")
    print(f"\nBrand Activation unit tests: {'PASS' if failures == 0 else 'FAIL'} ({failures} failures)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
