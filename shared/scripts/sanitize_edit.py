#!/usr/bin/env python3
"""Normalize and fail-close annotation-guided image edits before prompt compilation.

Public seam: sanitize_edit(request: dict) -> dict

The sanitizer does not edit pixels. It converts user/annotation intent into a bounded
EditContract or blocks execution when scope, geometry, source lineage, or mutations
are unsafe/ambiguous.
"""
from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "shared/contracts/edit-contract.schema.json"

GLOBAL_RESTYLE = re.compile(
    r"\b(?:whole|entire|overall|global|everywhere|all)\b.{0,48}\b(?:restyle|style|cinematic|dramatic|luxur(?:y|ious)|mood|lighting|background|composition|color grade|palette)\b",
    re.I,
)
BROAD_CHANGE = re.compile(
    r"\b(?:move|replace|change|redesign|restyle|add|remove)\b.{0,48}\b(?:background|composition|layout|lighting|camera|perspective|palette|color grade)\b",
    re.I,
)
ARABIC_RE = re.compile(r"[\u0600-\u06ff]")
LOCAL_MODES = {"local_edit", "inpaint", "annotation_guided", "copy_correction", "brand_correction", "object_replace"}


def _base_result(request: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(request)
    result.setdefault("forbidden_mutations", [])
    result.setdefault("identity_locks", [])
    result.setdefault("geometry_locks", [])
    result.setdefault("style_locks", [])
    result.setdefault("iteration", 1)
    result.setdefault("exact_copy", None)
    result["mutation_budget"] = "one" if result.get("mode") in LOCAL_MODES else "low"
    result["protected_regions"] = []
    result["acceptance_checks"] = []
    result["requires_arabic_review"] = False
    result["ambiguity"] = {"unresolved": False, "reasons": []}
    result["reasons"] = []
    result["status"] = "reject"
    result["execution_allowed"] = False
    return result


def _fail(result: dict[str, Any], status: str, reason: str) -> dict[str, Any]:
    result["status"] = status
    result["execution_allowed"] = False
    result["reasons"].append(reason)
    if status == "clarify":
        result["ambiguity"]["unresolved"] = True
        result["ambiguity"]["reasons"].append(reason)
    return result


def _normalize_bbox(g: dict[str, Any], space: str, width: int, height: int) -> dict[str, Any] | None:
    try:
        x, y = float(g["x"]), float(g["y"])
        w, h = float(g["width"]), float(g["height"])
    except (KeyError, TypeError, ValueError):
        return None

    if space == "normalized":
        if not all(0 <= v <= 1 for v in (x, y, w, h)):
            return None
        x, y, w, h = x * width, y * height, w * width, h * height

    if w <= 0 or h <= 0:
        return None
    if x < 0 or y < 0 or x + w > width or y + h > height:
        return None

    return {
        "kind": "bbox",
        "x": int(round(x)),
        "y": int(round(y)),
        "width": int(round(w)),
        "height": int(round(h)),
    }


def _normalize_targets(result: dict[str, Any]) -> str | None:
    geometry = result.get("source_geometry") or {}
    try:
        source_w, source_h = int(geometry["width"]), int(geometry["height"])
    except (KeyError, TypeError, ValueError):
        return "source geometry requires positive integer width and height"
    if source_w <= 0 or source_h <= 0:
        return "source geometry requires positive integer width and height"

    space = result.get("annotation_space")
    if space not in {"pixels", "normalized", "semantic", "mask"}:
        return "annotation_space must be pixels, normalized, semantic, or mask"

    targets = result.get("targets")
    if not isinstance(targets, list) or not targets:
        return "at least one explicit edit target is required"

    normalized: list[dict[str, Any]] = []
    for target in targets:
        if not isinstance(target, dict):
            return "each target must be an object"
        confidence = target.get("confidence")
        if not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1:
            return "target confidence must be between 0 and 1"
        semantic_target = str(target.get("semantic_target") or "").strip()
        if not semantic_target:
            return "each target requires a semantic_target"
        g = target.get("geometry") or {}
        kind = g.get("kind")
        normalized_target = copy.deepcopy(target)
        if kind == "bbox":
            bbox = _normalize_bbox(g, space, source_w, source_h)
            if bbox is None:
                return f"target {target.get('target_id', '<unknown>')} has invalid or out-of-bounds bbox"
            normalized_target["geometry"] = bbox
        elif kind == "polygon":
            points = g.get("points")
            if not isinstance(points, list) or len(points) < 3:
                return "polygon target requires at least three points"
        elif kind == "mask_ref":
            if not str(g.get("mask_ref") or "").strip():
                return "mask_ref target requires a non-empty mask reference"
        elif kind == "semantic":
            if space not in {"semantic", "pixels"}:
                return "semantic target is incompatible with the declared annotation space"
        else:
            return "target geometry kind must be bbox, polygon, mask_ref, or semantic"
        normalized.append(normalized_target)

    result["targets"] = normalized
    return None


def _detect_ambiguity(result: dict[str, Any]) -> str | None:
    targets = result["targets"]
    if len(targets) == 1:
        if float(targets[0]["confidence"]) < 0.60:
            return "annotation-to-target mapping confidence is too low to edit safely"
        return None

    ranked = sorted((float(t["confidence"]) for t in targets), reverse=True)
    if ranked[0] < 0.70 or ranked[0] - ranked[1] < 0.15:
        return "annotation maps to multiple plausible targets; choose the intended target before execution"
    return None


def _mutation_conflict(result: dict[str, Any]) -> str | None:
    mutations = result.get("requested_mutations")
    if not isinstance(mutations, list) or not mutations or any(not str(x).strip() for x in mutations):
        return "at least one atomic requested mutation is required"

    text = " ".join(str(x) for x in mutations) + " " + str(result.get("user_instruction", ""))
    if result.get("mode") in LOCAL_MODES:
        if len(mutations) > 2:
            return "bounded edit exceeds local mutation budget; split the request into separate approved edits"
        if GLOBAL_RESTYLE.search(text):
            return "local-edit request conflicts with a global restyle instruction"
        broad_hits = [m for m in mutations if BROAD_CHANGE.search(str(m))]
        if broad_hits and len(mutations) > 1:
            return "local edit mixes target mutation with unrelated scene-level changes"
    return None


def _protect_complement(result: dict[str, Any]) -> None:
    result["protected_regions"] = [
        {
            "region_id": "NON_TARGET_COMPLEMENT",
            "rule": "Treat all source content outside the sanitized target geometry as protected; allow only incidental blending required at the target boundary.",
            "geometry": None,
        }
    ]
    for lock in result.get("identity_locks", []):
        result["protected_regions"].append({"region_id": f"IDENTITY:{lock}", "rule": "Preserve identity, spelling, shape, and proportions unless this exact lock is the target.", "geometry": None})


def sanitize_edit(request: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(request, dict):
        return {
            "status": "reject",
            "execution_allowed": False,
            "reasons": ["edit request must be an object"],
            "ambiguity": {"unresolved": False, "reasons": []},
        }

    result = _base_result(request)

    required_text = ("edit_id", "source_asset_id", "source_checkpoint", "mode")
    missing = [key for key in required_text if not str(result.get(key) or "").strip()]
    if missing:
        return _fail(result, "reject", f"missing required edit fields: {', '.join(missing)}")

    if result["iteration"] < 1 or result["iteration"] > 3:
        return _fail(result, "reject", "edit iteration must be between 1 and 3")

    # Never chain a corrective edit from a failed/intermediate render. Each retry starts
    # from the last approved checkpoint so drift cannot accumulate.
    if result["iteration"] > 1 and result["source_asset_id"] != result["source_checkpoint"]:
        return _fail(result, "reject", "retry source is not the approved checkpoint; restart the edit from the last approved source")

    geometry_error = _normalize_targets(result)
    if geometry_error:
        return _fail(result, "reject", geometry_error)

    ambiguity = _detect_ambiguity(result)
    if ambiguity:
        return _fail(result, "clarify", ambiguity)

    mutation_error = _mutation_conflict(result)
    if mutation_error:
        return _fail(result, "veto", mutation_error)

    exact_copy = result.get("exact_copy")
    if result.get("mode") == "copy_correction":
        if not isinstance(exact_copy, str) or not exact_copy:
            return _fail(result, "reject", "copy correction requires exact_copy; the model must not invent replacement text")
        result["requires_arabic_review"] = bool(ARABIC_RE.search(exact_copy))

    _protect_complement(result)
    result["acceptance_checks"] = [
        "requested target mutation is visible and complete",
        "crop, canvas dimensions, camera perspective, and non-target composition remain materially stable",
        "protected identities and exact copy remain correct",
        "no new objects, text, effects, or restyling appear outside the approved mutation",
        "if collateral drift is material, reject the result and retry from source_checkpoint rather than editing the failed render",
    ]
    result["status"] = "ready"
    result["execution_allowed"] = True
    return result


def main() -> int:
    payload = json.load(sys.stdin)
    result = sanitize_edit(payload)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("status") == "ready" else 2


if __name__ == "__main__":
    raise SystemExit(main())
