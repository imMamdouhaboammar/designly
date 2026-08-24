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

PIPELINE_ROUTES = {
    "new_commercial_campaign": [
        "designly-director",
        "creative-strategy",
        "insight-mining",
        "creative-director",
        "campaign-canon",
        "brand-intelligence",
        "taste-engine",
        "composition-director",
        "typography-director",
        "photography-director",
        "image-director",
        "prompt-compiler",
        "visual-qa",
    ],
    "brand_activation_stunt": [
        "designly-director",
        "insight-mining",
        "brand-activation",
        "campaign-canon",
        "brand-intelligence",
        "manipulation-director",
        "prompt-compiler",
        "visual-qa",
    ],
    "arabic_first_poster": [
        "designly-director",
        "creative-strategy",
        "insight-mining",
        "creative-director",
        "brand-intelligence",
        "composition-director",
        "arabic-rtl-director",
        "typography-director",
        "photography-director",
        "prompt-compiler",
        "visual-qa",
    ],
    "narrative_storyboard": [
        "designly-director",
        "creative-strategy",
        "insight-mining",
        "visual-storytelling",
        "campaign-dna",
        "composition-director",
        "photography-director",
        "image-director",
        "prompt-compiler",
        "visual-qa",
    ],
    "bounded_image_edit": [
        "designly-director",
        "edit-sanitizer",
        "arabic-rtl-director",
        "image-director",
        "prompt-compiler",
        "visual-qa",
    ],
    "cinematic_video_spot": [
        "designly-director",
        "creative-strategy",
        "insight-mining",
        "creative-director",
        "visual-storytelling",
        "image-director",
        "video-director",
        "prompt-compiler",
        "visual-qa",
    ],
    "multi_panel_visual_campaign": [
        "designly-director",
        "creative-strategy",
        "brand-intelligence",
        "taste-engine",
        "image-director",
        "composition-director",
        "typography-director",
        "prompt-compiler",
        "visual-qa",
    ],
}

ROLE_AWARE_PIPELINES = set(PIPELINE_ROUTES)

SECTION_BADGES = {
    "section-start.svg": "#core-orchestration-workflows",
    "section-learn.svg": "#image--design-execution-workflows",
    "section-advanced.svg": "#video--narrative-workflows",
    "section-chatgpt.svg": "#review-repair--specialist-workflows",
    "section-coverage.svg": "#workflow-coverage-map",
}

GUIDE_PATH = "skills/designly-director/references/prompt-playground.md"
README_SHIELD_STYLE = "style=flat-square"


def check(condition: bool, message: str, failures: list[str]) -> None:
    print(("PASS " if condition else "FAIL ") + message)
    if not condition:
        failures.append(message)


def route_preserves_order(route_line: str, expected_skills: list[str]) -> bool:
    cursor = -1
    for skill in expected_skills:
        cursor = route_line.find(f"`{skill}`", cursor + 1)
        if cursor < 0:
            return False
    return True


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
    route_lines = [line for line in text.splitlines() if line.startswith("**Route:**")]

    check(len(workflows) >= 16, "at least 16 production Workflow Prompts", failures)
    check(text.count("@Designly") >= 16, "at least 16 copy-ready @Designly workflow prompts", failures)
    check(text.count("**Copy prompt**") >= 16, "every production workflow exposes a copy prompt", failures)
    check(len(route_lines) >= 16, "every workflow declares its Designly route", failures)
    check(text.count("**Use when:**") >= 16, "every workflow declares when to use it", failures)
    check(text.count("**Required inputs:**") >= 16, "every workflow declares required inputs", failures)

    for pipeline, expected_route in PIPELINE_ROUTES.items():
        matches = [line for line in route_lines if f"`{pipeline}`" in line]
        check(len(matches) == 1, f"role-aware pipeline has one declared workflow route: {pipeline}", failures)
        if matches:
            check(
                route_preserves_order(matches[0], expected_route),
                f"workflow preserves routing-graph Skill order: {pipeline}",
                failures,
            )

    unknown_route_tokens: set[str] = set()
    for line in route_lines:
        for token in re.findall(r"`([^`]+)`", line):
            if token not in EXPECTED_SKILLS and token not in ROLE_AWARE_PIPELINES:
                unknown_route_tokens.add(token)
    check(
        not unknown_route_tokens,
        f"route metadata invents no Skills or pipeline names{': ' + ', '.join(sorted(unknown_route_tokens)) if unknown_route_tokens else ''}",
        failures,
    )

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
    check("img.shields.io/badge/Workflow_Library-production-111111" in readme, "README surfaces Workflow Library with the established shields theme", failures)
    check("img.shields.io/badge/16_Workflows-copy--ready-111111" in readme, "README surfaces workflow count with the established shields theme", failures)
    check(readme.count(README_SHIELD_STYLE) >= 8, "README workflow badges use the same flat-square style as existing badges", failures)
    check("assets/badges/prompt-playground.svg" not in readme, "README no longer mixes rounded local badges with shields.io badges", failures)

    print(f"\nWorkflow Prompt Playground tests: {'PASS' if not failures else 'FAIL'} ({len(failures)} failures)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
