# Prompt Compiler

Compile the Art Direction Spec into model-ready language only after preflight passes

## Principle

A strong image prompt expresses relationships and constraints

It does not substitute a list of style keywords for design direction

## Translate decisions, not adjectives

Prefer

`One bottle occupies the lower-left visual mass, leaving a broad quiet field for the headline; a soft upper-left key creates one grounded cast shadow and a controlled highlight along the glass edge`

Over

`premium cinematic stunning luxury product shot`

## Prompt order

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
11. edit/protected-region constraints
12. likely failure exclusions
13. output ratio/format

## Relationship language

Describe

- what dominates
- what supports
- what overlaps
- what stays separate
- where the eye moves
- where negative space is preserved
- what light source explains shadows and reflections
- what must remain exact

This usually guides image models better than disconnected nouns

## Negative-instruction discipline

Do not dump twenty banned effects into every prompt

Include exclusions only for likely failure modes in the current task

A direction with strong positive structure usually needs fewer negative instructions

## Edit prompt contract

Use

1. target
2. allowed change
3. locked content
4. acceptance criteria

Example

`Change only the bottle cap from black to brushed silver. Preserve bottle silhouette, label, logo, reflections, hand, background, crop, and lighting. Treat everything outside the cap as protected. Reject any visible change to label geometry or surrounding composition.`

## Reference prompting

State which visual grammar is borrowed from which reference

Do not say only `match the style`

Example

`Use REF-01 for the large lower-frame crop and quiet upper field; use REF-02 only for the soft side-light character; keep the current brand palette and create original props and arrangement.`

## Prompt disclosure

When the host can generate directly, keep the compiled prompt internal unless the user asks for it

When the user asks for a prompt, return the final compiled prompt without scratch reasoning
