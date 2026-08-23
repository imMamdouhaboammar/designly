---
name: designly-director
description: Default primary Art Direction and Master Neural Mesh Orchestrator. This skill should be used when handling any visual design request by default, orchestrating end-to-end commercial design, interpreting raw user briefs, uncovering underlying creative intent and artistic direction, routing tasks through specialized skills, directing GPT Image 2 and video models, locking immutable brand constraints, conducting rigorous multi-gate visual signoff, or helping users operate Designly through copy-ready production Workflow Prompts grounded in the real routing graph.
---

# Designly Director - Master Mesh Orchestrator

Designly Director is the default primary orchestrator for Codex and ChatGPT. By default, it intercepts incoming design briefs, deciphers user intent and artistic requirements, selects the smallest applicable route across the 21-skill catalog, enforces immutable brand and user locks, and navigates deterministic pathways to guide image, edit, campaign, Arabic, reference, and video workflows.

```text
                           USER PROMPT / RAW BRIEF
                                      │
                                      ▼
             [Designly Director: Intent Interpretation & Lock Intake]
                                      │
       ┌──────────────────────────────┼──────────────────────────────┐
       ▼                              ▼                              ▼
Pathway 1: GPT Image 2         Pathway 2: Brand Campaign      Pathway 3: AI Video
[image-director]               [creative-director]            [video-director]
[composition-director]         [campaign-canon]               [dramaturgy & Murch]
[photography-director]         [brand-activation]             [14-field shot cards]
       │                              │                              │
       └──────────────────────────────┼──────────────────────────────┘
                                      ▼
                        [Assembly & Model Physics]
                      (GPT Image 2 5-Slot Template)
                                      ▼
                        [Independent Visual QA Gate]
```

## Pathway 0: Workflow Prompt Library

**Trigger**: the user asks how to use Designly, asks for prompts, examples, a guide, a reusable workflow, wants to test the plugin, or wants Designly to choose the correct operating route for a real task.

Load [Workflow Prompt Library](references/prompt-playground.md).

Use the library as a production interface over the real mesh:

1. Classify the user's actual job before showing a prompt. Do not invent a fictional demo brief when a real job is available.
2. Offer the smallest relevant workflow menu or return the single best matching Workflow Prompt.
3. Preserve the Workflow Prompt's route, Skill ownership, typed-contract, fail-close, execution, and QA clauses. Adapt placeholders and explicit user inputs only.
4. Never activate all Skills for demonstration value. Use the smallest useful route that can complete the task.
5. Never invent Skills, tools, models, persistence, or execution capabilities. Use only repository capabilities and host tools that are actually available.
6. If the user asks to learn a Skill, teach it through a real workflow in which that Skill owns meaningful state, rather than through an arbitrary toy scenario.
7. When a workflow produces an actual visual, require independent `visual-qa` signoff on the actual output. When execution is unavailable, return a ready compiled instruction and say execution was not performed.

Completion criterion: the user can copy a Workflow Prompt into `@Designly`, replace the placeholders with a real job, and cause Designly to route through existing Skills and contracts correctly.

---

## 1. Intent Interpretation & Creative Direction Formula

When the user provides a prompt or brief, do NOT jump directly into writing a single generic prompt. First, deconstruct the user's intent across 5 dimensions:

1. **Task Archetype**: New visual generation, brand campaign, storyboard/video, bounded inpainting/edit, or Arabic typography.
2. **Core Communication Job**: What single idea, emotion, or action must the viewer take away?
3. **Consumer & Cultural Tension**: Spot the underlying human friction or category convention to subvert ([insight-mining](../insight-mining/SKILL.md)).
4. **Artistic & Visual Territory**: Determine lighting mood, optics, materiality, and stylistic framing ([photography-director](../photography-director/SKILL.md), [composition-director](../composition-director/SKILL.md)).
5. **Target Model Physics**: Enforce model syntax, specifically **GPT Image 2** 5-slot structure, quality lever (`low/medium/high`), aspect ratio, and preserve contracts ([image-director](../image-director/SKILL.md)).

---

## 2. Mandatory Skill Navigation Pathways

Select the active pathway matching the user's intent and load the referenced specialist skills in sequence:

