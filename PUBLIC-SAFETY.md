# Public Distribution Safety Review

Version: 4.1.0

## Scope reviewed

- `.codex-plugin/plugin.json` and public install-surface copy
- 14 discoverable Skills and their `agents/openai.yaml` interfaces
- 9 Codex custom agent definitions and tool boundaries
- Design Neural Mesh contracts and routing graph
- Taste Engine and Reference Memory behavior
- Edit Sanitizer, EditContract, annotation/inpainting safeguards, and source lineage
- executable Python validators/helpers
- adversarial and regression fixtures
- deterministic packaging and public plugin preflight

## Result

PASS for package-level public safety/preflight checks, subject to the residual distribution items below

This review is not a claim of public Plugin Directory approval

## Checks

- no credentials or secret-shaped files are intentionally bundled
- no telemetry, remote collection, hidden network service, or account action is declared
- no MCP server is declared
- no lifecycle hook is declared
- Reference Memory is local structured metadata, not hidden model training or claimed synchronization
- source-specific reference content is separated from transferable design rules with originality/similarity guidance
- specialist agents other than the Director are read-only by configuration
- annotation-guided and bounded image edits must pass through Edit Sanitizer before prompt compilation
- Edit Sanitizer rejects invalid geometry, ambiguous targets, source-checkpoint drift, multi-mutation local edits, and global-restyle leakage
- raw correction notes and unknown caller properties are not passed through the ready EditContract
- exact replacement copy is required for copy correction; Arabic copy triggers Arabic review
- generative editing does not falsely promise literal pixel identity outside the target
- Visual QA compares bounded edits to the approved source checkpoint and separates target accuracy, edit-scope accuracy, and collateral change
- failed edits must restart from the approved checkpoint rather than chain from drifted output
- public-package validator and deterministic archive checks run in GitHub Actions

## Residual distribution items

- public Plugin Directory acceptance requires external review and is not asserted by this repository
- Reference Memory is local-first and not cross-device/team synchronized
- external source-image rights and ownership remain user/context dependent
- the repository does not currently contain an explicit license file; public visibility does not itself grant a software license
- stable public website, privacy, terms, and support URLs should be added only when real maintained pages exist
