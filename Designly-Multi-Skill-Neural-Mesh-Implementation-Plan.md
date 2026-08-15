# Designly Multi-Skill + Multi-Agent Neural Mesh Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** Refactor Designly from one monolithic `art-director` skill into a production-ready network of focused Skills and custom Codex agents coordinated by a single Designly Director through typed handoffs, shared design state, confidence signals, hard-gate vetoes, and feedback loops.

**Architecture:** Keep Designly as a skills-only plugin for public portability, but expose multiple focused Skill entries in `skills/` and add project-scoped custom agents under `.codex/agents/` for Codex multi-agent execution. Use a shared contract package to connect the capabilities: each specialist reads a bounded slice of `DesignContext` and returns a `DesignSignalPacket`. The Director resolves conflicts, preserves immutable locks, and re-routes only the failing design dimension during revision.

**Tech Stack:** Markdown Agent Skills, `agents/openai.yaml` Skill interface metadata, Codex custom-agent TOML, JSON Schema Draft 2020-12, Python 3 deterministic validators/evals, JSON/JSONL fixtures, SVG assets, deterministic ZIP packaging.

## Global Constraints

- Product name is `Designly`.
- Plugin manifest remains `.codex-plugin/plugin.json`.
- Every visible Skill lives directly under `skills/<slug>/SKILL.md`.
- Every Skill interface is configured in `skills/<slug>/agents/openai.yaml`, not in `SKILL.md` metadata.
- `SKILL.md` frontmatter contains only `name` and `description`.
- Skills are split only when trigger, input, output, or success criteria differ.
- One primary user-facing orchestrator Skill remains available: `designly-director`.
- Custom Codex agents are narrow and opinionated and live under `.codex/agents/*.toml`.
- Do not add an MCP server unless shared remote/team memory becomes a real requirement.
- Reference Memory remains local-first.
- Hard-gate order: exact user/brand locks > communication job > hierarchy/composition > craft > stylistic preference.
- Do not expose internal chain-of-thought. Handoffs contain decisions, evidence, confidence, constraints, and next actions only.
- No decorative AI slop is permitted without a communication job.
- Arabic exact-copy, RTL behavior, logo fidelity, product identity, protected edit regions, and local-edit boundaries remain hard gates.
- Public package must remain uploader-safe and deterministic.
- No `__pycache__`, `.pyc`, secrets, absolute user paths, stale legacy names, or duplicate manifests in release ZIPs.

---

# 1. Target Architecture

## 1.1 Visible Skill Layer

Create these focused Skills:

1. `designly-director`
   - Entry point and orchestrator
   - Brief intake, routing, conflict resolution, final approval
   - Never owns specialist craft details when a specialist Skill exists

2. `creative-strategy`
   - Objective, audience, message hierarchy, visual concept territory
   - Converts marketing brief into one primary communication idea

3. `brand-intelligence`
   - Brand rules, observed patterns, brand-off test, product/logo fidelity
   - Separates official rules from inferred design choices

4. `taste-engine`
   - Reference deconstruction, evidence-backed transferable rules, anti-rules
   - Taste profile creation and reference-job assignment

5. `reference-memory`
   - REF IDs, recall, scoped likes/dislikes, project preference ledger
   - No claim of training or hidden model weight updates

6. `composition-director`
   - Grid, hierarchy, focal structure, grouping, negative space, crop, eye path
   - Owns pre-generation structural quality

7. `typography-director`
   - Type hierarchy, text zones, line breaks, measure, spacing, exact-copy strategy
   - Routes Arabic typography constraints to `arabic-rtl-director` when applicable

8. `photography-director`
   - Camera logic, lighting, lens behavior, materials, realism, subject treatment
   - Photography language only when photography is relevant

9. `manipulation-director`
   - Compositing, perspective, scale, contact, reflections, relighting, occlusion
   - Owns physical plausibility for impossible or composite scenes

