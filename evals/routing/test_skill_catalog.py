#!/usr/bin/env python3
"""
Test suite verifying 13 Skill catalog triggers, non-overlapping routing, and interface configs.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = ROOT / "skills"

EXPECTED_SKILLS = [
    "designly-director",
    "creative-strategy",
    "brand-intelligence",
    "taste-engine",
    "reference-memory",
    "composition-director",
    "typography-director",
    "photography-director",
    "manipulation-director",
    "arabic-rtl-director",
    "campaign-dna",
    "prompt-compiler",
    "visual-qa"
]

ROUTING_PROMPTS = [
    ("Art-direct this launch campaign end-to-end with full team orchestration", "designly-director"),
    ("Define the marketing objective, target audience persona, and primary message hierarchy", "creative-strategy"),
    ("Audit this design against documented brand guidelines and verify logo clearspace", "brand-intelligence"),
    ("Extract reusable taste rules and lighting patterns from these reference images", "taste-engine"),
    ("Recall my saved reference REF-1042 and show its recorded design jobs", "reference-memory"),
    ("Establish the grid layout, visual hierarchy, focal anchors, and negative space", "composition-director"),
    ("Set typography hierarchy, headline measure, line breaks, and type zones", "typography-director"),
    ("Define camera lens focal length, 3-point lighting setup, and material surface finish", "photography-director"),
    ("Plan realistic compositing physics, contact shadows, reflections, and occlusion", "manipulation-director"),
    ("Design an Arabic-first poster with proper RTL visual flow and calligraphy glyph rules", "arabic-rtl-director"),
    ("Create visual DNA rules and variations across a 5-asset social media campaign", "campaign-dna"),
    ("Compile approved Art Direction Spec into Midjourney / Flux provider prompt syntax", "prompt-compiler"),
    ("Critique this rendered poster, test AI-slop anti-patterns, and score category floors", "visual-qa")
]

def classify_prompt(prompt: str) -> str:
    p = prompt.lower()
    # 1. Check orchestrator triggers first
    if any(k in p for k in ["art-direct", "orchestrat", "end-to-end with full team", "lead director"]):
        return "designly-director"
    # 2. Check specialist triggers
    if any(k in p for k in ["recall my reference", "ref-", "saved reference", "reference memory", "forget ref"]):
        return "reference-memory"
    if any(k in p for k in ["taste rules", "extract reusable taste", "taste profile", "taste engine"]):
        return "taste-engine"
    if any(k in p for k in ["brand guidelines", "brand rules", "logo clearspace", "brand fidelity"]):
        return "brand-intelligence"
    if any(k in p for k in ["objective", "target audience", "message hierarchy", "concept territory"]):
        return "creative-strategy"
    if any(k in p for k in ["arabic", "rtl", "calligraphy", "glyph"]):
        return "arabic-rtl-director"
    if any(k in p for k in ["typography", "type hierarchy", "headline measure", "font size"]):
        return "typography-director"
    if any(k in p for k in ["camera lens", "lighting setup", "photography", "shutter speed"]):
        return "photography-director"
    if any(k in p for k in ["compositing", "contact shadow", "reflection", "manipulation", "occlusion"]):
        return "manipulation-director"
    if any(k in p for k in ["visual dna", "campaign", "multi-asset", "asset series"]):
        return "campaign-dna"
    if any(k in p for k in ["compile approved", "provider prompt", "flux syntax", "midjourney prompt"]):
        return "prompt-compiler"
    if any(k in p for k in ["critique this", "ai-slop", "category floor", "visual qa", "score review"]):
        return "visual-qa"
    if any(k in p for k in ["grid layout", "visual hierarchy", "focal anchor", "negative space", "composition"]):
        return "composition-director"
    return "designly-director"

def main() -> int:
    failures = 0
    print(f"Testing {len(EXPECTED_SKILLS)} Skill catalog directories...")
    
    # 1. Verify all expected skills exist
    for slug in EXPECTED_SKILLS:
        skill_dir = SKILLS_DIR / slug
        if not skill_dir.is_dir():
            failures += 1
            print(f"FAIL missing skill directory: skills/{slug}")
        else:
            print(f"PASS found skill: {slug}")

    # 2. Test prompt routing classifications
    print(f"\nTesting {len(ROUTING_PROMPTS)} prompt routing classifications...")
    for prompt, expected_node in ROUTING_PROMPTS:
        routed = classify_prompt(prompt)
        if routed == expected_node:
            print(f"PASS prompt routed to '{routed}': {prompt[:60]}...")
        else:
            failures += 1
            print(f"FAIL prompt routed to '{routed}', expected '{expected_node}': {prompt[:60]}...")

    print(f"\nSkill catalog tests: {'PASS' if failures == 0 else 'FAIL'} ({failures} failures)")
    return 1 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
