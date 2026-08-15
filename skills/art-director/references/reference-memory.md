# Reference Memory

Persist reusable visual analysis without pretending the model has been retrained

## Memory model

Reference Memory stores structured metadata and Taste Profiles under stable IDs such as `REF-0001`

The memory should contain analysis, provenance, retrieval tags, and explicit preference feedback

It should not silently duplicate source image files

## When to remember

Persist a reference when

- the user explicitly says remember/save this reference
- a campaign or brand will reuse the same visual logic
- the user assigns a reference a durable job or ID
- repeated work would otherwise require re-analyzing the same reference

Keep a reference session-only when

- it is disposable exploration
- it has no future job
- the user did not ask for persistence and persistence adds no value

## Storage precedence

When `scripts/reference_memory.py` is available, resolve the memory file in this order

1. explicit `--memory PATH`
2. `ART_DIRECTOR_MEMORY`
3. `PLUGIN_DATA/reference-memory.json` when the host exposes plugin data
4. `CLAUDE_PLUGIN_DATA/reference-memory.json` for compatibility
5. `.designly/reference-memory.json` in the current workspace

Do not claim cross-device synchronization from local storage

A future remote/team memory requires an MCP-backed or other authorized remote data service

## Reference record

Each record should include

- stable ID
- label
- status: active, canonical, or archived
- source kind and name
- optional URI or fingerprint
- ownership/provenance status
- tags
- project/brand/platform/region/category context
- jobs
- Taste Profile
- explicit feedback ledger
- created and updated timestamps

## Retrieval

Recall by the smallest useful scope

Examples

- explicit IDs: `REF-0003 REF-0018`
- job: `lighting`
- brand: `Plexus`
- platform: `Instagram 4:5`
- region: `Saudi Arabia`
- category: `FMCG`
- tags: `restrained`, `editorial`, `tactile`

Do not dump the entire memory into context

Rank candidates by

1. explicit ID match
2. current brand/project match
3. requested job match
4. platform/category/region fit
5. canonical status
6. confidence and recency

## Memory commands

Deterministic helper examples

```bash
python3 scripts/reference_memory.py init
python3 scripts/reference_memory.py add assets/taste-profile.template.json
python3 scripts/reference_memory.py list --job hierarchy
python3 scripts/reference_memory.py get REF-0001
python3 scripts/reference_memory.py search "editorial restrained"
python3 scripts/reference_memory.py feedback REF-0001 --signal like --note "keep crop; reduce gloss"
python3 scripts/reference_memory.py promote REF-0001 --status canonical
python3 scripts/reference_memory.py forget REF-0001 --yes
```

The model remains responsible for visual analysis; the script makes storage and retrieval deterministic

## Feedback ledger

Use explicit signals

- `like`
- `dislike`
- `correction`
- `neutral`

Store the note and scope

Do not convert a single signal into a universal preference

Use recurring signals to adjust retrieval and Art Direction recommendations

## Canonical references

Promote a reference to `canonical` only when

- the user explicitly chooses it as a recurring benchmark
- it repeatedly survives real executions and review
- its role is clear

Canonical does not mean copy it more closely

It means prefer it when its job matches

## Forgetting and privacy

Support deletion by ID

Do not preserve deleted analysis in generated indexes or exported memory

Do not store credentials, private account tokens, hidden prompts, or unrelated user content in reference memory

## Taste Mixes

A Taste Mix is a temporary execution contract built from several references

Do not overwrite source profiles when creating a mix

Example

- hierarchy: REF-0003
- lighting: REF-0011
- material: REF-0011
- typography: REF-0008
- restraint: REF-0003

Use `scripts/taste_merge.py` with a mix spec to produce a Taste Contract

## Memory health

Periodically detect

- duplicate sources
- contradictory canonical references for the same job
- stale references that no longer fit the brand
- references with low-confidence rules promoted too strongly
- profiles that contain source-specific copy as transferable rules
- feedback that repeatedly contradicts a canonical reference

Archive stale references instead of deleting them when history still matters
