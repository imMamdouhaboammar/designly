---
name: prompt-compiler
description: Image, video, and design instruction compiler across Gemini Nano Banana, MiniMax Design, Kimi Design, Claude Design, Seedance, Kling, and GPT Image 2. This skill should be used when translating an approved Art Direction Spec or a ready EditContract into precise provider/model-ready instructions, linting prompt slop, compiling adapters, or preparing execution for the host tool without changing upstream creative decisions.
---

# Prompt Compiler & Multi-Model Adapter Engine

Compile approved design decisions into executable instructions across premier image, video, and design AI models (Gemini Nano Banana 2/Pro, MiniMax Design, Kimi Design, Claude Design, Seedance 2.5, Kling 3.0, and GPT Image 2). Do not invent the concept, repair weak hierarchy, reinterpret annotations, or broaden edit scope.

## Preconditions

### Generation
Require approved strategy/composition/craft state appropriate to the task.

### Editing, inpainting, annotation-guided correction
Require a typed `EditContract` from `edit-sanitizer` with:
- `status: ready`
- `execution_allowed: true`
- approved `source_checkpoint`
- normalized target geometry
- atomic requested mutations
- protected regions and semantic locks
- acceptance checks

If these are missing, route to `edit-sanitizer`. Do not compile a best-effort local edit from raw feedback.

---

## Supported Model Adapters

| Model Adapter | Key Compiler Rules |
|---|---|
| `gemini-nano-banana` | Descriptive prose, no numeric camera dumps, extreme aspect ratios, spatial JSON for 5+ subjects, 14 references |
| `minimax-design` | Cinematic lighting, volumetric physics, bilingual syntax, camera motions (`pan`, `tilt`, `zoom`, `dolly`, `orbit`) |
| `kimi-design` | Coordinate zoning (`[Top-Bar]`, `[Hero]`, `[Card-Grid]`), design tokens, exact typography bounding boxes |
| `claude-design` | Anti-slop finish gate, Tailwind design tokens, precision SVG `<viewBox>`, interactive state machines |
| `seedance` | 30s multi-shot timeline, 50-slot reference kit, `{ dialogue }` lip-sync markers, 3D blockout |
| `kling` | `[Character: ]` binding, Motion Brush 6-region vectors, negative prompt compilation, 6-axis camera matrix |
| `gpt-image-2` | 5-slot template (`Scene/Subject/Details/Use/Constraints`), 2-column edit preservation contract |
| `veo` | Native JSON schema format, cinematography parameters, audio/SFX cues |

---

## CLI Compilation & Linting

Run deterministic prompt compilation and anti-slop linting:

```bash
# List all available model adapters
python3 skills/prompt-compiler/scripts/compile_prompt.py --list-models

# Compile spec for Gemini Nano Banana
python3 skills/prompt-compiler/scripts/compile_prompt.py --model gemini-nano-banana --input spec.json

# Compile spec for Kling 3.0 Pro
python3 skills/prompt-compiler/scripts/compile_prompt.py --model kling --input spec.json

# Lint compiled text for synthetic slop and vague buzzwords
python3 skills/prompt-compiler/scripts/prompt_lint.py "<compiled instruction>"
```

---

## Cross-Skill Neural Connections & References

### Peer & Downstream Skills
- [Edit Sanitizer](../edit-sanitizer/SKILL.md) — Upstream sanitized EditContract provider
- [Image Director](../image-director/SKILL.md) — Visual design and image model physics
- [Video Director](../video-director/SKILL.md) — Dramaturgy and video shot list synthesis
- [Photography Director](../photography-director/SKILL.md) — Optical parameters and lighting models
- [Manipulation Director](../manipulation-director/SKILL.md) — Compositing physics and boundary blending rules
- [Visual QA](../visual-qa/SKILL.md) — Downstream independent visual verification gate
- [Designly Director](../designly-director/SKILL.md) — Orchestrator and state owner

### Schemas & References
- [Prompt Compiler Guide](../../shared/references/prompt-compiler.md) — Model prompt translation rules
- [Model Guides](../../shared/references/model-guides.md) — Multi-model physics & adapter details
- [Inclusive Representation](../../shared/references/inclusive-representation-and-ethics.md) — Anti-bias prompting rules
- [Edit Contract](../../shared/contracts/edit-contract.schema.json) — Local edit schema
- [Signal Packet](../../shared/contracts/signal-packet.schema.json) — Neural Mesh handoff
