# Visual Pattern Canon Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development recommended, or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox syntax for tracking

**Goal:** Add an internal, model-agnostic Visual Pattern Canon to Designly, seeded from a pinned `awesome-gpt-image-2` snapshot, with deterministic retrieval, strict provenance, anti-copy controls, Taste Engine handoff, Prompt Compiler isolation, and Visual QA expectations

**Architecture:** External visual corpora are imported through source adapters into a Designly-owned normalized contract. Retrieval happens only after strategy and locks are stable, returns evidence rather than prompts, and feeds Taste Engine before composition and generation. The local normalized snapshot is committed so ordinary Designly use and CI remain network-independent

**Tech Stack:** Python 3, JSON Schema Draft 2020-12, Markdown Agent Skills, deterministic JSON fixtures, existing Designly Neural Mesh contracts and eval harness

**Spec:** `docs/superpowers/specs/2026-08-29-visual-pattern-canon-design.md`

## Global Constraints

- Preserve Designly's current 21 public Skills and do not add a public Visual Pattern Canon Skill in v1
- Keep the feature internal under `shared/` with focused updates to existing Skills
- Initial upstream source is `freestylefly/awesome-gpt-image-2`
- Initial upstream pin is `c7d293963b21c60bf338003915438cc5c39dd3ca`
- Upstream license is MIT and attribution must be preserved
- Store normalized metadata only, never upstream image bytes or full prompt bodies
- Canon evidence can never outrank user locks, brand locks, communication job, hierarchy, accessibility, or cultural requirements
- Keep Personal Reference Memory `REF-####` semantics separate from Visual Canon `CANON-*` semantics
- Add `visual_canon_state` to `DesignContext` as optional in v1 to preserve backward compatibility
- Do not add embeddings, a vector database, a hosted retrieval service, or runtime network calls in v1
- CI validates committed snapshots and fixtures without depending on GitHub availability
- Use TDD for every behavioral change
- Keep commits atomic and independently reviewable

---

## File Structure

Create

```text
shared/contracts/visual-pattern.schema.json
shared/contracts/visual-canon-query.schema.json
shared/contracts/visual-canon-result.schema.json
shared/references/visual-canon.md
shared/references/visual-canon/source-registry.json
shared/references/visual-canon/generated/awesome-gpt-image-2.json
shared/scripts/visual_canon_lib.py
shared/scripts/sync_visual_canon.py
shared/scripts/search_visual_canon.py
shared/scripts/validate_visual_canon.py

evals/visual_canon/fixtures/awesome-style-library.fixture.json
evals/visual_canon/fixtures/expected-normalized.fixture.json
evals/visual_canon/test_contracts.py
evals/visual_canon/test_awesome_adapter.py
evals/visual_canon/test_sync_determinism.py
evals/visual_canon/test_provenance.py
evals/visual_canon/test_anti_copy.py
evals/visual_canon/test_ranking.py
evals/visual_canon/test_integration.py
```

Modify

```text
shared/contracts/design-context.schema.json
skills/designly-director/SKILL.md
skills/taste-engine/SKILL.md
skills/composition-director/SKILL.md
skills/image-director/SKILL.md
skills/prompt-compiler/SKILL.md
skills/visual-qa/SKILL.md
package.json
README.md
NOTICE
```

Primary module boundaries

```text
visual_canon_lib.py
  load_registry(path: Path) -> dict
  normalize_awesome_template(template: dict, source_meta: dict) -> dict
  validate_pattern(pattern: dict) -> list[str]
  validate_canon(canon: dict) -> list[str]
  score_pattern(query: dict, pattern: dict) -> tuple[float, dict[str, float]]
  search_canon(query: dict, canon: dict) -> dict
  should_retrieve(context: dict) -> tuple[bool, str]

sync_visual_canon.py
  sync_source(source_id: str, source_json: Path, output: Path, registry: Path) -> int

search_visual_canon.py
  CLI wrapper around search_canon

validate_visual_canon.py
  CLI wrapper around validate_canon
```

