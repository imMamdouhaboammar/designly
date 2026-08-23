#!/usr/bin/env python3
"""Unit tests for Image Director skill, pattern libraries, and model physics."""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SKILL_DIR = ROOT / "skills/image-director"
REFERENCES_DIR = SKILL_DIR / "references"
PATTERNS_DIR = REFERENCES_DIR / "patterns"

EXPECTED_REFERENCES = [
    "models.md",
    "nano-banana.md",
    "gpt-image.md",
    "golden-rules.md",
    "text-rendering.md",
    "editing.md",
    "characters.md",
    "slides.md",
    "storyboards.md",
    "structural.md",
    "dimensional.md",
    "vision-decomposer.md",
    "multi-panel.md",
    "creative-direction.md",
    "prompt-framework.md",
]

EXPECTED_PATTERNS = [
    "ecommerce.md",
    "fashion-editorial.md",
    "food-beverage.md",
    "portrait-cinema.md",
    "poster-illustration.md",
    "character-design.md",
    "ui-social.md",
]


def test_references_exist():
    for name in EXPECTED_REFERENCES:
        ref_file = REFERENCES_DIR / name
        assert ref_file.is_file(), f"Missing reference file: {name}"
    for name in EXPECTED_PATTERNS:
        pat_file = PATTERNS_DIR / name
        assert pat_file.is_file(), f"Missing pattern file: {name}"
    print("PASS test_references_exist")


def test_gpt_image_template_slots():
    gpt_text = (REFERENCES_DIR / "gpt-image.md").read_text(encoding="utf-8")
    assert "Scene:" in gpt_text
    assert "Subject:" in gpt_text
    assert "Important Details:" in gpt_text
    assert "Use Case:" in gpt_text
    assert "Constraints:" in gpt_text
    print("PASS test_gpt_image_template_slots")


def test_nano_banana_physics():
    nb_text = (REFERENCES_DIR / "nano-banana.md").read_text(encoding="utf-8")
    assert "Nano Banana" in nb_text
    assert "image grounding" in nb_text.lower() or "grounding" in nb_text.lower()
    print("PASS test_nano_banana_physics")


def test_multi_panel_grids():
    mp_text = (REFERENCES_DIR / "multi-panel.md").read_text(encoding="utf-8")
    assert "grid" in mp_text.lower()
    assert "panel" in mp_text.lower()
    print("PASS test_multi_panel_grids")


def main() -> int:
    print("Running Image Director unit tests (/test-guard verified)...")
    try:
        test_references_exist()
        test_gpt_image_template_slots()
        test_nano_banana_physics()
        test_multi_panel_grids()
        print("\nImage Director unit tests: PASS (0 failures)")
        return 0
    except AssertionError as ex:
        print(f"\nImage Director unit tests: FAIL - {ex}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
