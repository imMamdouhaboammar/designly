#!/usr/bin/env python3
"""Validate Design Neural Mesh contracts, orchestration graph, routes, loops, and gates."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTRACTS_DIR = ROOT / "shared/contracts"
ROUTING_GRAPH = CONTRACTS_DIR / "routing-graph.json"
REQUIRED_SCHEMAS = [
    "design-context.schema.json",
    "signal-packet.schema.json",
    "design-lock.schema.json",
    "revision-request.schema.json",
    "edit-contract.schema.json",
]


def check(cond: bool, msg: str, errors: list[str]):
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        errors.append(msg)


def validate_schemas(errors: list[str]):
    for name in REQUIRED_SCHEMAS:
        p = CONTRACTS_DIR / name
        check(p.is_file(), f"contract schema exists: {name}", errors)
        if not p.is_file():
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            check(data.get("$schema") == "https://json-schema.org/draft/2020-12/schema", f"schema draft 2020-12: {name}", errors)
            check(data.get("additionalProperties") is False, f"additionalProperties false: {name}", errors)
            check(bool(data.get("required")), f"required properties defined: {name}", errors)
        except Exception as ex:
            check(False, f"schema valid JSON {name}: {ex}", errors)


def validate_routing_graph(errors: list[str]):
    check(ROUTING_GRAPH.is_file(), "routing graph exists: routing-graph.json", errors)
    if not ROUTING_GRAPH.is_file():
        return
    try:
        graph = json.loads(ROUTING_GRAPH.read_text(encoding="utf-8"))
        nodes = graph.get("nodes", {})
        check(len(nodes) == 19, f"routing graph defines exactly 19 nodes (found {len(nodes)})", errors)
        check(graph.get("primary_orchestrator") == "designly-director", "primary_orchestrator is designly-director", errors)
        for expected_node in ("edit-sanitizer", "creative-director", "insight-mining", "campaign-canon", "brand-activation", "visual-storytelling"):
            check(expected_node in nodes, f"{expected_node} node exists", errors)
        
        # Validate Architecture Layers
        layers = graph.get("architecture_layers", [])
        check(len(layers) == 6, f"architecture defines 6 cognitive tiers (found {len(layers)})", errors)
        
        # Validate Role-Aware Pipelines
        pipelines = graph.get("role_aware_pipelines", {})
        check(len(pipelines) >= 5, f"at least 5 role-aware pipelines defined (found {len(pipelines)})", errors)
        for pipe_name, steps in pipelines.items():
            check(isinstance(steps, list) and len(steps) > 0, f"pipeline '{pipe_name}' has valid step sequence", errors)
            for step in steps:
                check(step in nodes, f"pipeline step '{step}' in '{pipe_name}' is a valid node", errors)
                
        # Validate Feedback Loops
        loops = graph.get("feedback_loops", [])
        check(len(loops) >= 5, f"at least 5 recursive feedback loops defined (found {len(loops)})", errors)
        for loop in loops:
            check(loop.get("source") in nodes, f"feedback loop source '{loop.get('source')}' valid", errors)
            check(loop.get("target") in nodes, f"feedback loop target '{loop.get('target')}' valid", errors)
            check(loop.get("max_iterations", 0) >= 1, f"feedback loop '{loop.get('name')}' has max_iterations", errors)
            
        # Validate Verification Gates
        gates = graph.get("verification_gates", [])
        check(len(gates) == 7, f"exactly 7 verification gates (GATE-0 to GATE-6) defined (found {len(gates)})", errors)
        for gate in gates:
            check(bool(gate.get("gate_id")), f"gate has ID: {gate.get('gate_id')}", errors)
            check(gate.get("owner") in nodes, f"gate owner '{gate.get('owner')}' is valid node", errors)

        for node_name, node_data in nodes.items():
            check(isinstance(node_data.get("type"), str), f"node {node_name} has type", errors)
            check(isinstance(node_data.get("agent"), str), f"node {node_name} has agent", errors)
            check(isinstance(node_data.get("description"), str), f"node {node_name} has description", errors)
            check(isinstance(node_data.get("reads"), list), f"node {node_name} has reads list", errors)
            check(isinstance(node_data.get("writes"), list), f"node {node_name} has writes list", errors)
            
        routes = graph.get("revision_routes", {})
        check(bool(routes), "revision routes defined", errors)
        for dim, target in routes.items():
            check(target in nodes, f"revision route '{dim}' targets valid node '{target}'", errors)
        for dim in ("edit_scope", "annotation_mapping", "collateral_change"):
            check(routes.get(dim) == "edit-sanitizer", f"{dim} routes to edit-sanitizer", errors)
        for dim in ("concept_originality", "creative_ideation"):
            check(routes.get(dim) == "creative-director", f"{dim} routes to creative-director", errors)
        check(routes.get("insight_depth") == "insight-mining", "insight_depth routes to insight-mining", errors)
        check(routes.get("pattern_saturation") == "campaign-canon", "pattern_saturation routes to campaign-canon", errors)
        check(routes.get("activation_mechanic") == "brand-activation", "activation_mechanic routes to brand-activation", errors)
        check(routes.get("narrative_arc") == "visual-storytelling", "narrative_arc routes to visual-storytelling", errors)
        
        priorities = graph.get("signal_priorities", [])
        check(len(priorities) == 11, f"signal priorities count is 11 (found {len(priorities)})", errors)
        for idx, prio in enumerate(priorities, start=1):
            check(prio.get("level") == idx, f"priority level {idx} matches index", errors)
    except Exception as ex:
        check(False, f"routing graph validation error: {ex}", errors)


def validate_lock_precedence():
    def can_overwrite(existing_prio: int, incoming_prio: int) -> bool:
        return incoming_prio < existing_prio
    assert not can_overwrite(existing_prio=2, incoming_prio=10)
    assert not can_overwrite(existing_prio=1, incoming_prio=2)
    assert can_overwrite(existing_prio=10, incoming_prio=2)


def main() -> int:
    errors: list[str] = []
    print("Validating Design Neural Mesh orchestration graph, layers, loops, and gates...")
    validate_schemas(errors)
    validate_routing_graph(errors)
    try:
        validate_lock_precedence()
        print("PASS lock precedence logic verified")
    except AssertionError as ex:
        check(False, f"lock precedence logic failed: {ex}", errors)
    print(f"\nMesh validation: {'PASS' if not errors else 'FAIL'}")
    if errors:
        for e in errors:
            print(f" - {e}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
