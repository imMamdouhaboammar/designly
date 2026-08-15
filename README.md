<p align="center">
  <img src="assets/logo.svg" width="96" height="96" alt="Designly logo" />
</p>

<h1 align="center">Designly</h1>

<p align="center">
  <strong>A senior commercial Art Director — as a ChatGPT / Codex skill.</strong><br/>
  Taste Engine · Reference Memory · Design Preflight · Anti-Slop Gates · Visual QA
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-3.2.1-111111?style=flat-square" alt="version" />
  <img src="https://img.shields.io/badge/platform-ChatGPT%20%2F%20Codex-10a37f?style=flat-square" alt="platform" />
  <img src="https://img.shields.io/badge/type-skills--only-111111?style=flat-square" alt="type" />
  <img src="https://img.shields.io/badge/Arabic%20RTL-supported-111111?style=flat-square" alt="arabic" />
  <img src="https://img.shields.io/badge/license-MIT-111111?style=flat-square" alt="license" />
</p>

---

## What it does

Designly installs as a single **skills-only** plugin — no remote server, no MCP endpoint. It turns ChatGPT or Codex into a working creative partner that can:

| Capability | Description |
|---|---|
| **Art Direction** | Brief → concept → structure → craft spec → generation prompt |
| **Taste Engine** | Evidence → observation → transferable rule → constraint (not adjective soup) |
| **Reference Memory** | Stable `REF-####` IDs, job-tagged recall, similarity guard, feedback ledger |
| **Design Preflight** | Structural lint before generation; blocks broken hierarchy from reaching the model |
| **Anti-Slop Gates** | Effect-job, effect-subtraction, category-camouflage, object-census, style-entropy, synthetic-detail tests |
| **Image Editing** | Surgical local edits with locked regions and preservation constraints |
| **Visual QA** | 10-point perception review; approval requires score ≥ 92 + category floors + hard gates |
| **Arabic RTL** | Native RTL/bidi direction, correct glyph handling, no Latin mirroring |
| **Campaign DNA** | Multi-asset continuity: palette roles, type behavior, crop logic, recurring motif |

---

## Repo structure

```
designly/
├── .codex-plugin/
│   └── plugin.json              # Marketplace install metadata
├── assets/
│   ├── logo.svg                 # Square plugin logo (512×512)
│   ├── icon.svg                 # Composer icon
│   └── wordmark.svg             # Horizontal wordmark (1200×320)
├── skills/
│   └── art-director/
│       ├── SKILL.md             # Skill identity + full runtime instructions
│       ├── agents/
│       │   └── openai.yaml      # ChatGPT/Codex interface config
│       ├── assets/              # JSON templates (taste-profile, art-direction, etc.)
│       ├── evals/               # Benchmark scenarios + adversarial rubric
│       ├── examples/            # Campaign walkthroughs (Arabic poster, FMCG, luxury…)
│       ├── references/          # Reference knowledge modules (20+ topics)
│       ├── schemas/             # JSON schemas for all structured outputs
│       └── scripts/             # Python CLI tools (lint, validate, eval, memory)
├── docs/
│   └── OFFICIAL-CONTRACT-CHECK.md
├── evals/
│   └── plugin-benchmark.json    # Plugin-wide benchmark scenarios
├── tools/
│   ├── validate_public_plugin.py
│   └── package_plugin.py
├── PLUGIN-EVAL.md
├── PUBLIC-SAFETY.md
└── VERIFICATION.md
```

---

## Installing

### ChatGPT / Codex (local marketplace)

```bash
# 1. Clone
git clone https://github.com/imMamdouhaboammar/designly.git

# 2. Register as a local marketplace source
codex plugin marketplace add /path/to/designly

# 3. Restart the ChatGPT desktop app → install Designly from the marketplace
```

The plugin is **skills-only** — it does not require a running server or internet connection beyond the AI model itself.

---

## Taste Engine

References are not compressed into words like `premium`, `cinematic`, or `minimal`.

Every reference becomes a **Taste Profile** built from observable evidence:

```
evidence → observation → transferable rule → constraint
```

When multiple references are active, each is assigned a **design job**:

```
REF-0007 → hierarchy
REF-0012 → lighting
REF-0021 → typography
```

Brand rules and the current brief always override saved taste. Source-specific content is quarantined inside a `SIMILARITY GUARD` and never treated as reusable grammar.

---

## Reference Memory

A local persistent store of structured visual analysis — not image copies.

