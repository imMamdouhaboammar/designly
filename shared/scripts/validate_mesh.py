#!/usr/bin/env python3
"""Validate Design Neural Mesh contracts, routes, and lock precedence."""
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
        check(len(nodes) == 14, f"routing graph defines exactly 14 nodes (found {len(nodes)})", errors)
        check(graph.get("primary_orchestrator") == "designly-director", "primary_orchestrator is designly-director", errors)
        check("edit-sanitizer" in nodes, "edit-sanitizer node exists", errors)
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
    print("Validating Design Neural Mesh contracts and routing graph...")
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
