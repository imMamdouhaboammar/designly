# Image Editing and Preservation

Use edit mode when the source image itself is an asset to preserve

## Edit contract

Define

- source image
- target region or object
- allowed changes
- locked objects
- locked text
- protected regions
- output dimensions
- acceptance criteria

## Preservation hierarchy

1. exact brand/product identity
2. exact required copy
3. geometry and composition
4. lighting and color continuity
5. background and secondary details

## Local edit

When one small element is wrong

- describe only the target change
- explicitly freeze surrounding elements
- avoid global restyling language
- keep the original crop and dimensions
- inspect for collateral changes after execution

## Brand correction

Use when the generated output altered logo, packshot, color, or official typography behavior

Correct the brand element without redesigning the image

## Copy correction

Use when text alone is wrong

Protect every non-text element

For Arabic, re-check glyph construction and letter joining after the repair

## Honest preservation language

Image generators may alter pixels outside a selected region

Describe unaffected areas as protected and use visual QA to detect collateral changes

Do not claim mathematical pixel identity unless a deterministic editor actually enforces it

## Regenerate threshold

Regenerate the whole image only when

- the concept is wrong
- composition is structurally unsalvageable
- the source cannot support the requested manipulation
- local repairs have introduced compounding artifacts
