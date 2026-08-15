# Prompt Compiler

Compile model-ready language only after the upstream design or edit preflight passes

## Principle

A strong image instruction expresses relationships, invariants and a bounded job

Do not substitute a list of style keywords for art direction

## Generate vs edit

Generation and bounded editing are different execution contracts

### Generation

Compile an approved Art Direction Spec

### Existing-image edit

Compile only a `ready` EditContract produced by `edit-sanitizer`

Never translate raw annotation feedback directly into an image-edit prompt

## Generation prompt order

Use the smallest useful subset of

1. subject and exact identity
2. action or relationship
3. environment
4. hierarchy and composition
5. text field or exact copy
6. camera relationship
7. light
8. material/environment interaction
9. color/value behavior
10. brand locks
11. likely failure exclusions
12. output ratio/format

## Edit instruction order

1. approved source checkpoint
2. exact semantic target and region/mask when the host accepts it
3. one atomic requested mutation
4. identity locks
5. geometry locks
6. text locks/exact replacement copy
7. style locks
8. non-target protection
9. minimal boundary-blending allowance
10. acceptance checks
11. rollback/retry rule

Example

`Edit only the selected bottle-cap region. Change the cap finish from matte black to brushed silver. Keep the bottle silhouette, label, logo, crop, camera perspective, background, lighting direction, and color grade materially stable. Do not add, remove, move, restyle, or rewrite any non-target content. Allow only the minimal edge blending needed to integrate the cap finish. If protected content drifts, reject this attempt and retry from the approved source checkpoint.`

Do not write `preserve 100% of pixels` unless the actual editor guarantees that behavior

## Annotation discipline

A pointer or mask indicates location, not necessarily intent

If `edit-sanitizer` has not resolved one target and one mutation, do not compile

## Exact copy

Use only supplied exact replacement text

Never ask the image model to invent copy during a correction

Require Arabic review for Arabic replacement text before execution

## Negative-instruction discipline

Include exclusions only for likely failure modes in the current task

A strong positive structure usually needs fewer negative instructions

## Reference prompting

State which visual grammar comes from which reference. Do not say only `match the style`

## Prompt disclosure

When the host can execute directly, keep compiled implementation instructions internal unless the user asks to see them

When the user asks for a prompt, return the approved compiled prompt without scratch reasoning
