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


def test_category_floors() -> int:
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
    return failures


def test_ai_slop_vetoes() -> int:
    failures = 0
    print("\nTesting AI-slop hard veto thresholds...")
    r1 = copy.deepcopy(BASE_REVIEW)
    r1["slop_findings"].append({"family": "concept", "severity": "critical", "evidence": "Effect stack is the concept"})
    failures += int(score_review.evaluate(r1)["approved"])
    print("PASS critical slop veto" if not score_review.evaluate(r1)["approved"] else "FAIL critical slop veto")
    r2 = copy.deepcopy(BASE_REVIEW)
    r2["slop_findings"].extend([
        {"family": "composition", "severity": "major", "evidence": "Equal emphasis"},
        {"family": "effects", "severity": "major", "evidence": "Generic effects"},
    ])
    failures += int(score_review.evaluate(r2)["approved"])
    print("PASS two-major slop veto" if not score_review.evaluate(r2)["approved"] else "FAIL two-major slop veto")
    return failures


def test_targeted_revision_routing() -> int:
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
        ("insight_depth", "creative-director"),
        ("edit_scope", "edit-sanitizer"),
        ("annotation_mapping", "edit-sanitizer"),
        ("collateral_change", "edit-sanitizer"),
        ("prompt_execution", "prompt-compiler"),
    ]
    for dim, expected in cases:
        routed = router.route_revision({"failing_dimension": dim, "defect_description": "fixture"})
        if routed == expected:
            print(f"PASS defect '{dim}' routed exclusively to {routed}")
        else:
            failures += 1
            print(f"FAIL defect '{dim}' routed to {routed}, expected {expected}")
    return failures


def main() -> int:
    failures = test_category_floors() + test_ai_slop_vetoes() + test_targeted_revision_routing()
    print(f"\nRevision Router Test Suite: {'PASS' if failures == 0 else 'FAIL'} ({failures} failures)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
