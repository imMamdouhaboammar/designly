# Visual QA and Revision Gates

Generation is a draft until visual inspection passes

## Review sequence

Review in layers so surface polish does not distract from structural failures

### Layer 1: Communication
- brief accuracy
- primary message
- desired action
- concept strength

### Layer 2: Perception and structure
- hierarchy
- composition
- grouping and alignment
- figure-ground
- spacing and density
- crop and edges

### Layer 3: Craft
- typography
- color and contrast
- brand fidelity
- product fidelity
- physical believability
- lighting and materials

### Layer 4: Context
- cultural fit
- platform/viewing fit
- originality
- AI slop

## Weighted score

Score each category from 0 to 100

| Category | Weight |
|---|---:|
| Brief accuracy | 8 |
| Concept strength | 10 |
| Marketing clarity | 8 |
| Hierarchy | 10 |
| Composition | 10 |
| Grouping and alignment | 6 |
| Spacing and density | 5 |
| Typography | 8 |
| Color and contrast | 5 |
| Brand fidelity | 8 |
| Product fidelity | 6 |
| Physical believability | 5 |
| Lighting and materials | 4 |
| Cultural fit | 3 |
| Platform fit | 2 |
| Craft | 2 |

Total = 100

Release threshold = 92

## Category floors

The average cannot hide a broken core category

All applicable floors must pass

- brief accuracy >= 85
- concept strength >= 85
- marketing clarity >= 85
- hierarchy >= 88
- composition >= 88
- grouping and alignment >= 82
- typography >= 88 when text matters
- color and contrast >= 85 when color/text contrast matters
- brand fidelity >= 92 when official brand assets are supplied
- product fidelity >= 95 when a supplied product must remain exact
- physical believability >= 88 for photoreal manipulation

## Hard gates

Record each hard gate as `pass`, `fail`, or `na`

Only applicable gates must pass, and `na` must mean genuinely not applicable rather than unknown

- exact required copy is correct
- Arabic glyph formation and RTL behavior are correct when applicable
- official logos and marks are not malformed
- supplied product identity and proportions remain correct
- no unresolved critical anatomy or physical defect at the focal point
- protected regions in edit mode have no material unintended change
- required accessibility target has a verification path
- source-specific protected creative content is not near-copied without appropriate ownership or editing context
- AI slop veto passes

## Perception checks before scoring

### One-second test
Identify the first meaningful read

### Thumbnail test
Check hierarchy at small size

### Squint or blur test
Check value masses without detail

### Grayscale test
Check hierarchy without hue

### Edge test
Check crop, tangency, trapped space, and accidental near-alignments

### Brand-off test
Hide the logo mentally and evaluate brand specificity

### Effect-subtraction test
Remove finish effects mentally and check whether idea and hierarchy survive

### Physics pass
Check contact, light, perspective, material, reflection, and depth

### Copy pass
Check all required text and marks character by character

## AI slop veto

Classify findings using `ai-slop-taxonomy.md`

Block when

- any critical slop finding exists
- 2 or more major slop findings exist
- 4 or more minor slop findings exist
- slop pressure score reaches 6 or more, where minor = 1 and major = 3

## Revision classifier

### concept-revision
Use when the idea does not communicate the job

### composition-revision
Use when hierarchy, grouping, placement, crop, eye path, or text zone fails

### type-color-revision
Use when structure works but typography, line breaks, palette roles, or contrast fails

### visual-polish
Use when idea and structure work but material, lighting, integration, or small craft remains weak

### local-edit
Use for one bounded defect

### brand-correction
Use for logo, product, palette, or official brand behavior errors

### copy-correction
Use for spelling, glyph, number, punctuation, or exact-copy errors without disturbing approved layers

## Critique format

State

1. defect
2. evidence
3. impact on communication or credibility
4. smallest repair
5. layers that must remain locked

Avoid vague comments such as `make it more premium` or `make it more realistic`

## Approval formula

`APPROVED = weighted_score >= 92 AND category_floors_pass AND hard_gates_pass AND slop_veto_pass`