---

### Task 1: Freeze contracts and backward compatibility

**Files:**
- Create: `shared/contracts/visual-pattern.schema.json`
- Create: `shared/contracts/visual-canon-query.schema.json`
- Create: `shared/contracts/visual-canon-result.schema.json`
- Modify: `shared/contracts/design-context.schema.json`
- Create: `evals/visual_canon/test_contracts.py`

**Interfaces:**
- Consumes: existing Draft 2020-12 Designly contract conventions
- Produces: canonical `VisualPattern`, `VisualCanonQuery`, `VisualCanonResult`, and optional `DesignContext.visual_canon_state`

- [ ] **Step 1: Write failing schema tests**

Create `evals/visual_canon/test_contracts.py` with tests that load the four schemas and prove the required boundary behavior

```python
from pathlib import Path
import json
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
CONTRACTS = ROOT / "shared" / "contracts"


def load(name: str) -> dict:
    return json.loads((CONTRACTS / name).read_text(encoding="utf-8"))


def test_visual_pattern_requires_provenance_and_transferable_rules():
    schema = load("visual-pattern.schema.json")
    validator = Draft202012Validator(schema)
    candidate = {
        "pattern_id": "CANON-AGI2-poster-layout-system",
        "source": {
            "source_id": "awesome-gpt-image-2",
            "source_ref": "c7d293963b21c60bf338003915438cc5c39dd3ca",
            "source_record_id": "poster-layout-system",
            "license": "MIT"
        },
        "task_family": "poster",
        "communication_jobs": ["campaign-key-visual"],
        "styles": ["poster"],
        "scenes": ["commerce"],
        "tags": ["poster", "typography"],
        "use_when": [],
        "transferable_rules": ["clear headline hierarchy"],
        "anti_rules": ["avoid collage density"],
        "example_case_ids": [345],
        "compatible_models": ["gpt-image-2"],
        "provenance_confidence": 1.0
    }
    assert list(validator.iter_errors(candidate)) == []


def test_design_context_accepts_missing_visual_canon_state():
    schema = load("design-context.schema.json")
    assert "visual_canon_state" not in schema["required"]
```

- [ ] **Step 2: Run the focused contract test and confirm RED**

Run

```bash
pytest evals/visual_canon/test_contracts.py -q
```

Expected before implementation

```text
FAIL because visual-pattern.schema.json and the other new contracts do not exist
```

- [ ] **Step 3: Add the three new schemas**

Contract requirements

`visual-pattern.schema.json`

- `additionalProperties: false`
- required provenance object with source id, pinned source ref, source record id, and license
- canonical `CANON-*` pattern id
- arrays for communication jobs, styles, scenes, tags, transferable rules, anti-rules, example case ids, and compatible models
- provenance confidence between `0` and `1`
- no `prompt`, `raw_prompt`, `image`, `image_bytes`, or arbitrary source payload fields

`visual-canon-query.schema.json`

- task family required
- communication job optional
- styles and composition intent optional
- model target optional
- constraints object allowed
- `top_k` integer from `1` to `5`, default behavior implemented in Python

`visual-canon-result.schema.json`

- required query id
- required selected pattern list
- each result carries pattern id, total score, score breakdown, source provenance, transferable rules, anti-rules, and nullable assigned job

- [ ] **Step 4: Extend `DesignContext` without breaking existing fixtures**

Add only this optional property

```json
"visual_canon_state": {"type": "object"}
```

Do not add it to the `required` array

- [ ] **Step 5: Run contract and existing handoff tests**

```bash
pytest evals/visual_canon/test_contracts.py evals/handoffs -q
```

Expected

```text
PASS
```

- [ ] **Step 6: Commit**

```bash
git add shared/contracts evals/visual_canon/test_contracts.py
git commit -m "feat: define visual canon contracts"
```

---

### Task 2: Add source registry and pinned `awesome-gpt-image-2` adapter

