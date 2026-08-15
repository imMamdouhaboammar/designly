<p align="center">
  <img src="assets/logo.svg" width="80" height="80" alt="Designly" />
</p>

<h1 align="center">Designly</h1>

<p align="center">
  <strong>Art direction for image-generation workflows that need judgment, not prompt decoration</strong><br/>
  14 focused Skills, 9 bounded Codex agents, typed handoffs, preflight, edit sanitization, and independent visual QA
</p>

<p align="center">
  <img src="https://img.shields.io/badge/v4.1.0-reviewing-111111?style=flat-square" alt="version 4.1.0" />
  <img src="https://img.shields.io/badge/14_Skills-modular-111111?style=flat-square" alt="14 skills" />
  <img src="https://img.shields.io/badge/9_Agents-bounded-111111?style=flat-square" alt="9 agents" />
  <img src="https://img.shields.io/badge/Arabic_RTL-native-111111?style=flat-square" alt="Arabic RTL" />
</p>

## What Designly is

Designly is a skills-only ChatGPT/Codex plugin for commercial art direction, brand visual work, campaign imagery, product advertising, image manipulation, Arabic-first design, and visual review

It does not treat image generation as a single-prompt task

The Director locks the brief, delegates bounded specialist jobs, merges typed recommendations, compiles approved visual direction, and submits the actual output to independent QA

For existing-image corrections, Designly now has a separate Edit Sanitizer so annotation notes and inpainting requests cannot flow directly into execution without scope checks

## Pipeline

```text
Brief
  |
  v
Designly Director
  |
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

## Why the Edit Sanitizer exists

Generative image editing can change more than the user intended

A circle, arrow, scribble, mask, or sentence such as `fix this` describes attention, but may not fully specify the intended mutation. Designly converts the raw request into a typed `EditContract` before execution

The sanitizer validates

- approved source checkpoint
- source dimensions and annotation coordinate space
- one resolved semantic target
- positive, in-bounds geometry or a real mask reference
- one atomic mutation for bounded local edits
- exact replacement copy when applicable
- identity, geometry, text, and style locks
- protected non-target regions
- global-restyle leakage
- ambiguous target selection
- retry lineage, so failed renders are not used as the source for the next correction

If the contract is ambiguous or contradictory, the edit does not execute

Visual QA then compares the edited output against the approved source checkpoint and reviews target accuracy, edit-scope accuracy, and collateral change separately

## 14 Skills

| Skill | Responsibility |
|---|---|
| `designly-director` | Intake, locks, orchestration, conflict resolution, final signoff |
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

Every Skill has its own `agents/openai.yaml` interface configuration

## 9 Codex agents

| Agent | Boundary |
|---|---|
| `designly-director` | Orchestration and state ownership |
| `strategy-planner` | Read-only strategy analysis |
| `brand-guardian` | Read-only brand/product audit and vetoes |
| `taste-analyst` | Read-only reference/taste analysis |
| `structure-critic` | Read-only composition/type preflight |
| `craft-director` | Read-only photography/manipulation craft review |
| `arabic-visual-director` | Read-only Arabic/RTL review and vetoes |
| `edit-sanitizer` | Read-only bounded-edit normalization and vetoes |
| `visual-reviewer` | Read-only independent release gate |

Only the Director owns state mutation. Specialists return typed decisions and evidence rather than silently rewriting shared state

## Design quality gates

Designly deliberately rejects attractive-looking output when the communication or craft is wrong

Applicable gates include

- brief and primary-message accuracy
- hierarchy and composition floors
- typography and exact-copy checks
- Arabic glyph and RTL checks
- brand and product fidelity
- physical believability for composites
- AI-slop vetoes
- source-specific originality constraints
- bounded-edit target/scope/collateral checks

The Visual Reviewer must inspect the actual output before final approval

## AI-slop policy

Effects are not a substitute for a concept

Designly penalizes or blocks patterns such as unjustified effect stacks, equal emphasis everywhere, fake-luxury material treatment, random 3D decoration, generic futuristic UI, decorative particles, unmotivated cinematic lighting, and style adjectives that replace concrete visual decisions

The goal is not minimalism by default. The goal is visual decisions that have a communication job

## Taste Engine and Reference Memory

Taste Engine converts reference evidence into observations, transferable rules, anti-rules, constraints, and confidence

Reference Memory stores structured local metadata under stable IDs. It does not claim hidden model training or cross-device synchronization

When references are mixed, jobs are assigned deliberately, for example composition from one reference and lighting behavior from another, instead of averaging whole references into an indistinct style

## Install and test

This repository contains the plugin source and uploader-ready manifest at `.codex-plugin/plugin.json`

It does **not** claim public Plugin Directory approval until that external review has actually occurred

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
python3 tools/validate_public_plugin.py .
```

GitHub Actions runs these gates on pull requests and pushes to `main`

## Typed contracts

The shared contract boundary includes

- `DesignContext`
- `DesignSignalPacket`
- `DesignLock`
- `RevisionRequest`
- `EditContract`
- routing graph

Higher-authority constraints cannot be overwritten by lower-authority preferences

## Repository layout

```text
designly/
├── .codex-plugin/plugin.json
├── .codex/
│   ├── config.toml
│   └── agents/                  9 custom Codex agents
├── .github/workflows/ci.yml
├── shared/
│   ├── contracts/
│   ├── references/
│   └── scripts/
├── skills/                      14 discoverable Skills
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

The release gate requires byte-identical archives from the same source tree

## Current distribution caveats

- Public Plugin Directory acceptance is external to this repository and must be reported separately from local package readiness
- Reference Memory is local-first, not a shared remote memory service
- The repository currently has no explicit license file; no license is implied by the public GitHub visibility
- Stable public website/privacy/terms/support URLs should be added only when real pages exist, not invented for a submission form
