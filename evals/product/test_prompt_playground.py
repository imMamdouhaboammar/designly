#!/usr/bin/env python3
"""Validate the copy-first Designly Prompt Playground product surface."""
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

SECTION_BADGES = {
    "section-start.svg": "#start-here",
    "section-learn.svg": "#learn-one-capability-by-doing-it",
    "section-advanced.svg": "#advanced-combinations",
    "section-chatgpt.svg": "#prompt-card-behavior-in-chatgpt",
    "section-coverage.svg": "#coverage-map",
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

    cards = re.findall(r"^###\s+\d+\.", text, flags=re.MULTILINE)
    check(len(cards) >= 20, "at least 20 numbered Prompt Cards", failures)
    check(text.count("@Designly") >= 20, "at least 20 copy-ready @Designly prompt examples", failures)
    check(text.count("**Copy prompt**") >= 6, "starter cards expose explicit copy prompts", failures)
    check("## Coverage map" in text, "coverage map is present", failures)
    check("## Prompt Card behavior in ChatGPT" in text, "ChatGPT presentation behavior is defined", failures)

    missing = sorted(slug for slug in EXPECTED_SKILLS if f"`{slug}`" not in text)
    check(not missing, f"all 21 Skills are covered by the Playground{': ' + ', '.join(missing) if missing else ''}", failures)
    check("REF-####" in text and "Reference Memory" in text, "Reference Memory is demonstrated with a stable REF workflow", failures)
    check("right to left" in text and "Arabic glyph" in text, "Arabic-first RTL behavior is demonstrated", failures)

    for filename, anchor in SECTION_BADGES.items():
        check((BADGES / filename).is_file(), f"section badge exists: {filename}", failures)
        check(filename in text and anchor in text, f"Playground navigation links {filename} to {anchor}", failures)

    check("Pathway 0: Prompt Playground" in director, "Designly Director routes discovery to Pathway 0", failures)
    check("references/prompt-playground.md" in director, "Director points to the Playground source of truth", failures)
    check("Prompt Playground" in plugin, "plugin marketplace interface surfaces the Playground", failures)

    check(GUIDE_PATH in readme, "README links directly to the Prompt Playground guide", failures)
    check("Start Here: Prompt Playground" in readme, "README exposes a Start Here product entrypoint", failures)
    check("assets/badges/prompt-playground.svg" in readme, "README surfaces the clickable Playground badge", failures)

    forbidden_feature_dump = "list all 21 skills first"
    check(forbidden_feature_dump not in text.lower(), "Playground is not framed as a feature dump", failures)

    print(f"\nPrompt Playground product tests: {'PASS' if not failures else 'FAIL'} ({len(failures)} failures)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
