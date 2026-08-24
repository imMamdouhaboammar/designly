# Designly Master Installation, Package Ecosystem & Adapters Guide

Designly is a modular commercial Art Direction and Design Neural Mesh plugin. It can be installed as a full package or as individual specialized skills across **skills.sh (Vercel)**, **Homebrew (macOS/Linux)**, **npm / Bun**, **OpenAI Codex / ChatGPT**, **Claude Code**, **Cursor**, **Antigravity / Gemini CLI**, or used programmatically via the **Python / TypeScript Adapter Engine**.

---

## 1. Quick Installation Ecosystems

### A. via skills.sh (Vercel)
Install the complete 21-skill neural mesh into your active project or agent harness:

```bash
# Full skill pack
npx skills add imMamdouhaboammar/designly

# Individual specialized skills
npx skills add imMamdouhaboammar/designly --skill image-director
npx skills add imMamdouhaboammar/designly --skill video-director
npx skills add imMamdouhaboammar/designly --skill prompt-compiler
npx skills add imMamdouhaboammar/designly --skill creative-director
npx skills add imMamdouhaboammar/designly --skill arabic-rtl-director
```

### B. via Homebrew (macOS / Linux)
Install the certified Homebrew formula:

```bash
brew tap imMamdouhaboammar/designly
brew install designly
```

### C. via npm / Bun (Clean Supply Chain)
Install the global CLI binary or run on-demand:

```bash
# Global install via Bun or npm
bun add -g designly
# or
npm install -g designly

# On-demand execution with npx
npx designly compile --model gemini-nano-banana --input spec.json
npx designly list-models
npx designly skills list
```

---

## 2. Platform-Specific Agent Setup

### A. Claude Code / OpenCode / Cursor
Clone or copy skills directly to your agent's configuration directory:

```bash
# Project-level skills
git clone https://github.com/imMamdouhaboammar/designly.git .agents/skills/designly

# Or global user-level skills
git clone https://github.com/imMamdouhaboammar/designly.git ~/.claude/skills/designly
```

### B. OpenAI Codex & ChatGPT Plugins
Designly contains a certified `.codex-plugin/plugin.json` manifest:

```bash
git clone https://github.com/imMamdouhaboammar/designly.git
cd designly
python3 -m pip install pyyaml jsonschema
python3 tools/validate_public_plugin.py
```

### C. Antigravity / Gemini CLI / Agent Kernel
Copy skills directly to your local skills directory:

```bash
cp -r skills/* ~/.gemini/config/skills/
```

---

## 3. Supported Model Adapters & Setup

Designly features 8 typed model adapters with calibrated physics, syntax, and parameter constraints:

| Model Adapter | Provider | Category | Best For |
|---|---|---|---|
| `gemini-nano-banana` | Google DeepMind | Image | Descriptive realism, real-world grounding, 1:8 to 8:1 ratios, spatial JSON |
| `minimax-design` | MiniMax / Hailuo | Image & Video | Cinematic lighting, volumetric atmosphere, camera vectors (`pan`, `dolly`) |
| `kimi-design` | Moonshot AI | UI & Design | Coordinate zoning (`[Top-Bar]`, `[Hero]`), design tokens, copy locks |
| `claude-design` | Anthropic | UI & Artifacts | Anti-slop finish gate, Tailwind tokens, precision SVG vector `<viewBox>` |
| `seedance` | ByteDance | AI Video | 30s multi-shot continuity, 50-slot reference kit, `{ dialogue }` lip-sync |
| `kling` | Kuaishou | AI Video | Multi-character `[Character: ]` binding, Motion Brush, negative prompt |
| `gpt-image-2` | OpenAI | Image | 5-slot template (`Scene/Subject/Details`), two-column edit preservation |
| `veo` | Google DeepMind | AI Video | Native JSON schema prompts, audio cues, commercial polish |

---

## 4. Environment Variables & API Credentials

To execute compiled prompts directly via provider APIs or CLI tools, configure your environment variables:

```bash
# Google Gemini / Nano Banana
export GEMINI_API_KEY="your-gemini-api-key"

# MiniMax / Hailuo AI
export MINIMAX_API_KEY="your-minimax-api-key"
export MINIMAX_GROUP_ID="your-minimax-group-id"

# Moonshot AI (Kimi)
export MOONSHOT_API_KEY="your-moonshot-api-key"

# Anthropic Claude
export ANTHROPIC_API_KEY="your-anthropic-api-key"

# ByteDance / Doubao / Seedance
export VOLCENGINE_ACCESS_KEY="your-volcengine-access-key"
export VOLCENGINE_SECRET_KEY="your-volcengine-secret-key"

# Kuaishou Kling AI
export KLING_API_KEY="your-kling-api-key"
export KLING_SECRET_KEY="your-kling-secret-key"

# OpenAI
export OPENAI_API_KEY="your-openai-api-key"
```

---

## 5. CLI & Programmatic Usage Examples

### CLI Execution
```bash
# 1. List registered adapters
designly list-models

# 2. Compile for Gemini Nano Banana
designly compile -m gemini-nano-banana -i '{"subject": "Titanium flacon", "aspect_ratio": "16:9", "copy": "EUPHORIA"}'

# 3. Compile for Kling 3.0 Pro
designly compile -m kling -i '{"characters": ["Pilot A"], "subject": "Starship bridge", "speaker": "Pilot A", "dialogue": "Engage warp drive!"}'

# 4. Inspect skills
designly skills list
designly skills show image-director
```

### TypeScript / Node / Bun Library Usage
```typescript
import { compilePrompt, getSkills, SUPPORTED_ADAPTERS } from "designly";

const prompt = await compilePrompt({
  model: "gemini-nano-banana",
  spec: {
    subject: "Minimalist luxury fragrance bottle on wet black obsidian rock",
    lighting: "Sharp rim lighting with subtle warm fill",
    aspect_ratio: "16:9",
    copy: "EUPHORIA"
  }
});

console.log(prompt);
```

---

## 6. Supply Chain Security & Quality Gates

Designly enforces strict supply chain security standards conforming to `test-guard` rules and `api-security-best-practices`:
- **Zero Insecure Dependencies**: Pure, zero-bloat runtime.
- **Strict File Whitelisting**: Only production binaries and verified skill folders are distributed.
- **Clean `.npmignore`**: Prevents accidental leakage of `.env`, credentials, or internal test files.
- **Input Sanitization**: All CLI arguments and subprocess calls avoid shell injection vulnerabilities.

Run all tests:
```bash
# Bun test suite
bun test

# Supply chain & Homebrew verification
python3 evals/supply_chain/test_supply_chain.py
python3 evals/homebrew/test_homebrew.py

# Complete Neural Mesh evals
python3 evals/run_mesh_evals.py
```
