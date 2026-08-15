#!/usr/bin/env python3
"""
Validates Codex configuration (.codex/config.toml) and custom agent definitions (.codex/agents/*.toml).
"""
from __future__ import annotations
import os
import sys
try:
    import tomllib
except ImportError:
    try:
        import tomli as tomllib
    except ImportError:
        import toml as tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CODEX_DIR = ROOT / ".codex"
AGENTS_DIR = CODEX_DIR / "agents"
CONFIG_FILE = CODEX_DIR / "config.toml"

EXPECTED_AGENTS = [
    "designly-director",
    "strategy-planner",
    "brand-guardian",
    "taste-analyst",
    "structure-critic",
    "craft-director",
    "arabic-visual-director",
    "visual-reviewer"
]

def check(cond: bool, msg: str, errors: list[str]):
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        errors.append(msg)

def validate_config(errors: list[str]):
    check(CONFIG_FILE.is_file(), ".codex/config.toml exists", errors)
    if not CONFIG_FILE.is_file():
        return
    try:
        data = tomllib.loads(CONFIG_FILE.read_text(encoding="utf-8"))
        agents_cfg = data.get("agents", {})
        check(bool(agents_cfg), "agents section in config.toml", errors)
        check(agents_cfg.get("max_concurrent_agents", 0) >= 1, "max_concurrent_agents >= 1", errors)
        check(agents_cfg.get("default_agent") == "designly-director", "default_agent is designly-director", errors)
    except Exception as ex:
        check(False, f"config.toml parse error: {ex}", errors)

def validate_agent(slug: str, errors: list[str]):
    agent_file = AGENTS_DIR / f"{slug}.toml"
    check(agent_file.is_file(), f"agent config exists: .codex/agents/{slug}.toml", errors)
    if not agent_file.is_file():
        return
    try:
        data = tomllib.loads(agent_file.read_text(encoding="utf-8"))
        name = data.get("name", "")
        desc = data.get("description", "")
        instructions = data.get("developer_instructions", "")
        tools = data.get("tools", [])

        check(name == slug, f"name matches filename in {slug}.toml", errors)
        check(bool(desc) and len(desc) <= 500, f"description present in {slug}.toml", errors)
        check(bool(instructions) and len(instructions) > 50, f"developer_instructions non-empty in {slug}.toml", errors)
        check(isinstance(tools, list), f"tools list defined in {slug}.toml", errors)

        # Check safety & packet requirements in instructions
        inst_lower = instructions.lower()
        check("packet" in inst_lower or "designsignalpacket" in inst_lower or "decision" in inst_lower, f"packet contract referenced in {slug}.toml", errors)
        check("raw" in inst_lower or "dump" in inst_lower or "without" in inst_lower or "never" in inst_lower, f"no raw dump instruction in {slug}.toml", errors)

    except Exception as ex:
        check(False, f"agent parse error in {slug}.toml: {ex}", errors)

def main() -> int:
    errors = []
    print("Validating Codex configuration and custom agents...")
    validate_config(errors)
    
    check(AGENTS_DIR.is_dir(), ".codex/agents directory exists", errors)
    present_agents = [p.stem for p in AGENTS_DIR.glob("*.toml")] if AGENTS_DIR.is_dir() else []
    check(set(present_agents) == set(EXPECTED_AGENTS), f"exactly 8 expected agents present (found {len(present_agents)})", errors)

    for slug in EXPECTED_AGENTS:
        print(f"\n--- Checking Agent: {slug} ---")
        validate_agent(slug, errors)

    print(f"\nAgent validation: {'PASS' if not errors else 'FAIL'} ({len(errors)} errors)")
    if errors:
        for e in errors:
            print(f" - {e}")
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
