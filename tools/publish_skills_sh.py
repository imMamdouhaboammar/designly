#!/usr/bin/env python3
"""
skills.sh (Vercel) Publisher & Verification Tool for Designly.

Validates the skill pack, individual skills, frontmatters, entry points,
and prepares distribution bundles for skills.sh registry.
"""
from __future__ import annotations
import argparse
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
SKILLS_JSON = ROOT / "skills.json"
DIST_DIR = ROOT / "dist/skills-sh"

FRONTMATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

def err(errors: list[str], msg: str):
    errors.append(msg)
    print(f"FAIL: {msg}")

def ok(msg: str):
    print(f"PASS: {msg}")

def check(cond: bool, msg: str, errors: list[str]):
    if cond:
        ok(msg)
    else:
        err(errors, msg)

def validate_skills_json(errors: list[str]) -> dict:
    if not SKILLS_JSON.is_file():
        err(errors, "skills.json does not exist at repo root")
        return {}
    
    try:
        data = json.loads(SKILLS_JSON.read_text(encoding="utf-8"))
    except Exception as e:
        err(errors, f"skills.json is invalid JSON: {e}")
        return {}
    
    check(data.get("name") == "designly", "package name is designly", errors)
    check(bool(re.match(r"^\d+\.\d+\.\d+", data.get("version", ""))), "semver version present", errors)
    check(isinstance(data.get("skills"), list) and len(data["skills"]) == 21, "all 21 skills declared in skills.json", errors)
    check("adapters" in data, "adapters declared in skills.json", errors)
    check("install" in data and "all" in data["install"], "install instructions present in skills.json", errors)
    
    declared_names = {s.get("name") for s in data.get("skills", [])}
    
    # Check that each skill exists on disk
    for skill_info in data.get("skills", []):
        s_name = skill_info.get("name")
        s_path = ROOT / skill_info.get("path", "")
        s_entry = ROOT / skill_info.get("entry", "")
        
        check(s_path.is_dir(), f"skill directory exists: {skill_info.get('path')}", errors)
        check(s_entry.is_file(), f"skill entry exists: {skill_info.get('entry')}", errors)
        
        # Verify SKILL.md frontmatter
        if s_entry.is_file():
            content = s_entry.read_text(encoding="utf-8")
            fm_match = FRONTMATTER_PATTERN.match(content)
            check(bool(fm_match), f"valid YAML frontmatter in {skill_info.get('entry')}", errors)
            if fm_match:
                fm_text = fm_match.group(1)
                check(f"name: {s_name}" in fm_text, f"frontmatter name matches {s_name}", errors)
                check("description:" in fm_text, f"frontmatter description present in {s_name}", errors)
    
    # Verify disk skills match declared skills
    disk_skills = {d.name for d in SKILLS_DIR.iterdir() if d.is_dir() and not d.name.startswith(".")}
    diff = disk_skills.symmetric_difference(declared_names)
    check(len(diff) == 0, f"skills.json matches skills/ on disk exactly (diff: {diff})", errors)
    
    return data

def build_export(data: dict) -> None:
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    export_manifest = {
        "registry": "skills.sh",
        "package": data.get("name"),
        "version": data.get("version"),
        "skills_count": len(data.get("skills", [])),
        "adapters": data.get("adapters", {}),
        "install_command": data.get("install", {}).get("all"),
        "skills": data.get("skills", [])
    }
    manifest_path = DIST_DIR / "skills-manifest.json"
    manifest_path.write_text(json.dumps(export_manifest, indent=2), encoding="utf-8")
    print(f"\nBuilt skills.sh distribution manifest at: {manifest_path}")

def main() -> int:
    parser = argparse.ArgumentParser(description="skills.sh packaging and verification tool")
    parser.add_argument("--check", action="store_true", help="Validate skills.sh compatibility")
    parser.add_argument("--build", action="store_true", help="Build export bundles for skills.sh")
    parser.add_argument("--stats", action="store_true", help="Display stats for skills.sh registry")
    args = parser.parse_args()

    errors = []
    print("=== Validating Designly for skills.sh (Vercel) Registry ===\n")
    data = validate_skills_json(errors)

    if errors:
        print(f"\nValidation FAILED with {len(errors)} errors.")
        return 1

    print("\nskills.sh Validation: PASS (0 errors)")

    if args.build or not (args.check or args.stats):
        build_export(data)

    if args.stats or not (args.check or args.build):
        print(f"\nPackage: {data.get('name')} v{data.get('version')}")
        print(f"Total Skills: {len(data.get('skills', []))}")
        print(f"Supported Image Adapters: {len(data.get('adapters', {}).get('image', []))}")
        print(f"Supported Video Adapters: {len(data.get('adapters', {}).get('video', []))}")
        print(f"Registry Command: npx skills add imMamdouhaboammar/designly")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
