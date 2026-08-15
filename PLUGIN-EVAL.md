# Plugin Eval Report

Target: Designly 4.1.0

Evaluation mode: static plugin-wide audit plus repository CI evidence, following the Plugin Eval `evaluate-plugin` workflow

The `plugin-eval` CLI is not available in this execution environment, so this report does not claim measured token usage, live Skill-selection latency, or a measured ChatGPT/Codex benchmark score

## At a Glance

- Architecture: skills-only public plugin package
- Discoverable Skills: 14
- Codex custom agent configs: 9
- Primary orchestrator: `designly-director`
- Typed mesh contracts: DesignContext, DesignSignalPacket, DesignLock, RevisionRequest, EditContract, routing graph
- Taste Engine: present
- Reference Memory: local-first
- Arabic RTL review: present
- Edit Sanitizer: present and mandatory for bounded existing-image edits
- Independent Visual QA: present
- GitHub Actions quality gate: present
- Public plugin preflight: included in CI
- Deterministic package A/B byte comparison: included in CI

## What v4.1 fixes

The main hardening target was annotation-guided editing and inpainting

Previously, preservation behavior was expressed mainly through instructions and post-output QA. v4.1 adds an explicit pre-execution boundary

`raw feedback -> edit-sanitizer -> ready EditContract -> prompt-compiler -> image editor -> visual-qa`

A ready EditContract contains an approved source checkpoint, normalized target geometry, one bounded mutation for local edits, exact copy where applicable, protected regions, locks, acceptance checks, and execution verdict

Raw user notes and unknown caller fields are deliberately not passed through the sanitized executable contract

## Strong areas

1. Skill boundaries are narrower than the old monolith and independently discoverable
2. Codex specialists are bounded; only the Director owns state mutation
3. Signal priority prevents inferred taste from overwriting user or documented brand locks
4. Taste extraction separates evidence, observations, transferable rules, and source-specific content
5. Reference Memory is deterministic local metadata rather than a claim of hidden training
6. Visual QA uses category floors plus hard gates so a high average cannot conceal a broken core dimension
7. Anti-slop review tests structural and decorative failure patterns rather than relying only on banned words
8. Bounded edit retries restart from the approved source checkpoint to reduce cumulative drift
9. Annotation geometry is normalized and checked for ambiguity, zero area, bounds, and target confidence
10. CI validates contracts, 14 Skill interfaces, 9 agents, routing, sanitizer behavior, revision routing, adversarial mesh cases, prompt lint, visual gates, public-plugin preflight, and deterministic packaging

## Strict limitations

1. Static/CI evaluation does not prove that every image model will honor a local edit perfectly. The sanitizer reduces bad instructions and drift risk; it does not create deterministic pixel guarantees in a generative editor
2. Actual target/collateral quality still requires inspection of the generated image
3. `plugin-eval` measured benchmark has not been run in this environment
4. Public Plugin Directory approval has not been verified and is not claimed
5. Reference Memory is not cross-device or team synchronized
6. There is currently no explicit repository license file
7. Stable public website/privacy/terms/support URLs are not fabricated when real maintained pages are unavailable

## Benchmark suite

`evals/plugin-benchmark.json` now covers

- Skill discovery
- orchestrator routing
- parallel specialist delegation
- signal conflict resolution
- targeted revision routing
- Reference Memory feedback scoping
- Arabic/exact-copy gates
- anti-slop/category-floor behavior
- annotation/inpainting sanitization
- source-checkpoint drift prevention
- graceful sequential fallback

## Recommended measured follow-up

In an environment with the Plugin Eval CLI and installed ChatGPT/Codex plugin surfaces, run the benchmark suite and measure

- selected Skill
- specialists invoked
- unnecessary specialist rate
- packet validity
- wrong-node revision rate
- lock violations
- sanitizer false positive/false negative rate
- final hard-gate pass
- token usage and latency where measurable

Do not weaken deterministic gates to improve a benchmark score. Treat measured failures as evidence for the next scoped change
