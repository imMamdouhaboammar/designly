# Visual Pattern Canon Design

**Status:** Approved design distilled from the repository analysis and the requested Designly integration

**Date:** 2026-08-29

**Primary source:** `freestylefly/awesome-gpt-image-2`

**Initial upstream snapshot:** `c7d293963b21c60bf338003915438cc5c39dd3ca`

## Problem

Designly already owns the high-value decisions around creative strategy, brand constraints, taste extraction, composition, model physics, prompt compilation, bounded editing, and independent visual QA

What it does not yet have is a dedicated external visual execution corpus that can answer a narrower question before image generation

> Which known visual execution patterns are relevant to this approved creative direction, and which transferable rules are useful without copying the source work

`awesome-gpt-image-2` is useful here because it turns a large GPT Image 2 case collection into structured categories, styles, scenes, industrial templates, guidance, pitfalls, and example case references

The integration must preserve Designly's existing decision hierarchy

External cases are evidence, not authority

Style retrieval must never outrank user locks, brand rules, communication job, hierarchy, composition, accessibility, or cultural requirements

## Goal

Add an internal `Visual Pattern Canon` capability to Designly that can ingest curated external visual corpora, starting with `awesome-gpt-image-2`, normalize them into a Designly-owned contract, retrieve relevant patterns deterministically, hand transferable evidence to Taste Engine and downstream directors, and provide pattern expectations to Visual QA

The result must stay model-agnostic even when an upstream source is model-specific

## Non-goals for v1

- Do not add a new public user-facing Skill only to expose the upstream library
- Do not copy upstream images into the Designly package
- Do not persist full upstream prompts in the normalized canon
- Do not feed raw upstream prompts directly into Prompt Compiler
- Do not treat canon matches as user preferences or save them under `REF-####`
- Do not add embeddings, a vector database, or a hosted retrieval service in v1
- Do not add a runtime network dependency for ordinary Designly use
- Do not auto-update the upstream corpus during package install or normal generation
- Do not let an external pattern override an existing DesignLock
- Do not infer that a user likes a canon case merely because it was retrieved or used

## Core product distinction

Designly keeps two separate reference domains

### Personal Reference Memory

- IDs use `REF-####`
- Represents references supplied, selected, or explicitly approved by the user or project
- Stores scoped likes and dislikes
- Can contribute to persistent Taste Profiles

### Visual Pattern Canon

- IDs use `CANON-<SOURCE>-<ID>`
- Represents external, curated execution evidence
- Never implies user preference
- Carries provenance, source license, transferable rules, anti-rules, and model compatibility
- Is disposable and regenerable from its source adapter

The two domains may be used in one Taste Engine pass, but they must never share identity or preference semantics

## Architecture

```text
Approved Brief and Strategy
        |
        v
Brand and User Locks
        |
        v
Visual Canon Query
        |
        +--> Designly-native patterns
        |
        +--> awesome-gpt-image-2 adapter
        |
        +--> future source adapters
        |
        v
Normalized Pattern Candidates
        |
        v
Deterministic Ranking + Explainability
        |
        v
Taste Engine
  assign one job per useful source
        |
        +--> composition evidence
        +--> typography evidence
        +--> lighting or material evidence
        +--> anti-rules
        |
        v
Composition / Typography / Craft Directors
        |
        v
Image Director
        |
        v
Prompt Compiler
  provider-native instructions only
        |
        v
Generation
        |
        v
Visual QA
  Art Direction Spec + Pattern Expectations
```

## Placement in the repository

The capability stays internal rather than adding another public Skill in v1

```text
shared/
  contracts/
    visual-pattern.schema.json
    visual-canon-query.schema.json
    visual-canon-result.schema.json
  references/
    visual-canon.md
    visual-canon/
      source-registry.json
      generated/
        awesome-gpt-image-2.json
  scripts/
    visual_canon_lib.py
    sync_visual_canon.py
    search_visual_canon.py
    validate_visual_canon.py

evals/
  visual_canon/
    fixtures/
    test_contracts.py
    test_awesome_adapter.py
    test_sync_determinism.py
    test_ranking.py
    test_provenance.py
    test_anti_copy.py
    test_integration.py
```

Existing Skills that receive focused updates

- `skills/designly-director/SKILL.md`
- `skills/taste-engine/SKILL.md`
- `skills/composition-director/SKILL.md`
- `skills/image-director/SKILL.md`
- `skills/prompt-compiler/SKILL.md`
- `skills/visual-qa/SKILL.md`

