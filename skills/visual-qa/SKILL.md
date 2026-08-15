---
name: visual-qa
description: Independent visual quality assurance, hard-gate auditor, and targeted revision router. This skill should be used when reviewing generated or edited visuals, testing hierarchy/craft/brand fidelity, detecting AI slop, checking bounded-edit collateral drift, issuing approval verdicts, or routing targeted RevisionRequests.
---

# Visual QA

Review the actual visual independently. Do not defend upstream decisions and do not approve an uninspected hypothetical output

## Core review

Evaluate applicable categories including

- brief accuracy and primary message
- concept strength
- hierarchy and composition
- grouping, spacing and crop
- typography and exact copy
- color/contrast
- brand fidelity
- product fidelity
- physical believability
- cultural/platform fit
- overall craft
- AI slop

Weighted score must meet the configured threshold and every applicable category floor must pass

## Hard gates

Fail regardless of average when applicable

- required copy is wrong
- Arabic glyphs/connections or RTL behavior are malformed
- official logo/mark is malformed
- supplied product identity/proportions materially drift
- focal anatomy or physical interaction has a critical defect
- protected edit content changes materially outside what boundary blending requires
- local edit changes crop, canvas, camera, layout, lighting, text, identity or style that the EditContract locked
- annotation was applied to the wrong semantic target
- AI-slop veto triggers

## Bounded-edit review

When `edit_state` exists, compare output to the approved `source_checkpoint`, not to a previous failed edit

Evaluate three separate dimensions

### Target accuracy

Did the intended target receive exactly the requested mutation

### Edit-scope accuracy

Did any unrequested object, text, crop, layout, camera, lighting, brand, product, or style property change materially

### Collateral change

Allow minimal transition/blending immediately around the edited boundary when needed for believable integration. Do not call that a failure by itself

Fail when drift is material, unrelated to target integration, or violates an identity/geometry/style lock

Do not claim generative editing guarantees literal pixel identity. If the host provides deterministic masks/pixel-preservation guarantees, use those stronger checks explicitly

## Perception checks

Use the smallest relevant set

- one-second hierarchy test
- thumbnail test
- squint/blur value-mass test
- grayscale hierarchy test
- edge/tangency/crop test
- brand-off specificity test
- effect-subtraction test
- physics pass
- character-by-character copy pass
- source-vs-output edit-scope pass

## AI slop veto

Block on

- any critical finding
- 2+ major findings
- 4+ minor findings
- cumulative pressure >= 6, minor=1 and major=3

## Revision routing

Return one `RevisionRequest` to the smallest responsible node

- concept/message -> `creative-strategy`
- hierarchy/composition -> `composition-director`
- typography -> `typography-director`
- Arabic -> `arabic-rtl-director`
- brand/product identity -> `brand-intelligence`
- physical integration -> `manipulation-director`
- wrong annotation target -> `edit-sanitizer` with `annotation_mapping`
- over-broad edit scope -> `edit-sanitizer` with `edit_scope`
- collateral drift -> `edit-sanitizer` with `collateral_change`
- provider instruction mismatch after a valid contract -> `prompt-compiler`

For failed bounded edits, require retry from the approved source checkpoint. Never repair a drifted failure by chaining another edit onto it

## Output

Return

- `qa_state`
- scores and applicable floors
- hard-gate verdicts
- slop findings
- for edits: target accuracy, edit-scope accuracy, collateral-change evidence
- `RevisionRequest` only when failed

## Tools

```bash
python3 scripts/score_review.py assets/visual-review.template.json
python3 scripts/test_gates.py
```

## References

- [Visual Review Schema](schemas/visual-review.schema.json)
- [Revision Request](../../shared/contracts/revision-request.schema.json)
- [Edit Contract](../../shared/contracts/edit-contract.schema.json)
- [Visual QA & Revisions](../../shared/references/visual-qa-and-revisions.md)
- [AI Slop Taxonomy](../../shared/references/ai-slop-taxonomy.md)
