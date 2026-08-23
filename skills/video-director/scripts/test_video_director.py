#!/usr/bin/env python3
"""Unit tests for Video Director skill, dramaturgy checks, and reference integrity."""
from __future__ import annotations
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
SKILL_DIR = ROOT / "skills/video-director"
REFERENCES_DIR = SKILL_DIR / "references"

EXPECTED_REFERENCES = [
    "dramaturgy.md",
    "universal-rules.md",
    "seedance.md",
    "seedance-25.md",
    "kling.md",
    "veo.md",
    "role-modes.md",
    "animatic-keyframes.md",
    "race-and-speed.md",
    "patterns-and-genres.md",
    "fixes-and-skeletons.md",
    "camera-lighting-vocabulary.md",
]


def test_references_exist():
    for name in EXPECTED_REFERENCES:
        ref_file = REFERENCES_DIR / name
        assert ref_file.is_file(), f"Missing reference file: {name}"
    print("PASS test_references_exist")


def test_dramaturgy_scene_formula():
    text = (REFERENCES_DIR / "dramaturgy.md").read_text(encoding="utf-8")
    assert "desire + obstacle + geometry + gaze + rhythm" in text
    assert "Rule of Six" in text
    assert "Details Law" in text
    print("PASS test_dramaturgy_scene_formula")


def test_murch_weights():
    text = (REFERENCES_DIR / "dramaturgy.md").read_text(encoding="utf-8")
    assert "51%" in text  # emotion
    assert "23%" in text  # story
    assert "10%" in text  # rhythm
    print("PASS test_murch_weights")


def test_model_references():
    seedance = (REFERENCES_DIR / "seedance-25.md").read_text(encoding="utf-8")
    assert "Seedance 2.5" in seedance
    kling = (REFERENCES_DIR / "kling.md").read_text(encoding="utf-8")
    assert "Kling" in kling
    veo = (REFERENCES_DIR / "veo.md").read_text(encoding="utf-8")
    assert "Veo" in veo
    print("PASS test_model_references")


def main() -> int:
    print("Running Video Director unit tests (/test-guard verified)...")
    try:
        test_references_exist()
        test_dramaturgy_scene_formula()
        test_murch_weights()
        test_model_references()
        print("\nVideo Director unit tests: PASS (0 failures)")
        return 0
    except AssertionError as ex:
        print(f"\nVideo Director unit tests: FAIL - {ex}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
