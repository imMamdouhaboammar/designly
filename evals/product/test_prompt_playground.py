#!/usr/bin/env python3
"""Validate the workflow-grounded Designly Prompt Playground product surface."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PLAYGROUND = ROOT / "skills" / "designly-director" / "references" / "prompt-playground.md"
DIRECTOR = ROOT / "skills" / "designly-director" / "SKILL.md"
PLUGIN = ROOT / ".codex-plugin" / "plugin.json"
README = ROOT / "README.md"
BADGES = ROOT / "assets" / "badges"

EXPECTED_SKILLS = {
    "designly-director",
    "creative-strategy",
    "creative-director",
    "insight-mining",
    "campaign-canon",
    "brand-activation",
    "visual-storytelling",
    "brand-intelligence",
    "taste-engine",
    "reference-memory",
    "composition-director",
    "typography-director",
    "photography-director",
    "manipulation-director",
    "arabic-rtl-director",
    "campaign-dna",
    "video-director",
    "image-director",
    "edit-sanitizer",
    "prompt-compiler",
    "visual-qa",
}

ROLE_AWARE_PIPELINES = {
    "new_commercial_campaign",
    "brand_activation_stunt",
    "arabic_first_poster",
    "narrative_storyboard",
    "bounded_image_edit",
    "cinematic_video_spot",
    "multi_panel_visual_campaign",
}

SECTION_BADGES = {
    "section-start.svg": "#core-orchestration-workflows",
    "section-learn.svg": "#image--design-execution-workflows",
    "section-advanced.svg": "#video--narrative-workflows",
    "section-chatgpt.svg": "#review-repair--specialist-workflows",
    "section-coverage.svg": "#workflow-coverage-map",
}

GUIDE_PATH = "skills/designly-director/references/prompt-playground.md"


def check(condition: bool, message: str, failures: list[str]) -> None:
    print(("PASS " if condition else "FAIL ") + message)
    if not condition:
        failures.append(message)


def main() -> int:
    failures: list[str] = []

    check(PLAYGROUND.is_file(), "Prompt Playground reference exists", failures)
    check(README.is_file(), "README exists", failures)
    if not PLAYGROUND.is_file() or not README.is_file():
        return 1

    text = PLAYGROUND.read_text(encoding="utf-8")
    director = DIRECTOR.read_text(encoding="utf-8")
    plugin = PLUGIN.read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")

    workflows = re.findall(r"^###\s+WF-\d{2}\b", text, flags=re.MULTILINE)
    check(len(workflows) >= 16, "at least 16 production Workflow Prompts", failures)
    check(text.count("@Designly") >= 16, "at least 16 copy-ready @Designly workflow prompts", failures)
    check(text.count("**Route:**") >= 16, "every workflow declares its Designly route", failures)
    check(text.count("**Use when:**") >= 16, "every workflow declares when to use it", failures)
    check(text.count("**Required inputs:**") >= 16, "every workflow declares required inputs", failures)

    for pipeline in sorted(ROLE_AWARE_PIPELINES):
        check(pipeline in text, f"role-aware pipeline is productized: {pipeline}", failures)

    missing = sorted(slug for slug in EXPECTED_SKILLS if f"`{slug}`" not in text)
    check(not missing, f"all 21 Skills appear in grounded workflow coverage{': ' + ', '.join(missing) if missing else ''}", failures)

    required_contracts = ["DesignContext", "DesignSignalPacket", "EditContract", "RevisionRequest", "generation_state"]
    for contract in required_contracts:
        check(contract in text, f"workflow prompts use real contract: {contract}", failures)

    required_operating_rules = [
        "smallest useful route",
        "Do not invent Skills",
        "actual output",
        "approved source checkpoint",
        "host-native image",
        "Do not expose private chain-of-thought",
    ]
    for phrase in required_operating_rules:
        check(phrase in text, f"Playground enforces production rule: {phrase}", failures)

    check("{{BRIEF}}" in text, "workflow prompts use editable placeholders instead of fictional briefs", failures)
    check("{{BRAND_ASSETS}}" in text, "workflow prompts expose brand-asset input placeholders", failures)
    check("{{TARGET_MODEL}}" in text, "workflow prompts expose target-model input placeholders", failures)

    stale_examples = [
        "premium sparkling water",
        "fictional event company called NORTH",
        "food-delivery apps",
        "sunscreen brand",
        "AFTER SIX",
    ]
    for stale in stale_examples:
        check(stale not in text, f"removed arbitrary demo scenario: {stale}", failures)

    check("## Workflow coverage map" in text, "workflow coverage map is present", failures)
    check("## Prompt behavior in ChatGPT" in text, "ChatGPT workflow presentation behavior is defined", failures)

    for filename, anchor in SECTION_BADGES.items():
        check((BADGES / filename).is_file(), f"section badge exists: {filename}", failures)
        check(filename in text and anchor in text, f"Playground navigation links {filename} to {anchor}", failures)

    check("Pathway 0: Workflow Prompt Library" in director, "Designly Director routes discovery to Workflow Prompt Library", failures)
    check("references/prompt-playground.md" in director, "Director points to the workflow source of truth", failures)
    check("Workflow Prompt Library" in plugin, "plugin marketplace interface surfaces workflow prompts", failures)

    check(GUIDE_PATH in readme, "README links directly to the workflow guide", failures)
    check("Production Workflow Prompts" in readme, "README exposes the production workflow entrypoint", failures)
    check("assets/badges/prompt-playground.svg" in readme, "README surfaces the clickable Playground badge", failures)

    print(f"\nWorkflow Prompt Playground tests: {'PASS' if not failures else 'FAIL'} ({len(failures)} failures)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
