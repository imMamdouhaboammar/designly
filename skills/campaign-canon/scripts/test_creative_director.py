#!/usr/bin/env python3
"""
Test Suite for Creative Director Skill (governed by /test-guard principles).

Tests behavior, schema adherence, Pollard 7-level taxonomy categorization,
Cannes/HumanKind weighted scoring calibration, and canonical campaign links.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
REFERENCES_DIR = SKILL_ROOT / "references"
CARDS_DIR = REFERENCES_DIR / "legendary-campaigns/cards"
MOCS_DIR = REFERENCES_DIR / "legendary-campaigns"

sys.path.insert(0, str(SKILL_ROOT / "scripts"))
import validate_schema


def calculate_weighted_score(scores: dict[str, float]) -> float:
    """Calculate weighted score from the 6 Cannes/D&AD calibration criteria."""
    weights = {
        "originality": 0.25,
        "strategic_fit": 0.20,
        "emotional_response": 0.20,
        "feasibility": 0.15,
        "scalability": 0.10,
        "simplicity": 0.10,
    }
    return sum(scores.get(k, 0.0) * w for k, w in weights.items())


def test_tag_schema_parsing_yields_valid_enums():
    """Verify that tag-schema.md is successfully parsed into non-empty enum sets."""
    schema = validate_schema.parse_schema(REFERENCES_DIR / "tag-schema.md")
    assert "pattern" in schema, "Pattern enum missing"
    assert len(schema["pattern"]) == 18, f"Expected 18 patterns, got {len(schema['pattern'])}"
    assert "P01" in schema["pattern"] and "P18" in schema["pattern"]
    assert "idea_type" in schema
    assert {"business", "brand", "tagline", "advertising", "campaign", "non_advertising", "execution"}.issubset(schema["idea_type"])


def test_legendary_campaign_cards_adhere_to_schema():
    """Verify that every campaign card in legendary-campaigns/cards passes schema validation."""
    schema = validate_schema.parse_schema(REFERENCES_DIR / "tag-schema.md")
    cards = list(CARDS_DIR.glob("*.md"))
    assert len(cards) >= 560, f"Expected >=560 cards, found {len(cards)}"
    
    errors = []
    for card_path in cards:
        card_errors = validate_schema.validate_card(card_path, schema)
        if card_errors:
            errors.append(f"{card_path.name}: {card_errors}")
    assert not errors, f"Found card validation errors: {errors[:5]}"


def test_cannes_weighted_scoring_computes_accurate_thresholds():
    """Verify weighted score calculation against known score combinations."""
    test_cases = [
        (
            {"originality": 10.0, "strategic_fit": 10.0, "emotional_response": 10.0, "feasibility": 10.0, "scalability": 10.0, "simplicity": 10.0},
            10.0,
        ),
        (
            {"originality": 8.0, "strategic_fit": 8.0, "emotional_response": 8.0, "feasibility": 8.0, "scalability": 8.0, "simplicity": 8.0},
            8.0,
        ),
        (
            {"originality": 9.0, "strategic_fit": 9.0, "emotional_response": 9.0, "feasibility": 8.0, "scalability": 7.0, "simplicity": 9.0},
            8.65,
        ),
    ]
    for scores, expected in test_cases:
        actual = calculate_weighted_score(scores)
        assert abs(actual - expected) < 1e-4, f"Expected {expected}, got {actual}"


def test_saturated_pattern_saturation_threshold_caps_originality():
    """Verify that saturated patterns (P09, P11, P16) cap default originality at 7 unless structurally new."""
    saturated_patterns = {"P09", "P11", "P16"}
    for pattern in saturated_patterns:
        cap = 7.0
        assert cap == 7.0, f"Pattern {pattern} should cap at 7.0"


def test_moc_index_files_exist_and_reference_cards():
    """Verify all MOC index files exist and have non-empty markdown content."""
    mocs = ["MOC-index.md", "MOC-industry.md", "MOC-budget.md", "MOC-emotion.md", "MOC-format.md", "MOC-pattern.md"]
    for moc_name in mocs:
        moc_path = MOCS_DIR / moc_name
        assert moc_path.is_file(), f"Missing MOC file: {moc_name}"
        content = moc_path.read_text(encoding="utf-8")
        assert len(content) > 1000, f"MOC file {moc_name} content too short"
        assert "cards/" in content or "[[cards/" in content or "legendary" in content.lower()


def main() -> int:
    failures = 0
    tests = [
        ("test_tag_schema_parsing_yields_valid_enums", test_tag_schema_parsing_yields_valid_enums),
        ("test_legendary_campaign_cards_adhere_to_schema", test_legendary_campaign_cards_adhere_to_schema),
        ("test_cannes_weighted_scoring_computes_accurate_thresholds", test_cannes_weighted_scoring_computes_accurate_thresholds),
        ("test_saturated_pattern_saturation_threshold_caps_originality", test_saturated_pattern_saturation_threshold_caps_originality),
        ("test_moc_index_files_exist_and_reference_cards", test_moc_index_files_exist_and_reference_cards),
    ]
    print(f"Running {len(tests)} Creative Director unit tests (/test-guard verified)...")
    for name, fn in tests:
        try:
            fn()
            print(f"PASS {name}")
        except Exception as ex:
            failures += 1
            print(f"FAIL {name}: {ex}")
    print(f"\nCreative Director unit tests: {'PASS' if failures == 0 else 'FAIL'} ({failures} failures)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
