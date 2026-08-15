# Taste Engine

Turn visual references into evidence-backed design guidance without reducing taste to adjectives or copying surface style

## Purpose

Taste is a pattern of decisions about what receives attention, what is suppressed, how elements relate, how much finish is enough, and which tradeoffs are repeatedly preferred

Do not treat taste as a mood word, aesthetic genre, artist name, or prompt suffix

The engine produces five things

1. `Taste Profile`: structured evidence from one reference or coherent reference set
2. `Transferable Rules`: relationships that can move to a new brief
3. `Anti-Rules`: decisions that should not be inherited
4. `Similarity Guard`: elements that must be transformed or excluded
5. `Taste Contract`: a job-based mix of several references for one execution

## Evidence ladder

Always move in this order

### 1. Evidence

Record only what can be observed

Examples

- hero occupies roughly half the frame height
- headline aligns to one vertical anchor
- background value range is narrow
- only one saturated accent appears
- cast shadow is hard and directional
- texture frequency is low outside the product

### 2. Observation

Explain what the evidence does

Examples

- large hero scale creates immediate product dominance
- one vertical anchor keeps a dense layout readable
- narrow background values keep the subject separation dependent on edge and material contrast

### 3. Transferable rule

Generalize the relationship without copying the source

Examples

- keep one dominant lower-frame hero and reserve a clean vertical text zone
- concentrate chroma in one functional accent rather than distributing saturation evenly
- use hard directional shadow only where it explains object contact and orientation

### 4. Constraint

Record where the rule stops being useful

Examples

- do not use the same crop if the packshot silhouette becomes ambiguous
- do not inherit the original campaign's trademarked prop arrangement
- do not use low text contrast in a performance ad where rapid scanning matters

## Taste dimensions

Use dimensions to compare and retrieve references, not to claim objective quality

Score each from 0 to 100 only when enough evidence exists; otherwise mark it unknown

### Structure

- focal dominance
- information density
- negative-space generosity
- asymmetry
- grid rigidity
- overlap pressure
- edge pressure
- depth

### Typography

- type-scale contrast
- copy density
- alignment formality
- line-shape control
- display-type personality

### Color and value

- value contrast
- chroma intensity
- palette breadth
- accent scarcity

### Image craft

- realism
- material fidelity
- lighting drama
- camera intimacy
- depth-of-field pressure
- texture frequency

### Restraint

- decoration pressure
- effect dependency
- synthetic-detail pressure
- novelty pressure

High or low is not inherently good. The job determines whether the profile is appropriate

## Confidence

Every observation and rule needs confidence

- `0.9-1.0`: repeated and directly visible
- `0.7-0.89`: strong visual evidence but some interpretation
- `0.5-0.69`: plausible but context-dependent
- `<0.5`: do not promote to a reusable rule without more evidence

Do not manufacture confidence from a single ambiguous reference

## Job-based reference mixing

Never blend whole references by averaging all attributes

First assign each source one or more jobs

Supported jobs include

- concept
- hierarchy
- composition
- grid
- crop
- spacing
- typography
- color
- lighting
- camera
- material
- manipulation
- texture
- brand-behavior
- restraint
- cultural-direction

For every job, choose

- primary reference
- optional secondary reference
- weight or priority
- conflicts
- current-brief override

Brand rules, exact copy, product truth, accessibility, cultural requirements, and platform constraints always override taste memory

## Conflict protocol

When two references disagree on the same job

1. identify the disagreement explicitly
2. choose the source whose behavior serves the current communication job better
3. record the rejected behavior as a constraint for this execution
4. do not compromise into a midpoint merely to preserve both sources

Example

REF-0002 uses centered symmetry for calm luxury

REF-0011 uses aggressive edge crop for urgency

For a limited-time performance ad, use REF-0011 for crop and keep REF-0002 only for material restraint if that restraint still supports the offer

## Originality and similarity guard

Before transferring rules, isolate source-specific elements

Mark as protected or transform-required when relevant

- logos and marks
- characters
- product designs not supplied by the user
- distinctive campaign copy
- unusual prop combinations strongly tied to one campaign
- distinctive branded shapes or trade dress
- highly specific arrangement where copying is unnecessary to achieve the communication job

Preserve direct source content only when the user supplied/owns it and asks for editing or adaptation

## Anti-slop integration

Taste should reduce genericity, not add more surface detail

For each profile record

- what the reference intentionally omits
- where visual quiet is doing work
- which effects are absent
- which materials stay understated
- how many focal events exist
- how much decorative entropy is tolerated

When a generated visual adds unsupported gloss, glow, micro-detail, 3D props, particles, panels, or lighting complexity, treat it as taste drift even if those effects are not globally banned

## Taste learning from feedback

Record explicit user approvals and rejections as preference evidence

Do not silently infer permanent taste from one correction

Promote a preference only after repeated compatible evidence or an explicit instruction such as `remember that I prefer...`

When feedback conflicts with a saved reference, the latest explicit user preference wins for that project or scope

## Output contract

A useful Taste Profile contains

- source provenance and ownership status
- jobs
- evidence-backed observations
- normalized dimensions where justified
- transferable rules
- anti-rules
- similarity guard
- tags and context
- confidence

Use `schemas/taste-profile.schema.json` when structured output is useful
