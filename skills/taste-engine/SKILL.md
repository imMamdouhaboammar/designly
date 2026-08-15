---
name: taste-engine
description: Taste extraction and transferable visual rule mixing engine. This skill should be used when deconstructing visual reference images into transferable design principles, building Taste Profiles, mixing multiple references by assigned design jobs, or preventing plagiarism and AI-slop anti-patterns.
---

# Taste Engine

Taste Engine converts raw reference images into evidence-backed, transferable design rules and structured Taste Profiles. It prevents literal copying by abstracting principles (lighting ratios, color harmonies, focal geometry, surface finishes) and assigning dedicated jobs to each reference.

---

## 1. Core Workflow

1. **Reference Deconstruction**:
   - Analyze reference image across 5 core dimensions:
     - **Lighting**: Key angle, fill ratio, shadow softness, color temperature.
     - **Palette**: Dominant, secondary, and accent ratios (e.g. 60-30-10 rule).
     - **Texture & Finish**: Material response (matte, satin, metallic, specular).
     - **Spatial Geometry**: Grid anchors, visual weight distribution, negative space.
     - **Mood & Tension**: Atmosphere, grain, contrast level.

2. **The 4-Step Rule Extraction Pipeline**:
   - `Evidence` (what is physically visible in the image)
   - `Observation` (structural or aesthetic pattern)
   - `Transferable Rule` (generalizable principle applicable to new briefs)
   - `Constraint / Anti-Rule` (what to strictly avoid to prevent unintended slop)

3. **Job-Based Reference Mixing**:
   - Never blend references indiscriminately.
   - Assign distinct, non-overlapping design jobs:
     - Reference A -> **Lighting Job** (e.g. 45° soft directional rim lighting).
     - Reference B -> **Composition Job** (e.g. dynamic diagonal off-center anchor).
     - Reference C -> **Color Harmony Job** (e.g. muted warm earth tones).

4. **Originality & Anti-Plagiarism Guard**:
   - Strictly discard subject matter, character identity, and proprietary artistic trademarks from the reference.
   - Never copy unique composite artwork verbatim.

5. **Output Contract**:
   - Emits structured `TasteProfile` JSON and `DesignSignalPacket` containing `taste_state`.

---

## 2. Tools & Scripts

- Lint Taste Profile: `python3 scripts/taste_lint.py <taste-profile.json>`
- Merge References: `python3 scripts/taste_merge.py <taste-mix.json>`

---

## 3. Schemas & References

- Local Schema: [Taste Profile Schema](schemas/taste-profile.schema.json)
- Local Schema: [Taste Mix Schema](schemas/taste-mix.schema.json)
- Shared Reference: [Taste Engine Guide](../../shared/references/taste-engine.md)
- Shared Reference: [Reference Analysis](../../shared/references/reference-analysis.md)
