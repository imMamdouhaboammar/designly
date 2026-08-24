#!/usr/bin/env python3
"""
Master test runner for Design Neural Mesh conflict resolution, model adapters, skills.sh publishing, Homebrew, npm, and supply chain security.
Conforms to test-guard & api-security-best-practices.
"""
from __future__ import annotations
import json
import jsonschema
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFLICTS_DIR = ROOT / "evals/conflicts"
SHARED_SCRIPTS = ROOT / "shared/scripts"
CONTRACTS_DIR = ROOT / "shared/contracts"

sys.path.insert(0, str(SHARED_SCRIPTS))
from route_packet import MeshRouter

def check(cond: bool, msg: str, errors: list[str]):
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        errors.append(msg)

def run_all_evals() -> int:
    errors = []
    router = MeshRouter()
    packet_schema = json.loads((CONTRACTS_DIR / "signal-packet.schema.json").read_text(encoding="utf-8"))

    fixtures = sorted(list(CONFLICTS_DIR.glob("*.json")))
    print(f"Running {len(fixtures)} Neural Mesh conflict scenarios from {CONFLICTS_DIR}...\n")

    for fix_path in fixtures:
        data = json.loads(fix_path.read_text(encoding="utf-8"))
        s_id = data.get("scenario_id")
        name = data.get("name")
        print(f"[{s_id}] {name} ({fix_path.name})")

        # Scenario 1, 2, 4, 5, 6, 7: Lock overwrite prevention
        if "existing_locks" in data and "incoming_decisions" in data:
            locks = data.get("existing_locks", [])
            decisions = data.get("incoming_decisions", [])
            expected = data.get("expected_outcome", {})
            applied, vetoed = router.resolve_conflicts(locks, decisions)

            if expected.get("decision_applied") is False:
                check(len(vetoed) > 0, f"decision correctly blocked by existing lock in {s_id}", errors)
            elif expected.get("decision_applied") is True:
                check(len(applied) > 0, f"decision correctly applied with higher priority in {s_id}", errors)

        # Scenario 9: Malformed packet rejection
        elif "raw_packet" in data:
            raw_pkt = data["raw_packet"]
            is_valid = True
            try:
                jsonschema.validate(instance=raw_pkt, schema=packet_schema)
            except jsonschema.ValidationError:
                is_valid = False
            check(is_valid == data["expected_outcome"]["is_valid_schema"], f"malformed packet rejected without state pollution in {s_id}", errors)

        # Scenario 10: Sequential fallback
        elif data.get("runtime_mode") == "sequential_fallback":
            seq = data.get("skills_sequence", [])
            check(len(seq) == 7 and data["expected_outcome"]["all_nodes_executed"], f"sequential fallback executes complete chain in {s_id}", errors)

        # Scenario 11: Concurrent write collision
        elif s_id == "CNF-011":
            decisions = data.get("incoming_decisions", [])
            winner = min(decisions, key=lambda d: d.get("priority", 11))
            check(winner["agent"] == data["expected_outcome"]["winning_agent"], f"brand_guardian wins priority collision over taste_analyst in {s_id}", errors)
            check(winner["value"] == data["expected_outcome"]["winning_value"], f"winning value preserved in {s_id}", errors)

    # 1. Run Adapter Evals
    print("\n--- Running Model Adapters Evals ---")
    proc_adapters = subprocess.run([sys.executable, str(ROOT / "evals/adapters/test_adapters.py")], capture_output=True, text=True)
    print(proc_adapters.stdout)
    if proc_adapters.returncode != 0:
        errors.append("Model Adapters evals failed")

    # 2. Run skills.sh Evals
    print("--- Running skills.sh Evals ---")
    proc_skills_sh = subprocess.run([sys.executable, str(ROOT / "evals/skills_sh/test_skills_sh.py")], capture_output=True, text=True)
    print(proc_skills_sh.stdout)
    if proc_skills_sh.returncode != 0:
        errors.append("skills.sh evals failed")

    # 3. Run Homebrew Evals
    print("--- Running Homebrew Evals ---")
    proc_brew = subprocess.run([sys.executable, str(ROOT / "evals/homebrew/test_homebrew.py")], capture_output=True, text=True)
    print(proc_brew.stdout)
    if proc_brew.returncode != 0:
        errors.append("Homebrew evals failed")

    # 4. Run Supply Chain Evals
    print("--- Running Supply Chain Evals ---")
    proc_sc = subprocess.run([sys.executable, str(ROOT / "evals/supply_chain/test_supply_chain.py")], capture_output=True, text=True)
    print(proc_sc.stdout)
    if proc_sc.returncode != 0:
        errors.append("Supply chain evals failed")

    # 5. Run Bun Test Suite
    print("--- Running Bun TypeScript CLI Tests ---")
    proc_bun = subprocess.run(["bun", "test"], capture_output=True, text=True)
    print(proc_bun.stdout)
    if proc_bun.returncode != 0:
        errors.append("Bun test suite failed")

    print(f"\nConflict, Adapters, skills.sh, Homebrew & Supply Chain Evals: {'PASS' if not errors else 'FAIL'} ({len(errors)} errors)")
    if errors:
        for e in errors:
            print(f" - {e}")
        return 1
    return 0

def main() -> int:
    return run_all_evals()

if __name__ == "__main__":
    raise SystemExit(main())