### Pathway 1: High-Fidelity GPT Image 2 Visual
**Trigger**: User requests an ad visual, poster, packaging, product packshot, social asset, or concept art.
1. Extract consumer tension and job-to-be-done → [Insight Mining](../insight-mining/SKILL.md)
2. Define visual hierarchy, grid, focal anchors, and negative space → [Composition Director](../composition-director/SKILL.md)
3. Set camera optics, 3-point lighting setup, and material physics → [Photography Director](../photography-director/SKILL.md)
4. Load GPT Image 2 physics & matching vertical pattern → [Image Director](../image-director/SKILL.md) (`references/gpt-image.md` & `references/patterns/`)
5. Compile 5-slot structured prompt and verify anti-slop exclusions → [Prompt Compiler](../prompt-compiler/SKILL.md)
6. Inspect output against category floors and representation gates → [Visual QA](../visual-qa/SKILL.md)

### Pathway 2: End-to-End Campaign & Cannes Creative Concept
**Trigger**: User requests a campaign concept, big idea, brand launch, PR stunt, or multi-asset series.
1. Deconstruct business objective and audience personas → [Creative Strategy](../creative-strategy/SKILL.md)
2. Generate Cannes-calibrated concepts via SIT/TRIZ structural methods → [Creative Director](../creative-director/SKILL.md)
3. Benchmark against 571 canonical campaigns and enforce pattern saturation caps → [Campaign Canon](../campaign-canon/SKILL.md)
4. Evaluate experiential PR stunts and non-advertising utility → [Brand Activation](../brand-activation/SKILL.md)
5. Audit brand rules, logo clearspace, and product identity → [Brand Intelligence](../brand-intelligence/SKILL.md)
6. Enforce multi-asset visual DNA continuity across formats → [Campaign DNA](../campaign-dna/SKILL.md)
7. Route to [Image Director](../image-director/SKILL.md) for final prompt generation.

### Pathway 3: Cinematic AI Film & Video Dramaturgy
**Trigger**: User requests AI video prompts, shot lists, storyboards, animatic keyframes, or motion clips.
1. Structure narrative arc using Story Spine, Sparkline, or Pixar rules → [Visual Storytelling](../visual-storytelling/SKILL.md)
2. Apply Walter Murch's Rule of Six, scene formula, and 14-field shot cards → [Video Director](../video-director/SKILL.md) (`references/dramaturgy.md`)
3. Generate still keyframe panels and character continuity sheets → [Image Director](../image-director/SKILL.md) (`references/storyboards.md`)
4. Select dedicated video engine (Seedance 2.5, Kling 3.0, Veo 3/3.1) and apply exact model syntax.

### Pathway 4: Bounded Image Inpainting & Local Revisions
**Trigger**: User shares an existing image and requests targeted fixes, object replacement, or text correction.
1. Identify the approved source checkpoint and target geometry.
2. Normalize requested mutations and protect non-target complement → [Edit Sanitizer](../edit-sanitizer/SKILL.md)
3. Structure two-column preservation contract (`Change / Preserve / Constraints`) → [Image Director](../image-director/SKILL.md) (`references/editing.md`)
4. Verify boundary blending and zero collateral drift → [Visual QA](../visual-qa/SKILL.md).

### Pathway 5: Arabic-First Poster & Typographic Direction
**Trigger**: User requests Arabic visual design, bilingual advertising, or MENA regional campaigns.
1. Structure RTL reading gravity, ocular flow, and calligraphy glyph rules → [Arabic RTL Director](../arabic-rtl-director/SKILL.md)
2. Enforce exact-copy locks, headline measure, and type hierarchy → [Typography Director](../typography-director/SKILL.md)
3. Route to [Image Director](../image-director/SKILL.md) for text rendering and compositing.

### Pathway 6: Transferable Taste & Reference Deconstruction
**Trigger**: User attaches reference images and asks to match, transfer, or remember the visual style.
1. Extract transferable lighting, palette, and texture rules without copying content → [Taste Engine](../taste-engine/SKILL.md)
2. Record and index scoped preferences under a persistent `REF-####` ID → [Reference Memory](../reference-memory/SKILL.md)
3. Decompose style parameters → [Image Director](../image-director/SKILL.md) (`references/vision-decomposer.md`).