Existing shared contracts that receive backward-compatible updates

- `shared/contracts/design-context.schema.json`

## Canon source contract

Each source entry records enough information to reproduce and audit a sync

```json
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
```

A sync must record the actual source ref used and must not silently replace a pinned snapshot

Updating the pin is an explicit repository change with regenerated output and tests

## Normalized VisualPattern contract

The normalized contract belongs to Designly, not the upstream repository

Minimum shape

```json
{
  "pattern_id": "CANON-AGI2-poster-layout-system",
  "source": {
    "source_id": "awesome-gpt-image-2",
    "source_ref": "c7d293963b21c60bf338003915438cc5c39dd3ca",
    "source_record_id": "poster-layout-system",
    "license": "MIT"
  },
  "task_family": "poster",
  "communication_jobs": ["event-awareness", "campaign-key-visual"],
  "styles": ["poster"],
  "scenes": ["commerce", "social"],
  "tags": ["poster", "typography", "campaign"],
  "use_when": [],
  "transferable_rules": [],
  "anti_rules": [],
  "example_case_ids": [345, 5, 10],
  "compatible_models": ["gpt-image-2"],
  "provenance_confidence": 1.0
}
```

The normalized record may contain compact descriptive metadata and rule summaries derived from the source's structured guidance

It must not contain image bytes or a full prompt body copied from the source

## Query contract

The Director builds a query only after strategy and locks are stable enough to make visual retrieval useful

```json
{
  "task_family": "poster",
  "communication_job": "conference-awareness",
  "style_preferences": ["premium", "editorial"],
  "scene": "event",
  "model_target": "gpt-image-2",
  "constraints": {
    "minimal": true,
    "rtl": true,
    "exact_copy": true
  },
  "top_k": 3
}
```

The query does not include private reference images or raw brand documents

It works against the local normalized canon only

## v1 retrieval scoring

Use a deterministic weighted score before considering semantic retrieval

```text
Task family            0.30
Communication job      0.20
Scene                   0.15
Style                   0.15
Composition intent      0.10
Model compatibility     0.10
```

Rules

- Exact structured matches score higher than inferred aliases
- Every returned match includes the score breakdown
- Stable input plus stable canon must produce stable ordering
- Ties use canonical `pattern_id` ordering
- No hidden model call is required for ranking
- `top_k` defaults to 3 and is capped at 5

## Result contract

Visual Canon returns evidence, not a generation prompt

```json
{
  "query_id": "VCQ-1021",
  "selected_patterns": [
    {
      "pattern_id": "CANON-AGI2-poster-layout-system",
      "score": 0.88,
      "score_breakdown": {},
      "assigned_job": null,
      "transferable_rules": [
        "single dominant hero",
        "clear headline hierarchy",
        "restrained supporting copy"
      ],
      "anti_rules": [
        "avoid collage density",
        "avoid decorative symbols"
      ],
      "source": {}
    }
  ]
}
```

`assigned_job` remains null until Taste Engine chooses whether and how to use the pattern

## Taste Engine integration

Taste Engine remains the interpretation boundary

Canon retrieval may nominate multiple candidates, but Taste Engine decides the job assigned to each useful source

Examples

```text
CANON-AGI2-345 -> composition
CANON-AGI2-355 -> typography
REF-1042       -> lighting
Brand rules    -> palette and logo behavior
```

The existing job-based reference mixing rule remains mandatory

A canon case cannot contribute subject identity, character identity, proprietary marks, exact copy, or a distinctive source-specific finished composition

## Anti-copy gate

Transfer is allowed for

- hierarchy principles
- layout archetypes described at a general level
- spacing and density guidance
- lighting relationships
- material behavior
- camera relationships
- information flow
- constraints and failure modes

Transfer is blocked for

- source subject identity
- named or recognizable character identity unless separately licensed and requested
- source logos or trademarks
- exact textual copy
- full prompt bodies
- distinctive source-specific compositions represented as exact coordinates
- direct image assets

The validator must fail generated canon records that contain forbidden source fields configured by the adapter

## DesignContext integration

Add an optional `visual_canon_state` object to `DesignContext`

It stays optional in v1 so current fixtures and workflows remain valid

Suggested content

```json
{
  "query": {},
  "selected_patterns": [],
  "assigned_jobs": [],
  "pattern_expectations": []
}
```

The state is session-scoped and must not be copied into personal Reference Memory

## Director routing

The Director triggers canon retrieval only when visual execution references can materially reduce uncertainty

Likely triggers

