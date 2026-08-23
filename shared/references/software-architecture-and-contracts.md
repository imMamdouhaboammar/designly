# Software Architecture & Neural Mesh Contracts

This reference governs the architectural integrity, bounded contexts, and dependency boundaries of the Designly Art Direction Neural Mesh.

---

## 1. Architectural Philosophy

1. **Domain-Driven Context Boundaries**:
   - Every Skill and Agent operates strictly within its bounded domain (Strategy, Insight, Ideation, Composition, Typography, Craft, Sanitization, QA).
   - Domain logic does not leak across boundaries. Specialists communicate via typed, validated JSON schemas (`DesignContext`, `DesignSignalPacket`, `DesignLock`, `EditContract`, `RevisionRequest`).

2. **Unidirectional State Mutation**:
   - Only `designly-director` possesses orchestration and write authority to mutate shared state.
   - All other 13 specialist Codex agents are read-only (`tools = ["read_file"]`) and emit immutable `DesignSignalPacket` handoffs.

3. **Explicit Lock Precedence (ADR Hierarchy)**:
   ```text
   Level 1: user_exact_constraints
   Level 2: documented_brand_rules
   Level 3: safety_legal_cultural_gates
   Level 4: primary_communication_job
   Level 5: hierarchy_and_composition
   Level 6: accessibility_and_legibility
   Level 7: campaign_continuity
   Level 8: craft_realism
   Level 9: explicit_user_taste_preference
   Level 10: inferred_taste_preference
   Level 11: decorative_finish
   ```
   *Rule: A lower-priority signal never overwrites a higher-priority lock.*

4. **Targeted Revision Routing Over Whole-System Rewrites**:
   - When Visual QA fails, the system computes the exact failing dimension (`failing_dimension`) and dispatches a `RevisionRequest` exclusively to the smallest responsible specialist node, preserving upstream invariants.
