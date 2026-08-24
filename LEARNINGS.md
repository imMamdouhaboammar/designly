# Designly - Project Learnings & Architecture Invariants

## Milestone: v5.0.2 Hardening & Multi-Channel Deployment

### 1. Test Suite Architecture & Discovery
- **Pytest Signature Invariant**: In Pytest, functions named `test_*` treat positional arguments without default values as fixtures. All test utility functions exposed as tests must define parameter defaults (e.g. `errors: list[str] | None = None`).
- **Discovery Boundary**: Never invoke `raise SystemExit(main())` at module top-level. Always gate inside `if __name__ == "__main__":` to allow test runners (pytest, custom eval scripts) to import functions cleanly.
- **Assertion Discipline**: All test assertions must use native `assert condition, message` without returning integers to avoid `PytestReturnNotNoneWarning`.
- **Master Eval Runner**: `evals/run_mesh_evals.py` acts as the canonical orchestrator, sequentially verifying neural mesh conflicts, model adapters, skills.sh manifest, Homebrew Ruby syntax, supply chain security, and skill unit tests.

### 2. Multi-Channel Distribution & Packaging
- **npm / Bun Granular Whitelisting**: `package.json` `"files"` takes absolute precedence over `.npmignore`. Never whitelist root directories containing historical archives (`dist/*.zip`, `dist/*.tar.gz`), as this bloats npm packages by 30+ MB. Explicitly declare runtime deliverables (`dist/index.js`, `dist/skills-sh`).
- **Release Checksum Synchronization**: `tools/homebrew_installer.py` and `tools/package_plugin.py` must compute SHA256 checksums on clean distribution tarballs (`designly-X.Y.Z.tar.gz`) matching GitHub Release artifacts.
- **GitHub Release Automation**: Uses GitHub CLI (`gh release create`) attaching both ZIP and TAR.GZ archives alongside `SHA256SUMS`.

### 3. Model Adapters & Runtime Resilience
- **Subprocess Promise Invariant**: In TypeScript/Bun wrappers (`compilePrompt` in `src/index.ts`), `child_process.spawn()` must always register `child.on("error", reject)` to prevent hanging on missing binaries or spawn failures.
- **Defensive Schema Ingestion**: Adapters (`kimi_design.py`, `claude_design.py`, etc.) must use nested `.get()` lookups with fallbacks to remain resilient against partial or non-standard token/typography specs.
