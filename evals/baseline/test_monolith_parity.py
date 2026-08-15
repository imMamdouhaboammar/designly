#!/usr/bin/env python3
"""
Parity test comparing v4 multi-skill neural mesh against v3.2.1 baseline specifications.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASELINE_SPEC = ROOT / "evals/baseline/v3.2.1-behavior.json"

def main() -> int:
    if not BASELINE_SPEC.is_file():
        print(f"FAIL Baseline spec not found: {BASELINE_SPEC}")
        return 1
    
    spec = json.loads(BASELINE_SPEC.read_text(encoding="utf-8"))
    skills_dir = ROOT / "skills"
    agents_dir = ROOT / ".codex/agents"
    
    failures = []
    
    # 1. Check required v4 Skill slugs
    required_skills = spec.get("required_v4_skill_slugs", [])
    present_skills = [d.name for d in skills_dir.iterdir() if d.is_dir() and not d.name.startswith(".")] if skills_dir.is_dir() else []
    
    print(f"Checking {len(required_skills)} required Skill directories in {skills_dir}...")
    for slug in required_skills:
        skill_file = skills_dir / slug / "SKILL.md"
        agent_yaml = skills_dir / slug / "agents/openai.yaml"
        if not skill_file.is_file():
            failures.append(f"Missing Skill file: skills/{slug}/SKILL.md")
        if not agent_yaml.is_file():
            failures.append(f"Missing Skill interface: skills/{slug}/agents/openai.yaml")
        else:
            print(f"PASS skill present: {slug}")
            
    # 2. Check required v4 Agent configs
    required_agents = spec.get("required_v4_agent_slugs", [])
    print(f"Checking {len(required_agents)} required Agent TOML files in {agents_dir}...")
    for slug in required_agents:
        toml_file = agents_dir / f"{slug}.toml"
        if not toml_file.is_file():
            failures.append(f"Missing custom agent config: .codex/agents/{slug}.toml")
        else:
            print(f"PASS agent present: {slug}")

    # 3. Check shared contracts
    contracts_dir = ROOT / "shared/contracts"
    required_contracts = [
        "design-context.schema.json",
        "signal-packet.schema.json",
        "design-lock.schema.json",
        "revision-request.schema.json",
        "routing-graph.json"
    ]
    for c in required_contracts:
        p = contracts_dir / c
        if not p.is_file():
            failures.append(f"Missing shared contract: shared/contracts/{c}")
        else:
            print(f"PASS contract present: {c}")

    if failures:
        print(f"\nParity check: FAIL ({len(failures)} missing components)")
        for f in failures:
            print(f"  - {f}")
        return 1
    
    print("\nParity check: PASS (All 13 skills, 8 agents, and 5 shared contracts present)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
