---
name: edit-sanitizer
description: Pre-execution sanitizer for annotation-guided edits, inpainting, copy corrections, local retouching, and object replacement. This skill should be used when a user points at or annotates part of an existing image and expects a bounded change without collateral redesign, or when edit scope, mask geometry, exact copy, or protected regions must be validated before image execution.
---

# Edit Sanitizer

Edit Sanitizer is the fail-close boundary between user feedback/annotations and image-edit execution. It exists because generative image editors may reinterpret more of a source image than the user intended. Do not send a local-edit request directly to `prompt-compiler` until this Skill has produced a `ready` EditContract.

## Core rule

Convert feedback into the smallest explicit mutation that can satisfy the request

Do not treat a scribble, arrow, selection, bounding box, or phrase such as `fix this` as self-explanatory when more than one plausible target exists

## Workflow

1. Identify the approved source checkpoint
2. Resolve annotation coordinates against the source dimensions
3. Map the annotation to one semantic target
4. Split user feedback into atomic requested mutations
5. Reject or veto unrelated global restyling when the request says `only`, `just`, `this area`, or otherwise implies a bounded edit
6. Lock crop, canvas, perspective, identities, exact text, lighting, and unaffected composition unless the user explicitly targets one of them
7. Derive protected regions from the complement of the editable target plus semantic locks
8. Set a conservative mutation budget
9. Require Arabic review for Arabic copy corrections
10. Produce a typed EditContract
11. Only when status is `ready`, forward the contract to `prompt-compiler`

## Annotation handling

Treat annotation geometry and semantic intent as separate evidence

- `bbox`: validate positive area and source bounds
- `polygon`: require a valid polygon around the intended area
- `mask_ref`: require an actual mask reference
- `semantic`: require one clearly identifiable object or text region
- `normalized`: convert coordinates to native pixels before execution

If two plausible targets have similar confidence, return `clarify` rather than guessing

## Drift prevention

Every retry starts from `source_checkpoint`, which must be the last approved source

Never chain a second corrective edit from a failed or visibly drifted render

Maximum edit loop: 3 attempts. If the same defect persists or collateral changes grow, stop and return the evidence rather than continuing destructive edits

## Bounded-edit vetoes

Veto execution when

- a local edit also asks to restyle the whole image
- there are multiple unrelated mutations that should be separate edits
- the target is outside the source or has zero area
- the annotation cannot be mapped confidently
- exact replacement copy is missing for copy correction
- the retry source is not the approved checkpoint

## Preservation language

Do not promise literal pixel identity from a generative editor

Require material stability outside the edit target and validate collateral changes after execution

If the host provides a deterministic mask/editor that guarantees pixel preservation, that stronger guarantee may be used explicitly

## Output

Return the EditContract plus a short execution verdict

- `ready`: may proceed to Prompt Compiler
- `clarify`: ask one target/scope question, do not execute
- `reject`: invalid geometry/source/copy contract, do not execute
- `veto`: conflicting or over-broad mutation request, do not execute

## Runtime helper

```bash
python3 ../../shared/scripts/sanitize_edit.py < edit-request.json
```

## Shared contracts

- [Edit Contract](../../shared/contracts/edit-contract.schema.json)
- [Image Editing Guidance](../../shared/references/image-editing.md)
- [Routing Graph](../../shared/contracts/routing-graph.json)
