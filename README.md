<p align="center">
  <img src="assets/logo.svg" width="80" height="80" alt="Designly" />
</p>

<h1 align="center">Designly</h1>

<p align="center">
  <strong>The AI Art Director that thinks like a creative team.</strong><br/>
  A Design Neural Mesh for ChatGPT &amp; Codex — 13 specialist skills working together<br/>so every ad, poster, and campaign asset looks like a human team made it.
</p>

<p align="center">
  <a href="#install"><img src="https://img.shields.io/badge/Install_in_ChatGPT-→-10a37f?style=for-the-badge&logoColor=white" alt="Install" /></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/v4.0.0-stable-111111?style=flat-square" alt="version 4.0.0" />
  <img src="https://img.shields.io/badge/13_Skills-modular-111111?style=flat-square" alt="13 skills" />
  <img src="https://img.shields.io/badge/8_Agents-coordinated-111111?style=flat-square" alt="8 agents" />
  <img src="https://img.shields.io/badge/Arabic_RTL-native-111111?style=flat-square" alt="Arabic RTL" />
  <img src="https://img.shields.io/badge/license-MIT-111111?style=flat-square" alt="MIT license" />
</p>

---

## The Problem

AI image generation gives you one shot. You type a prompt, cross your fingers, and hope the composition, typography, brand colors, lighting, and shadows all land at once. When they don't — and they usually don't — you start over from scratch.

Real creative teams don't work this way. A strategist defines the message. A brand guardian protects the identity. A compositor builds the layout. A retoucher checks the physics. They each own one thing, and they get it right.

**Designly brings that team structure to AI.**

---

## How It Works

Instead of one prompt doing everything, Designly splits art direction into **13 focused specialists** coordinated by a single director. Each specialist owns one domain, produces typed outputs, and hands off to the next — exactly like a production pipeline at an agency.

```
Your Brief
    │
    ▼
 Designly Director ─── locks your constraints so nothing overrides them
    │
    ├──► Creative Strategy ── audience, message hierarchy, concept territory
    ├──► Brand Intelligence ── logo clearspace, color formulas, product fidelity
    └──► Taste Engine ◄──► Reference Memory ── learns what you like across sessions
    │
    ▼
 Composition Director ── grid, focal anchor, negative space
    │
    ├──► Typography Director ──► Arabic RTL Director (when needed)
    ├──► Photography Director ── lens physics, 3-point lighting, materials
    ├──► Manipulation Director ── compositing, contact shadows, reflections
    └──► Campaign DNA ── consistency across every format (1:1, 9:16, 16:9)
    │
    ▼
 Prompt Compiler ── translates approved spec → Midjourney / Flux / DALL-E syntax
    │
    ▼
 Visual QA ─── PASS → ship it
    │
    └──── FAIL → sends a targeted fix request to the one specialist that dropped the ball
```

When Visual QA catches a shadow angle that doesn't match the light source, it doesn't regenerate the entire design. It sends a `RevisionRequest` to the **Manipulation Director** alone. The brand, composition, and typography stay locked.

---

## What Makes Designly Different

### 🔒 Your constraints are protected
Every decision is ranked on an 11-level priority system. User constraints sit at Priority 1 and brand rules at Priority 2 — no downstream specialist can override them, no matter how confident its recommendation.

### 🧠 It remembers what you like
The **Taste Engine** extracts transferable rules from references you share — not "make it like this," but *why* it works: the color temperature, the negative space ratio, the typographic scale. **Reference Memory** stores these with stable `REF-####` IDs so you can recall them months later.

### 🎯 Fixes are surgical, not nuclear
When something fails QA, only the responsible specialist reruns. A typography problem doesn't touch your composition. A shadow error doesn't regenerate your layout. This saves tokens, time, and sanity.

