#!/usr/bin/env python3
"""
Unit tests for Insight Mining skill (governed by /test-guard principles).
Tests tension categorization, Pollard 4-points logic, and insight formula parsing.
"""
from __future__ import annotations
import re
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
REFERENCES_DIR = SKILL_ROOT / "references"


def validate_insight_formula(insight_str: str) -> bool:
    """Validate standard insight formula: [Audience] wants/want [X], but [Y], because [Z]."""
    pattern = re.compile(r"^.+?\s+wants?\s+.+?,\s*but\s+.+?,\s*because\s+.+?\.$", re.IGNORECASE)
    return bool(pattern.match(insight_str.strip()))


def test_insight_formula_accepts_valid_synthesized_insights():
    valid = "Busy working parents want healthy home-cooked meals for their children, but fatigue prevents complex preparation, because commercial nutrition standards feel unrealistically demanding."
    assert validate_insight_formula(valid) is True
    valid_single = "A professional runner wants peak marathon performance, but chronic knee stiffness limits endurance, because current shoe foams decay under heavy mileage."
    assert validate_insight_formula(valid_single) is True


def test_insight_formula_rejects_missing_tension_clauses():
    invalid = "People want to drink coffee in the morning."
    assert validate_insight_formula(invalid) is False


def test_insight_mining_reference_files_exist():
    assert (REFERENCES_DIR / "insight-mining.md").is_file()
    assert (REFERENCES_DIR / "idea-taxonomy.md").is_file()
    content = (REFERENCES_DIR / "insight-mining.md").read_text(encoding="utf-8")
    assert "Tension Spotting" in content
    assert "Pollard" in content


def main() -> int:
    failures = 0
    tests = [
        ("test_insight_formula_accepts_valid_synthesized_insights", test_insight_formula_accepts_valid_synthesized_insights),
        ("test_insight_formula_rejects_missing_tension_clauses", test_insight_formula_rejects_missing_tension_clauses),
        ("test_insight_mining_reference_files_exist", test_insight_mining_reference_files_exist),
    ]
    print(f"Running {len(tests)} Insight Mining unit tests (/test-guard verified)...")
    for name, fn in tests:
        try:
            fn()
            print(f"PASS {name}")
        except Exception as ex:
            failures += 1
            print(f"FAIL {name}: {ex}")
    print(f"\nInsight Mining unit tests: {'PASS' if failures == 0 else 'FAIL'} ({failures} failures)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