10. `arabic-rtl-director`
    - Arabic-first composition, RTL reading flow, glyph correctness, mixed Arabic/English behavior, regional visual judgment

11. `campaign-dna`
    - Multi-asset continuity, visual-family rules, deliberate variation
    - Produces reusable campaign DNA rather than repeated layouts

12. `prompt-compiler`
    - Converts approved Art Direction Spec into provider/model-ready generation or edit instructions
    - Does not invent concept or repair weak structure

13. `visual-qa`
    - Post-generation critique, hard gates, category floors, anti-slop veto
    - Selects smallest revision route and sends the defect back to the correct specialist

This produces multiple Skills in the plugin UI while keeping each one recognizable and independently useful.

## 1.2 Custom Agent Layer

Create these Codex custom agents:

- `designly_director`
- `strategy_planner`
- `brand_guardian`
- `taste_analyst`
- `structure_critic`
- `craft_director`
- `arabic_visual_director`
- `visual_reviewer`

Do not create one agent per Skill automatically. Agents exist where isolated context or parallel analysis provides value.

Recommended responsibilities:

### `designly_director`
Own session state, spawn specialists, merge outputs, enforce locks, decide next node.

### `strategy_planner`
Read-only analysis of objective, audience, message, concept territories. No final artwork instructions.

### `brand_guardian`
Read-only review of supplied brand/product assets. May veto violations.

### `taste_analyst`
Read-only reference analysis and Taste Profile extraction. Never copies source-specific creative content.

### `structure_critic`
Read-only preflight of hierarchy, grid, composition, spacing, type zones, and visual path.

### `craft_director`
Handles photography/manipulation craft reasoning after structure is approved.

### `arabic_visual_director`
Owns Arabic/RTL-specific checks and returns hard-gate failures when copy or reading logic is malformed.

### `visual_reviewer`
Independent final QA. Must not defend the Director's previous decisions. Returns pass/fail, evidence, failing dimensions, and smallest repair route.

---

# 2. Design Neural Mesh

The connections are not free-form conversation between agents. They use typed packets.

## 2.1 Shared State Objects

Create:

- `DesignContext`
- `DesignSignalPacket`
- `DesignDecision`
- `DesignLock`
- `DesignVeto`
- `RevisionRequest`
- `CampaignDNA`
- `TasteProfile`
- `ReferenceRecord`
- `VisualReview`

### `DesignContext`

Contains only the current approved state:

```json
{
  "session_id": "DSN-2026-0001",
  "task_type": "campaign",
  "objective": "launch",
  "audience": {},
  "primary_message": "",
  "desired_action": "",
  "platform": {},
  "cultural_context": {},
  "locks": [],
  "brand_state": {},
  "taste_state": {},
  "strategy_state": {},
  "composition_state": {},
  "typography_state": {},
  "craft_state": {},
  "campaign_state": {},
  "generation_state": {},
  "qa_state": {}
}
```

### `DesignSignalPacket`

Every specialist returns:

```json
{
  "packet_id": "PKT-001",
  "from": "brand_guardian",
  "to": "designly_director",
  "job": "brand-audit",
  "decisions": [],
  "evidence": [],
  "confidence": 0.92,
  "hard_vetoes": [],
  "soft_warnings": [],
  "unresolved": [],
  "recommended_next": []
}
```

No hidden reasoning dump is allowed in packets.

## 2.2 Signal Priority

When signals conflict, resolve in this order:

1. user-supplied exact constraints
2. documented brand/product rules
3. safety/legal/cultural hard gates
4. primary communication job
5. hierarchy and composition
6. accessibility and legibility
7. campaign continuity
8. craft realism
9. explicit user taste preference
10. inferred taste preference
11. decorative finish

A lower-priority signal cannot overwrite a higher-priority lock.

## 2.3 Confidence Rules

- Explicit user instruction: `1.00`
- Documented brand rule: `1.00`
- Repeated observed brand behavior: target `0.75-0.90`
- Single-reference observation: target `0.55-0.80`
- Inferred design recommendation: target `0.40-0.70`
- Weak stylistic guess: do not promote to a persistent rule

