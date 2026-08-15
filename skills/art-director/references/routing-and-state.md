# Routing and State

Use when a request spans more than one visual job or execution mode is unclear

## Lifecycle

`INTAKE -> CONTEXT_LOCK -> MARKETING_LOCK -> ROUTE -> CONCEPT -> STRUCTURE -> CRAFT_SPEC -> PREFLIGHT -> EXECUTE -> VISUAL_QA -> REVISION -> APPROVED`

Return to the smallest state that owns the defect

- wrong business/message priority -> `MARKETING_LOCK`
- weak idea -> `CONCEPT`
- weak hierarchy/crop/grid -> `STRUCTURE`
- weak type/color/light/material plan -> `CRAFT_SPEC`
- generation drift -> `EXECUTE` with tighter locks
- one local defect -> `REVISION` with local-edit or visual-polish
- wrong brand fact -> `CONTEXT_LOCK`
- wrong exact copy -> `CONTEXT_LOCK` then copy-correction

## Task classifier

Prefer evidence over keywords

### generate
No source image must be preserved and the primary job is a new visual

### edit
The source image is part of the required final result and unaffected areas should remain stable

### manipulation
The core act is physical integration, insertion, replacement, scale change, relighting, or impossible-but-believable interaction

### reference
References are primarily used to learn composition, treatment, visual grammar, or mood

### campaign
Several outputs need shared visual DNA

### typography-heavy
Text hierarchy, exact spelling, or layout carries a large share of communication

### review
The existing artifact is the thing being judged or repaired

## Deliverable precedence

Explicit user choice wins

Otherwise

1. source image plus bounded change -> `edit`
2. campaign or series -> `campaign`
3. compositing/insertion -> `manipulation`
4. reference-led recreation -> `reference-replication`
5. several structurally distinct routes -> `exploration`
6. prompt-only -> `quick`
7. default -> `director`

## Decision-critical questions

Ask only when unresolved input can cause a materially different output

Examples

- required exact headline or legal copy is missing
- ratio/placement is contractually fixed but unknown
- supplied product identity is ambiguous
- local edit target is not identifiable
- official brand documents conflict on a required rule

Do not ask about normal taste choices a senior Art Director can decide

## Tool decision

If an image tool exists and the user asks for an image, use it

If the user asks for a prompt only, do not generate unless they also request generation

If no image tool exists, compile an approved direction and prompt without pretending generation occurred

If an image exists after execution, route to VISUAL_QA automatically
