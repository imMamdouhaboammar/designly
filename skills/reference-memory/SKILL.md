---
name: reference-memory
description: Local-first reference memory and scoped preference ledger manager. This skill should be used when saving, recalling, updating, or deleting reference records with stable REF IDs (e.g. REF-1042), managing user likes/dislikes, or querying persistent taste preferences.
---

# Reference Memory

Reference Memory provides local-first, transparent persistence for user references, assigned design jobs, and scoped feedback ledgers. It uses stable human-readable IDs (`REF-####`) and does not make misleading claims of fine-tuning or modifying underlying model weights.

---

## 1. Core Workflow

1. **Reference Registration**:
   - Assign next available sequential ID: `REF-####` (e.g. `REF-1001`, `REF-1002`).
   - Store reference metadata, file path, source tags, and primary design jobs (e.g. `lighting`, `composition`, `palette`).

2. **Scoped Preference Feedback**:
   - When a user expresses a preference (e.g., "I love the rim light in REF-1042 but hate the typography"), scope the feedback precisely:
     - Record `likes: ["lighting.rim_light"]`
     - Record `dislikes: ["typography.layout"]`
   - Never allow a dislike on one dimension (typography) to discard or invalidate rules on another dimension (lighting).

3. **Recall & Filtering**:
   - Query references by job tag, domain (e.g. `fmcg`, `luxury`, `automotive`), or aesthetic keyword.
   - Return active Taste Profiles associated with the recalled reference.

4. **Output Contract**:
   - Emits structured JSON reference records and `DesignSignalPacket` containing `taste_state.reference_memory`.

---

## 2. CLI Tooling

Execute the local Reference Memory CLI:
```bash
# Add a new reference
python3 scripts/reference_memory.py add --id REF-1001 --title "Nordic Minimalist Poster" --jobs composition,palette

# Query existing references
python3 scripts/reference_memory.py list

# Recall specific reference
python3 scripts/reference_memory.py get REF-1001

# Record scoped feedback
python3 scripts/reference_memory.py feedback REF-1001 --like "lighting.soft_directional" --dislike "background.clutter"
```

---

## 3. Cross-Skill Neural Connections & References

### Peer & Downstream Skills
- [Taste Engine](../taste-engine/SKILL.md) — Extracting transferable rules from recalled references
- [Brand Intelligence](../brand-intelligence/SKILL.md) — Auditing reference tags against brand constraints
- [Designly Director](../designly-director/SKILL.md) — Lead orchestrator and memory state manager

### Schemas & References
- [Reference Memory Schema](schemas/reference-memory.schema.json) — Local schema
- [Reference Memory Guide](../../shared/references/reference-memory.md) — Usage rules
- [Signal Packet Schema](../../shared/contracts/signal-packet.schema.json) — Neural Mesh handoff
