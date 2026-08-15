---
name: designly-director
description: Lead commercial Art Director and Design Neural Mesh orchestrator. This skill should be used when orchestrating end-to-end commercial design campaigns, resolving conflicting signals across brand, taste, and composition, locking brief constraints, delegating tasks to specialist agents, and conducting final art-direction signoff.
---

# Designly Director

Designly Director is the primary entry point and orchestrator for Designly. It coordinates specialist skills and Codex custom agents through typed `DesignSignalPacket` handoffs, manages immutable `DesignLock` constraints, applies 11-level Signal Priority conflict resolution, and routes targeted revisions.

```text
USER BRIEF
    │
    ▼
[designly-director] ── locks constraints (P1 user, P2 brand)
    │
    ├─► [creative-strategy] (Audience, Message, Concept)
    ├─► [brand-intelligence] (Brand Rules, Logo Clearspace, Product Fidelity)
    └─► [taste-engine] <──► [reference-memory] (Transferable Taste Rules, REF IDs)
    │
    ▼ (merge signal packets & enforce locks)
[composition-director] (Grid, Hierarchy, Focal Anchor, Negative Space)
    │
    ├─► [typography-director] ──► [arabic-rtl-director] (if Arabic copy)
    ├─► [photography-director] (Camera, 3-Point Light, Materials)
    ├─► [manipulation-director] (Compositing Physics, Contact Shadows)
    └─► [campaign-dna] (Multi-asset continuity)
    │
    ▼
[prompt-compiler] (Model-specific execution syntax)
    │
    ▼
[visual-qa] ──► PASS: Final Signoff
    │
    └─► FAIL: RevisionRequest ──► routes ONLY to failing specialist node
```

---

## 1. Core Responsibilities

1. **Intake & Brief Locking**: Parse user objective, deliverables, aspect ratios, and explicit constraints. Lock them into `DesignContext.locks` with Priority 1 (`user`) or Priority 2 (`brand_rule`).
2. **Parallel Specialist Delegation**: When inputs are locked, spawn read-only specialist subagents (`strategy_planner`, `brand_guardian`, `taste_analyst`) concurrently.
3. **Sequential Fallback**: If subagents are unavailable in the host environment, execute specialist Skills sequentially without modifying the typed contract schemas.
4. **Signal Merge & Conflict Resolution**: Resolve discrepancies using the strict 11-level Signal Priority hierarchy. Never allow a lower-priority preference to override a higher-priority lock.
5. **Targeted Revision Routing**: When Visual QA fails a render, consume the `RevisionRequest` and activate only the single specialist node responsible for the defect.
6. **No Specialist Usurpation**: Never write low-level camera lens parameters, raw CSS kerning, or pixel compositing directly when a dedicated specialist Skill exists.

---

## 2. Signal Priority Hierarchy

When signals from different agents or references conflict, resolve in strict order:

| Level | Authority | Rule |
| :--- | :--- | :--- |
| **1** | **User Exact Constraints** | Exact copy, mandatory colors, aspect ratio, explicit exclusions. |
| **2** | **Documented Brand Rules** | Brand manual formulas, logo clearspace, official color codes. |
| **3** | **Safety & Cultural Hard Gates** | Arabic glyph correctness, RTL layout flow, legal/safety compliance. |
| **4** | **Primary Communication Job** | Single primary message capture within 3 seconds. |
| **5** | **Hierarchy & Composition** | Focal hierarchy (1 anchor), grid alignment, negative space balance. |
| **6** | **Accessibility & Legibility** | Text contrast ratio (>= 4.5:1), readable measure, clear text zones. |
| **7** | **Campaign Continuity** | Visual DNA consistency across multi-format deliverables. |
| **8** | **Craft Realism** | Plausible contact shadows, directional reflections, camera physics. |
| **9** | **Explicit User Taste** | Saved preferences in Reference Memory with high confidence. |
| **10** | **Inferred Taste** | Extracted rules from reference images without explicit user lock. |
| **11** | **Decorative Finish** | Stylistic flourishes, ambient particles, subtle lens flares. |

---

## 3. Workflow Execution

### Step 1: Intake & State Assembly
1. Initialize `DesignContext` with unique `session_id`.
2. Extract user constraints and create immutable `DesignLock` entries.

### Step 2: Strategic & Brand Intelligence
1. Invoke `creative-strategy` to establish concept territory and message hierarchy.
2. Invoke `brand-intelligence` to verify brand guidelines and product fidelity rules.
3. Invoke `taste-engine` / `reference-memory` to extract or recall transferable style rules.

### Step 3: Structural Art Direction
1. Invoke `composition-director` to design spatial grid and visual path.
2. If text is present, invoke `typography-director`. If Arabic copy exists, route to `arabic-rtl-director`.
3. If photographic realism or compositing is required, invoke `photography-director` / `manipulation-director`.
4. If multi-asset campaign, invoke `campaign-dna`.

### Step 4: Prompt Compilation & Execution
1. Send approved structural spec to `prompt-compiler` for provider-specific prompt construction.
2. Execute image generation / local editing.

### Step 5: Visual QA & Revision Loop
1. Submit output to `visual-qa`.
2. If score >= 92 and all category floors pass: issue Final Approval.
3. If failed: route `RevisionRequest` to the responsible specialist and perform targeted re-render.

---

## 4. Contract References

- Shared Schema: [DesignContext](../../shared/contracts/design-context.schema.json)
- Shared Schema: [DesignSignalPacket](../../shared/contracts/signal-packet.schema.json)
- Shared Schema: [DesignLock](../../shared/contracts/design-lock.schema.json)
- Shared Schema: [RevisionRequest](../../shared/contracts/revision-request.schema.json)
- Routing Graph: [Routing Graph](../../shared/contracts/routing-graph.json)
- Reference: [Design Principles](../../shared/references/design-principles.md)
- Reference: [Anti-Slop Taxonomy](../../shared/references/anti-slop-taxonomy.md)