- new campaign key visual
- poster or editorial visual
- product advertising visual
- infographic or structured explainer
- photography direction where a known execution family is relevant
- image generation with broad style language and weak structural specificity

Likely skips

- exact local image edit
- logo correction with strict source geometry
- pure strategy request
- copy-only request
- a task where the user already supplied sufficient exact references and asked for faithful bounded execution

Retrieval occurs after strategy, user locks, and brand constraints, never before them

## Prompt Compiler boundary

Prompt Compiler receives only approved Art Direction state and provider-specific requirements

It must never compile an upstream raw prompt as authoritative source material

A test must prove that source-specific prompt fields are rejected or ignored at the compiler boundary

This keeps the same Art Direction Spec portable across GPT Image 2, Gemini Nano Banana, MiniMax Design, Kimi Design, Claude Design, and future adapters

## Visual QA integration

Useful selected patterns may emit `pattern_expectations`

Example

```json
{
  "pattern_id": "CANON-AGI2-poster-layout-system",
  "expectations": {
    "subject_dominance": "high",
    "text_density": "low",
    "negative_space": "high"
  }
}
```

Visual QA compares the generated result against

1. immutable user and brand locks
2. approved Art Direction Spec
3. relevant pattern expectations

Pattern expectations are advisory unless the Art Direction Spec explicitly promoted one into a higher-priority decision

A pattern mismatch alone must not override a valid creative decision

## Source sync and reproducibility

The local package must work with no network access

Therefore v1 uses committed normalized snapshots

Sync is a maintainer operation

```text
source registry
     |
     v
fetch pinned artifact
     |
     v
adapter parse
     |
     v
normalize
     |
     v
validate provenance and anti-copy rules
     |
     v
deterministic JSON output
     |
     v
commit generated snapshot
```

The sync command must support an offline fixture mode for tests

CI must not depend on GitHub availability to validate the committed canon

A separate optional freshness check may report that the upstream main branch moved beyond the pin, but it must not rewrite the corpus automatically

## Failure modes

### Upstream schema changes

Fail sync with an actionable adapter error that names the missing or changed field

Never generate a partial snapshot silently

### Missing source artifact

Fail before replacing the existing generated canon

### Invalid license metadata

Fail validation

### Duplicate normalized IDs

Fail validation

### Retrieval finds no useful match

Return an empty result with a reason and let Designly continue without canon evidence

Do not force a weak pattern into the workflow

### User or brand lock conflicts with a pattern

The lock wins and the conflict is recorded as a veto or ignored recommendation

### Source record contains prompt-like text beyond allowed metadata

Drop the field and fail the anti-copy test if it appears in normalized output

## Verification strategy

The implementation must use TDD and preserve existing Designly behavior

Required test groups

- JSON Schema contract tests
- source adapter fixture tests
- deterministic sync snapshot test
- provenance and attribution tests
- forbidden-field and anti-copy tests
- stable ranking tests with score breakdowns
- no-match behavior
- optional `visual_canon_state` backward compatibility
- Director trigger and skip scenarios
- Taste Engine job assignment boundary
- Prompt Compiler raw-source rejection
- Visual QA advisory expectation behavior
- full `evals/run_mesh_evals.py` regression pass
- existing adapter, supply-chain, and public-plugin validation suites

## Acceptance criteria

The v1 feature is complete when all conditions below are true

- Designly can regenerate a compact normalized canon from the pinned `awesome-gpt-image-2` source artifact
- The generated canon records provenance and license metadata for every record
- The generated canon contains no image bytes and no full upstream prompts
- Retrieval returns stable top-k results with explainable scoring
- Empty or weak retrieval does not block the existing workflow
- Taste Engine can assign separate jobs to canon patterns and user references without mixing preference semantics
- `DesignContext` remains backward compatible when `visual_canon_state` is absent
- Prompt Compiler never treats upstream prompt text as executable authority
- Visual QA can consume advisory pattern expectations without allowing them to outrank DesignLocks
- Existing Designly evals continue to pass
- Documentation clearly credits `freestylefly/awesome-gpt-image-2` and its MIT license

## Future extensions excluded from this plan

Once v1 has stable evidence and usage data, later plans may consider

- semantic retrieval or embeddings
- multi-source canon federation
- Designly-native manually curated patterns
- visual similarity retrieval from user-approved image references
- user feedback weighting without contaminating Personal Reference Memory
- scheduled upstream freshness checks
- model-specific effectiveness statistics
- a visual browser or gallery for canon exploration

These are intentionally not prerequisites for v1
