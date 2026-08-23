---
name: image-director
description: AI art direction and model-physics image prompting for Nano Banana (NB2/NBP) and GPT Image 2. This skill should be used when writing provider-physics image prompts, generating multi-panel grids, character sheets, e-commerce product shots, fashion editorials, food/beverage ads, cinematic portraits, slides, posters, 3D dimensional plans, structural sketch-to-renders, style transfer, or vision decomposition.
---

# AI Image Director & Model-Physics Prompter

Direct and compile high-fidelity image prompts tailored to the exact physics of the target generator (Nano Banana 2/Pro and GPT Image 2).

## Mandatory Reading Order

Prompt quality collapses into mush when generated from generic adjectives. Always load reference files in this exact sequence:

### Step 1 — Model Physics Selector → [models.md](references/models.md)
Decide between **Nano Banana (NB2/NBP)** or **GPT Image 2**:
- **Nano Banana**: Natural-language paragraphs, image grounding for real locations, extreme aspect ratios (1:8, 8:1, 4:1), thinking mode, JSON for 5+ elements, up to 14 references. Do NOT use camera numbers (`50mm / f-stop`).
- **GPT Image 2**: 5-slot template (`Scene / Subject / Important Details / Use Case / Constraints`), anti-slop banned words, `quality: low / medium / high` fidelity lever, size in multiples of 16, two-column edit logic (`Change / Preserve / Constraints`), up to 16 references.

### Step 2 — Read Chosen Model Physics
- **Nano Banana Rules** → [nano-banana.md](references/nano-banana.md)
- **GPT Image 2 Rules** → [gpt-image.md](references/gpt-image.md)

### Step 3 — Universal Golden Rules → [golden-rules.md](references/golden-rules.md)
- Start with a verb, positive framing, hex colors (`#HEX`), quote rendered text, edit don't re-roll, one atomic change per iteration.

### Step 4 — Task-Shaped Specialized Modules
- Text rendering, typography, multilingual in-image text → [text-rendering.md](references/text-rendering.md)
- Bounded edits, object removal, colorization, localization → [editing.md](references/editing.md)
- Character continuity across multi-frame sequences → [characters.md](references/characters.md)
- Presentation slides & executive decks → [slides.md](references/slides.md)
- Sequential narrative & comic panels → [storyboards.md](references/storyboards.md)
- Sketch-to-final wireframes & structural layout → [structural.md](references/structural.md)
- 2D to 3D, floor plans & isometric orthographic views → [dimensional.md](references/dimensional.md)
- Vision analysis, style transfer & reference decomposition → [vision-decomposer.md](references/vision-decomposer.md)
- Multi-panel compositions (TVC 9-cell, 2x2 grids, collages) → [multi-panel.md](references/multi-panel.md)

### Step 5 — Industry Pattern Libraries
- E-commerce product photography → [patterns/ecommerce.md](references/patterns/ecommerce.md)
- Fashion editorial campaigns → [patterns/fashion-editorial.md](references/patterns/fashion-editorial.md)
- Food & beverage advertising → [patterns/food-beverage.md](references/patterns/food-beverage.md)
- Cinematic portraits → [patterns/portrait-cinema.md](references/patterns/portrait-cinema.md)
- Posters & graphic illustration → [patterns/poster-illustration.md](references/patterns/poster-illustration.md)
- Character design (turnarounds, expression sheets) → [patterns/character-design.md](references/patterns/character-design.md)
- UI mockups & social media formats → [patterns/ui-social.md](references/patterns/ui-social.md)

### Step 6 — Studio Vocabulary & Prompt Framework
- Camera, lighting, color grading & film stock vocabulary → [creative-direction.md](references/creative-direction.md)
- 10-element checklist & detail modes → [prompt-framework.md](references/prompt-framework.md)

---

## Output Standard

Structure output following model physics:

```text
Model: <nano-banana-2 | nano-banana-pro | gpt-image-2>
Quality: <low | medium | high>          (only for gpt-image-2)
Size / Ratio: <e.g. 1536×1024 or 16:9>

Prompt:
<the compiled prompt text, ready to execute>

Notes:
- <explicit assumptions and technical choices made>
```

For bounded edits, include the mandatory preservation contract:
```text
Change: <one atomic mutation>
Preserve: <face, pose, lighting, framing, geometry, background>
Constraints: <no extra objects, no drift>
```

---

## Cross-Skill Neural Connections & References

### Peer & Downstream Skills
- [Video Director](../video-director/SKILL.md) — Motion synthesis from keyframe stills
- [Creative Director](../creative-director/SKILL.md) — Upstream creative concept territory
- [Prompt Compiler](../prompt-compiler/SKILL.md) — Multi-provider prompt generation
- [Photography Director](../photography-director/SKILL.md) — Optics, lenses, and lighting geometry
- [Visual QA](../visual-qa/SKILL.md) — Quality gates and defect auditing
- [Designly Director](../designly-director/SKILL.md) — Orchestration and state management

### Schemas & Contracts
- [Signal Packet](../../shared/contracts/signal-packet.schema.json) — Neural Mesh handoff
- [Routing Graph](../../shared/contracts/routing-graph.json) — Orchestration graph

---
*Attribution: Image prompting physics and patterns created by Serge Shima ([github.com/smixs/visual-skills](https://github.com/smixs/visual-skills)), licensed under CC BY 4.0.*