### 🌍 Arabic is a first-class citizen
The **Arabic RTL Director** doesn't just flip layouts. It redesigns the visual flow for native right-to-left reading, protects Arabic calligraphy glyph connections, and balances bilingual compositions where Arabic leads and English supports.

### 📐 Physics-grounded realism
Photography Director enforces real camera optics — focal length, aperture, depth-of-field. Manipulation Director enforces contact shadows, directional reflections, and scale consistency. The result: composites that look photographed, not pasted.

### 🧬 Campaign consistency across formats
Campaign DNA ensures your Instagram story, LinkedIn banner, and billboard all look like they came from the same shoot — with deliberate creative variation, not lazy cropping.

---

## The 13 Skills

| Skill | What it owns |
| :--- | :--- |
| **Designly Director** | Orchestration, brief intake, constraint locking, conflict resolution, final signoff |
| **Creative Strategy** | Marketing brief deconstruction, audience psychology, message hierarchy |
| **Brand Intelligence** | Brand manuals, logo clearspace, color formulas, product fidelity, Brand-Off test |
| **Taste Engine** | Evidence-backed taste extraction, reference job allocation, originality guard |
| **Reference Memory** | Local-first persistence, stable `REF-####` IDs, scoped feedback ledger |
| **Composition Director** | Spatial grids, focal hierarchy (one hero anchor), negative space, preflight |
| **Typography Director** | Typographic scale, headline measure, semantic line breaks, contrast ratios |
| **Photography Director** | Camera focal lengths, aperture physics, 3-point studio lighting, material finishes |
| **Manipulation Director** | Compositing physics, contact shadows, directional reflections, perspective |
| **Arabic RTL Director** | Arabic-first visual flow, calligraphy glyph fidelity, bilingual balance |
| **Campaign DNA** | Multi-asset continuity across 1:1, 9:16, 16:9 with deliberate variation |
| **Prompt Compiler** | Translates approved specs into Flux, Midjourney, and DALL-E syntax |
| **Visual QA** | 10-point critique, category floor scores, AI-slop hard veto, targeted revision routing |

Each skill is independently discoverable in ChatGPT and has its own interface configuration in `agents/openai.yaml`.

---

## The 8 Codex Agents

For Codex users, Designly ships 8 custom agents in `.codex/agents/` with strict tool boundaries:

| Agent | Mode | What it does |
| :--- | :--- | :--- |
| **Designly Director** | Orchestration | Owns state, spawns subagents, merges signals, enforces locks |
| **Strategy Planner** | Read-only | Audience insight, primary message, concept territories |
| **Brand Guardian** | Read-only / Veto | Brand compliance, logo protection, product fidelity |
| **Taste Analyst** | Read-only | Reference deconstruction, taste profile synthesis |
| **Structure Critic** | Read-only | Grid preflight, visual weight, negative space, typographic measure |
| **Craft Director** | Read-only | Camera optics, 3-point lighting, compositing physics |
| **Arabic Visual Director** | Read-only / Veto | RTL layout, exact Arabic copy protection, glyph audits |
| **Visual Reviewer** | Read-only / Gate | Independent scoring, category floors, AI-slop veto, revision routing |

Only the Director can write. Every other agent is read-only — they analyze and recommend, but cannot alter state. Brand Guardian, Arabic Visual Director, and Visual Reviewer hold veto power: they can block a design from shipping.

---

## Install

### ChatGPT Plugin Marketplace

Search **"Designly"** in the ChatGPT plugin store, or install directly from the `.codex-plugin/plugin.json` manifest.

### Manual / Codex CLI

```bash
# Clone the repository
git clone https://github.com/imMamdouhaboammar/designly.git
cd designly

# Verify the mesh is intact (all tests should pass)
python3 shared/scripts/validate_mesh.py
python3 shared/scripts/validate_skill_interfaces.py
python3 shared/scripts/validate_agent_configs.py
```

### Verify your installation

