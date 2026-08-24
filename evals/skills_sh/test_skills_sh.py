#!/usr/bin/env python3
"""
Test suite for Vercel skills.sh integration, manifests, and CLI publishing tool.
"""
from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILLS_JSON = ROOT / "skills.json"
SKILLS_DIR = ROOT / "skills"
PUBLISH_TOOL = ROOT / "tools/publish_skills_sh.py"

def check(cond: bool, msg: str, errors: list[str]):
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        errors.append(msg)

def main() -> int:
    errors = []
    print("--- Testing skills.sh Registry Manifest & Tooling ---")

    # 1. Check skills.json existence and schema
    check(SKILLS_JSON.is_file(), "skills.json exists at root", errors)
    data = json.loads(SKILLS_JSON.read_text(encoding="utf-8"))
    
    check(data.get("name") == "designly", "manifest name is designly", errors)
    check("skills" in data and len(data["skills"]) == 21, "21 skills registered in skills.json", errors)
    check("adapters" in data, "adapters declared in skills.json", errors)
    
    # Check 6 core models are declared in adapters
    img_adapters = data.get("adapters", {}).get("image", [])
    vid_adapters = data.get("adapters", {}).get("video", [])
    
    check("gemini-nano-banana" in img_adapters, "gemini-nano-banana in image adapters", errors)
    check("minimax-design" in img_adapters, "minimax-design in image adapters", errors)
    check("kimi-design" in img_adapters, "kimi-design in image adapters", errors)
    check("claude-design" in img_adapters, "claude-design in image adapters", errors)
    check("seedance-2.5" in vid_adapters, "seedance-2.5 in video adapters", errors)
    check("kling-3.0" in vid_adapters, "kling-3.0 in video adapters", errors)

    # 2. Check publish_skills_sh.py CLI output
    proc = subprocess.run([sys.executable, str(PUBLISH_TOOL), "--check"], capture_output=True, text=True)
    check(proc.returncode == 0, "publish_skills_sh.py --check exited 0", errors)
    check("skills.sh Validation: PASS" in proc.stdout, "publisher validation passed", errors)

    # 3. Test build command
    proc_build = subprocess.run([sys.executable, str(PUBLISH_TOOL), "--build"], capture_output=True, text=True)
    check(proc_build.returncode == 0, "publish_skills_sh.py --build exited 0", errors)
    manifest_out = ROOT / "dist/skills-sh/skills-manifest.json"
    check(manifest_out.is_file(), "distribution manifest generated", errors)

    print(f"\n==========================================")
    print(f"skills.sh Test Suite: {'PASS' if not errors else 'FAIL'} ({len(errors)} errors)")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
