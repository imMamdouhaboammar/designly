# Plugin Eval Report

Target: Designly 3.2.1

Evaluation mode: static local plugin audit following the Plugin Eval `evaluate-plugin` workflow

The `plugin-eval` CLI is not installed in this runtime, so this report does not claim measured harness token usage or a live Codex benchmark score

## At a Glance

- Classification: skills-only ChatGPT/Codex plugin
- Public plugin structure: PASS
- Skill package validation: PASS
- Trigger/routing evals: 21/21 PASS
- Design-preflight evals: 7/7 PASS
- Release-gate regressions: 15/15 PASS
- Prompt-lint regressions: 4/4 PASS
- Taste Engine lint: PASS
- Reference Memory CRUD: PASS
- Taste Mix routing/conflict guard: PASS
- Taste lint regression: PASS
- Marketplace metadata: PASS
- Core SKILL.md: 410 lines, 2253 words, 17358 bytes
- Reference corpus: 10720 words loaded on demand
- Plugin files before packaging: 85

## Why It Matters

The plugin keeps one user-facing Art Director entry point while moving specialized visual craft, Taste Engine, and Reference Memory detail into on-demand references. This reduces routing competition and keeps saved reference logic subordinate to the current brief, brand rules, exact copy, accessibility, and product truth

The memory layer is deterministic local storage rather than a claim of hidden model learning. Reference mixing is job-based, so hierarchy can come from one REF and lighting from another without averaging entire references into generic visual mush

## Strongest Areas

1. Design quality gates run before and after image execution
2. AI-slop detection is behavior-based rather than a keyword blacklist
3. Taste extraction requires evidence and confidence before a rule can become reusable
4. Similarity guards separate transferable design logic from source-specific content and trade dress
5. Reference Memory supports stable IDs, search, feedback, promotion, deletion, and export
6. Public manifest uses the current Codex plugin shape, square assets, supported Creativity category, and concise install-surface copy
7. Local marketplace layout follows the current `.agents/plugins/marketplace.json` convention

## Fix First

1. Run a live `plugin-eval benchmark` in an environment where the Plugin Eval CLI and Codex/ChatGPT plugin surfaces are installed. Static checks cannot measure actual skill-selection latency or tool-context cost
2. Add stable website, privacy, terms, and support URLs before a serious public-directory submission if those pages exist. They are not invented in this package
3. Capture real plugin screenshots after installing the local marketplace build if screenshots are desired for public listing
4. If cross-device or team-shared Reference Memory becomes a requirement, add a deliberately scoped MCP-backed memory service rather than pretending local JSON is synchronized

## Recommended Next Step

Install the marketplace bundle locally, run the seven benchmark scenarios in `evals/plugin-benchmark.json`, then run Plugin Eval's measured benchmark flow on the installed plugin. Compare any failures against the static gates before changing the core Skill