**Files:**
- Create: `shared/references/visual-canon/source-registry.json`
- Create: `shared/scripts/visual_canon_lib.py`
- Create: `evals/visual_canon/fixtures/awesome-style-library.fixture.json`
- Create: `evals/visual_canon/fixtures/expected-normalized.fixture.json`
- Create: `evals/visual_canon/test_awesome_adapter.py`

**Interfaces:**
- Consumes: a local JSON file shaped like upstream `data/style-library.json`
- Produces: `normalize_awesome_template(template, source_meta) -> VisualPattern dict`

- [ ] **Step 1: Add a minimal source fixture before implementation**

The fixture must include at least

- one poster template
- one photography template
- category, style, scene, tags, `useWhen`, guidance, pitfalls, and example cases
- one unknown extra upstream field to prove the adapter ignores unsupported source data instead of leaking it

Use source metadata matching

```json
{
  "id": "awesome-gpt-image-2",
  "repository": "freestylefly/awesome-gpt-image-2",
  "pinned_ref": "c7d293963b21c60bf338003915438cc5c39dd3ca",
  "source_artifact": "data/style-library.json",
  "license": "MIT"
}
```

- [ ] **Step 2: Write failing adapter tests**

```python
from shared.scripts.visual_canon_lib import normalize_awesome_template


def test_adapter_preserves_provenance_and_drops_unknown_source_fields(source_meta, poster_template):
    result = normalize_awesome_template(poster_template, source_meta)
    assert result["pattern_id"] == "CANON-AGI2-poster-layout-system"
    assert result["source"]["source_ref"] == source_meta["pinned_ref"]
    assert "unknown_upstream_field" not in result
    assert "prompt" not in result
```

Add a second test proving normalization is stable across identical inputs

- [ ] **Step 3: Run the adapter tests and confirm RED**

```bash
pytest evals/visual_canon/test_awesome_adapter.py -q
```

- [ ] **Step 4: Create the source registry**

Use a versioned top-level contract

```json
{
  "schema_version": 1,
  "sources": [
    {
      "id": "awesome-gpt-image-2",
      "kind": "visual-pattern-library",
      "repository": "freestylefly/awesome-gpt-image-2",
      "license": "MIT",
      "enabled": true,
      "priority": 70,
      "adapter": "awesome_gpt_image_2",
      "source_artifact": "data/style-library.json",
      "pinned_ref": "c7d293963b21c60bf338003915438cc5c39dd3ca"
    }
  ]
}
```

- [ ] **Step 5: Implement normalization in `visual_canon_lib.py`**

Normalization rules

```text
Posters & Typography -> poster
Photography & Realism -> photography
Products & E-commerce -> product
Charts & Infographics -> infographic
Brand & Logos -> brand
UI & Interfaces -> ui
Characters & People -> character
Scenes & Storytelling -> scene
Documents & Publishing -> document
Architecture & Spaces -> architecture
Illustration & Art -> illustration
History & Classical Themes -> history
Other Use Cases -> other
```

Convert structured guidance into compact transferable rules and pitfalls into anti-rules

Do not include full prompt bodies even if they become available in a future upstream shape

- [ ] **Step 6: Run adapter tests and compare against the expected normalized fixture**

```bash
pytest evals/visual_canon/test_awesome_adapter.py -q
```

- [ ] **Step 7: Commit**

```bash
git add shared/references/visual-canon/source-registry.json shared/scripts/visual_canon_lib.py evals/visual_canon/fixtures evals/visual_canon/test_awesome_adapter.py
git commit -m "feat: add awesome image canon adapter"
```

---

### Task 3: Build deterministic sync, provenance validation, and anti-copy gates

**Files:**
- Create: `shared/scripts/sync_visual_canon.py`
- Create: `shared/scripts/validate_visual_canon.py`
- Create: `shared/references/visual-canon/generated/awesome-gpt-image-2.json`
- Create: `evals/visual_canon/test_sync_determinism.py`
- Create: `evals/visual_canon/test_provenance.py`
- Create: `evals/visual_canon/test_anti_copy.py`
- Modify: `shared/scripts/visual_canon_lib.py`

