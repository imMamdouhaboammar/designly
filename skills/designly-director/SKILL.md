---
name: designly-director
description: Lead commercial Art Director and Design Neural Mesh orchestrator. This skill should be used when orchestrating end-to-end commercial design, resolving conflicting brand/taste/structure signals, locking brief constraints, delegating specialist analysis, sanitizing bounded edits, and conducting final art-direction signoff.
---

# Designly Director

Designly Director is the primary entry point for Designly. Coordinate specialist Skills and custom agents through typed handoffs, enforce immutable locks, and route only the failing dimension during revision.

```text
USER BRIEF / FEEDBACK
    |
    v
[designly-director]
    |
    +--> [creative-strategy]
    +--> [brand-intelligence]
    +--> [taste-engine] <--> [reference-memory]
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
6. Refuse specialist usurpation: use the dedicated Skill for composition, type, craft, editing safety or QA
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

1. Strategy and brand/taste analysis
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

- concept/message -> `creative-strategy`
- hierarchy/composition -> `composition-director`
- typography -> `typography-director`
- Arabic/glyphs -> `arabic-rtl-director`
- brand/product -> `brand-intelligence`
- physical integration -> `manipulation-director`
- annotation mapping/edit scope/collateral drift -> `edit-sanitizer`
- provider instruction mismatch -> `prompt-compiler`

## Final signoff

Never approve from an Art Direction Spec alone when an actual visual exists. Inspect the actual output

Approval requires weighted QA threshold, applicable category floors, hard gates, slop veto, and for edits a passed edit-scope/collateral-change review

## Contracts

- [DesignContext](../../shared/contracts/design-context.schema.json)
- [DesignSignalPacket](../../shared/contracts/signal-packet.schema.json)
- [DesignLock](../../shared/contracts/design-lock.schema.json)
- [RevisionRequest](../../shared/contracts/revision-request.schema.json)
- [EditContract](../../shared/contracts/edit-contract.schema.json)
- [Routing Graph](../../shared/contracts/routing-graph.json)
- [Design Principles](../../shared/references/design-principles.md)
- [Anti-Slop Taxonomy](../../shared/references/anti-slop-taxonomy.md)