```bash
# Initialize
python3 skills/art-director/scripts/reference_memory.py init

# Add a taste profile
python3 skills/art-director/scripts/reference_memory.py add \
  skills/art-director/assets/taste-profile.template.json

# Recall by job
python3 skills/art-director/scripts/reference_memory.py list --job hierarchy

# Semantic search
python3 skills/art-director/scripts/reference_memory.py search editorial restrained

# Build a job-based Taste Contract from multiple refs
python3 skills/art-director/scripts/taste_merge.py
```

---

## Design Preflight

Before any generation, the direction is linted against structural blockers:

- No single primary message
- Adjective-only concept
- No dominant focal event
- Equal emphasis across all elements
- Missing alignment logic
- Decorative effects without jobs
- Text zone fighting the hero
- Contradictory light or perspective plan

```bash
python3 skills/art-director/scripts/design_lint.py
```

Generation is blocked until all critical and major preflight defects are resolved.

---

## Validation & Packaging

```bash
# Validate the plugin package structure
python3 skills/art-director/scripts/validate_package.py
python3 tools/validate_public_plugin.py .

# Build a deterministic ZIP for release
python3 tools/package_plugin.py . /tmp/designly.zip

# Build twice and compare SHA256 before shipping
shasum -a 256 /tmp/designly.zip
```

---

## Running evals

```bash
# Full benchmark suite
python3 skills/art-director/scripts/run_evals.py

# Design-specific evals (good vs bad structural decisions)
python3 skills/art-director/scripts/run_design_evals.py

# Score a visual review output
python3 skills/art-director/scripts/score_review.py

# Gate checks
python3 skills/art-director/scripts/test_gates.py
```

Eval fixtures live in `skills/art-director/evals/fixtures/` and cover both well-structured directions and known failure modes (adjective-only concept, four focal points, effect stack, style entropy, etc.).

---

## Reference knowledge

The skill loads focused reference modules on demand rather than keeping everything in context:

| Module | Topic |
|---|---|
| `art-direction.md` | Core direction framework |
| `design-principles.md` | Hierarchy, alignment, contrast, rhythm |
| `composition-and-photography.md` | Crop, eye path, rule of thirds, depth |
| `layout-grid-and-spacing.md` | Grid systems, spacing rhythm |
| `gestalt-and-perception.md` | Figure-ground, proximity, continuity |
| `typography.md` | Type roles, scale, tracking, legibility |
| `arabic-rtl-and-cultural.md` | Bidi, glyph fidelity, RTL composition |
| `color-and-contrast.md` | Value hierarchy, WCAG AA, palette roles |
| `taste-engine.md` | Evidence → rule → constraint pipeline |
| `reference-analysis.md` | Deconstruct visual grammar from references |
| `reference-memory.md` | REF-IDs, CRUD, feedback ledger |
| `ai-slop-taxonomy.md` | Slop family classification by severity |
| `design-preflight.md` | Structural lint checklist |
| `advertising-manipulation.md` | Coherent local physics for composites |
| `visual-qa-and-revisions.md` | 10-point review + scoring rubric |
| `brand-intelligence.md` | Rules vs patterns vs inferences |
| `campaign-visual-dna.md` | Multi-asset continuity contract |
| `prompt-compiler.md` | Direction → model instructions |
| `model-guides.md` | Per-model generation behavior |
| `image-editing.md` | Surgical edit regions and preservation |
| `marketing-brief.md` | Message hierarchy, audience, objective |
| `platform-and-format.md` | Placement, viewing distance, safe zones |
| `routing-and-state.md` | Task classification and mode selection |

---

## Examples

| Example | Description |
|---|---|
| [`arabic-poster.md`](skills/art-director/examples/arabic-poster.md) | RTL poster with correct bidi and cultural direction |
| [`egypt-fmcg.md`](skills/art-director/examples/egypt-fmcg.md) | Egyptian FMCG campaign with product fidelity |
| [`saudi-luxury-event.md`](skills/art-director/examples/saudi-luxury-event.md) | Luxury event visual with brand-off test |
| [`campaign-series.md`](skills/art-director/examples/campaign-series.md) | Multi-asset campaign with Visual DNA lock |
| [`cosmetics-manipulation.md`](skills/art-director/examples/cosmetics-manipulation.md) | Product composite with coherent local physics |
| [`local-edit.md`](skills/art-director/examples/local-edit.md) | Surgical region edit with locked areas |

---

## Author

**Mamdouh Abo Ammar** — [github.com/imMamdouhaboammar](https://github.com/imMamdouhaboammar)

---

<p align="center">
  <img src="assets/wordmark.svg" width="320" alt="Designly wordmark" />
</p>
