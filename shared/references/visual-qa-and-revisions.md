# Visual QA and Revision Gates

Generation or editing is a draft until inspection passes

## Review order

1. Communication: brief accuracy, primary message, action, concept
2. Structure: hierarchy, composition, grouping, alignment, figure-ground, spacing, crop
3. Craft: typography, color/contrast, brand/product fidelity, physical believability, materials
4. Context: culture, platform, originality, AI slop
5. For edits: target accuracy, edit-scope accuracy, collateral change against the approved source checkpoint

## Weighted release rule

Weighted score must be >= 92 and every applicable category floor must pass

Core category floors

- brief accuracy >= 85
- concept strength >= 85
- marketing clarity >= 85
- hierarchy >= 88
- composition >= 88
- grouping/alignment >= 82
- typography >= 88 when applicable
- color/contrast >= 85 when applicable
- brand fidelity >= 92 when official assets are supplied
- product fidelity >= 95 when supplied product identity must remain exact
- physical believability >= 88 for photoreal manipulation

## Hard gates

Record each as `pass`, `fail`, or `na`

- exact copy
- Arabic glyph/RTL correctness
- official mark geometry
- supplied product identity/proportions
- critical focal anatomy/physics
- accessibility verification path
- originality/source-specific copy risk
- AI-slop veto
- for bounded edits: correct target mapping
- for bounded edits: no material protected-content drift
- for bounded edits: source lineage uses the approved checkpoint

## Bounded-edit comparison protocol

Always compare the edited output to `source_checkpoint`

Do not compare only to memory or to a failed previous edit

Inspect separately

### Target accuracy
Did the requested target receive the requested delta, no more and no less

### Scope accuracy
Did crop, canvas, camera, composition, unrelated text, identities, background, lighting direction, color grade or non-target objects change without authorization

### Collateral change
Minimal edge blending at the target boundary can be acceptable if required for visual integration

Material unrelated drift is a hard failure

Do not promise literal pixel identity from a generative editor unless the host/editor guarantees it

On collateral failure

1. reject the edited output
2. create RevisionRequest with failing_dimension `collateral_change`
3. route to `edit-sanitizer`
4. retry from source_checkpoint
5. do not chain from the failed render

## Perception checks

Use relevant checks: one-second, thumbnail, squint/blur, grayscale, edge/tangency, brand-off, effect-subtraction, physics, character-by-character copy, source-vs-edit scope

## AI slop veto

Block on any critical, 2+ major, 4+ minor, or cumulative pressure >= 6 where minor=1 and major=3

## Revision classifier

- concept -> creative-strategy
- hierarchy/composition -> composition-director
- typography -> typography-director
- Arabic -> arabic-rtl-director
- brand/product -> brand-intelligence
- physical integration -> manipulation-director
- annotation mapping/edit scope/collateral change -> edit-sanitizer
- provider execution mismatch after valid contract -> prompt-compiler

## Critique format

State defect, evidence, impact, smallest repair, and locks that remain untouched

Avoid comments like `make it more premium` or `make it more realistic`

## Approval formula

`APPROVED = weighted_score >= 92 AND category_floors_pass AND hard_gates_pass AND slop_veto_pass`
