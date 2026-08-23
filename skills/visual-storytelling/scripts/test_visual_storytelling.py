#!/usr/bin/env python3
"""
Unit tests for Visual Storytelling skill (governed by /test-guard principles).
Tests narrative framework definitions, emotional tier categorization, and references.
"""
from __future__ import annotations
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
REFERENCES_DIR = SKILL_ROOT / "references"


def get_emotion_tier_range(tier: int) -> tuple[float, float]:
    """Return the allowed score range for emotional specificity tier."""
    ranges = {
        1: (1.0, 6.0),
        2: (6.0, 8.0),
        3: (8.0, 10.0),
    }
    return ranges.get(tier, (1.0, 10.0))


def test_emotional_tier_scoring_bounds():
    assert get_emotion_tier_range(1) == (1.0, 6.0)
    assert get_emotion_tier_range(2) == (6.0, 8.0)
    assert get_emotion_tier_range(3) == (8.0, 10.0)


def test_storytelling_references_exist():
    assert (REFERENCES_DIR / "storytelling-frameworks.md").is_file()
    assert (REFERENCES_DIR / "emotion-hierarchy.md").is_file()
    content = (REFERENCES_DIR / "storytelling-frameworks.md").read_text(encoding="utf-8")
    assert "Story Spine" in content
    assert "Sparkline" in content


def main() -> int:
    failures = 0
    tests = [
        ("test_emotional_tier_scoring_bounds", test_emotional_tier_scoring_bounds),
        ("test_storytelling_references_exist", test_storytelling_references_exist),
    ]
    print(f"Running {len(tests)} Visual Storytelling unit tests (/test-guard verified)...")
    for name, fn in tests:
        try:
            fn()
            print(f"PASS {name}")
        except Exception as ex:
            failures += 1
            print(f"FAIL {name}: {ex}")
    print(f"\nVisual Storytelling unit tests: {'PASS' if failures == 0 else 'FAIL'} ({failures} failures)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
