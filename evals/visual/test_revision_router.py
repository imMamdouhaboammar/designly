#!/usr/bin/env python3
"""
Test suite for Visual QA independent scoring, category floors, AI-slop hard vetoes, and targeted revision routing.
"""
from __future__ import annotations
import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
QA_SCRIPTS = ROOT / "skills/visual-qa/scripts"
SHARED_SCRIPTS = ROOT / "shared/scripts"

sys.path.insert(0, str(QA_SCRIPTS))
sys.path.insert(0, str(SHARED_SCRIPTS))

import score_review
from route_packet import MeshRouter

BASE_REVIEW = json.loads((ROOT / "skills/visual-qa/assets/visual-review.template.json").read_text(encoding="utf-8"))

def test_category_floors() -> int:
    failures = 0
    print("Testing category floor isolation from weighted average...")
    
    # 1. High average, low hierarchy (80 < floor 85)
    r1 = copy.deepcopy(BASE_REVIEW)
    r1["scores"]["hierarchy"] = 80
    res1 = score_review.evaluate(r1)
    if res1["approved"]:
        failures += 1
        print("FAIL high average with low hierarchy should have been rejected")
    else:
        print("PASS low hierarchy rejected by category floor")

    # 2. High average, low brand fidelity (91 < floor 95)
    r2 = copy.deepcopy(BASE_REVIEW)
    r2["scores"]["brand_fidelity"] = 91
    res2 = score_review.evaluate(r2)
    if res2["approved"]:
        failures += 1
        print("FAIL high average with low brand_fidelity should have been rejected")
    else:
        print("PASS low brand_fidelity rejected by category floor")

    # 3. Low product fidelity (94 < floor 98)
    r3 = copy.deepcopy(BASE_REVIEW)
    r3["scores"]["product_fidelity"] = 94
    res3 = score_review.evaluate(r3)
    if res3["approved"]:
        failures += 1
        print("FAIL low product_fidelity should have been rejected")
    else:
        print("PASS low product_fidelity rejected by category floor")

    return failures

def test_ai_slop_vetoes() -> int:
    failures = 0
    print("\nTesting AI-slop hard veto thresholds...")

    # 1. One critical slop finding blocks
    r1 = copy.deepcopy(BASE_REVIEW)
    r1["slop_findings"].append({"family": "concept", "severity": "critical", "evidence": "Effect stack is the concept"})
    if score_review.evaluate(r1)["approved"]:
        failures += 1
        print("FAIL critical slop did not trigger hard veto")
    else:
        print("PASS 1 critical slop triggers hard veto")

    # 2. Two major slop findings block
    r2 = copy.deepcopy(BASE_REVIEW)
    r2["slop_findings"].extend([
        {"family": "composition", "severity": "major", "evidence": "Equal emphasis across 3 subjects"},
        {"family": "effects", "severity": "major", "evidence": "Generic glowing particles"}
    ])
    if score_review.evaluate(r2)["approved"]:
        failures += 1
        print("FAIL 2 major slop findings did not trigger hard veto")
    else:
        print("PASS 2 major slop findings trigger hard veto")

    # 3. Four minor slop findings block
    r3 = copy.deepcopy(BASE_REVIEW)
    r3["slop_findings"].extend([{"family": str(i), "severity": "minor", "evidence": "localized noise"} for i in range(4)])
    if score_review.evaluate(r3)["approved"]:
        failures += 1
        print("FAIL 4 minor slop findings did not trigger hard veto")
    else:
        print("PASS 4 minor slop findings trigger hard veto")

    return failures

def test_targeted_revision_routing() -> int:
    failures = 0
    router = MeshRouter()
    print("\nTesting targeted defect-to-specialist revision routing...")

    cases = [
        ({"failing_dimension": "hierarchy", "defect_description": "Equal emphasis on 3 subjects"}, "composition-director"),
        ({"failing_dimension": "brand_fidelity", "defect_description": "Logo clearspace violated by headline"}, "brand-intelligence"),
        ({"failing_dimension": "physical_believability", "defect_description": "Contact shadow missing beneath bottle"}, "manipulation-director"),
        ({"failing_dimension": "typography", "defect_description": "Headline awkward line break"}, "typography-director"),
        ({"failing_dimension": "arabic_rtl", "defect_description": "Arabic letter connection broken"}, "arabic-rtl-director"),
        ({"failing_dimension": "strategy", "defect_description": "Message does not match target persona"}, "creative-strategy"),
        ({"failing_dimension": "prompt_execution", "defect_description": "Negative keyword ignored by provider"}, "prompt-compiler")
    ]

    for req, expected_target in cases:
        routed = router.route_revision(req)
        if routed == expected_target:
            print(f"PASS defect '{req['failing_dimension']}' routed exclusively to {routed}")
        else:
            failures += 1
            print(f"FAIL defect '{req['failing_dimension']}' routed to {routed}, expected {expected_target}")

    return failures

def main() -> int:
    total_failures = 0
    total_failures += test_category_floors()
    total_failures += test_ai_slop_vetoes()
    total_failures += test_targeted_revision_routing()

    print(f"\nRevision Router Test Suite: {'PASS' if total_failures == 0 else 'FAIL'} ({total_failures} failures)")
    return 1 if total_failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
