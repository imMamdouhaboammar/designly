# Designly 3.2

A skills-only ChatGPT/Codex plugin for professional art direction, Taste Engine analysis, persistent Reference Memory, design preflight, image-generation direction, image editing, and visual QA

## Skill interface contract

`skills/art-director/SKILL.md` contains only the Skill identity and runtime instructions. Skill interface settings live in `skills/art-director/agents/openai.yaml` under `interface`. Do not add a `metadata` interface block to `SKILL.md`.

Designly uses one boxed line-art D mark across the plugin logo, composer icon, and Skill icons so the installed surface does not drift between identities.

## What 3.2 includes

- Taste Engine: evidence → observation → transferable rule → constraint
- stable `REF-####` Reference Memory
- job-based reference mixing instead of vague whole-style blending
- explicit originality / similarity guards
- preference feedback ledger that records approvals and corrections without claiming model retraining
- deterministic local memory CRUD and Taste Contract generation
- `agents/openai.yaml` interface configuration for ChatGPT/Codex skill presentation
- current `.codex-plugin/plugin.json` install-surface metadata
- square marketplace assets
- public-plugin validation and deterministic archive packaging
- local repo marketplace bundle
- plugin-wide benchmark scenarios

## Architecture

The plugin remains **skills-only**. It does not need a remote MCP server to perform art direction or store local reference analysis. Local persistence uses a workspace file or a host-provided writable plugin-data path when available. Cross-device/team-synced memory would be a separate future hybrid/MCP feature.

## Taste Engine

References are not reduced to `premium`, `cinematic`, or `minimal`. Each reference becomes a Taste Profile with observable evidence, confidence, transferable rules, anti-rules, retrieval jobs, and a similarity guard.

When multiple references are used, assign each one a design job. Example: REF-0007 for hierarchy, REF-0012 for lighting, REF-0021 for typography. Brand rules and the current brief always override stored taste.

## Reference Memory

```bash
python3 skills/art-director/scripts/reference_memory.py init
python3 skills/art-director/scripts/reference_memory.py add skills/art-director/assets/taste-profile.template.json
python3 skills/art-director/scripts/reference_memory.py list --job hierarchy
python3 skills/art-director/scripts/reference_memory.py search editorial restrained
```

The helper stores structured analysis, not secret image copies.

## Validation

```bash
python3 skills/art-director/scripts/validate_package.py
python3 tools/validate_public_plugin.py .
```

## Deterministic plugin ZIP

```bash
python3 tools/package_plugin.py . /tmp/designly.zip
```

Build twice and compare SHA256 before release.

## Marketplace

A separate marketplace bundle places this plugin at `plugins/designly` and its catalog at `.agents/plugins/marketplace.json`.

With current Codex tooling, a local marketplace root can be added with:

```bash
codex plugin marketplace add /path/to/designly-marketplace
```

Then restart the ChatGPT desktop app and install from that marketplace source.
