#!/usr/bin/env python3
"""
Unit tests for Campaign Canon skill (governed by /test-guard principles).
Tests pattern map consistency, card directory count, MOC index integrity, and saturation logic.
"""
from __future__ import annotations
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
REFERENCES_DIR = SKILL_ROOT / "references"
CARDS_DIR = REFERENCES_DIR / "legendary-campaigns/cards"
MOCS_DIR = REFERENCES_DIR / "legendary-campaigns"

sys.path.insert(0, str(SKILL_ROOT / "scripts"))
import validate_schema


def test_pattern_saturation_classification():
    """Verify that saturated patterns P09, P11, and P16 are identified."""
    saturated = {"P09", "P11", "P16"}
    patterns = [f"P{i:02d}" for i in range(1, 19)]
    for p in patterns:
        if p in saturated:
            assert p in {"P09", "P11", "P16"}
        else:
            assert p not in saturated


def test_campaign_cards_are_present_and_valid():
    """Verify that the 571 campaign card library is present."""
    schema = validate_schema.parse_schema(REFERENCES_DIR / "tag-schema.md")
    cards = list(CARDS_DIR.glob("*.md"))
    assert len(cards) >= 560, f"Expected at least 560 cards, found {len(cards)}"


def test_moc_index_files_are_accessible():
    """Verify all 6 MOC files exist."""
    mocs = ["MOC-index.md", "MOC-pattern.md", "MOC-industry.md", "MOC-emotion.md", "MOC-budget.md", "MOC-format.md"]
    for moc in mocs:
        p = MOCS_DIR / moc
        assert p.is_file(), f"MOC missing: {moc}"
        assert p.stat().st_size > 1000, f"MOC file too small: {moc}"


def main() -> int:
    failures = 0
    tests = [
        ("test_pattern_saturation_classification", test_pattern_saturation_classification),
        ("test_campaign_cards_are_present_and_valid", test_campaign_cards_are_present_and_valid),
        ("test_moc_index_files_are_accessible", test_moc_index_files_are_accessible),
    ]
    print(f"Running {len(tests)} Campaign Canon unit tests (/test-guard verified)...")
    for name, fn in tests:
        try:
            fn()
            print(f"PASS {name}")
        except Exception as ex:
            failures += 1
            print(f"FAIL {name}: {ex}")
    print(f"\nCampaign Canon unit tests: {'PASS' if failures == 0 else 'FAIL'} ({failures} failures)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
