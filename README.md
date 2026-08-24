<p align="center">
  <img src="assets/logo.svg" width="128" height="128" alt="Designly Logo" />
</p>

<h1 align="center">Designly</h1>

<p align="center">
  <strong>Commercial Art Direction & Design Neural Mesh Plugin</strong><br/>
  21 focused Skills, 16 bounded Codex agents, Cannes-calibrated Creative Direction, 571 Legendary Campaign Canon, dramaturgy-first AI Video Direction (Seedance 2.5, Kling 3.0, Veo), model-physics Image & Design Direction (Gemini Nano Banana 2/Pro, MiniMax Design, Kimi Design, Claude Design, GPT Image 2), Insight Mining, Brand Activation, Visual Storytelling, typed handoffs, preflight, bounded edit sanitization, and independent visual QA
</p>

<p align="center">
  <a href="https://skills.sh/imMamdouhaboammar/designly"><img src="https://img.shields.io/badge/skills.sh-package-black?style=flat-square&logo=vercel" alt="skills.sh" /></a>
  <a href="https://www.npmjs.com/package/designly"><img src="https://img.shields.io/badge/npm-v5.0.0-CB3837?style=flat-square&logo=npm" alt="npm package" /></a>
  <a href="Formula/designly.rb"><img src="https://img.shields.io/badge/homebrew-tap-FBB040?style=flat-square&logo=homebrew" alt="Homebrew" /></a>
  <img src="https://img.shields.io/badge/21_Skills-modular-111111?style=flat-square" alt="21 skills" />
  <img src="https://img.shields.io/badge/8_Adapters-typed-111111?style=flat-square" alt="8 adapters" />
  <img src="https://img.shields.io/badge/16_Agents-bounded-111111?style=flat-square" alt="16 agents" />
  <img src="https://img.shields.io/badge/571_Campaigns-canonical-111111?style=flat-square" alt="571 campaigns" />
  <img src="https://img.shields.io/badge/Arabic_RTL-native-111111?style=flat-square" alt="Arabic RTL" />
  <a href="skills/designly-director/references/prompt-playground.md"><img src="https://img.shields.io/badge/Workflow_Library-production-111111?style=flat-square" alt="Workflow Library" /></a>
</p>

---

## ⚡ Quick Install

### 1. via skills.sh (Vercel)
Install the complete 21-skill pack directly into your agent environment:
```bash
npx skills add imMamdouhaboammar/designly
```

### 2. via Homebrew (macOS / Linux)
```bash
brew tap imMamdouhaboammar/designly
brew install designly
```

### 3. via npm / Bun
```bash
# Global CLI installation
npm install -g designly
# or
bun add -g designly

# Or run directly without installing
npx designly compile --model gemini-nano-banana --input spec.json
```

👉 See the complete **[Installation & Adapters Guide](docs/INSTALLATION.md)** for Codex, Claude Code, Cursor, Antigravity, and Python API setups.

---

## Start Here: Production Workflow Prompts

If you are new to Designly, do not start by memorizing the architecture or reading a feature list.

Start with the **[Designly Workflow Prompt Library](skills/designly-director/references/prompt-playground.md)**: 16 long-form, copy-ready `@Designly` production prompts that explicitly route real work through the existing Skills, contracts, model-physics rules, feedback loops, and Visual QA gates.

These are not fictional demo prompts. Pick the workflow that matches your real job, replace the `{{PLACEHOLDERS}}`, attach your actual assets, and paste it into ChatGPT with `@Designly`. The prompt tells Designly which route to use, which specialist owns each decision, when compilation is allowed, when execution should happen, and how failures must be routed for repair.

**[Open the Workflow Prompt Library →](skills/designly-director/references/prompt-playground.md)**

---

## What Designly is

Designly is a skills-only ChatGPT, Codex, and Claude/Agent plugin for commercial art direction, creative ideation, consumer insight mining, brand activation, narrative design, AI video directing, model-physics image prompting, brand visual systems, product advertising, bounded image manipulation, Arabic-first design, and rigorous visual QA.

It does not treat visual creation as a single-prompt guessing game.