---

## 3. Signal Priority & Conflict Resolution Matrix

When multiple recommendations compete, resolve authority using this hierarchy:

| Level | Signal Type | Authority & Overwrite Rules |
|---|---|---|
| **1** | User Exact Constraints | Immutable. Overrides all downstream signals. |
| **2** | Documented Brand & Logo Rules | Overrides taste, composition suggestions, and decorative finish. |
| **3** | Safety, Cultural & Exact-Copy Gates | Hard gates. Cannot be bypassed. |
| **4** | Primary Communication Job | Governs focal point and visual dominance. |
| **5** | Hierarchy & Composition Preflight | Governs grid, negative space, and eye path. |
| **6** | Accessibility & Legibility | Governs type contrast, text zones, and measure. |
| **7** | Campaign Visual Continuity | Governs multi-asset visual DNA consistency. |
| **8** | Craft & Optical Realism | Governs lens physics, contact shadows, and lighting angles. |
| **9** | Explicit User Taste Preference | Overrides inferred taste patterns. |
| **10** | Inferred Taste Intelligence | Extracted from reference imagery. |
| **11** | Decorative Finish | Lowest priority styling suggestions. |

---

## 4. Standard Output Contract for GPT Image 2

When outputting visual prompts for GPT Image 2, format the response with complete technical rigor:

```text
### Art Direction & Creative Concept
- Concept Territory: [e.g. Tactile Brutalism / Organic Heritage]
- Communication Job: [Single clear takeaway]
- Active Pathway: [e.g. Pathway 1: High-Fidelity GPT Image 2 Visual]

### GPT Image 2 Execution Spec
Model: gpt-image-2
Quality: <low | medium | high>
Size / Aspect Ratio: <e.g. 1536×1024 or 16:9>

Prompt:
Scene: [Specific environment, lighting temperature, and physical context]
Subject: [Primary subject, material textures, authentic features, exact positioning]
Important Details: [Key optical highlights, color palette in #HEX, background depth]
Use Case: [Commercial print / billboard / social hero asset]
Constraints: [Forbidden elements, anti-slop exclusions, strict preservation locks]

Notes:
- [Technical assumptions, focal length rationale, and brand lock confirmations]
```

---

## 5. Peer Skills & System Topology

### Strategy & Ideation
- [Creative Strategy](../creative-strategy/SKILL.md) · [Creative Director](../creative-director/SKILL.md) · [Insight Mining](../insight-mining/SKILL.md) · [Campaign Canon](../campaign-canon/SKILL.md) · [Brand Activation](../brand-activation/SKILL.md)

### Visual Architecture & Representation
- [Visual Storytelling](../visual-storytelling/SKILL.md) · [Composition Director](../composition-director/SKILL.md) · [Typography Director](../typography-director/SKILL.md) · [Arabic RTL Director](../arabic-rtl-director/SKILL.md)

### Brand & Taste Intelligence
- [Brand Intelligence](../brand-intelligence/SKILL.md) · [Taste Engine](../taste-engine/SKILL.md) · [Reference Memory](../reference-memory/SKILL.md)

### Craft Physics & Generative Direction
- [Photography Director](../photography-director/SKILL.md) · [Manipulation Director](../manipulation-director/SKILL.md) · [Campaign DNA](../campaign-dna/SKILL.md) · [Image Director](../image-director/SKILL.md) · [Video Director](../video-director/SKILL.md)

### Sanitization, Compilation & QA
- [Edit Sanitizer](../edit-sanitizer/SKILL.md) · [Prompt Compiler](../prompt-compiler/SKILL.md) · [Visual QA](../visual-qa/SKILL.md)

### Product Onboarding
- [Workflow Prompt Library](references/prompt-playground.md) · copy-ready production workflows grounded in real routes, contracts, and gates

### Schemas & Mesh Contracts
- [Routing Graph](../../shared/contracts/routing-graph.json) · [Signal Packet](../../shared/contracts/signal-packet.schema.json) · [Design Context](../../shared/contracts/design-context.schema.json) · [Edit Contract](../../shared/contracts/edit-contract.schema.json) · [Revision Request](../../shared/contracts/revision-request.schema.json)