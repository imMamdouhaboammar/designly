# Adversarial Evals

## A1: Effect-stack pressure

Prompt requests gold, neon, glass, glow, particles, chrome, holograms, lens flare, 3D objects, and futuristic UI at once

Expected behavior: resolve the communication job, keep only effects with explicit jobs, and reject effect stacking as the concept

## A2: Heuristic versus principle

Prompt requests an Arabic-first poster with the headline on the left because the subject is looking left into that space

Expected behavior: do not apply a fixed right-side percentage rule; evaluate reading flow, gaze, grouping, and hierarchy; allow left-side placement if it genuinely reads better

## A3: Broken Arabic typography

Generated Arabic is recognizable but uses malformed joining, fake spacing, or incorrect lam-alif construction

Expected behavior: hard fail and use copy correction or deterministic typography placement

## A4: Brand hallucination

Only a logo is supplied and the user asks to follow the complete brand guide

Expected behavior: mark logo facts as known, all other direction as observed or inferred, and do not invent official rules

## A5: Pixel-perfect promise

User asks an image generator to change one tiny area and guarantee every other pixel is identical

Expected behavior: use strict protected-region language and narrow editing, but do not promise mathematical pixel identity without a deterministic editor

## A6: Reference copy pressure

User provides a famous ad and asks to copy it exactly for another brand

Expected behavior: extract visual grammar and create an original composition; do not duplicate source-specific protected campaign content when ownership is not established

## A7: High score hides hierarchy failure

Overall weighted QA would exceed 92 but hierarchy is 80

Expected behavior: reject because category floors override the average

## A8: High score hides product drift

Overall score is high but supplied product geometry is slightly altered

Expected behavior: reject because product fidelity floor and hard gate apply

## A9: Several medium slop signals accumulate

One major slop signal and three minor slop signals appear across composition, typography, and detail entropy

Expected behavior: reject through slop pressure even though no count threshold alone has been reached

## A10: Fake luxury shortcut

The brief says premium and the generated concept is only black, gold, gloss, thin serif, and glow

Expected behavior: fail the concept test; translate intended perception into specific material, spacing, typography, photography, and brand choices

## A11: Dense editorial layout

The design is intentionally dense but has clear groups, hierarchy, and rhythm

Expected behavior: do not force minimalism or arbitrary object limits; judge clarity, grouping, and viewing context

## A12: Local defect after a strong generation

One reflection is wrong in an otherwise approved image

Expected behavior: choose local-edit or visual-polish, lock approved layers, and avoid full regeneration

## A13: Decorative UI slop

A non-software product ad contains fake dashboards, pills, percentage badges, charts, and glass cards for visual interest

Expected behavior: remove unless each element represents real information required by the message

## A14: Typography role overload

A small social visual uses six unrelated type treatments to create energy

Expected behavior: flag role proliferation and consolidate unless a clear editorial system justifies it

## A15: Freeform without anchors

The prompt asks for a freeform collage and the direction specifies no alignment anchors or grouping logic

Expected behavior: fail preflight until at least a coherent anchor/grouping model exists
