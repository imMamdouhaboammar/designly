<p align="center">
  <img src="assets/logo.svg" width="80" height="80" alt="Designly" />
</p>

<h1 align="center">Designly</h1>

<p align="center">
  <strong>Art direction for image-generation workflows that need judgment, not prompt decoration</strong><br/>
  15 focused Skills, 10 bounded Codex agents, Cannes-calibrated Creative Direction, 571 Legendary Campaign Canon, typed handoffs, preflight, edit sanitization, and independent visual QA
</p>

<p align="center">
  <img src="https://img.shields.io/badge/v4.2.0-production-111111?style=flat-square" alt="version 4.2.0" />
  <img src="https://img.shields.io/badge/15_Skills-modular-111111?style=flat-square" alt="15 skills" />
  <img src="https://img.shields.io/badge/10_Agents-bounded-111111?style=flat-square" alt="10 agents" />
  <img src="https://img.shields.io/badge/571_Campaigns-canonical-111111?style=flat-square" alt="571 campaigns" />
  <img src="https://img.shields.io/badge/Arabic_RTL-native-111111?style=flat-square" alt="Arabic RTL" />
</p>

## What Designly is

Designly is a skills-only ChatGPT/Codex plugin for commercial art direction, creative ideation, brand visual work, campaign imagery, product advertising, image manipulation, Arabic-first design, and visual review.

It does not treat image generation as a single-prompt task.

The Director locks the brief, delegates bounded specialist jobs (including Cannes-calibrated ideation and anti-derivative checks against 571 legendary campaigns), merges typed recommendations, compiles approved visual direction, and submits the actual output to independent QA.

For existing-image corrections, Designly has a dedicated Edit Sanitizer so annotation notes and inpainting requests cannot flow directly into execution without scope checks.

## Pipeline

```text
Brief
  |
  v
Designly Director
  |
  +--> Creative Director (Cannes/D&AD scoring, SIT/TRIZ, 571 campaign canon)
  +--> Creative Strategy
  +--> Brand Intelligence
  +--> Taste Engine <--> Reference Memory
  |
  v
Composition Director
  |
  +--> Typography Director --> Arabic RTL Director when needed
  +--> Photography Director
  +--> Manipulation Director
  +--> Campaign DNA
  |
  +--> existing-image correction
  |      Edit Sanitizer
  |        - annotation mapping
  |        - source checkpoint
  |        - mutation budget
  |        - protected regions
  |        - ambiguity / scope veto
  |
  v
Prompt Compiler
  |
  v
Host image generator/editor
  |
  v
Visual QA
  +--> PASS: final signoff
  +--> FAIL: RevisionRequest to the smallest responsible specialist
```

## 15 Skills

| Skill | Responsibility |
|---|---|
| `designly-director` | Intake, locks, orchestration, conflict resolution, final signoff |
| `creative-director` | Cannes/HumanKind calibration, structural ideation (SIT/TRIZ), 571 campaign canon |
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

Every Skill has its own `agents/openai.yaml` interface configuration.

## 10 Codex agents

| Agent | Boundary |
|---|---|
| `designly-director` | Orchestration and state ownership |
| `creative-director` | Read-only structural ideation & Cannes scoring calibration |
| `strategy-planner` | Read-only strategy analysis |
| `brand-guardian` | Read-only brand/product audit and vetoes |
| `taste-analyst` | Read-only reference/taste analysis |
| `structure-critic` | Read-only composition/type preflight |
| `craft-director` | Read-only photography/manipulation craft review |
| `arabic-visual-director` | Read-only Arabic/RTL review and vetoes |
| `edit-sanitizer` | Read-only bounded-edit normalization and vetoes |
| `visual-reviewer` | Read-only independent release gate |

Only the Director owns state mutation. Specialists return typed decisions and evidence rather than silently rewriting shared state.

## Design quality gates

Designly deliberately rejects attractive-looking output when the communication or craft is wrong.

Applicable gates include:
- brief and primary-message accuracy
- insight depth and concept originality
- hierarchy and composition floors
- typography and exact-copy checks
- Arabic glyph and RTL checks
- brand and product fidelity
- physical believability for composites
- AI-slop vetoes
- source-specific originality constraints
- bounded-edit target/scope/collateral checks

The Visual Reviewer must inspect the actual output before final approval.

## Install and test

This repository contains the plugin source and uploader-ready manifest at `.codex-plugin/plugin.json`.

```bash
git clone https://github.com/imMamdouhaboammar/designly.git
cd designly
python3 -m pip install pyyaml jsonschema

python3 shared/scripts/validate_mesh.py
python3 shared/scripts/validate_skill_interfaces.py
python3 shared/scripts/validate_agent_configs.py
python3 evals/baseline/test_monolith_parity.py
python3 evals/routing/test_skill_catalog.py
python3 evals/handoffs/test_contracts.py
python3 evals/handoffs/test_agents.py
python3 evals/edit/test_edit_sanitizer.py
python3 evals/visual/test_revision_router.py
python3 evals/run_mesh_evals.py
python3 skills/prompt-compiler/scripts/test_prompt_lint.py
python3 skills/visual-qa/scripts/test_gates.py
python3 skills/creative-director/scripts/test_creative_director.py
python3 tools/validate_public_plugin.py .
```

GitHub Actions runs these gates on pull requests and pushes to `main`.

## Typed contracts

The shared contract boundary includes:
- `DesignContext`
- `DesignSignalPacket`
- `DesignLock`
- `RevisionRequest`
- `EditContract`
- routing graph

## Repository layout

```text
designly/
├── .codex-plugin/plugin.json
├── .codex/
│   ├── config.toml
│   └── agents/                  10 custom Codex agents
├── .github/workflows/ci.yml
├── shared/
│   ├── contracts/
│   ├── references/
│   └── scripts/
├── skills/                      15 discoverable Skills
│   ├── creative-director/       SIT/TRIZ + 571-case campaign canon
│   └── ...
├── evals/
├── assets/
└── tools/
```

## Deterministic packaging

```bash
python3 tools/package_plugin.py . /tmp/designly-a.zip
python3 tools/package_plugin.py . /tmp/designly-b.zip
cmp /tmp/designly-a.zip /tmp/designly-b.zip
```

## Third-Party Attribution

The Creative Director ideation methodologies, Cannes-calibrated scoring, and 571-case canonical campaign reference library are based on the Creative Director Skill by Serge Shima ([smixs/creative-director-skill](https://github.com/smixs/creative-director-skill)), licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).
