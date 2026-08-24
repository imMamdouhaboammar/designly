#!/usr/bin/env python3
"""
Unit and integration test suite for Designly Model Adapters.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SHARED_SCRIPTS = ROOT / "shared/scripts"
sys.path.insert(0, str(SHARED_SCRIPTS))

from adapters import (
    registry,
    GeminiNanoBananaAdapter,
    MiniMaxDesignAdapter,
    KimiDesignAdapter,
    ClaudeDesignAdapter,
    SeedanceAdapter,
    KlingAdapter,
    GPTImageAdapter,
    VeoAdapter
)

def check(cond: bool, msg: str, errors: list[str] | None = None):
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        if errors is not None:
            errors.append(msg)
        assert cond, msg

def test_gemini_nano_banana(errors: list[str] | None = None):
    print("\n--- Testing Gemini Nano Banana Adapter ---")
    adapter = GeminiNanoBananaAdapter()
    
    # 1. Prose generation without camera numbers
    spec = {
        "subject": "Basalt monolith in stormy sea",
        "lighting": "Dramatic sunset backlight",
        "optics": "50mm f/1.4 shallow depth",
        "aspect_ratio": "1:8",
        "copy": "NORDIC"
    }
    res = adapter.compile(spec)
    check(res.model in ["gemini-nano-banana-pro", "gemini-nano-banana-2"], "gemini model name set", errors)
    check("50mm" not in res.prompt and "f/1.4" not in res.prompt, "camera dump numbers sanitized from prompt", errors)
    check(res.aspect_ratio == "1:8", "extreme aspect ratio 1:8 supported", errors)
    check('"NORDIC"' in res.prompt, "exact copy quoted", errors)
    
    # 2. Multi-subject JSON structure (>= 5 elements)
    spec_multi = {
        "concept": "Complex UI dashboard breakdown",
        "subjects": ["Navigation sidebar", "Analytics chart", "User profile card", "Activity feed", "KPI tile"],
        "aspect_ratio": "16:9"
    }
    res_multi = adapter.compile(spec_multi)
    check(res_multi.prompt.strip().startswith("{"), "multi-subject compiled into spatial JSON", errors)
    data = json.loads(res_multi.prompt)
    check(len(data.get("elements", [])) == 5, "all 5 elements in JSON structure", errors)
    
    # 3. Bounded Edit
    spec_edit = {
        "mode": "edit",
        "target": "bottle cap",
        "mutation": "change matte black to gold",
        "preserve": ["bottle body", "label", "lighting"]
    }
    res_edit = adapter.compile(spec_edit)
    check("Keep bottle body, label, lighting" in res_edit.prompt, "edit preservation intact", errors)
    check("Change only the bottle cap" in res_edit.prompt, "atomic mutation enforced", errors)

def test_minimax_design(errors: list[str] | None = None):
    print("\n--- Testing MiniMax Design Adapter ---")
    adapter = MiniMaxDesignAdapter()
    
    # Video compilation
    spec = {
        "media_type": "video",
        "subject": "Running cheetah across savannah",
        "action": "high-speed sprint with kicking dust",
        "duration": 6,
        "camera_motion": "truck_right",
        "motion_intensity": 9
    }
    res = adapter.compile(spec)
    check(res.model == "minimax-video-01", "minimax video model selected", errors)
    check(res.parameters.get("motion_intensity") == 9, "motion intensity calibrated", errors)
    check(res.negative_prompt is not None and "distorted hands" in res.negative_prompt, "negative prompt present", errors)
    check("truck_right" in res.prompt, "camera directive included", errors)
    
    # Validation error for invalid camera motion
    invalid_spec = {"camera_motion": "teleport_spin"}
    errs = adapter.validate(invalid_spec)
    check(len(errs) > 0, "invalid camera motion rejected", errors)

def test_kimi_design(errors: list[str] | None = None):
    print("\n--- Testing Kimi Design Adapter ---")
    adapter = KimiDesignAdapter()
    
    spec = {
        "concept": "Fintech Mobile App Dashboard",
        "colors": ["#000000", "#FFFFFF", "#10B981"],
        "copy": "BALANCE: $42,500.00",
        "layout_zones": {
            "zone_top": "Account selector and notification icon",
            "zone_hero": "Large balance readout with percentage delta",
            "zone_body": "Transaction history card list",
            "zone_footer": "Bottom navigation tab bar"
        }
    }
    res = adapter.compile(spec)
    check("=== KIMI MULTIMODAL DESIGN SYSTEM SPECIFICATION ===" in res.prompt, "kimi header present", errors)
    check("ZONE_TOP:" in res.prompt and "ZONE_HERO:" in res.prompt, "layout coordinate zones present", errors)
    check("#10B981" in res.prompt, "design token palette present", errors)
    check('"BALANCE: $42,500.00"' in res.prompt, "exact copy lock present", errors)

def test_claude_design(errors: list[str] | None = None):
    print("\n--- Testing Claude Design Adapter ---")
    adapter = ClaudeDesignAdapter()
    
    # SVG Vector specification
    spec_svg = {
        "subject": "Isometric Cloud Architecture Diagram",
        "output_format": "svg",
        "interactive": True,
        "copy": "99.99% UPTIME"
    }
    res_svg = adapter.compile(spec_svg)
    check("### Claude Design System & Artifact Contract" in res_svg.prompt, "claude header present", errors)
    check("Anti-Slop Finish Gate" in res_svg.prompt, "anti-slop finish gate present", errors)
    check("viewBox=" in res_svg.prompt, "SVG viewBox specification present", errors)
    check("Interactive State Machine Matrix" in res_svg.prompt, "interactive state matrix present", errors)
    check('"99.99% UPTIME"' in res_svg.prompt, "verbatim copy lock present", errors)

def test_seedance(errors: list[str] | None = None):
    print("\n--- Testing Seedance Adapter ---")
    adapter = SeedanceAdapter()
    
    spec = {
        "dramaturgy": "Detective searching abandoned warehouse under moonlight",
        "duration": 30,
        "references": ["Detective Marcus (Ref A)", "Warehouse Interior (Ref B)"],
        "shots": [
            {"start": "00:00", "end": "00:10", "camera": "Slow wide tracking", "action": "Enters through rusty door"},
            {"start": "00:10", "end": "00:20", "camera": "Over-the-shoulder", "action": "Flashlight beam cuts through dust", "speaker": "Marcus", "dialogue": "I know you're in here."},
            {"start": "00:20", "end": "00:30", "camera": "Close-up on eyes", "action": "Spots fresh footprints"}
        ]
    }
    res = adapter.compile(spec)
    check(res.model == "seedance-2.5-pro", "seedance model selected", errors)
    check("=== SEEDANCE 2.5 DRAMATURGY VIDEO DIRECTING SPEC" in res.prompt, "seedance header present", errors)
    check("[Character ID-01]" in res.prompt, "reference kit indexed", errors)
    check('{ Marcus: "I know you\'re in here." }' in res.prompt, "dialogue lip-sync markers formatted", errors)
    check("[Shot 3: 00:20-00:30" in res.prompt, "30s multi-shot timeline present", errors)

def test_kling(errors: list[str] | None = None):
    print("\n--- Testing Kling Adapter ---")
    adapter = KlingAdapter()
    
    spec = {
        "characters": ["Cyberpunk pilot in flight jacket", "Android co-pilot with blue optical sensor"],
        "subject": "Starfighter cockpit during planetary re-entry",
        "action": "Vigorous turbulence shaking cockpit as pilot grips flight stick",
        "speaker": "Character A",
        "dialogue": "Shields holding at thirty percent!",
        "camera_matrix": {"horizontal": -2, "vertical": 1, "zoom": 5, "tilt": -3, "pan": 0, "roll": 2},
        "motion_brushes": [
            {"target": "Pilot hands", "trajectory": "rapid vibration", "velocity": "+8"}
        ]
    }
    res = adapter.compile(spec)
    check(res.model == "kling-3.0-pro", "kling model selected", errors)
    check("[Character A:" in res.prompt and "[Character B:" in res.prompt, "multi-character binding present", errors)
    check('Native Lip-Sync Dialogue: [Character A] "Shields holding at thirty percent!"' in res.prompt, "dialogue present", errors)
    check("Motion Brush" in res.prompt or "MOTION BRUSH" in res.prompt, "motion brush vectors present", errors)
    check(res.negative_prompt is not None and "distorted limbs" in res.negative_prompt, "negative prompt present", errors)

def test_registry(errors: list[str] | None = None):
    print("\n--- Testing Adapter Registry ---")
    all_adapters = registry.list_all()
    check(len(all_adapters) >= 8, f"at least 8 adapters registered (found {len(all_adapters)})", errors)
    
    # Test aliases
    check(registry.get("nano-banana") is not None, "alias nano-banana resolves", errors)
    check(registry.get("hailuo") is not None, "alias hailuo resolves", errors)
    check(registry.get("kimi") is not None, "alias kimi resolves", errors)
    check(registry.get("claude") is not None, "alias claude resolves", errors)
    check(registry.get("kling") is not None, "alias kling resolves", errors)
    check(registry.get("seedance") is not None, "alias seedance resolves", errors)

def main() -> int:
    errors = []
    test_gemini_nano_banana(errors)
    test_minimax_design(errors)
    test_kimi_design(errors)
    test_claude_design(errors)
    test_seedance(errors)
    test_kling(errors)
    test_registry(errors)
    
    print(f"\n==========================================")
    print(f"Model Adapters Test Suite: {'PASS' if not errors else 'FAIL'} ({len(errors)} errors)")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
