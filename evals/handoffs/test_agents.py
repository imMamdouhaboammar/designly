#!/usr/bin/env python3
"""Test Codex custom agent role coverage and tool boundaries."""
from __future__ import annotations
try:
    import tomllib
except ImportError:
    try:
        import tomli as tomllib
    except ImportError:
        import toml as tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AGENTS_DIR = ROOT / ".codex/agents"
CONFIG_FILE = ROOT / ".codex/config.toml"
READ_ONLY_AGENTS = [
    "strategy-planner", "brand-guardian", "taste-analyst", "structure-critic",
    "craft-director", "arabic-visual-director", "edit-sanitizer", "visual-reviewer"
]


def main() -> int:
    failures = 0
    print("Testing Codex custom agent configurations and role bounds...")
    cfg = tomllib.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    max_concurrent = cfg.get("agents", {}).get("max_concurrent_agents", 0)
    if max_concurrent != 6:
        failures += 1
        print(f"FAIL max_concurrent_agents is {max_concurrent}, expected 6")
    else:
        print("PASS max_concurrent_agents is 6")

    present = [p.stem for p in AGENTS_DIR.glob("*.toml")]
    if len(present) != 9:
        failures += 1
        print(f"FAIL expected 9 agents, found {len(present)}")
    else:
        print("PASS exactly 9 agents present")

    for name in READ_ONLY_AGENTS:
        p = AGENTS_DIR / f"{name}.toml"
        data = tomllib.loads(p.read_text(encoding="utf-8"))
        tools = data.get("tools", [])
        if "write_file" in tools or "invoke_subagent" in tools:
            failures += 1
            print(f"FAIL agent {name} should be read-only, found tools: {tools}")
        else:
            print(f"PASS agent {name} is read-only: {tools}")

    dir_data = tomllib.loads((AGENTS_DIR / "designly-director.toml").read_text(encoding="utf-8"))
    dir_tools = dir_data.get("tools", [])
    if "invoke_subagent" not in dir_tools or "write_file" not in dir_tools:
        failures += 1
        print(f"FAIL designly-director must have orchestration tools, got {dir_tools}")
    else:
        print(f"PASS designly-director has required orchestration tools: {dir_tools}")

    print(f"\nAgents test suite: {'PASS' if failures == 0 else 'FAIL'} ({failures} failures)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