Confidence is not a quality score. It expresses evidence strength.

## 2.4 Routing Graph

```text
USER
  |
  v
DESIGNLY DIRECTOR
  |
  +--> Creative Strategy
  |
  +--> Brand Intelligence --------+
  |                               |
  +--> Taste Engine <--> Reference Memory
  |                               |
  +-------------------------------+
  |
  v
COMPOSITION DIRECTOR
  |
  +--> Typography Director
  |       |
  |       +--> Arabic RTL Director when needed
  |
  +--> Photography Director
  |
  +--> Manipulation Director when needed
  |
  +--> Campaign DNA when multi-asset
  |
  v
PROMPT COMPILER / EXECUTION
  |
  v
VISUAL QA
  |
  +-- PASS --> Director approval
  |
  +-- FAIL --> route only failing dimension
                |
                +--> Strategy if concept failed
                +--> Composition if hierarchy failed
                +--> Typography if type failed
                +--> Arabic RTL if Arabic failed
                +--> Brand if identity failed
                +--> Craft if realism failed
                +--> Prompt Compiler if execution wording failed
```

This revision loop is the main "neural" behavior: the review signal activates only the node responsible for the defect.

---

# 3. Target File Structure

```text
Designly/
├── .codex-plugin/
│   └── plugin.json
├── .codex/
│   ├── config.toml
│   └── agents/
│       ├── designly-director.toml
│       ├── strategy-planner.toml
│       ├── brand-guardian.toml
│       ├── taste-analyst.toml
│       ├── structure-critic.toml
│       ├── craft-director.toml
│       ├── arabic-visual-director.toml
│       └── visual-reviewer.toml
├── shared/
│   ├── contracts/
│   │   ├── design-context.schema.json
│   │   ├── signal-packet.schema.json
│   │   ├── design-lock.schema.json
│   │   ├── revision-request.schema.json
│   │   └── routing-graph.json
│   ├── references/
│   │   ├── design-principles.md
│   │   ├── anti-slop-taxonomy.md
│   │   ├── model-guides.md
│   │   └── design-sources.md
│   └── scripts/
│       ├── validate_mesh.py
│       ├── validate_skill_interfaces.py
│       ├── validate_agent_configs.py
│       └── route_packet.py
├── skills/
│   ├── designly-director/
│   ├── creative-strategy/
│   ├── brand-intelligence/
│   ├── taste-engine/
│   ├── reference-memory/
│   ├── composition-director/
│   ├── typography-director/
│   ├── photography-director/
│   ├── manipulation-director/
│   ├── arabic-rtl-director/
│   ├── campaign-dna/
│   ├── prompt-compiler/
│   └── visual-qa/
├── evals/
│   ├── routing/
│   ├── handoffs/
│   ├── conflicts/
│   ├── visual/
│   ├── adversarial/
│   └── plugin-benchmark.json
├── assets/
└── tools/
```

Every Skill directory gets:

```text
SKILL.md
agents/openai.yaml
references/        only if specialist-specific
scripts/           only if specialist-specific
assets/            only when required
```

Do not duplicate shared design principles into every Skill.

---

# 4. Implementation Tasks

### Task 1: Freeze v3.2.1 behavior as regression baseline

**Files**
- Create: `evals/baseline/v3.2.1-behavior.json`
- Create: `evals/baseline/test_monolith_parity.py`
- Preserve current package as fixture outside release root

**Interfaces**
- Consumes: current v3.2.1 routing, taste-memory, design-preflight, release-gate behavior
- Produces: executable parity baseline used by later tasks

- [ ] Capture all existing passing scenarios: 21 routing, 7 design-preflight, 15 release-gate, prompt-lint, Taste Engine, Reference Memory, Arabic, local edit.
- [ ] Write failing parity test against an empty future multi-skill catalog.
- [ ] Verify it fails because required new Skill slugs do not exist.
- [ ] Commit baseline tests before structural changes.

