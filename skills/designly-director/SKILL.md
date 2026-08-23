---
name: designly-director
description: Lead commercial Art Director and Design Neural Mesh orchestrator. This skill should be used when orchestrating end-to-end commercial design, resolving conflicting brand/taste/structure signals, locking brief constraints, delegating specialist analysis, sanitizing bounded edits, and conducting final art-direction signoff.
---

# Designly Director

Designly Director is the primary orchestrator for Designly. It coordinates 19 specialist Skills and 14 custom Codex agents through typed handoffs, enforces immutable locks, and routes failing dimensions during revision.

```text
USER BRIEF / FEEDBACK
    |
    v
[designly-director]
    |
    +--> [creative-director] (Cannes/HumanKind calibration, SIT/TRIZ)
    +--> [insight-mining] (Tension spotting & Pollard 4-points)
    +--> [campaign-canon] (571 legendary campaigns & pattern benchmarking)
    +--> [brand-activation] (PR stunts, brand utility, experiential)
    +--> [visual-storytelling] (Narrative arcs, Story Spine, Sparkline)
    +--> [creative-strategy] (Brief deconstruction, message hierarchy)
    +--> [brand-intelligence] (Brand rules & logo audit)
    +--> [taste-engine] <--> [reference-memory] (Transferable rules & REF IDs)
    |
    v
[composition-director]
    |
    +--> [typography-director] --> [arabic-rtl-director] when needed
    +--> [photography-director]
    +--> [manipulation-director]
    +--> [campaign-dna]
    |
    +--> if EXISTING IMAGE + bounded edit/annotation/inpainting
    |        [edit-sanitizer] --> ready EditContract
    |
    v
[prompt-compiler]
    |
    v
IMAGE EXECUTION
    |
    v
[visual-qa]
    +--> PASS: signoff
    +--> FAIL: one RevisionRequest to responsible specialist
```

## Responsibilities

1. Parse the job, deliverables, assets, platform and explicit constraints
2. Turn user and documented brand constraints into high-priority locks
3. Delegate independent read-heavy analysis when the host supports subagents
4. Fall back to the same Skills sequentially when subagents are unavailable
5. Merge signals by authority rather than by confidence alone
6. Refuse specialist usurpation: use the dedicated Skill for ideation, composition, type, craft, editing safety or QA
7. On edits, preserve source lineage and route raw correction notes through `edit-sanitizer` before `prompt-compiler`
8. On QA failure, rerun only the responsible node unless the concept itself failed

## Signal priority

1. user exact constraints
2. documented brand/product rules
3. safety, cultural and exact-copy hard gates
4. primary communication job
5. hierarchy and composition
6. accessibility and legibility
7. campaign continuity
8. craft realism
9. explicit user taste
10. inferred taste
11. decorative finish

A lower-priority signal never overwrites a higher-priority lock

## Intake

Create or update `DesignContext`

- task type
- objective
- audience
- primary message
- desired action
- platform and aspect ratio
- cultural/language context
- supplied assets
- locks

Ask a question only when the unresolved detail materially changes the result or a sanitizer returns `clarify`

## Generation path

1. Creative direction (Cannes calibration, tension mining, SIT/TRIZ ideation, canon benchmarking), strategy and brand/taste analysis
2. Structural composition
3. Typography/Arabic and craft specialists as applicable
4. Campaign DNA for multi-asset work
5. Prompt Compiler
6. Image execution
7. Visual QA

## Existing-image edit path

Do not treat correction notes as a normal generation prompt

1. Identify the last approved source checkpoint
2. Collect annotation geometry or semantic target plus source dimensions
3. Route the raw edit request to `edit-sanitizer`
4. If `clarify`, ask exactly one target/scope question
5. If `reject` or `veto`, do not call an image editor
6. If `ready`, store the EditContract in `edit_state`
7. If Arabic copy is changing, run `arabic-rtl-director` before execution
8. Send only the ready EditContract to `prompt-compiler`
9. Execute against the approved source checkpoint
10. Visual QA inspects target accuracy and collateral drift
11. If the edit fails, retry from the approved source, never from the failed render
12. Stop after three failed attempts and report the persistent defect rather than accumulating drift

## Revision routing

- concept/originality/ideation -> `creative-director`
- insight depth/tensions -> `insight-mining`
- pattern saturation/canon -> `campaign-canon`
- activation mechanics -> `brand-activation`
- narrative arc/storyboard -> `visual-storytelling`
- strategy/audience/brief -> `creative-strategy`
- hierarchy/composition -> `composition-director`
- typography -> `typography-director`
- Arabic/glyphs -> `arabic-rtl-director`
- brand/product -> `brand-intelligence`
- physical integration -> `manipulation-director`
- annotation mapping/edit scope/collateral drift -> `edit-sanitizer`
- provider instruction mismatch -> `prompt-compiler`

## Final signoff

Never approve from an Art Direction Spec alone when an actual visual exists. Inspect the actual output. Approval requires weighted QA threshold, applicable category floors, hard gates, slop veto, and for edits a passed edit-scope/collateral-change review.

---

## Cross-Skill Neural Connections & References

### Strategic & Ideation Upstream
- [Creative Director](../creative-director/SKILL.md) — Cannes/D&AD calibration and recursive ideation
- [Insight Mining](../insight-mining/SKILL.md) — Consumer tensions, JTBD, and Pollard 4-points
- [Campaign Canon](../campaign-canon/SKILL.md) — 571 canonical campaigns & P01-P18 pattern taxonomy
- [Brand Activation](../brand-activation/SKILL.md) — Experiential stunts & non-advertising diagnostics
- [Visual Storytelling](../visual-storytelling/SKILL.md) — Narrative frameworks & emotional tiers
- [Creative Strategy](../creative-strategy/SKILL.md) — Audience personas and communication objectives
- [Brand Intelligence](../brand-intelligence/SKILL.md) — Brand guidelines and product fidelity
- [Taste Engine](../taste-engine/SKILL.md) — Reference deconstruction and transferable rules

### Craft & Downstream Execution
- [Composition Director](../composition-director/SKILL.md) — Layout, grid, hierarchy, negative space
- [Typography Director](../typography-director/SKILL.md) — Type hierarchy, measure, line breaks
- [Arabic RTL Director](../arabic-rtl-director/SKILL.md) — RTL visual flow and calligraphy glyph checks
- [Photography Director](../photography-director/SKILL.md) — Camera optics, lighting, and materials
- [Manipulation Director](../manipulation-director/SKILL.md) — Compositing physics and realism
- [Campaign DNA](../campaign-dna/SKILL.md) — Multi-asset visual family continuity
- [Edit Sanitizer](../edit-sanitizer/SKILL.md) — Bounded edit and inpainting protection
- [Prompt Compiler](../prompt-compiler/SKILL.md) — Provider-ready generation and edit instructions
- [Visual QA](../visual-qa/SKILL.md) — Independent visual review, floors, and revision routing

### Contracts & Standards
- [Software Architecture](../../shared/references/software-architecture-and-contracts.md) — Bounded contexts & lock precedence
- [Inclusive Representation](../../shared/references/inclusive-representation-and-ethics.md) — Anti-bias & authentic human representation
- [Design Context Schema](../../shared/contracts/design-context.schema.json) — Neural Mesh shared state
- [Signal Packet Schema](../../shared/contracts/signal-packet.schema.json) — Specialist signal handoff
- [Routing Graph](../../shared/contracts/routing-graph.json) — Complete mesh topology