**Interfaces:**
- Consumes: source registry entry plus a local upstream JSON artifact
- Produces: deterministic committed canon snapshot and validation errors

- [ ] **Step 1: Write RED tests for deterministic output**

The same fixture and registry must produce byte-identical output twice

```python

def test_sync_output_is_byte_deterministic(tmp_path, fixture_path, registry_path):
    first = tmp_path / "first.json"
    second = tmp_path / "second.json"
    sync_source("awesome-gpt-image-2", fixture_path, first, registry_path)
    sync_source("awesome-gpt-image-2", fixture_path, second, registry_path)
    assert first.read_bytes() == second.read_bytes()
```

Serialize with sorted keys, UTF-8, stable record ordering by `pattern_id`, and a trailing newline

- [ ] **Step 2: Write provenance and anti-copy RED tests**

Required failures

```text
missing source_ref
missing license
duplicate pattern_id
pattern_id outside CANON namespace
raw_prompt field
prompt field
image_bytes field
embedded base64 image payload
source payload passthrough
```

Also prove that ordinary short rule text such as `clear headline hierarchy` is allowed

- [ ] **Step 3: Implement validators in `visual_canon_lib.py`**

Use explicit forbidden field names and a bounded base64/data-URI detector

Return error strings instead of throwing deep inside record validation

`validate_canon` aggregates errors with pattern ids so sync failures are actionable

- [ ] **Step 4: Implement `sync_visual_canon.py` with safe-write behavior**

Required flow

```text
read registry
read source artifact
parse all supported templates
normalize in memory
validate all records
serialize to temporary sibling file
fsync or close successfully
atomic replace destination
```

If validation fails, leave the previous generated snapshot untouched

The script must accept

```bash
python3 shared/scripts/sync_visual_canon.py \
  --source awesome-gpt-image-2 \
  --input evals/visual_canon/fixtures/awesome-style-library.fixture.json \
  --output /tmp/canon.json
```

Do not add network fetching to the script in v1

Maintainers obtain or update the upstream artifact separately, then run the deterministic importer

- [ ] **Step 5: Generate the initial committed snapshot from the pinned upstream artifact**

The committed snapshot header must include

```json
{
  "schema_version": 1,
  "source_id": "awesome-gpt-image-2",
  "source_ref": "c7d293963b21c60bf338003915438cc5c39dd3ca",
  "license": "MIT",
  "patterns": []
}
```

Do not commit upstream images or raw full prompts

- [ ] **Step 6: Run sync and safety tests**

```bash
pytest \
  evals/visual_canon/test_sync_determinism.py \
  evals/visual_canon/test_provenance.py \
  evals/visual_canon/test_anti_copy.py -q

python3 shared/scripts/validate_visual_canon.py shared/references/visual-canon/generated/awesome-gpt-image-2.json
```

- [ ] **Step 7: Commit**

```bash
git add shared/scripts shared/references/visual-canon/generated evals/visual_canon
git commit -m "feat: add deterministic visual canon sync"
```

---

### Task 4: Implement explainable deterministic retrieval

**Files:**
- Create: `shared/scripts/search_visual_canon.py`
- Create: `evals/visual_canon/test_ranking.py`
- Modify: `shared/scripts/visual_canon_lib.py`

**Interfaces:**
- Consumes: `VisualCanonQuery` plus committed normalized canon
- Produces: `VisualCanonResult` with stable top-k ranking and score breakdown

- [ ] **Step 1: Write ranking RED tests**

Use at least six patterns across poster, product, infographic, and photography families

Required scenarios

```text
exact task family outranks style-only match
communication job improves score when present
model compatibility contributes only 10 percent
weak style similarity cannot beat a task-family mismatch
stable ties sort by pattern_id
no meaningful match returns an empty selection
requested top_k above 5 is rejected by schema or CLI
```