Acceptance: no future task can remove a v3.2.1 capability without a deliberate test update.

### Task 2: Define shared Design Neural Mesh contracts

**Files**
- Create: `shared/contracts/design-context.schema.json`
- Create: `shared/contracts/signal-packet.schema.json`
- Create: `shared/contracts/design-lock.schema.json`
- Create: `shared/contracts/revision-request.schema.json`
- Create: `shared/contracts/routing-graph.json`
- Create: `shared/scripts/validate_mesh.py`
- Test: `evals/handoffs/test_contracts.py`

**Interfaces**
- Produces: canonical `DesignContext`, `DesignSignalPacket`, `DesignLock`, `RevisionRequest`

- [ ] Write failing tests for missing `from`, `to`, `job`, `decisions`, `confidence`, and veto fields.
- [ ] Add schemas with `additionalProperties: false` at contract boundaries.
- [ ] Add routing-graph validation: every node exists, every edge targets an existing Skill, no unreachable visible Skill.
- [ ] Add lock precedence validator.
- [ ] Pass tests and commit.

### Task 3: Create the Skill catalog and interface configs

**Files**
- Create 13 `skills/<slug>/SKILL.md`
- Create 13 `skills/<slug>/agents/openai.yaml`
- Create: `shared/scripts/validate_skill_interfaces.py`
- Test: `evals/routing/test_skill_catalog.py`

**Interfaces**
- Produces: 13 discoverable, focused Skill entries

- [ ] Write tests expecting exactly the approved Skill slugs.
- [ ] Test that every `SKILL.md` frontmatter contains only `name` and `description`.
- [ ] Test each description for non-overlapping primary triggers.
- [ ] Test every Skill has `agents/openai.yaml` with `interface.display_name`, `short_description`, icons, and default prompt.
- [ ] Implement Skill files with a narrow workflow boundary.
- [ ] Verify the UI-discovery catalog now exposes multiple Skills.
- [ ] Commit.

### Task 4: Convert the old monolith into `designly-director`

**Files**
- Replace: `skills/art-director/SKILL.md`
- Create: `skills/designly-director/SKILL.md`
- Move only orchestration references needed by Director
- Remove old `skills/art-director/` after parity is proven

**Interfaces**
- Consumes all SignalPackets
- Produces approved state transitions and specialist routing

- [ ] Write a failing test that Director refuses to implement specialist craft directly when a specialist exists.
- [ ] Implement intake, locks, state assembly, parallel-read routing, merge, conflict resolution, final approval.
- [ ] Make Director instruct Codex to delegate independent specialist analysis to subagents when the host supports subagents.
- [ ] Add fallback: if subagents unavailable, run the same specialist Skills sequentially without changing contracts.
- [ ] Pass parity tests and commit.

### Task 5: Create Codex custom-agent configs

**Files**
- Create: `.codex/config.toml`
- Create: `.codex/agents/*.toml`
- Create: `shared/scripts/validate_agent_configs.py`
- Test: `evals/handoffs/test_agents.py`

**Interfaces**
- Agents consume bounded tasks and return `DesignSignalPacket` summaries.

- [ ] Set `[agents]` concurrency cap conservatively, starting at 6.
- [ ] Keep analysis/review agents read-only when they do not need writes.
- [ ] Ensure each custom agent has `name`, `description`, `developer_instructions`.
- [ ] Ensure agent instructions prohibit raw hidden-reasoning dumps and require packet output.
- [ ] Verify no agent can overwrite locked fields.
- [ ] Commit.

### Task 6: Split marketing, brand, and taste intelligence

**Files**
- Create/modify:
  - `skills/creative-strategy/`
  - `skills/brand-intelligence/`
  - `skills/taste-engine/`
  - `skills/reference-memory/`
- Migrate relevant old references and scripts without duplication.

