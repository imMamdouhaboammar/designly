# Designly Architecture & Engineering Learnings

**Date**: August 2026  
**Milestone**: v5.0.0 (Visual Skills Module Deep Integration, Master Mesh Orchestration, & Public Plugin Preflight)

---

## 1. Decisions & Architectural Invariants

### A. Deep Integration of Visual Skills into 21-Skill Neural Mesh
* **Decision**: Convert external modules (`visual-skills-module`) into first-class production skills (`skills/video-director` and `skills/image-director`) with 27 curated reference guides and pattern libraries.
* **Why**: Monolithic or loosely-coupled visual prompt generators lack domain physics, dramaturgy constraints, and bounded editing safety.
* **Invariant**: Every skill must have valid YAML frontmatter with trigger conditions, strict line limits (<500 lines), typed interface manifest (`agents/openai.yaml`), and unique high-contrast SVG assets (128x128 & 512x512).

### B. Master Mesh Orchestrator Pattern (`designly-director`)
* **Decision**: Establish `designly-director` as the default front-door entry point in `.codex/agents/` and `.codex-plugin/plugin.json`.
* **Why**: Prevents models from jumping straight into generating shallow, generic prompt mush.
* **Invariant**: The orchestrator must parse every prompt through the 5-dimension Intent Interpretation Formula (Task Archetype, Core Communication Job, Consumer Tension, Visual Territory, and Model Physics) before dispatching to one of 6 deterministic pathways.

### C. Standardized 5-Slot Template for GPT Image 2
* **Decision**: Enforce an unalterable 5-slot structure (`Scene / Subject / Important Details / Use Case / Constraints`) with explicit quality levers (`low/medium/high`) and aspect ratio bounds.
* **Why**: GPT Image 2 requires strict semantic separation between environmental context, foreground subjects, optical color highlights, and negative anti-slop exclusions.

### D. Read-Only Custom Agent Isolation
* **Decision**: Configure all 15 specialist agents in `.codex/agents/*.toml` with strictly `tools = ["read_file"]`.
* **Why**: Guarantees non-destructive analysis and prevents specialist agents from corrupting the master `DesignContext` state or triggering unauthorized disk writes. Only `designly-director` possesses orchestration tools (`invoke_subagent`, `write_file`).

---

## 2. Model Physics & Compiler Insights

| Model | Generative Physics & Syntax Invariants | Common Failure Mode Avoided |
|---|---|---|
| **GPT Image 2** | 5-slot structured syntax, quality levers (`low/medium/high`), two-column preservation contracts (`Change / Preserve / Constraints`) for inpainting, anti-slop exclusions. | Prevents semantic bleeding, accidental background drift, and generic AI smoothing. |
| **Nano Banana 2 / Pro (NB2/NBP)** | Rich descriptive prose, spatial JSON blockout for 5+ subjects, natural light grounding, 14 reference slots. | Eliminates unnatural camera dump numbers (`35mm f/1.8`) and negative prompt bloat. |
| **Seedance 2.5** | Walter Murch's Rule of Six (Emotion 51%, Story 23%, Rhythm 10%), 14-field shot cards, 30s timeline, synchronized lip-sync `{ dialogue }`. | Prevents timeline drift, unnatural camera velocity, and narrative incoherence. |
| **Kling 3.0 Pro** | `[Character: ]` binding tags, 6-region Motion Brush vectors, 6-axis camera motion matrix. | Prevents character identity loss across multi-character cuts. |
| **Veo 3 / 3.1** | Real-world cinematic physical simulations, volumetric atmospheric lighting, anamorphic optical framing. | Prevents synthetic uncanny-valley physics in complex fluid and particle motion. |

---

## 3. Visual Identity & Asset Styling Patterns

* **Unique Color-Coded Palette**: Every skill in the catalog is assigned a distinct, accessible brand color (e.g. Cobalt Blue for Strategy, Cannes Gold for Creative Director, Deep Amethyst for Insight Mining, Cinema Indigo for Video Director, Magenta for Image Director).
* **High-Contrast Retina SVGs**: Generated scalable, mathematically clean SVG glyphs on rounded gradient squircles with high visual legibility at both 128px and 512px.
* **Public Plugin Store Preflight**: Enforced OpenAI public store rules (square icons >= 48x48, single-line default prompts <= 128 chars, description <= 1024 chars without workflow leakage).

---

## 4. Surprises & Gotchas Encountered

1. **Frontmatter Trigger Matching in Interface Validators**:
   - `validate_skill_interfaces.py` enforces exact phrases like `"This skill should be used when"`. Altering the wording to `"This skill should be used by default when"` tripped the regex validator. Fixed by phrasing as `"This skill should be used when handling any visual design request by default"`.
2. **GitHub Release Asset Clobbering**:
   - Re-uploading assets to an existing tag via `gh release upload --clobber` requires deterministic zip packaging with SHA256 integrity updates to prevent corrupted binary caches.

---

## 5. Verification & Test-Guard Standards

* **100% Deterministic Evals**: 21 skill routing classifications, 22 revision defect routes, 16 agent configs, and 11 adversarial conflict scenarios pass with zero mocking.
* **Continuous Release Automation**: Every update rebuilds the distribution archive, regenerates SHA256 sums, validates against the public store preflight suite, and pushes cleanly to GitHub with official release assets.