- [ ] **Step 2: Define exact scoring behavior**

Implement weights

```python
WEIGHTS = {
    "task_family": 0.30,
    "communication_job": 0.20,
    "scene": 0.15,
    "style": 0.15,
    "composition_intent": 0.10,
    "model_compatibility": 0.10,
}
```

Each dimension returns a value from `0.0` to `1.0`

The first implementation uses exact normalized tags plus an explicit small alias map only

Do not use fuzzy matching libraries or an LLM in v1

- [ ] **Step 3: Add a minimum usefulness threshold**

Start with

```python
MIN_USEFUL_SCORE = 0.35
```

Patterns below the threshold are omitted

The threshold must be one constant with tests around both sides of the boundary

- [ ] **Step 4: Implement `score_pattern` and `search_canon`**

Result ordering

```python
sorted(matches, key=lambda item: (-item["score"], item["pattern_id"]))
```

Round exposed score values consistently to four decimals while using full precision internally

- [ ] **Step 5: Add CLI support**

Example

```bash
python3 shared/scripts/search_visual_canon.py \
  --query '{"task_family":"poster","communication_job":"campaign-key-visual","styles":["poster"],"top_k":3}'
```

The CLI prints JSON only on stdout and diagnostics only on stderr

- [ ] **Step 6: Run ranking tests**

```bash
pytest evals/visual_canon/test_ranking.py -q
```

- [ ] **Step 7: Commit**

```bash
git add shared/scripts/search_visual_canon.py shared/scripts/visual_canon_lib.py evals/visual_canon/test_ranking.py
git commit -m "feat: add explainable visual canon retrieval"
```

---

### Task 5: Wire retrieval into Director and Taste Engine without changing authority order

**Files:**
- Modify: `skills/designly-director/SKILL.md`
- Modify: `skills/taste-engine/SKILL.md`
- Modify: `skills/composition-director/SKILL.md`
- Create: `shared/references/visual-canon.md`
- Create: `evals/visual_canon/test_integration.py`

**Interfaces:**
- Consumes: approved strategy state, DesignLocks, brand state, optional personal references, `VisualCanonResult`
- Produces: session-scoped `visual_canon_state` and Taste Engine assigned jobs

- [ ] **Step 1: Write RED integration tests for retrieval triggers**

Test `should_retrieve(context)` with these cases

Expected `True`

```text
new campaign key visual with broad visual direction
poster request without strong supplied visual references
product ad generation with approved strategy
infographic request where structural examples reduce uncertainty
```

Expected `False`

```text
exact local image edit
logo correction with strict source geometry
copy-only request
pure strategy request
user supplied sufficient exact references and requested bounded replication
```

- [ ] **Step 2: Implement `should_retrieve` as deterministic policy**

Return a tuple

```python
(bool, reason_code)
```

Use explicit reason codes such as

```text
visual-reference-useful
exact-edit-skip
non-visual-skip
sufficient-user-reference-skip
```

- [ ] **Step 3: Update Designly Director workflow**

Add the Visual Canon decision after

```text
strategy approval
user and brand locks
reference sufficiency check
```

and before

```text
Taste Engine final reference-job assignment
Composition Director
```

The Director must be instructed to continue normally when retrieval returns zero matches

- [ ] **Step 4: Update Taste Engine contract**

Add explicit distinction

```text
REF-* = personal or project preference evidence
CANON-* = external execution evidence
```

Taste Engine may assign a narrow job to each useful canon pattern, but must not record canon use as a persistent user like or dislike

Add an example

```text
CANON-AGI2-poster-layout-system -> composition
CANON-AGI2-conceptual-typography-poster -> typography
REF-1042 -> lighting
brand rules -> palette and logo behavior
```

- [ ] **Step 5: Update Composition Director guidance**

Composition Director may consume transferable geometry, density, hierarchy, and negative-space rules from assigned canon evidence

It must not reconstruct exact source layouts or coordinates

- [ ] **Step 6: Add integration assertions**

Tests must prove