**Interfaces**
- Strategy produces `strategy_state`
- Brand produces `brand_state` + vetoes
- Taste produces `taste_state`
- Memory produces REF records and scoped preference evidence

- [ ] Write routing tests showing each activates on distinct requests.
- [ ] Write conflict test: documented brand rule beats inferred taste.
- [ ] Write memory test: dislike for lighting does not become dislike for composition.
- [ ] Write originality test: reference content is not copied as transferable taste.
- [ ] Implement and pass.
- [ ] Commit.

### Task 7: Split structure and typography intelligence

**Files**
- Create/modify:
  - `skills/composition-director/`
  - `skills/typography-director/`
  - `skills/arabic-rtl-director/`

**Interfaces**
- Composition produces structural Art Direction Spec
- Typography produces type plan
- Arabic RTL may hard-veto malformed copy or reading logic

- [ ] Write structural preflight tests for equal emphasis, accidental tangencies, dead space, unsupported center bias, weak type zones.
- [ ] Write exact-copy Arabic gate tests.
- [ ] Write mixed Arabic/English layout tests.
- [ ] Verify RTL is not implemented as simple mirroring.
- [ ] Implement and commit.

### Task 8: Split photography and manipulation craft

**Files**
- Create/modify:
  - `skills/photography-director/`
  - `skills/manipulation-director/`

**Interfaces**
- Photography produces camera/light/material plan
- Manipulation produces physical-integration plan and consistency checks

- [ ] Write tests proving camera specs must have a visible job.
- [ ] Write physics tests for contact shadow, reflection direction, occlusion, scale, and perspective.
- [ ] Test surreal concepts for believable physical response.
- [ ] Implement and commit.

### Task 9: Campaign DNA and Prompt Compiler

**Files**
- Create/modify:
  - `skills/campaign-dna/`
  - `skills/prompt-compiler/`

**Interfaces**
- Campaign DNA emits reusable continuity constraints
- Prompt Compiler consumes only approved states and produces provider-ready execution instructions

- [ ] Write test that campaign assets vary conceptually without losing family resemblance.
- [ ] Write test that Prompt Compiler cannot silently invent an unresolved concept.
- [ ] Write model-adapter tests for generation vs edit vs protected local edit.
- [ ] Implement and commit.

### Task 10: Independent Visual QA and revision routing

**Files**
- Create/modify: `skills/visual-qa/`
- Create: `evals/visual/test_revision_router.py`

**Interfaces**
- Produces `VisualReview` and `RevisionRequest`

- [ ] Test category floors independently from weighted average.
- [ ] Test AI-slop hard veto.
- [ ] Test defect-to-specialist routing.
- [ ] Test local edit does not cause concept regeneration.
- [ ] Test Visual QA cannot approve its own uninspected hypothetical output.
- [ ] Implement and commit.

### Task 11: Cross-Skill conflict and adversarial suite

**Files**
- Create:
  - `evals/conflicts/*.json`
  - `evals/adversarial/*.json`
  - `evals/handoffs/*.json`
  - `evals/run_mesh_evals.py`

Scenarios must include:
- brand rule vs taste preference
- exact Arabic copy vs aesthetic line break
- campaign continuity vs new-platform crop
- user requests effect stack
- multiple references disagree on lighting
- product packshot conflicts with generated perspective
- local edit with unrelated redesign pressure
- Director receives two equal-confidence contradictory recommendations
- one agent fails or returns malformed packet
- subagents unavailable
- more than one specialist tries to modify the same state field

Acceptance:
- deterministic routing
- no silent conflict resolution
- no lock overwrite
- correct fallback behavior
- no design slop introduced by merge

### Task 12: Plugin UI, manifest, and Marketplace update

**Files**
- Modify: `.codex-plugin/plugin.json`
- Modify Marketplace entry
- Update README capability map
- Keep Designly line-art identity consistent across all Skill interfaces

