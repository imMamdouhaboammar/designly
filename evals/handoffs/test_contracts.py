#!/usr/bin/env python3
"""Test Design Neural Mesh JSON contracts at their public seams."""
from __future__ import annotations
import copy
import json
import jsonschema
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTRACTS_DIR = ROOT / "shared/contracts"


def load_schema(name: str) -> dict:
    return json.loads((CONTRACTS_DIR / name).read_text(encoding="utf-8"))


def validates(instance: dict, schema: dict) -> bool:
    try:
        jsonschema.validate(instance=instance, schema=schema)
        return True
    except jsonschema.ValidationError:
        return False


def main() -> int:
    failures = 0
    lock_schema = load_schema("design-lock.schema.json")
    packet_schema = load_schema("signal-packet.schema.json")
    revision_schema = load_schema("revision-request.schema.json")
    edit_schema = load_schema("edit-contract.schema.json")
    context_schema = load_schema("design-context.schema.json")

    lock = {"lock_id":"LCK-001","target_field":"primary_message","locked_value":"Pure Sound","locked_by":"user","priority":1,"reason":"Exact copy","immutable":True}
    if validates(lock, lock_schema): print("PASS valid DesignLock")
    else: failures += 1; print("FAIL valid DesignLock")
    bad = copy.deepcopy(lock); bad["extra"] = True
    if not validates(bad, lock_schema): print("PASS extra DesignLock field rejected")
    else: failures += 1; print("FAIL extra DesignLock field accepted")

    packet = {
        "packet_id":"PKT-001","from":"brand_guardian","to":"designly_director","job":"brand-audit",
        "decisions":[],"evidence":["brand manual"],"confidence":0.95,"hard_vetoes":[],"soft_warnings":[],"unresolved":[],"recommended_next":["composition-director"]
    }
    if validates(packet, packet_schema): print("PASS valid DesignSignalPacket")
    else: failures += 1; print("FAIL valid DesignSignalPacket")
    bad_packet = copy.deepcopy(packet); bad_packet["confidence"] = 1.5
    if not validates(bad_packet, packet_schema): print("PASS invalid confidence rejected")
    else: failures += 1; print("FAIL invalid confidence accepted")

    revision = {
        "revision_id":"REV-EDIT-001","origin_packet_id":"PKT-009","source_qa":"visual_reviewer",
        "target_node":"edit-sanitizer","failing_dimension":"collateral_change",
        "defect_description":"Background lighting drifted outside the cap edit",
        "evidence":["source-vs-output comparison"],"category_floor_failed":False,"slop_finding":None,
        "required_delta":"Rebuild the bounded edit from the approved source checkpoint","protected_regions":["non-target complement"]
    }
    if validates(revision, revision_schema): print("PASS edit-sanitizer RevisionRequest")
    else: failures += 1; print("FAIL edit-sanitizer RevisionRequest")

    edit = {
        "edit_id":"EDT-001","source_asset_id":"approved-01","source_checkpoint":"approved-01","mode":"local_edit",
        "source_geometry":{"width":1200,"height":1500},"annotation_space":"pixels",
        "targets":[{"target_id":"TGT-1","semantic_target":"bottle cap","confidence":0.98,"geometry":{"kind":"bbox","x":450,"y":210,"width":180,"height":120}}],
        "requested_mutations":["change cap finish to brushed silver"],"forbidden_mutations":["no layout changes"],
        "identity_locks":["bottle label"],"geometry_locks":["crop"],"style_locks":["background lighting"],
        "mutation_budget":"one","protected_regions":[{"region_id":"NON_TARGET_COMPLEMENT","rule":"materially stable","geometry":None}],
        "exact_copy":None,"requires_arabic_review":False,"ambiguity":{"unresolved":False,"reasons":[]},
        "acceptance_checks":["target changed","non-target materially stable"],"iteration":1,"status":"ready","execution_allowed":True,"reasons":[]
    }
    if validates(edit, edit_schema): print("PASS valid EditContract")
    else: failures += 1; print("FAIL valid EditContract")
    bad_edit = copy.deepcopy(edit); bad_edit["surprise_global_restyle"] = True
    if not validates(bad_edit, edit_schema): print("PASS unknown EditContract property rejected")
    else: failures += 1; print("FAIL unknown EditContract property accepted")

    context = {
        "session_id":"DSN-1","task_type":"edit","objective":"correct cap","audience":{},"primary_message":"","desired_action":"",
        "platform":{},"cultural_context":{},"locks":[lock],"brand_state":{},"taste_state":{},"strategy_state":{},"composition_state":{},
        "typography_state":{},"craft_state":{},"campaign_state":{},"edit_state":edit,"generation_state":{},"qa_state":{}
    }
    resolver = jsonschema.RefResolver(base_uri=f"file://{CONTRACTS_DIR}/", referrer=context_schema)
    try:
        jsonschema.validate(instance=context, schema=context_schema, resolver=resolver)
        print("PASS DesignContext accepts edit_state")
    except Exception as ex:
        failures += 1; print(f"FAIL DesignContext edit_state: {ex}")

    print(f"\nContracts test suite: {'PASS' if failures == 0 else 'FAIL'} ({failures} failures)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
