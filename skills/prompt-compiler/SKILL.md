---
name: prompt-compiler
description: Image-generation and image-edit instruction compiler. This skill should be used when translating an approved Art Direction Spec or a ready EditContract into precise provider/model-ready instructions, linting prompt slop, or preparing execution for the host image tool without changing upstream creative decisions.
---

# Prompt Compiler

Compile approved design decisions into executable image instructions. Do not invent the concept, repair weak hierarchy, reinterpret annotations, or broaden edit scope.

## Preconditions

### Generation

Require approved strategy/composition/craft state appropriate to the task

### Editing, inpainting, annotation-guided correction

Require a typed `EditContract` from `edit-sanitizer` with

- `status: ready`
- `execution_allowed: true`
- approved `source_checkpoint`
- normalized target geometry
- atomic requested mutations
- protected regions and semantic locks
- acceptance checks

If these are missing, route to `edit-sanitizer`. Do not compile a best-effort local edit from raw feedback

## Compilation rules

1. State subject identity and required invariants first
2. Express composition as relationships, not disconnected style words
3. Use camera language only when it materially changes the visual result
4. Preserve brand, product, copy, and campaign locks verbatim
5. Include only likely failure exclusions for the current task
6. Keep provider-specific syntax modular and subordinate to the Art Direction Spec
7. When the host has a native image tool, use its supported interface instead of inventing API parameters
8. Apply inclusive visual representation rules: eliminate clone faces, mandate authentic ethnic features and melanin-calibrated lighting

## Bounded edit compilation

Compile the sanitized contract in this order

1. Approved source checkpoint
2. Exact semantic target and normalized/native geometry if the host accepts region data
3. One atomic allowed mutation
4. Identity, geometry, text, and style locks
5. Protected-region rule for all non-target content
6. Boundary blending allowance limited to what is needed for believable integration
7. Acceptance checks
8. Retry rule: restart from the approved checkpoint if collateral drift is material

Use language such as

`Edit only the selected bottle-cap region. Change the cap finish from matte black to brushed silver. Keep the bottle silhouette, label, logo, crop, perspective, background, lighting direction, and color grade materially stable. Do not add, remove, move, restyle, or rewrite anything outside the target. Allow only the minimal edge blending needed to integrate the new cap finish. If the result changes protected content, reject it and retry from the approved source checkpoint.`

Do not claim literal pixel identity unless the available editor guarantees it deterministically

## Copy correction

- exact copy is immutable
- never ask the image model to invent replacement copy
- Arabic copy requires `arabic-rtl-director` review before execution
- if text correctness remains unreliable, generate/retain the visual foundation and use a deterministic text workflow where the host supports one

## Prompt lint

Run

```bash
python3 scripts/prompt_lint.py "<compiled instruction>"
python3 scripts/test_prompt_lint.py
```

Reject prompt text when vague quality adjectives or effect stacks replace visual decisions

## Output

Return `generation_state` with

- operation: `generate` or `edit`
- provider/host assumptions actually verified
- compiled instruction
- source checkpoint when editing
- edit contract ID when editing
- acceptance checks
- likely failure exclusions

---

## Cross-Skill Neural Connections & References

### Peer & Downstream Skills
- [Edit Sanitizer](../edit-sanitizer/SKILL.md) — Upstream sanitized EditContract provider
- [Photography Director](../photography-director/SKILL.md) — Optical parameters and lighting models
- [Manipulation Director](../manipulation-director/SKILL.md) — Compositing physics and boundary blending rules
- [Visual QA](../visual-qa/SKILL.md) — Downstream independent visual verification gate
- [Designly Director](../designly-director/SKILL.md) — Orchestrator and state owner

### Schemas & References
- [Prompt Compiler Guide](../../shared/references/prompt-compiler.md) — Model prompt translation rules
- [Model Guides](../../shared/references/model-guides.md) — Provider-specific nuances
- [Inclusive Representation](../../shared/references/inclusive-representation-and-ethics.md) — Anti-bias prompting rules
- [Edit Contract](../../shared/contracts/edit-contract.schema.json) — Local edit schema
- [Signal Packet](../../shared/contracts/signal-packet.schema.json) — Neural Mesh handoff