- `CANON-*` never enters Reference Memory persistence APIs or sample records
- a higher-priority DesignLock vetoes conflicting canon evidence
- empty canon matches do not stop the pipeline
- canon evidence is downstream of strategy rather than a source of the primary concept

- [ ] **Step 7: Run focused integration plus routing regressions**

```bash
pytest evals/visual_canon/test_integration.py evals/routing evals/conflicts -q
```

- [ ] **Step 8: Commit**

```bash
git add skills/designly-director skills/taste-engine skills/composition-director shared/references/visual-canon.md evals/visual_canon/test_integration.py shared/scripts/visual_canon_lib.py
git commit -m "feat: route visual canon through taste engine"
```

---

### Task 6: Enforce Image Director, Prompt Compiler, and Visual QA boundaries

**Files:**
- Modify: `skills/image-director/SKILL.md`
- Modify: `skills/prompt-compiler/SKILL.md`
- Modify: `skills/visual-qa/SKILL.md`
- Modify: `evals/visual_canon/test_integration.py`

**Interfaces:**
- Consumes: approved Art Direction Spec plus optional assigned canon rules and expectations
- Produces: provider-native prompt instructions and advisory QA expectations without upstream prompt authority

- [ ] **Step 1: Add a failing compiler-boundary test**

Create a synthetic state containing

```json
{
  "source_prompt": "verbatim upstream prompt text",
  "raw_prompt": "another forbidden payload"
}
```

The expected behavior is rejection or omission before provider-native compilation

The test must also prove that safe normalized rules such as `clear headline hierarchy` remain usable

- [ ] **Step 2: Update Image Director guidance**

Image Director may use normalized canon evidence to clarify execution family and model compatibility after composition approval

It cannot use canon selection to invent or replace the approved creative concept

- [ ] **Step 3: Update Prompt Compiler hard boundary**

Document and test

```text
Accepted
approved strategy
composition state
typography state
craft state
pattern expectations
provider physics

Rejected as authority
raw upstream prompt
full source record passthrough
unapproved source copy
```

The existing GPT Image 2 adapter remains one provider adapter among several

- [ ] **Step 4: Update Visual QA**

Visual QA evaluates in this order

```text
1 user and brand hard gates
2 approved Art Direction Spec
3 accessibility and legibility
4 campaign continuity when applicable
5 craft realism
6 advisory pattern expectations
```

A pattern mismatch alone cannot fail an otherwise valid design unless the relevant expectation was explicitly promoted into approved Art Direction state

- [ ] **Step 5: Add QA behavior tests**

Required cases

- output violates a user lock but matches a canon pattern -> FAIL due to user lock
- output honors Art Direction but differs from a canon pattern -> PASS or warning only
- output violates a promoted structural expectation -> route to Composition Director
- raw source prompt appears in compiler input -> rejected

- [ ] **Step 6: Run focused tests plus adapter tests**

```bash
pytest evals/visual_canon/test_integration.py evals/adapters evals/visual -q
```

- [ ] **Step 7: Commit**

```bash
git add skills/image-director skills/prompt-compiler skills/visual-qa evals/visual_canon/test_integration.py
git commit -m "feat: enforce visual canon execution boundaries"
```

---

### Task 7: Add maintainer commands, attribution, and documentation

**Files:**
- Modify: `package.json`
- Modify: `README.md`
- Modify: `NOTICE`
- Modify: `shared/references/visual-canon.md`
- Modify: `shared/references/visual-canon/source-registry.json`

**Interfaces:**
- Consumes: existing scripts and generated canon
- Produces: discoverable maintainer workflow and correct third-party attribution

- [ ] **Step 1: Add package scripts without changing runtime dependencies**

Add commands equivalent to

```json
{
  "canon:validate": "python3 shared/scripts/validate_visual_canon.py shared/references/visual-canon/generated/awesome-gpt-image-2.json",
  "canon:search": "python3 shared/scripts/search_visual_canon.py",
  "canon:sync:fixture": "python3 shared/scripts/sync_visual_canon.py --source awesome-gpt-image-2 --input evals/visual_canon/fixtures/awesome-style-library.fixture.json --output /tmp/designly-canon-fixture.json"
}
```

