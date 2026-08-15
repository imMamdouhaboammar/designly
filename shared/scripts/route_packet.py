#!/usr/bin/env python3
"""
Route packets, handle revision re-routing, and resolve signal conflicts based on Neural Mesh rules.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
from typing import Any, Dict, Optional

ROOT = Path(__file__).resolve().parents[2]
GRAPH_PATH = ROOT / "shared/contracts/routing-graph.json"

class MeshRouter:
    def __init__(self, graph_path: Optional[Path] = None):
        self.graph_path = graph_path or GRAPH_PATH
        self.graph = json.loads(self.graph_path.read_text(encoding="utf-8"))
        self.nodes = self.graph.get("nodes", {})
        self.revision_routes = self.graph.get("revision_routes", {})
        self.priorities = {p["level"]: p["name"] for p in self.graph.get("signal_priorities", [])}

    def route_revision(self, revision_request: Dict[str, Any]) -> str:
        """
        Determines the single responsible specialist node for a defect.
        """
        target = revision_request.get("target_node")
        if target and target in self.nodes:
            return target
        
        dim = revision_request.get("failing_dimension", "")
        if dim in self.revision_routes:
            return self.revision_routes[dim]
        
        # Fallback to director
        return "designly-director"

    def can_apply_decision(self, current_lock: Optional[Dict[str, Any]], incoming_priority: int) -> bool:
        """
        Returns True if incoming decision has sufficient priority to overwrite current lock.
        Lower numerical level means higher authority (1 = highest, 11 = lowest).
        """
        if not current_lock:
            return True
        existing_priority = current_lock.get("priority", 11)
        if current_lock.get("immutable", False) and existing_priority <= incoming_priority:
            return False
        return incoming_priority < existing_priority

    def resolve_conflicts(self, locks: list[dict], incoming_decisions: list[dict]) -> tuple[list[dict], list[dict]]:
        """
        Filters incoming decisions against existing locks. Returns (applied_decisions, vetoed_decisions).
        """
        applied = []
        vetoed = []
        lock_map = {l["target_field"]: l for l in locks}
        
        for dec in incoming_decisions:
            field = dec.get("key")
            incoming_prio = dec.get("priority", 11)
            current_lock = lock_map.get(field)
            if self.can_apply_decision(current_lock, incoming_prio):
                applied.append(dec)
            else:
                vetoed.append({
                    "decision": dec,
                    "reason": f"Blocked by existing lock '{current_lock['lock_id']}' with higher priority {current_lock['priority']} (incoming was {incoming_prio})"
                })
        return applied, vetoed

def main() -> int:
    router = MeshRouter()
    print(f"MeshRouter initialized with {len(router.nodes)} nodes.")
    print("Testing revision routing for failing dimensions:")
    for dim, target in router.revision_routes.items():
        routed = router.route_revision({"failing_dimension": dim})
        print(f"  {dim} -> {routed} (matches {target})")
        assert routed == target
    print("All sample revision routes verified.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
