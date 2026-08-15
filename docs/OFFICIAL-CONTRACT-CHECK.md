# Official Plugin Contract Check

Verified: 2026-08-15

Checked against the current OpenAI Plugin packaging and Skill documentation before preparing 3.2.1

Applied constraints:

- `.codex-plugin/plugin.json` is the native manifest entry point
- `skills` points to `./skills/`
- plugin remains skills-only; no MCP or app mapping is invented
- public install metadata uses a supported category
- `displayName`, `shortDescription`, `longDescription`, `developerName`, capabilities, default prompts, brand colors, logo, and composer icon are present
- logo and composer icon are square SVG assets under `./assets/`
- `SKILL.md` frontmatter contains only `name` and `description` for discovery
- `skills/art-director/agents/openai.yaml` owns supported skill interface settings under `interface`
- no `metadata:` block is used in `SKILL.md` to configure the skill interface
- local marketplace catalog is kept separate from public-directory status
- repo marketplace path is `.agents/plugins/marketplace.json`
- marketplace plugin source path is `./plugins/designly`

No claim is made that this package has been submitted to or accepted by the universal public Plugins Directory
