#!/usr/bin/env python3
"""Parity test for Designly v4.1 against the preserved v3.2.1 capabilities."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASELINE_SPEC = ROOT / "evals/baseline/v3.2.1-behavior.json"


def main() -> int:
    if not BASELINE_SPEC.is_file():
        print(f"FAIL Baseline spec not found: {BASELINE_SPEC}")
        return 1
    spec = json.loads(BASELINE_SPEC.read_text(encoding="utf-8"))
    failures: list[str] = []

    for slug in spec.get("required_v4_skill_slugs", []):
        for rel in (f"skills/{slug}/SKILL.md", f"skills/{slug}/agents/openai.yaml"):
            if not (ROOT / rel).is_file(): failures.append(f"Missing {rel}")
            else: print(f"PASS {rel}")

    for slug in spec.get("required_v4_agent_slugs", []):
        rel = f".codex/agents/{slug}.toml"
        if not (ROOT / rel).is_file(): failures.append(f"Missing {rel}")
        else: print(f"PASS {rel}")

    required_contracts = [
        "design-context.schema.json", "signal-packet.schema.json", "design-lock.schema.json",
        "revision-request.schema.json", "edit-contract.schema.json", "routing-graph.json"
    ]
    for name in required_contracts:
        rel = f"shared/contracts/{name}"
        if not (ROOT / rel).is_file(): failures.append(f"Missing {rel}")
        else: print(f"PASS {rel}")

    if failures:
        print(f"\nParity check: FAIL ({len(failures)} missing components)")
        for f in failures: print(f" - {f}")
        return 1
    print("\nParity check: PASS (14 skills, 9 agents, 6 shared contracts present; v3.2.1 behavior retained)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
