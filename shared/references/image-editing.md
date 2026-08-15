# Image Editing and Preservation

Use edit mode when the source image itself is an asset to preserve

## Mandatory pre-execution boundary

Raw user feedback, arrows, scribbles, selections, masks, bounding boxes, or phrases such as `fix this` are not executable image instructions by themselves

Route bounded edits through `edit-sanitizer` first and require a `ready` EditContract before `prompt-compiler`

## Edit Contract

Define

- approved source checkpoint
- source dimensions
- annotation coordinate space
- one semantic target or an explicitly approved multi-target edit
- target geometry or mask reference
- atomic allowed mutations
- forbidden mutations
- identity locks
- geometry locks
- style locks
- protected regions
- exact replacement copy when applicable
- mutation budget
- acceptance checks
- retry/rollback rule

## Annotation semantics

Separate where the user pointed from what the user means

A red circle around two nearby objects does not prove which one is the target

A scribble may indicate remove, replace, repair, recolor, or simply draw attention

Therefore

1. resolve annotation coordinates against the correct source dimensions
2. normalize coordinates before execution
3. map geometry to a semantic target
4. estimate confidence
5. if multiple plausible targets remain, ask one precise clarification rather than guessing

Reject

- zero-area targets
- out-of-bounds geometry
- mismatched coordinate systems
- missing mask references
- low-confidence ambiguous targets

## Preservation hierarchy

1. exact user instruction and edit scope
2. exact brand/product identity
3. exact required copy
4. canvas, crop, camera and composition
5. lighting, color and material continuity
6. background and secondary details

## Local edit

When one small element is wrong

- express one atomic delta
- avoid global restyling language
- lock crop, dimensions, perspective and unaffected composition
- protect identities and text not being edited
- permit only minimal boundary blending needed for believable integration
- compare the output to the approved source checkpoint after execution

Do not add unrelated improvements while fixing a local defect

## Source lineage and drift prevention

Every corrective retry starts from the last approved source checkpoint

Never use a failed or visibly drifted edit as the input to the next retry

This prevents cumulative changes to faces, logos, product proportions, text, crop, lighting and background details

Use at most three bounded attempts for the same defect. If the same failure persists or collateral changes worsen, stop and report the persistent failure instead of continuing edits

## Brand correction

Correct the smallest brand defect without redesigning surrounding art

Lock official mark geometry, color, clearspace and supplied product identity unless the user explicitly targets one of those properties

## Copy correction

Replacement text must be supplied exactly

Do not ask an image model to invent or paraphrase copy during correction

For Arabic

- route exact replacement copy through `arabic-rtl-director`
- verify glyph construction, joins, direction and punctuation after execution

If reliable text rendering cannot be achieved with the image editor, preserve/generate the visual foundation and use a deterministic text workflow where the host provides one

## Honest preservation language

Generative image editors may alter content outside a selected region

Describe unaffected areas as protected and require material stability plus post-edit QA

Do not claim mathematical pixel identity unless the available editor actually guarantees it

## Regenerate threshold

Regenerate globally only when

- the concept is wrong
- composition is structurally unsalvageable
- the requested change is genuinely global
- the source cannot support the manipulation

Do not choose global regeneration merely because local editing is difficult
