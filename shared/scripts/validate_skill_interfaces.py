#!/usr/bin/env python3
"""
Validates all Skill entries, SKILL.md frontmatter, links, and agents/openai.yaml interface configs.
"""
from __future__ import annotations
import os
import re
import sys
import yaml
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

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\(([^)]+)\)")

def check(cond: bool, msg: str, errors: list[str]):
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        errors.append(msg)

def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter marker '---'")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("SKILL.md frontmatter closing marker '---' missing")
    vals = {}
    for line in text[4:end].splitlines():
        if not line or line.startswith((" ", "\t")):
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            vals[k.strip()] = v.strip().strip('"').strip("'")
    return vals

def validate_skill(slug: str, errors: list[str]):
    skill_dir = SKILLS_DIR / slug
    check(skill_dir.is_dir(), f"skill directory exists: skills/{slug}", errors)
    if not skill_dir.is_dir():
        return
    
    skill_md = skill_dir / "SKILL.md"
    check(skill_md.is_file(), f"SKILL.md exists: skills/{slug}/SKILL.md", errors)
    if not skill_md.is_file():
        return

    text = skill_md.read_text(encoding="utf-8")
    try:
        fm = parse_frontmatter(text)
    except Exception as ex:
        check(False, f"SKILL.md frontmatter parse error in {slug}: {ex}", errors)
        return

    name = fm.get("name", "")
    desc = fm.get("description", "")
    check(bool(name), f"frontmatter has name in {slug}", errors)
    check(bool(desc), f"frontmatter has description in {slug}", errors)
    check(name == slug, f"frontmatter name matches directory: {slug}", errors)
    check(bool(NAME_RE.fullmatch(name)), f"name uses lowercase hyphen format: {slug}", errors)
    check(len(name) <= 64, f"name <= 64 chars: {slug}", errors)
    check(0 < len(desc) <= 1024, f"description length 1..1024 in {slug}", errors)
    check("This skill should be used when" in desc or "Use when" in desc or "Used when" in desc or "Triggers when" in desc, f"description states trigger condition: {slug}", errors)
    check(len(text.splitlines()) <= 500, f"SKILL.md under 500 lines ({len(text.splitlines())} lines): {slug}", errors)
    
    # Check no metadata in frontmatter
    fm_raw = text[4:text.find("\n---\n", 4)]
    check("metadata:" not in fm_raw, f"no metadata block in frontmatter: {slug}", errors)

    # Check openai.yaml
    agent_yaml = skill_dir / "agents/openai.yaml"
    check(agent_yaml.is_file(), f"agents/openai.yaml exists: {slug}", errors)
    if agent_yaml.is_file():
        try:
            cfg = yaml.safe_load(agent_yaml.read_text(encoding="utf-8"))
            iface = cfg.get("interface", {})
            check(bool(iface), f"interface block present in agents/openai.yaml: {slug}", errors)
            display_name = iface.get("display_name", "")
            check(bool(display_name) and len(display_name) <= 40, f"display_name valid in {slug}: '{display_name}'", errors)
            short_desc = iface.get("short_description", "")
            check(bool(short_desc) and len(short_desc) <= 80, f"short_description valid in {slug}: '{short_desc}'", errors)
            
            icon_small = iface.get("icon_small", "")
            if icon_small:
                icon_path = (skill_dir / icon_small).resolve()
                check(icon_path.is_file(), f"icon_small exists for {slug}: {icon_small}", errors)
            
            icon_large = iface.get("icon_large", "")
            if icon_large:
                icon_path = (skill_dir / icon_large).resolve()
                check(icon_path.is_file(), f"icon_large exists for {slug}: {icon_large}", errors)

            prompt = iface.get("default_prompt", "")
            if isinstance(prompt, list):
                check(len(prompt) <= 3, f"default_prompt count <= 3 in {slug}", errors)
                for p in prompt:
                    check(isinstance(p, str) and len(p) <= 128 and "\n" not in p, f"default_prompt valid string in {slug}", errors)
            else:
                check(isinstance(prompt, str) and len(prompt) <= 128 and "\n" not in prompt, f"default_prompt single line <= 128 in {slug}", errors)
        except Exception as ex:
            check(False, f"agents/openai.yaml YAML error in {slug}: {ex}", errors)

    # Check markdown links
    for target in LINK_RE.findall(text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        link_path = (skill_dir / target).resolve()
        check(link_path.exists(), f"link target exists in {slug}: {target}", errors)

def main() -> int:
    errors = []
    print("Validating Skill catalog interfaces and metadata...")
    present_slugs = sorted([d.name for d in SKILLS_DIR.iterdir() if d.is_dir() and not d.name.startswith(".")]) if SKILLS_DIR.is_dir() else []
    
    check(set(present_slugs) == set(EXPECTED_SKILLS), f"skill directory contains exactly the 13 expected skills (found {len(present_slugs)})", errors)
    
    for slug in EXPECTED_SKILLS:
        print(f"\n--- Checking Skill: {slug} ---")
        validate_skill(slug, errors)

    print(f"\nSkill interface validation: {'PASS' if not errors else 'FAIL'} ({len(errors)} errors)")
    if errors:
        for e in errors:
            print(f" - {e}")
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
