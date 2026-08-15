#!/usr/bin/env python3
"""Behavioral regression tests for annotation-guided and local image edits."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "shared/scripts"))

from sanitize_edit import sanitize_edit  # noqa: E402


def base_request() -> dict:
    return {
        "edit_id": "EDT-001",
        "source_asset_id": "approved-render-07",
        "source_checkpoint": "approved-render-07",
        "mode": "local_edit",
        "source_geometry": {"width": 1200, "height": 1500},
        "annotation_space": "pixels",
        "targets": [
            {
                "target_id": "TGT-001",
                "semantic_target": "bottle cap",
                "geometry": {"kind": "bbox", "x": 470, "y": 245, "width": 180, "height": 120},
                "confidence": 0.97,
            }
        ],
        "requested_mutations": ["change bottle cap finish from matte black to brushed silver"],
        "forbidden_mutations": ["do not alter bottle silhouette", "do not alter label or logo"],
        "identity_locks": ["bottle label", "brand logo"],
        "geometry_locks": ["canvas dimensions", "crop", "camera perspective"],
        "style_locks": ["background", "lighting direction", "color grade"],
        "user_instruction": "Change only the bottle cap to brushed silver",
        "iteration": 1,
    }


def expect(name: str, condition: bool, detail: object = None) -> int:
    if condition:
        print(f"PASS {name}")
        return 0
    print(f"FAIL {name}: {detail!r}")
    return 1


def main() -> int:
    failures = 0

    result = sanitize_edit(base_request())
    failures += expect("bounded-local-edit-approved", result["status"] == "ready", result)
    failures += expect("approved-source-retained", result["source_checkpoint"] == "approved-render-07", result)
    failures += expect("mutation-budget-is-one", result["mutation_budget"] == "one", result)
    failures += expect("protected-complement-created", bool(result["protected_regions"]), result)

    conflict = base_request()
    conflict["user_instruction"] = "Change only the cap, and make the whole image more cinematic, dramatic and luxurious"
    conflict["requested_mutations"].append("restyle the whole image with cinematic dramatic lighting")
    result = sanitize_edit(conflict)
    failures += expect("global-restyle-conflict-blocked", result["status"] == "veto", result)
    failures += expect("global-restyle-never-executed", not result.get("execution_allowed", True), result)

    ambiguous = base_request()
    ambiguous["targets"] = [
        {"target_id": "TGT-A", "semantic_target": "left cap-like object", "geometry": {"kind": "bbox", "x": 100, "y": 100, "width": 80, "height": 80}, "confidence": 0.55},
        {"target_id": "TGT-B", "semantic_target": "right cap-like object", "geometry": {"kind": "bbox", "x": 900, "y": 100, "width": 80, "height": 80}, "confidence": 0.54},
    ]
    result = sanitize_edit(ambiguous)
    failures += expect("ambiguous-annotation-asks-clarification", result["status"] == "clarify", result)

    outside = base_request()
    outside["targets"][0]["geometry"] = {"kind": "bbox", "x": 1180, "y": 1490, "width": 100, "height": 80}
    result = sanitize_edit(outside)
    failures += expect("out-of-bounds-annotation-rejected", result["status"] == "reject", result)

    zero = base_request()
    zero["targets"][0]["geometry"] = {"kind": "bbox", "x": 400, "y": 200, "width": 0, "height": 80}
    result = sanitize_edit(zero)
    failures += expect("zero-area-target-rejected", result["status"] == "reject", result)

    copy_fix = base_request()
    copy_fix["mode"] = "copy_correction"
    copy_fix["exact_copy"] = "خصم ٢٥٪ اليوم فقط"
    copy_fix["requested_mutations"] = ["replace the selected Arabic offer text with the exact supplied copy"]
    result = sanitize_edit(copy_fix)
    failures += expect("arabic-copy-routed-for-glyph-check", result.get("requires_arabic_review") is True, result)
    failures += expect("exact-copy-locked", result.get("exact_copy") == "خصم ٢٥٪ اليوم فقط", result)

    chained = base_request()
    chained["iteration"] = 2
    chained["source_asset_id"] = "failed-edit-01"
    chained["source_checkpoint"] = "approved-render-07"
    result = sanitize_edit(chained)
    failures += expect("failed-output-cannot-be-next-source", result["status"] == "reject", result)

    too_many = base_request()
    too_many["requested_mutations"] = [
        "change cap finish",
        "move product to center",
        "change background",
        "add dramatic rim light",
    ]
    result = sanitize_edit(too_many)
    failures += expect("local-edit-mutation-budget-enforced", result["status"] == "veto", result)

    normalized = base_request()
    normalized["annotation_space"] = "normalized"
    normalized["targets"][0]["geometry"] = {"kind": "bbox", "x": 0.4, "y": 0.2, "width": 0.2, "height": 0.1}
    result = sanitize_edit(normalized)
    failures += expect("normalized-coordinates-supported", result["status"] == "ready", result)
    failures += expect("normalized-converted-to-pixels", result["targets"][0]["geometry"]["x"] == 480, result)

    print(f"\nEdit sanitizer tests: {'PASS' if failures == 0 else 'FAIL'} ({failures} failures)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
