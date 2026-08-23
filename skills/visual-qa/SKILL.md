---
name: visual-qa
description: Independent visual quality assurance, hard-gate auditor, and targeted revision router. This skill should be used when reviewing generated or edited visuals, testing hierarchy/craft/brand fidelity, detecting AI slop, checking bounded-edit collateral drift, issuing approval verdicts, or routing targeted RevisionRequests.
---

# Visual QA

Review the actual visual independently. Do not defend upstream decisions and do not approve an uninspected hypothetical output.

## Core review

Evaluate applicable categories including:

- brief accuracy and primary message
- concept strength
- hierarchy and composition
- grouping, spacing and crop
- typography and exact copy
- color/contrast
- brand fidelity
- product fidelity
- physical believability
- cultural/platform fit and inclusive representation
- overall craft
- AI slop

Weighted score must meet the configured threshold and every applicable category floor must pass

## Hard gates

Fail regardless of average when applicable:

- required copy is wrong
- Arabic glyphs/connections or RTL behavior are malformed
- official logo/mark is malformed
- supplied product identity/proportions materially drift
- focal anatomy, human dignity, or physical interaction has a critical defect
- protected edit content changes materially outside what boundary blending requires
- local edit changes crop, canvas, camera, layout, lighting, text, identity or style that the EditContract locked
- annotation was applied to the wrong semantic target
- AI-slop veto triggers

## Bounded-edit review

When `edit_state` exists, compare output to the approved `source_checkpoint`, not to a previous failed edit. Evaluate target accuracy, edit-scope accuracy, and collateral change.

## Perception checks

- one-second hierarchy test
- thumbnail test
- squint/blur value-mass test
- grayscale hierarchy test
- edge/tangency/crop test
- brand-off specificity test
- 7-point inclusive representation review
- effect-subtraction test
- physics pass
- character-by-character copy pass
- source-vs-output edit-scope pass

## AI slop veto

Block on:
- any critical finding
- 2+ major findings
- 4+ minor findings
- cumulative pressure >= 6, minor=1 and major=3

## Revision routing

Return one `RevisionRequest` to the smallest responsible node:
- concept/originality -> `creative-director`
- insight depth -> `insight-mining`
- pattern saturation -> `campaign-canon`
- activation mechanic -> `brand-activation`
- narrative arc -> `visual-storytelling`
- strategy/message -> `creative-strategy`
- hierarchy/composition -> `composition-director`
- typography -> `typography-director`
- Arabic -> `arabic-rtl-director`
- brand/product identity -> `brand-intelligence`
- physical integration -> `manipulation-director`
- wrong annotation target -> `edit-sanitizer` with `annotation_mapping`
- over-broad edit scope -> `edit-sanitizer` with `edit_scope`
- collateral drift -> `edit-sanitizer` with `collateral_change`
- provider instruction mismatch -> `prompt-compiler`

---

## Cross-Skill Neural Connections & References

### Peer & Specialist Skills
- [Designly Director](../designly-director/SKILL.md) — Lead orchestrator and final signoff authority
- [Composition Director](../composition-director/SKILL.md) — Hierarchy & spatial layout revisions
- [Brand Intelligence](../brand-intelligence/SKILL.md) — Brand guidelines & product fidelity revisions
- [Edit Sanitizer](../edit-sanitizer/SKILL.md) — Bounded edit scope & annotation corrections
- [Prompt Compiler](../prompt-compiler/SKILL.md) — Provider prompt adjustments

### Schemas & References
- [Visual Review Schema](schemas/visual-review.schema.json) — Local review schema
- [Revision Request](../../shared/contracts/revision-request.schema.json) — Mesh revision contract
- [Edit Contract](../../shared/contracts/edit-contract.schema.json) — Bounded edit contract
- [Visual QA & Revisions](../../shared/references/visual-qa-and-revisions.md) — Review methodology
- [AI Slop Taxonomy](../../shared/references/ai-slop-taxonomy.md) — Slop families & severity criteria
- [Inclusive Representation](../../shared/references/inclusive-representation-and-ethics.md) — 7-point representation checklist
- [Software Architecture](../../shared/references/software-architecture-and-contracts.md) — Bounded contexts & lock hierarchy
