#!/usr/bin/env python3
"""Validate Codex configuration and custom agent definitions."""
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
EXPECTED_AGENTS = [
    "designly-director", "strategy-planner", "creative-director", "insight-miner", "canon-analyst",
    "activation-strategist", "story-architect", "brand-guardian", "taste-analyst",
    "structure-critic", "craft-director", "arabic-visual-director", "video-director", "image-director",
    "edit-sanitizer", "visual-reviewer"
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
        cfg = data.get("agents", {})
        check(bool(cfg), "agents section in config.toml", errors)
        check(cfg.get("max_concurrent_agents", 0) >= 1, "max_concurrent_agents >= 1", errors)
        check(cfg.get("default_agent") == "designly-director", "default_agent is designly-director", errors)
    except Exception as ex:
        check(False, f"config.toml parse error: {ex}", errors)


def validate_agent(slug: str, errors: list[str]):
    p = AGENTS_DIR / f"{slug}.toml"
    check(p.is_file(), f"agent config exists: .codex/agents/{slug}.toml", errors)
    if not p.is_file():
        return
    try:
        data = tomllib.loads(p.read_text(encoding="utf-8"))
        name, desc = data.get("name", ""), data.get("description", "")
        instructions, tools = data.get("developer_instructions", ""), data.get("tools", [])
        check(name == slug, f"name matches filename in {slug}.toml", errors)
        check(bool(desc) and len(desc) <= 500, f"description present in {slug}.toml", errors)
        check(bool(instructions) and len(instructions) > 50, f"developer_instructions non-empty in {slug}.toml", errors)
        check(isinstance(tools, list), f"tools list defined in {slug}.toml", errors)
        lower = instructions.lower()
        check("packet" in lower or "designsignalpacket" in lower or "decision" in lower, f"packet contract referenced in {slug}.toml", errors)
        check("raw" in lower or "dump" in lower or "never" in lower, f"no raw dump instruction in {slug}.toml", errors)
    except Exception as ex:
        check(False, f"agent parse error in {slug}.toml: {ex}", errors)


def main() -> int:
    errors: list[str] = []
    print("Validating Codex configuration and custom agents...")
    validate_config(errors)
    present = [p.stem for p in AGENTS_DIR.glob("*.toml")] if AGENTS_DIR.is_dir() else []
    check(set(present) == set(EXPECTED_AGENTS), f"exactly {len(EXPECTED_AGENTS)} expected agents present (found {len(present)})", errors)
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