Do not create a default network sync command in v1

- [ ] **Step 2: Document the update procedure**

`shared/references/visual-canon.md` must explain

1. inspect upstream changes
2. deliberately update `pinned_ref`
3. obtain the corresponding `data/style-library.json`
4. run the adapter and validator
5. inspect normalized diff for unexpected copied content or taxonomy drift
6. run the full visual canon eval suite
7. commit pin and generated output together

- [ ] **Step 3: Add README architecture mention**

Describe Visual Pattern Canon as an internal evidence corpus, not another creative decision-maker

Keep the existing 21 public Skill count unchanged

- [ ] **Step 4: Add NOTICE attribution**

Credit

```text
freestylefly/awesome-gpt-image-2
MIT License
Used as the initial external structured visual-pattern source for Designly Visual Pattern Canon
```

Do not imply endorsement or ownership of upstream assets

- [ ] **Step 5: Verify docs and commands**

```bash
npm run canon:validate
npm run canon:sync:fixture
python3 shared/scripts/search_visual_canon.py --query '{"task_family":"poster","top_k":3}'
```

- [ ] **Step 6: Commit**

```bash
git add package.json README.md NOTICE shared/references/visual-canon*
git commit -m "docs: document visual canon maintenance"
```

---

### Task 8: Run full regression, supply-chain checks, and release gate

**Files:**
- Modify only if a failing check reveals a defect in the implementation
- Do not broaden scope during this task

**Interfaces:**
- Consumes: completed Tasks 1 through 7
- Produces: release evidence for the Visual Pattern Canon feature

- [ ] **Step 1: Run the complete Visual Canon suite**

```bash
pytest evals/visual_canon -q
```

Expected

```text
PASS
```

- [ ] **Step 2: Run Neural Mesh regressions**

```bash
python3 evals/run_mesh_evals.py
pytest evals/handoffs evals/routing evals/conflicts -q
```

Expected

```text
PASS
```

- [ ] **Step 3: Run model adapter and visual regressions**

```bash
python3 evals/adapters/test_adapters.py
pytest evals/visual -q
```

Expected

```text
PASS
```

- [ ] **Step 4: Run supply-chain and public-package checks**

```bash
python3 evals/supply_chain/test_supply_chain.py
python3 tools/validate_public_plugin.py .
python3 tools/publish_skills_sh.py --check
```

Expected

```text
PASS
```

- [ ] **Step 5: Run package-level tests**

```bash
bun test
```

Expected

```text
PASS
```

- [ ] **Step 6: Inspect generated snapshot diff manually**

Acceptance inspection

```text
no image blobs
no data URIs
no full prompts
all patterns have source_ref and license
all IDs use CANON namespace
record ordering is stable
upstream pin matches source registry
```

- [ ] **Step 7: Verify no public Skill-count regression**

Confirm the package still exposes the same 21 public Skills unless another independently approved change landed on the base branch

- [ ] **Step 8: Commit any verification-only adjustments**

Only create this commit if verification required a focused correction

```bash
git add <only-files-needed-for-verification-fix>
git commit -m "test: harden visual canon release checks"
```

---

## Engineering Review Pressure Test

### Data flow

```text
Pinned source artifact
  -> adapter
  -> normalized records
  -> contract validator
  -> committed local snapshot
  -> deterministic query
  -> score breakdown
  -> Taste Engine job assignment
  -> approved Art Direction state
  -> model adapter compilation
  -> generation
  -> Visual QA
```

No reverse edge may write canon usage into Personal Reference Memory

### Highest-risk failure modes