```bash
# Run the full test suite
python3 evals/baseline/test_monolith_parity.py
python3 evals/routing/test_skill_catalog.py
python3 evals/handoffs/test_contracts.py
python3 evals/handoffs/test_agents.py
python3 evals/visual/test_revision_router.py
python3 evals/run_mesh_evals.py
python3 tools/validate_public_plugin.py .
```

All commands exit with code 0 and print `PASS` for every check.

---

## Quick Start

### 1. Full campaign art direction

> *"Art-direct this launch campaign end-to-end with specialist agents and lock enforcement."*

Designly Director takes the brief, spawns strategy and brand analysis in parallel, locks your constraints, builds the composition, and runs Visual QA before delivering the final prompt.

### 2. Learn from a reference

> *"Extract evidence-backed transferable taste rules and save with a stable REF ID."*

The Taste Engine analyzes your reference into portable rules (color temperature, spatial ratios, lighting mood) and Reference Memory stores them as `REF-1042` for future sessions.

### 3. QA an existing design

> *"Review this visual with category floors and route targeted revisions to the failing node."*

Visual QA scores across 10 categories. If brand fidelity drops below 95 or hierarchy below 85, it routes a `RevisionRequest` exclusively to the responsible specialist — not the entire pipeline.

---

## Architecture

### Typed Contracts

All communication between skills flows through JSON Schema (Draft 2020-12) validated contracts:

| Contract | Purpose |
| :--- | :--- |
| `DesignContext` | The canonical state object — brief, constraints, active locks, specialist outputs |
| `DesignSignalPacket` | Typed recommendation from any specialist, with confidence score and evidence |
| `DesignLock` | Immutable constraint with priority level (1–11) and the locking authority |
| `RevisionRequest` | Targeted fix order routed to exactly one specialist, with defect category and evidence |

### Signal Priority (Conflict Resolution)

When two specialists disagree, the Director resolves it deterministically:

| Priority | Signal | Mutability |
| :---: | :--- | :--- |
| 1 | User exact constraints | Immutable |
| 2 | Documented brand rules | Immutable |
| 3 | Safety & cultural hard gates | Immutable |
| 4 | Primary communication job | Director override only |
| 5 | Hierarchy & composition | Director override only |
| 6 | Accessibility & legibility | Director override only |
| 7 | Campaign continuity | Negotiable |
| 8 | Craft realism | Negotiable |
| 9 | Explicit user taste | Negotiable |
| 10 | Inferred taste | Negotiable |
| 11 | Decorative finish | Negotiable |

### Test Coverage

The `evals/` directory contains 11 adversarial conflict scenarios, category floor isolation tests, AI-slop veto threshold tests, targeted revision routing tests, and a 10-group plugin benchmark — all verified green.

---

## Repository Layout

```
designly/
├── .codex-plugin/plugin.json         Marketplace manifest (v4.0.0)
├── .codex/
│   ├── config.toml                   Multi-agent runtime config
│   └── agents/                       8 custom Codex agent definitions
├── shared/
│   ├── contracts/                    5 typed JSON Schemas + routing graph
│   ├── references/                   25 design knowledge modules
│   └── scripts/                      Mesh, skill, and agent validators
├── skills/                           13 independent discoverable skills
├── evals/                            Conflict, routing, handoff, and QA tests
├── assets/                           Logo, icon, and wordmark SVGs
└── tools/                            Plugin validator + deterministic packager
```

---

## Build & Package

```bash
# Build a deterministic release ZIP
python3 tools/package_plugin.py . dist/designly-v4.0.0.zip

# Verify reproducibility — two builds produce identical SHA256
python3 tools/package_plugin.py . /tmp/a.zip
python3 tools/package_plugin.py . /tmp/b.zip
shasum -a 256 /tmp/a.zip /tmp/b.zip
# Both hashes will match exactly
```

---

## License

MIT © [Mamdouh Abo Ammar](https://github.com/imMamdouhaboammar)
