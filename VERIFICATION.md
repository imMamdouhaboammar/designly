# Verification 3.2.1

Verified locally on 2026-08-15

## Architecture

- skills-only ChatGPT/Codex plugin
- one user-facing `art-director` Skill
- no MCP server
- no hooks
- local-first Reference Memory
- Taste Engine with job-based reference mixing

## Automated evidence

- 21/21 routing evals passed
- 7/7 design-preflight evals passed
- 15/15 release-gate regression tests passed
- 4/4 prompt-lint regression tests passed
- Taste Profile lint passed
- Reference Memory CRUD test passed
- Taste Mix routing/conflict test passed
- Taste lint regression passed
- public plugin manifest/assets validation passed
- marketplace catalog/source-path validation passed

## Public package checks

- `.codex-plugin/plugin.json` exists at plugin root
- strict semver 3.2.1
- author name present
- skills path resolves to `./skills/`
- public category is `Creativity`
- display, short, long, and developer copy are within local public-validator limits
- default prompts are one-line and <=128 characters
- square SVG logo and composer icon are present
- no secret-shaped files are bundled
- no MCP or hidden remote service is declared

## Unavailable live checks

- Codex CLI is not installed in this runtime
- Plugin Eval CLI is not installed in this runtime
- ChatGPT desktop local-marketplace install could not be smoke-tested here
- universal public Plugins Directory submission was not attempted

These unavailable checks are not represented as passes

## Skill interface contract

- `SKILL.md` frontmatter contains only `name` and `description`
- Skill UI fields are configured under `interface` in `skills/art-director/agents/openai.yaml`
- Boxed line-art Designly mark is shared across plugin and Skill icon assets
- transient Python bytecode is excluded from release artifacts
