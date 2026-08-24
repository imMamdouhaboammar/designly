#!/usr/bin/env python3
"""Test Visual QA floors, slop vetoes, and targeted revision routing."""
from __future__ import annotations
import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "skills/visual-qa/scripts"))
sys.path.insert(0, str(ROOT / "shared/scripts"))
import score_review
from route_packet import MeshRouter

BASE_REVIEW = json.loads((ROOT / "skills/visual-qa/assets/visual-review.template.json").read_text(encoding="utf-8"))


def test_category_floors() -> None:
    failures = 0
    print("Testing category floor isolation from weighted average...")
    cases = [("hierarchy", 80), ("brand_fidelity", 91), ("product_fidelity", 94)]
    for field, score in cases:
        r = copy.deepcopy(BASE_REVIEW)
        r["scores"][field] = score
        if score_review.evaluate(r)["approved"]:
            failures += 1
            print(f"FAIL low {field} should have been rejected")
        else:
            print(f"PASS low {field} rejected by category floor")
    assert failures == 0, f"category floors had {failures} failures"


def test_ai_slop_vetoes() -> None:
    failures = 0
    print("\nTesting AI-slop hard veto thresholds...")
    r1 = copy.deepcopy(BASE_REVIEW)
    r1["slop_findings"].append({"family": "concept", "severity": "critical", "evidence": "Effect stack is the concept"})
    approved1 = score_review.evaluate(r1)["approved"]
    if approved1:
        failures += 1
        print("FAIL critical slop veto")
    else:
        print("PASS critical slop veto")

    r2 = copy.deepcopy(BASE_REVIEW)
    r2["slop_findings"].extend([
        {"family": "composition", "severity": "major", "evidence": "Equal emphasis"},
        {"family": "effects", "severity": "major", "evidence": "Generic effects"},
    ])
    approved2 = score_review.evaluate(r2)["approved"]
    if approved2:
        failures += 1
        print("FAIL two-major slop veto")
    else:
        print("PASS two-major slop veto")
    assert failures == 0, f"ai slop vetoes had {failures} failures"


def test_targeted_revision_routing() -> None:
    failures = 0
    router = MeshRouter()
    print("\nTesting targeted defect-to-specialist revision routing...")
    cases = [
        ("hierarchy", "composition-director"),
        ("brand_fidelity", "brand-intelligence"),
        ("physical_believability", "manipulation-director"),
        ("typography", "typography-director"),
        ("arabic_rtl", "arabic-rtl-director"),
        ("strategy", "creative-strategy"),
        ("concept_originality", "creative-director"),
        ("creative_ideation", "creative-director"),
        ("insight_depth", "insight-mining"),
        ("pattern_saturation", "campaign-canon"),
        ("activation_mechanic", "brand-activation"),
        ("narrative_arc", "visual-storytelling"),
        ("edit_scope", "edit-sanitizer"),
        ("annotation_mapping", "edit-sanitizer"),
        ("collateral_change", "edit-sanitizer"),
        ("prompt_execution", "prompt-compiler"),
        ("video_dramaturgy", "video-director"),
        ("motion_rhythm", "video-director"),
        ("shot_card_continuity", "video-director"),
        ("model_physics", "image-director"),
        ("multi_panel_grid", "image-director"),
        ("character_continuity", "image-director"),
    ]
    for dim, expected in cases:
        routed = router.route_revision({"failing_dimension": dim, "defect_description": "fixture"})
        if routed == expected:
            print(f"PASS defect '{dim}' routed exclusively to {routed}")
        else:
            failures += 1
            print(f"FAIL defect '{dim}' routed to {routed}, expected {expected}")
    assert failures == 0, f"revision routing had {failures} failures"


def main() -> int:
    try:
        test_category_floors()
        test_ai_slop_vetoes()
        test_targeted_revision_routing()
        print("\nRevision Router Test Suite: PASS (0 failures)")
        return 0
    except AssertionError as e:
        print(f"\nRevision Router Test Suite: FAIL ({e})")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
