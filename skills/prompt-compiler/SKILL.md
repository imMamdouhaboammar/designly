---
name: prompt-compiler
description: Image generation prompt compilation and model syntax adapter. This skill should be used when translating approved Art Direction Specs into provider-specific prompts (Midjourney, Flux, DALL-E, SDXL), linting prompts against buzzword-slop anti-patterns, or compiling targeted inpainting/edit instructions.
---

# Prompt Compiler

Prompt Compiler translates approved upstream design specifications (strategy, composition, lighting, materials, typography zones) into clean, high-precision image generation prompts tailored to specific AI models. It never invents concepts or fixes broken hierarchy.

---

## 1. Core Workflow

1. **Approved State Ingestion**:
   - Ingest `strategy_state`, `composition_state`, `craft_state`, `brand_state`, and `taste_state`.
   - Verify that all necessary structural decisions are approved before compilation.

2. **Model-Specific Translation**:
   - **Flux (.1 / Pro)**: Natural language descriptive paragraphs, physical spatial relationships, precise lighting direction, typography placement inside quotation marks.
   - **Midjourney (v6)**: Compact comma-separated token clauses, explicit aspect ratio `--ar`, stylized parameters `--stylize`, raw style `--style raw`.
   - **DALL-E 3**: Detailed semantic descriptions, strict scene layout constraints, avoidance of quality buzzwords.

3. **Local Edit & Inpainting Mode**:
   - When executing local edits (e.g., replacing an object or changing a label), specify:
     - Target edit region (bounding coordinates / mask area).
     - Explicit preservation clause: "Preserve 100% of surrounding background, lighting, and composition unchanged."
     - Targeted modification description.

4. **Prompt Linting & Anti-Slop Enforcement**:
   - Strip out useless AI quality filler ("hyperrealistic", "8k resolution", "masterpiece", "trending on artstation", "photorealistic award winning").
   - Replace generic fluff with concrete optical properties (e.g., "shot on Hasselblad H6D-100c, 85mm lens, f/2.8, diffuse softbox lighting").

5. **Output Contract**:
   - Return structured `generation_state` inside `DesignSignalPacket` containing compiled prompts and parameters.

---

## 2. Tools & Scripts

- Lint prompt syntax and detect slop keywords:
  ```bash
  python3 scripts/prompt_lint.py "Commercial studio photograph of matte black headphones, 85mm lens, f/2.8"
  ```
- Run prompt lint tests:
  ```bash
  python3 scripts/test_prompt_lint.py
  ```

---

## 3. References & Schemas

- Shared Contract: [Signal Packet Schema](../../shared/contracts/signal-packet.schema.json)
- Shared Reference: [Prompt Compiler Guide](../../shared/references/prompt-compiler.md)
- Shared Reference: [Model Guides](../../shared/references/model-guides.md)
