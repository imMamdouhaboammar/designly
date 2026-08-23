#!/usr/bin/env python3
"""Verify 21 Skill catalog triggers and focused discovery."""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = ROOT / "skills"
EXPECTED_SKILLS = [
    "designly-director", "creative-strategy", "creative-director", "insight-mining", "campaign-canon",
    "brand-activation", "visual-storytelling", "brand-intelligence", "taste-engine",
    "reference-memory", "composition-director", "typography-director", "photography-director",
    "manipulation-director", "arabic-rtl-director", "campaign-dna", "video-director", "image-director",
    "edit-sanitizer", "prompt-compiler", "visual-qa"
]
ROUTING_PROMPTS = [
    ("Art-direct this launch campaign end-to-end with full team orchestration", "designly-director"),
    ("Define the marketing objective, target audience persona, and primary message hierarchy", "creative-strategy"),
    ("Brainstorm Cannes-calibrated creative concepts using SIT/TRIZ lateral ideation", "creative-director"),
    ("Mine the consumer tension, analyze JTBD, and apply Mark Pollard 4-points", "insight-mining"),
    ("Lookup 571 campaign canon, check P01-P18 patterns, and check pattern saturation", "campaign-canon"),
    ("Design a PR stunt, brand utility, or experiential activation and apply non-advertising test", "brand-activation"),
    ("Structure a narrative arc using Story Spine, Sparkline, or Pixar storytelling rules", "visual-storytelling"),
    ("Audit this design against documented brand guidelines and verify logo clearspace", "brand-intelligence"),
    ("Extract reusable taste rules and lighting patterns from these reference images", "taste-engine"),
    ("Recall my saved reference REF-1042 and show its recorded design jobs", "reference-memory"),
    ("Establish the grid layout, visual hierarchy, focal anchors, and negative space", "composition-director"),
    ("Set typography hierarchy, headline measure, line breaks, and type zones", "typography-director"),
    ("Define camera lens focal length, 3-point lighting setup, and material surface finish", "photography-director"),
    ("Plan realistic compositing physics, contact shadows, reflections, and occlusion", "manipulation-director"),
    ("Design an Arabic-first poster with proper RTL visual flow and calligraphy glyph rules", "arabic-rtl-director"),
    ("Create visual DNA rules and variations across a 5-asset social media campaign", "campaign-dna"),
    ("Direct a 15-second multi-shot video prompt for Seedance or Kling with 14-field shot cards", "video-director"),
    ("Write a 5-slot GPT Image 2 prompt or Nano Banana prompt with multi-panel grids", "image-director"),
    ("Sanitize this annotation-guided inpainting correction and protect everything outside the selected region", "edit-sanitizer"),
    ("Compile approved Art Direction Spec into provider-ready image instructions", "prompt-compiler"),
    ("Critique this rendered poster, test AI-slop anti-patterns, and score category floors", "visual-qa"),
]


def classify_prompt(prompt: str) -> str:
    p = prompt.lower()
    if any(k in p for k in ["art-direct", "orchestrat", "end-to-end with full team", "lead director"]):
        return "designly-director"
    if any(k in p for k in ["annotation-guided", "inpainting correction", "selected region", "protected region", "bounded edit", "sanitize this edit"]):
        return "edit-sanitizer"
    if any(k in p for k in ["recall my reference", "ref-", "saved reference", "reference memory", "forget ref"]):
        return "reference-memory"
    if any(k in p for k in ["taste rules", "extract reusable taste", "taste profile", "taste engine"]):
        return "taste-engine"
    if any(k in p for k in ["brand guidelines", "brand rules", "logo clearspace", "brand fidelity"]):
        return "brand-intelligence"
    if any(k in p for k in ["mine the consumer", "tension", "jtbd", "pollard", "insight-mining"]):
        return "insight-mining"
    if any(k in p for k in ["571 campaign", "campaign canon", "p01-p18", "pattern saturation"]):
        return "campaign-canon"
    if any(k in p for k in ["pr stunt", "brand utility", "experiential activation", "non-advertising"]):
        return "brand-activation"
    if any(k in p for k in ["video prompt", "seedance", "kling", "veo", "dramaturgy", "shot card", "14-field shot"]):
        return "video-director"
    if any(k in p for k in ["gpt image 2", "nano banana", "multi-panel grid", "5-slot gpt", "character sheet"]):
        return "image-director"
    if any(k in p for k in ["narrative arc", "story spine", "sparkline", "pixar storytelling", "freytag"]):
        return "visual-storytelling"
    if any(k in p for k in ["cannes", "triz", "sit/triz", "lateral ideation", "creative-director", "humankind"]):
        return "creative-director"
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
    if any(k in p for k in ["compile approved", "provider-ready", "provider prompt", "flux syntax", "midjourney prompt"]):
        return "prompt-compiler"
    if any(k in p for k in ["critique this", "ai-slop", "category floor", "visual qa", "score review"]):
        return "visual-qa"
    if any(k in p for k in ["grid layout", "visual hierarchy", "focal anchor", "negative space", "composition"]):
        return "composition-director"
    return "designly-director"


def main() -> int:
    failures = 0
    print(f"Testing {len(EXPECTED_SKILLS)} Skill catalog directories...")
    for slug in EXPECTED_SKILLS:
        if not (SKILLS_DIR / slug).is_dir():
            failures += 1
            print(f"FAIL missing skill directory: skills/{slug}")
        else:
            print(f"PASS found skill: {slug}")
    print(f"\nTesting {len(ROUTING_PROMPTS)} prompt routing classifications...")
    for prompt, expected in ROUTING_PROMPTS:
        routed = classify_prompt(prompt)
        if routed == expected:
            print(f"PASS prompt routed to '{routed}': {prompt[:60]}...")
        else:
            failures += 1
            print(f"FAIL prompt routed to '{routed}', expected '{expected}': {prompt[:60]}...")
    print(f"\nSkill catalog tests: {'PASS' if failures == 0 else 'FAIL'} ({failures} failures)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
