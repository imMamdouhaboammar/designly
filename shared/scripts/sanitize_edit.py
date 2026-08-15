#!/usr/bin/env python3
"""Normalize and fail-close annotation-guided image edits before prompt compilation.

Public seam: sanitize_edit(request: dict) -> dict
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

CONTRACT_INPUT_FIELDS = {
    "edit_id", "source_asset_id", "source_checkpoint", "mode", "source_geometry",
    "annotation_space", "targets", "requested_mutations", "forbidden_mutations",
    "identity_locks", "geometry_locks", "style_locks", "exact_copy", "iteration",
}
GLOBAL_RESTYLE = re.compile(
    r"\b(?:whole|entire|overall|global|everywhere|all)\b.{0,48}\b(?:restyle|style|cinematic|dramatic|luxur(?:y|ious)|premium|mood|lighting|background|composition|color grade|palette)\b",
    re.I,
)
VAGUE_STYLE = re.compile(r"\b(?:premium|cinematic|dramatic|luxur(?:y|ious)|beautiful|better|nicer|more polished)\b", re.I)
BOUNDING_LANGUAGE = re.compile(r"\b(?:only|just|selected|this area|this region|this object)\b", re.I)
BROAD_CHANGE = re.compile(
    r"\b(?:move|replace|change|redesign|restyle|add|remove)\b.{0,48}\b(?:background|composition|layout|lighting|camera|perspective|palette|color grade)\b",
    re.I,
)
ARABIC_RE = re.compile(r"[\u0600-\u06ff]")
LOCAL_MODES = {"local_edit", "inpaint", "annotation_guided", "copy_correction", "brand_correction", "object_replace"}


def _base_result(request: dict[str, Any]) -> dict[str, Any]:
    result = {key: copy.deepcopy(request[key]) for key in CONTRACT_INPUT_FIELDS if key in request}
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
        x, y, w, h = float(g["x"]), float(g["y"]), float(g["width"]), float(g["height"])
    except (KeyError, TypeError, ValueError):
        return None
    if space == "normalized":
        if not all(0 <= v <= 1 for v in (x, y, w, h)):
            return None
        x, y, w, h = x * width, y * height, w * width, h * height
    if w <= 0 or h <= 0 or x < 0 or y < 0 or x + w > width or y + h > height:
        return None
    return {"kind": "bbox", "x": int(round(x)), "y": int(round(y)), "width": int(round(w)), "height": int(round(h))}


def _normalize_polygon(points: Any, space: str, width: int, height: int) -> list[list[int]] | None:
    if not isinstance(points, list) or len(points) < 3:
        return None
    converted: list[list[int]] = []
    for point in points:
        if not isinstance(point, list) or len(point) != 2:
            return None
        try:
            x, y = float(point[0]), float(point[1])
        except (TypeError, ValueError):
            return None
        if space == "normalized":
            if not (0 <= x <= 1 and 0 <= y <= 1):
                return None
            x, y = x * width, y * height
        if x < 0 or y < 0 or x > width or y > height:
            return None
        converted.append([int(round(x)), int(round(y))])
    # Reject degenerate polygons by requiring a non-zero shoelace area.
    area2 = 0
    for idx, (x1, y1) in enumerate(converted):
        x2, y2 = converted[(idx + 1) % len(converted)]
        area2 += x1 * y2 - x2 * y1
    if area2 == 0:
        return None
    return converted


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
        target_id = str(target.get("target_id") or "").strip()
        if not target_id or not semantic_target:
            return "each target requires target_id and semantic_target"
        g = target.get("geometry") or {}
        kind = g.get("kind")
        normalized_target = {"target_id": target_id, "semantic_target": semantic_target, "confidence": float(confidence), "geometry": {}}
        if kind == "bbox":
            bbox = _normalize_bbox(g, space, source_w, source_h)
            if bbox is None:
                return f"target {target_id} has invalid or out-of-bounds bbox"
            normalized_target["geometry"] = bbox
        elif kind == "polygon":
            polygon = _normalize_polygon(g.get("points"), space, source_w, source_h)
            if polygon is None:
                return f"target {target_id} has invalid, degenerate, or out-of-bounds polygon"
            normalized_target["geometry"] = {"kind": "polygon", "points": polygon}
        elif kind == "mask_ref":
            mask_ref = str(g.get("mask_ref") or "").strip()
            if not mask_ref:
                return "mask_ref target requires a non-empty mask reference"
            normalized_target["geometry"] = {"kind": "mask_ref", "mask_ref": mask_ref}
        elif kind == "semantic":
            if space not in {"semantic", "pixels"}:
                return "semantic target is incompatible with the declared annotation space"
            normalized_target["geometry"] = {"kind": "semantic"}
        else:
            return "target geometry kind must be bbox, polygon, mask_ref, or semantic"
        normalized.append(normalized_target)
    result["targets"] = normalized
    return None


def _resolve_target(result: dict[str, Any]) -> str | None:
    targets = result["targets"]
    if len(targets) == 1:
        if float(targets[0]["confidence"]) < 0.60:
            return "annotation-to-target mapping confidence is too low to edit safely"
        return None
    ranked = sorted(targets, key=lambda t: float(t["confidence"]), reverse=True)
    top, second = float(ranked[0]["confidence"]), float(ranked[1]["confidence"])
    if top < 0.70 or top - second < 0.15:
        return "annotation maps to multiple plausible targets; choose the intended target before execution"
    result["targets"] = [ranked[0]]
    return None


def _mutation_conflict(result: dict[str, Any], raw_instruction: str) -> tuple[str, str] | None:
    mutations = result.get("requested_mutations")
    if not isinstance(mutations, list) or not mutations or any(not str(x).strip() for x in mutations):
        return "reject", "at least one atomic requested mutation is required"
    mutation_text = " ".join(str(x) for x in mutations)
    full_text = f"{mutation_text} {raw_instruction}"
    if result.get("mode") in LOCAL_MODES:
        if len(mutations) != 1:
            return "veto", "bounded local edits require exactly one atomic requested mutation; split additional changes into separate approved edits"
        if GLOBAL_RESTYLE.search(full_text):
            return "veto", "local-edit request conflicts with a global restyle instruction"
        if BROAD_CHANGE.search(mutation_text) and not any(str(t["semantic_target"]).lower() in mutation_text.lower() for t in result["targets"]):
            return "clarify", "scene-level change language is not clearly bound to the sanitized target"
        if BOUNDING_LANGUAGE.search(raw_instruction) and VAGUE_STYLE.search(full_text):
            concrete_terms = re.compile(r"\b(?:color|finish|texture|roughness|gloss|metal|silver|black|white|red|blue|size|shape|remove|replace|text|copy)\b", re.I)
            if not concrete_terms.search(mutation_text):
                return "clarify", "bounded edit uses vague style language; specify the visible target property to change"
    return None


def _protect_complement(result: dict[str, Any]) -> None:
    result["protected_regions"] = [{
        "region_id": "NON_TARGET_COMPLEMENT",
        "rule": "Treat all source content outside the sanitized target geometry as protected; allow only incidental blending required at the target boundary.",
        "geometry": None,
    }]
    for lock in result.get("identity_locks", []):
        result["protected_regions"].append({
            "region_id": f"IDENTITY:{lock}",
            "rule": "Preserve identity, spelling, shape, and proportions unless this exact lock is the target.",
            "geometry": None,
        })


def sanitize_edit(request: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(request, dict):
        return {"status": "reject", "execution_allowed": False, "reasons": ["edit request must be an object"], "ambiguity": {"unresolved": False, "reasons": []}}

    raw_instruction = str(request.get("user_instruction") or "")
    result = _base_result(request)
    required_text = ("edit_id", "source_asset_id", "source_checkpoint", "mode")
    missing = [key for key in required_text if not str(result.get(key) or "").strip()]
    if missing:
        return _fail(result, "reject", f"missing required edit fields: {', '.join(missing)}")
    if result["iteration"] < 1 or result["iteration"] > 3:
        return _fail(result, "reject", "edit iteration must be between 1 and 3")
    # Every bounded edit executes from an approved checkpoint. This is enforced on the
    # first attempt too, not just on retries, so unapproved intermediate renders cannot
    # enter the edit chain.
    if result["source_asset_id"] != result["source_checkpoint"]:
        return _fail(result, "reject", "edit source is not the approved checkpoint; restart from the last approved source")

    geometry_error = _normalize_targets(result)
    if geometry_error:
        return _fail(result, "reject", geometry_error)
    ambiguity = _resolve_target(result)
    if ambiguity:
        return _fail(result, "clarify", ambiguity)
    conflict = _mutation_conflict(result, raw_instruction)
    if conflict:
        status, reason = conflict
        return _fail(result, status, reason)

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
