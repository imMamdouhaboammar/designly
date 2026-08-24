#!/usr/bin/env python3
"""
Unit test suite for Composition Director design_lint rule engine.
Conforms to /test-guard principles.
"""
from __future__ import annotations
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL_ROOT / "scripts"))
import design_lint


def valid_spec() -> dict:
    return {
        "intent": {
            "primary_message": "Precision Swiss Engineering for Urban Cyclists"
        },
        "concept": {
            "visual_proposition": "Titanium bicycle frame suspended in dark studio with focused directional key light revealing raw metallic weld textures"
        },
        "hierarchy": {
            "primary": "The monolithic frame geometry",
            "one_second_read": "Ultra-lightweight aerodynamic architecture"
        },
        "composition": {
            "grid_type": "3x3 golden ratio",
            "alignment_anchors": ["top-left-brand", "center-focal-crankset"],
            "focal_points": 1,
            "negative_space": "Deep charcoal void framing the bottom and right edges",
            "crop_logic": "Bleed on left handlebar, 80px breathing room on right",
            "eye_path": "Enters frame at headtube, follows top tube to seat post, drops to bottom bracket"
        },
        "typography": {
            "class": "poster-ad-layout",
            "exact_copy_locked": True,
            "roles": ["headline", "subhead", "spec-table"]
        },
        "color": {
            "contrast_target": "7:1 against dark background",
            "roles": ["primary-titanium-silver", "accent-signal-orange"],
            "accent_strategy": "Direct attention to internal cable routing exit port"
        },
        "style_families": ["industrial-minimalism"],
        "effects": [
            {
                "name": "directional-specular-highlight",
                "purpose": "Define the hydroformed tube cross-section curvature"
            }
        ]
    }


def test_clean_spec_passes_with_zero_blockers():
    spec = valid_spec()
    findings = design_lint.lint(spec)
    assert not any(f["severity"] in {"critical", "major"} for f in findings)


def test_missing_primary_message_triggers_critical():
    spec = valid_spec()
    spec["intent"]["primary_message"] = ""
    findings = design_lint.lint(spec)
    codes = [f["code"] for f in findings]
    assert "missing-primary-message" in codes


def test_missing_visual_proposition_triggers_critical():
    spec = valid_spec()
    spec["concept"]["visual_proposition"] = ""
    findings = design_lint.lint(spec)
    codes = [f["code"] for f in findings]
    assert "missing-visual-proposition" in codes


def test_adjective_only_concept_triggers_major():
    spec = valid_spec()
    spec["concept"]["visual_proposition"] = "modern luxury sleek stunning"
    findings = design_lint.lint(spec)
    codes = [f["code"] for f in findings]
    assert "adjective-only-concept" in codes


def test_missing_grid_or_anchors_triggers_major():
    spec = valid_spec()
    spec["composition"]["grid_type"] = ""
    spec["composition"]["alignment_anchors"] = []
    findings = design_lint.lint(spec)
    codes = [f["code"] for f in findings]
    assert "missing-grid-logic" in codes
    assert "missing-alignment-anchors" in codes


def test_unpurposed_effects_trigger_critical():
    spec = valid_spec()
    spec["effects"] = [{"name": "neon glow", "purpose": ""}]
    findings = design_lint.lint(spec)
    codes = [f["code"] for f in findings]
    assert "effect-without-job" in codes


def test_slop_effect_stack_triggers_major():
    spec = valid_spec()
    spec["effects"] = [
        {"name": "neon glow", "purpose": "lighting"},
        {"name": "particles sparks", "purpose": "ambience"},
        {"name": "hologram chrome", "purpose": "reflection"},
        {"name": "lens flare smoke", "purpose": "depth"}
    ]
    findings = design_lint.lint(spec)
    codes = [f["code"] for f in findings]
    assert "slop-effect-family-stack" in codes


def main() -> int:
    try:
        test_clean_spec_passes_with_zero_blockers()
        test_missing_primary_message_triggers_critical()
        test_missing_visual_proposition_triggers_critical()
        test_adjective_only_concept_triggers_major()
        test_missing_grid_or_anchors_triggers_major()
        test_unpurposed_effects_trigger_critical()
        test_slop_effect_stack_triggers_major()
        print("PASS Composition Director design_lint test suite")
        return 0
    except AssertionError as e:
        print(f"FAIL Composition Director design_lint: {e}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