The Director locks the brief, delegates bounded specialist jobs (including Cannes-calibrated ideation, consumer tension mining, non-advertising activation diagnostics, 571 legendary campaigns, dramaturgy-first video directing with Walter Murch's Rule of Six, and model-physics prompt synthesis for Gemini Nano Banana, MiniMax Design, Kimi Design, Claude Design, Seedance 2.5, and Kling 3.0), merges typed recommendations, compiles approved visual direction, and submits the output to independent QA.

For existing-image corrections, Designly enforces a dedicated Edit Sanitizer so annotation notes and inpainting requests cannot flow directly into execution without strict scope and preservation checks.

---

## Neural Mesh Architecture

```text
Brief
  │
  ▼
Designly Director (Orchestrator & State Owner)
  │
  ├──► Creative Director (Cannes/D&AD scoring, SIT/TRIZ structural methods)
  ├──► Insight Mining (Consumer tension spotting, JTBD & Mark Pollard 4-points)
  ├──► Campaign Canon (571 canonical campaigns & P01-P18 pattern benchmark)
  ├──► Brand Activation (PR stunts, brand utility, experiential diagnostics)
  ├──► Visual Storytelling (Narrative arcs, Story Spine, Sparkline, Pixar rules)
  ├──► Creative Strategy (Brief deconstruction, message hierarchy)
  ├──► Brand Intelligence (Brand rules, product identity, logo behavior)
  ├──► Taste Engine <──► Reference Memory (Transferable rules & REF IDs)
  │
  ▼
Composition & Spatial Preflight
  ├──► Composition Director (Grids, visual hierarchy, focal anchors, negative space)
  ├──► Typography Director ──► Arabic RTL Director (when Arabic copy/layout needed)
  ├──► Photography Director (Camera optics, 3-point lighting geometry, materials)
  ├──► Manipulation Director (Compositing physics, contact shadows, reflections)
  ├──► Campaign DNA (Multi-asset continuity & visual-family rules)
  │
  ▼
Generative Direction & Model Physics
  ├──► Image Director (Gemini Nano Banana 2/Pro, MiniMax Design, Kimi Design, Claude Design, GPT Image 2)
  ├──► Video Director (Seedance 2.5, Kling 3.0, MiniMax Video, Veo 3/3.1, 14-field shot cards, Murch montage)
  │
  ├──► Existing-Image Bounded Correction
  │      Edit Sanitizer (Annotation mapping, source checkpoint, protected regions)
  │
  ▼
Prompt Compiler (Assembly into provider-native parameters)
  │
  ▼
Host Image / Video / Design Generator
  │
  ▼
Visual QA (Independent Reviewer & Release Gates)
  ├──► PASS: final signoff
  └──► FAIL: RevisionRequest routed to the single responsible specialist
```

---

## Supported Model Adapters

| Model Adapter | Provider | Output Grammar | Key Capabilities |
|---|---|---|---|
| `gemini-nano-banana` | Google DeepMind | Descriptive Prose & Spatial JSON | Real-world grounding, 1:8 to 8:1 ratios, thinking mode, 14 references, zero camera dumps |
| `minimax-design` | MiniMax / Hailuo | Cinematic Physics & Bilingual | Volumetric lighting, camera vectors (`pan`, `tilt`, `zoom`, `dolly`, `orbit`), intensity 1-10 |
| `kimi-design` | Moonshot AI | Coordinate Zoning & Token Contracts | `[ZONE_TOP]`, `[ZONE_HERO]`, `#HEX` palettes, exact copy bounding box locks, paired SVG/HTML |
| `claude-design` | Anthropic 3.7 | Token Contracts & Vector SVG | Anti-slop finish gate, Tailwind tokens, precision `<viewBox>` with zero clipping, state machines |
| `seedance` | ByteDance | 30s Multi-Shot Timeline | 50-slot reference kit, `{ dialogue }` lip-sync, 3D blockout coordinates |
| `kling` | Kuaishou | Multi-Character Binding & Motion Brush | `[Character: ]` tags, 6-region motion brush vectors, native negative prompt, 6-axis camera matrix |
| `gpt-image-2` | OpenAI | 5-Slot Template & 2-Column Edit | `quality: low/medium/high`, two-column preservation contract (`Change/Preserve/Constraints`) |
| `veo` | Google DeepMind | JSON Schema | Native JSON prompt structure, synchronized dialogue and ambient sound cues |

---

## 21 Modular Skills

| Skill | Responsibility |
|---|---|
| `designly-director` | Intake, locks, orchestration, conflict resolution, final signoff |
| `creative-director` | Cannes/HumanKind calibration, structural ideation (SIT/TRIZ), recursive refinement |
| `insight-mining` | Consumer tension spotting (cultural, category, human), JTBD, Pollard 4-points |
| `campaign-canon` | 571 canonical campaigns, P01-P18 pattern map, anti-derivative benchmarking |
| `brand-activation` | Experiential stunts, brand utility, ambient media, non-advertising diagnostics |
| `visual-storytelling` | 6 narrative frameworks (Story Spine, Sparkline, Freytag, Monroe), emotional tiers |
| `video-director` | AI film director, dramaturgy, Murch Rule of Six, 14-field shot cards, Seedance 2.5 / Kling 3.0 / MiniMax / Veo |
| `image-director` | AI art director, model physics, Gemini Nano Banana 2/Pro, MiniMax Design, Kimi Design, Claude Design, GPT Image 2 |
| `creative-strategy` | Objective, audience, primary message, concept territory |
| `brand-intelligence` | Brand rules, product identity, logo behavior, brand-off test |
| `taste-engine` | Evidence-backed transferable rules from references |
| `reference-memory` | Local-first `REF-####` records and scoped preference feedback |
| `composition-director` | Grid, hierarchy, focal structure, negative space, crop |
| `typography-director` | Type hierarchy, measure, line breaks, text zones |
| `photography-director` | Camera relationships, lighting, materials, subject treatment |
| `manipulation-director` | Compositing, perspective, contact, reflections, occlusion |
| `arabic-rtl-director` | Arabic-first flow, exact Arabic copy, RTL and glyph checks |
| `campaign-dna` | Multi-asset continuity with deliberate variation |
| `edit-sanitizer` | Annotation/inpainting scope, EditContract, drift prevention |
| `prompt-compiler` | Approved direction or EditContract to host/model instructions |
| `visual-qa` | Independent scoring, hard gates, slop veto, revision routing |

---

## 16 Codex Custom Agents

| Agent | Boundary |
|---|---|
| `designly-director` | Orchestration and state ownership |
| `creative-director` | Read-only structural ideation & Cannes scoring calibration |
| `insight-miner` | Read-only consumer tension spotting & insight formulation |
| `canon-analyst` | Read-only 571 campaign canon & pattern saturation analysis |
| `activation-strategist` | Read-only experiential activations & non-advertising diagnostics |
| `story-architect` | Read-only narrative arcs & storytelling frameworks |
| `video-director` | Read-only AI video directing, dramaturgy & shot lists |
| `image-director` | Read-only model physics, prompt templates & multi-panel structures |
| `strategy-planner` | Read-only strategy analysis |
| `brand-guardian` | Read-only brand/product audit and vetoes |
| `taste-analyst` | Read-only reference/taste analysis |
| `structure-critic` | Read-only composition/type preflight |
| `craft-director` | Read-only photography/manipulation craft review |
| `arabic-visual-director` | Read-only Arabic/RTL review and vetoes |
| `edit-sanitizer` | Read-only bounded-edit normalization and vetoes |
| `visual-reviewer` | Read-only independent release gate |

---

## Testing & Quality Assurance

Designly enforces strict unit and integration testing conforming to `test-guard` rules and `api-security-best-practices`:

```bash
# 1. Run Bun unit test suite (TypeScript & CLI binary)
bun test

# 2. Run supply chain security audit
python3 evals/supply_chain/test_supply_chain.py

# 3. Run Homebrew formula tests
python3 evals/homebrew/test_homebrew.py

# 4. Run skills.sh registry validation
python3 tools/publish_skills_sh.py --check

# 5. Run Model Adapters test suite
python3 evals/adapters/test_adapters.py

# 6. Run Neural Mesh conflict & integration tests
python3 evals/run_mesh_evals.py

# 7. Validate OpenAI Codex public plugin
python3 tools/validate_public_plugin.py .
```

---

## Third-Party Attribution

- **Creative Director Skill Module**: Ideation methodologies, Cannes-calibrated scoring, and 571-case canonical campaign reference library are based on the Creative Director Skill by Serge Shima ([smixs/creative-director-skill](https://github.com/smixs/creative-director-skill)), licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).
- **Visual Skills Module**: AI film director video dramaturgy, Walter Murch Rule of Six, 14-field shot cards, model-physics image prompting, multi-panel grids, and pattern libraries are based on Visual Skills by Serge Shima ([smixs/visual-skills](https://github.com/smixs/visual-skills)), licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).
