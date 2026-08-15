#!/usr/bin/env python3
"""
Test suite for Design Neural Mesh contracts, schemas, and typed handoffs.
"""
from __future__ import annotations
import copy
import json
import jsonschema
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTRACTS_DIR = ROOT / "shared/contracts"

def load_schema(name: str) -> dict:
    p = CONTRACTS_DIR / name
    return json.loads(p.read_text(encoding="utf-8"))

def main() -> int:
    failures = 0
    
    # 1. Load schemas
    context_schema = load_schema("design-context.schema.json")
    packet_schema = load_schema("signal-packet.schema.json")
    lock_schema = load_schema("design-lock.schema.json")
    revision_schema = load_schema("revision-request.schema.json")
    
    # 2. Test valid DesignLock
    sample_lock = {
        "lock_id": "LCK-001",
        "target_field": "primary_message",
        "locked_value": "Pure Sound, Zero Distraction",
        "locked_by": "user",
        "priority": 1,
        "reason": "Exact client brief headline constraint",
        "immutable": True
    }
    try:
        jsonschema.validate(instance=sample_lock, schema=lock_schema)
        print("PASS valid DesignLock schema validation")
    except Exception as ex:
        failures += 1
        print(f"FAIL valid DesignLock: {ex}")

    # 3. Test invalid DesignLock (missing priority, extra property)
    bad_lock = copy.deepcopy(sample_lock)
    del bad_lock["priority"]
    try:
        jsonschema.validate(instance=bad_lock, schema=lock_schema)
        failures += 1
        print("FAIL bad DesignLock (missing priority) should have failed validation")
    except jsonschema.ValidationError:
        print("PASS bad DesignLock (missing priority) rejected")

    bad_lock_extra = copy.deepcopy(sample_lock)
    bad_lock_extra["extra_prop"] = "illegal"
    try:
        jsonschema.validate(instance=bad_lock_extra, schema=lock_schema)
        failures += 1
        print("FAIL bad DesignLock (extra property) should have failed validation")
    except jsonschema.ValidationError:
        print("PASS bad DesignLock (extra property) rejected")

    # 4. Test valid DesignSignalPacket
    sample_packet = {
        "packet_id": "PKT-001",
        "from": "brand_guardian",
        "to": "designly_director",
        "job": "brand-audit",
        "decisions": [
            {
                "key": "brand_state.palette",
                "value": ["#000000", "#FFFFFF", "#FF3B30"],
                "rationale": "Official guidelines 2026",
                "priority": 2
            }
        ],
        "evidence": ["Brand guidelines PDF page 4", "Observed 3 reference packaging assets"],
        "confidence": 0.95,
        "hard_vetoes": [
            {
                "rule": "no-unapproved-accent-gradients",
                "reason": "Brand manual strictly forbids multi-color gradient fills on primary logo",
                "severity": "critical",
                "remediation": "Use flat #000000 or single-color knockout"
            }
        ],
        "soft_warnings": ["Secondary gold accent is optional for premium tiers only"],
        "unresolved": [],
        "recommended_next": ["composition-director"]
    }
    try:
        jsonschema.validate(instance=sample_packet, schema=packet_schema)
        print("PASS valid DesignSignalPacket schema validation")
    except Exception as ex:
        failures += 1
        print(f"FAIL valid DesignSignalPacket: {ex}")

    # 5. Test invalid DesignSignalPacket (missing required field: 'confidence')
    bad_packet = copy.deepcopy(sample_packet)
    del bad_packet["confidence"]
    try:
        jsonschema.validate(instance=bad_packet, schema=packet_schema)
        failures += 1
        print("FAIL bad DesignSignalPacket (missing confidence) should have failed")
    except jsonschema.ValidationError:
        print("PASS bad DesignSignalPacket (missing confidence) rejected")

    # 6. Test invalid confidence range (> 1.0)
    bad_packet_conf = copy.deepcopy(sample_packet)
    bad_packet_conf["confidence"] = 1.5
    try:
        jsonschema.validate(instance=bad_packet_conf, schema=packet_schema)
        failures += 1
        print("FAIL bad DesignSignalPacket (confidence > 1.0) should have failed")
    except jsonschema.ValidationError:
        print("PASS bad DesignSignalPacket (confidence > 1.0) rejected")

    # 7. Test valid RevisionRequest
    sample_revision = {
        "revision_id": "REV-001",
        "origin_packet_id": "PKT-009",
        "source_qa": "visual_reviewer",
        "target_node": "typography-director",
        "failing_dimension": "typography",
        "defect_description": "Headline text line-breaks across semantic phrase, damaging readability",
        "evidence": ["Headline broken after first word of hyphenated name", "Type floor score was 78 < 88"],
        "category_floor_failed": True,
        "slop_finding": None,
        "required_delta": "Adjust measure and font-size to keep primary headline on 2 balanced lines",
        "protected_regions": ["product packshot center-left", "brand logo top-right"]
    }
    try:
        jsonschema.validate(instance=sample_revision, schema=revision_schema)
        print("PASS valid RevisionRequest schema validation")
    except Exception as ex:
        failures += 1
        print(f"FAIL valid RevisionRequest: {ex}")

    # 8. Test valid DesignContext
    sample_context = {
        "session_id": "DSN-2026-0001",
        "task_type": "campaign",
        "objective": "Launch premium noise-canceling headphones in MENA market",
        "audience": {"demographic": "Audio enthusiasts & professionals 25-45"},
        "primary_message": "Pure Sound, Zero Distraction",
        "desired_action": "Pre-order on ecommerce store",
        "platform": {"aspect_ratio": "4:5", "safe_zones": "standard"},
        "cultural_context": {"region": "GCC", "language": "ar-SA", "reading_flow": "RTL"},
        "locks": [sample_lock],
        "brand_state": {"palette": ["#000000", "#FFFFFF"], "tone": "minimalist"},
        "taste_state": {"rules": ["directional key lighting", "matte finishes"]},
        "strategy_state": {"concept": "The Silence Chamber"},
        "composition_state": {"focal_point": "headphones at optical center"},
        "typography_state": {"headline": "نقاء الصوت بلا تشويش", "weight": "bold"},
        "craft_state": {"camera": "85mm f/2.8", "lighting": "soft rim light"},
        "campaign_state": {"family_id": "CAM-2026-A", "assets_count": 3},
        "generation_state": {"compiled_prompt": "Commercial studio shot of matte black headphones..."},
        "qa_state": {"approved": False, "scores": {"overall": 89}}
    }
    try:
        # Note: $ref in schema needs resolver or simple validation
        resolver = jsonschema.RefResolver(base_uri=f"file://{CONTRACTS_DIR}/", referrer=context_schema)
        jsonschema.validate(instance=sample_context, schema=context_schema, resolver=resolver)
        print("PASS valid DesignContext schema validation")
    except Exception as ex:
        failures += 1
        print(f"FAIL valid DesignContext: {ex}")

    print(f"\nContracts test suite: {'PASS' if failures == 0 else 'FAIL'} ({failures} failures)")
    return 1 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