- [ ] Update plugin capabilities to describe multi-skill network accurately.
- [ ] Keep listing limits valid.
- [ ] Validate every Skill interface independently.
- [ ] Verify multiple Skills appear in scanner/discovery output.
- [ ] Ensure only one plugin manifest exists in upload package.
- [ ] Commit.

### Task 13: Plugin Eval benchmark redesign

**Files**
- Replace: `evals/plugin-benchmark.json`
- Create: `.plugin-eval/benchmark.json` when the CLI is available

Benchmark groups:
1. correct Skill discovery
2. orchestrator routing
3. parallel specialist delegation
4. conflict resolution
5. token/context isolation benefit
6. revision-loop accuracy
7. reference-memory correctness
8. Arabic hard gates
9. anti-slop behavior
10. graceful single-agent fallback

Measure:
- skill selected
- agents spawned
- packet validity
- number of unnecessary specialists
- wrong-node routing rate
- lock violations
- final hard-gate pass
- tokens where measurable
- wall-clock where measurable

### Task 14: Release gate and deterministic packaging

**Files**
- Modify: `tools/validate_public_plugin.py`
- Modify: `tools/package_plugin.py`
- Create: `VERIFICATION-v4.md`
- Create: `SHA256SUMS`

- [ ] Run every repository-native test.
- [ ] Run mesh validator.
- [ ] Run Skill interface validator.
- [ ] Run custom-agent validator.
- [ ] Run public plugin validator.
- [ ] Build ZIP A.
- [ ] Build ZIP B.
- [ ] Require byte-identical SHA256.
- [ ] Inspect archive first-level paths.
- [ ] Extract to clean directory.
- [ ] Rerun all tests from extracted copy.
- [ ] Verify uploader detects `.codex-plugin/plugin.json`.
- [ ] Verify skill scanner returns all 13 Skill entries.
- [ ] Only then label release `Designly v4.0.0`.

---

# 5. Parallelism Strategy

Parallelize read-heavy specialists only when their inputs are already locked.

Good parallel batch after intake:
- `strategy_planner`
- `brand_guardian`
- `taste_analyst`

Do not parallelize:
- Prompt Compiler before composition is approved
- Visual QA before output exists
- two agents that write the same state section
- typography and Arabic exact-copy decisions when one depends on the other

Default max concurrent specialist threads: 6.

The Director waits for required packets, merges them, then advances the graph.

---

# 6. Failure Behavior

If a specialist fails:
- preserve previous approved state
- mark that node `failed`
- retry once only when failure is transient or malformed output
- otherwise run sequential fallback with the corresponding Skill
- never fabricate a specialist result

If a packet violates schema:
- reject packet
- do not partially merge it

If two specialists conflict:
- apply Signal Priority
- if equal-priority hard constraints remain incompatible, ask one user question

If Visual QA fails:
- create one `RevisionRequest`
- route to the smallest responsible node
- do not rerun the full network by default

---

# 7. Definition of Done

Designly v4 is complete only when:

- Plugin scanner shows multiple focused Skills, not one `art-director` Skill.
- `designly-director` remains the primary end-to-end entry.
- Every Skill has its own valid `agents/openai.yaml`.
- At least 8 custom Codex agents are valid and bounded.
- All cross-agent handoffs validate against JSON Schema.
- Hard locks cannot be overwritten by a lower-priority specialist.
- Reference Memory and Taste Engine remain local-first and compatible with direct use.
- Arabic/RTL, brand fidelity, product fidelity, local edit, anti-slop, and design-preflight behavior from v3.2.1 remain regression-safe.
- Visual QA routes revisions to the correct specialist rather than restarting everything.
- Multi-agent execution falls back safely to sequential Skills.
- Plugin Eval contains network-specific benchmark scenarios.
- Public plugin validation passes.
- ZIP A and B are byte-identical.
- Clean-extraction tests pass.
- Uploader detects the manifest.
- The release contains no transient caches, secrets, duplicate manifests, absolute user paths, or stale legacy names.