| Risk | Prevention | Verification |
|---|---|---|
| External style starts driving concept | Retrieval occurs after strategy approval | Director routing tests |
| Prompt copying enters package | Strict normalized allowlist and forbidden fields | Anti-copy tests |
| User preference memory gets polluted | Separate `CANON-*` namespace and no persistence handoff | Integration tests |
| Upstream changes break sync | Pinned ref and fail-closed adapter | Adapter fixture tests |
| Network outage breaks Designly | Committed local snapshot | Offline test path |
| Ranking becomes opaque | Fixed weights and score breakdown | Ranking tests |
| Canon overrides brand lock | Existing lock priority remains authoritative | Conflict test |
| GPT Image 2 source locks Designly to one model | Prompt Compiler consumes model-agnostic rules only | Multi-adapter regression |
| Generated snapshot drifts between machines | Stable serialization and sorting | Byte determinism test |

## Taskplane Execution Mapping

Taskplane's own task-creation workflow requires `.pi/taskplane-config.json` or its legacy config before task packets are created

That file is not present in the current Designly `main` branch at plan-authoring time, so this plan intentionally does not commit invalid `PROMPT.md` or `STATUS.md` packets yet

When Taskplane execution is desired, initialize it explicitly from the repository root

```bash
taskplane init --preset full --tasks-root docs/task-management
```

Then convert the implementation into these dependency-aware packets

```text
VC-001 contracts-and-compatibility
  dependencies: none
  maps to: Task 1

VC-002 source-adapter
  dependencies: VC-001
  maps to: Task 2

VC-003 sync-provenance-anti-copy
  dependencies: VC-001, VC-002
  maps to: Task 3

VC-004 deterministic-retrieval
  dependencies: VC-001, VC-003
  maps to: Task 4

VC-005 director-taste-integration
  dependencies: VC-004
  maps to: Task 5

VC-006 execution-qa-boundaries
  dependencies: VC-005
  maps to: Task 6

VC-007 docs-maintenance-attribution
  dependencies: VC-003, VC-006
  maps to: Task 7

VC-008 full-release-verification
  dependencies: VC-004, VC-005, VC-006, VC-007
  maps to: Task 8
```

Recommended Taskplane review levels after initialization

```text
VC-001 L2 Plan + Code
VC-002 L2 Plan + Code
VC-003 L3 Full
VC-004 L2 Plan + Code
VC-005 L3 Full
VC-006 L3 Full
VC-007 L1 Plan
VC-008 L3 Full
```

The highest review levels are assigned to provenance, anti-copy, routing authority, Prompt Compiler boundaries, and release verification because those changes have the broadest behavioral impact

## Parallelization Guidance

Safe after VC-001

```text
VC-002 can begin first
VC-004 must wait for normalized source output from VC-003
VC-005 waits for retrieval contract
VC-007 documentation can partially draft after VC-003 but final content waits for VC-006
```

Preferred execution waves

```text
Wave 1: VC-001
Wave 2: VC-002
Wave 3: VC-003
Wave 4: VC-004
Wave 5: VC-005
Wave 6: VC-006
Wave 7: VC-007
Wave 8: VC-008
```

This looks mostly serial because the feature establishes contracts that later tasks depend on. Do not manufacture parallel work that creates merge conflicts across the same Skills and shared contracts

## Definition of Done

- All acceptance criteria from the design spec are covered by Tasks 1 through 8
- No placeholders or unspecified implementation steps remain
- Every new external-derived record is traceable to a source id and pinned ref
- The package contains no upstream image bytes or full prompt bodies
- Retrieval behavior is deterministic and explainable
- Designly still works when the canon returns no match or is not invoked
- Personal Reference Memory semantics remain unchanged
- Prompt Compiler remains provider-facing and concept-neutral
- Visual QA preserves Designly's existing authority order
- Full regression and packaging checks pass

## Execution Handoff

After this plan is approved for implementation, use one of these routes

1. `superpowers:subagent-driven-development` for fresh-context task execution with review gates
2. `superpowers:executing-plans` for inline execution with checkpoints
3. Taskplane after explicit repository initialization, using the VC-001 through VC-008 dependency map above
