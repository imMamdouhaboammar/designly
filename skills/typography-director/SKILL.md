---
name: typography-director
description: Typographic hierarchy, layout, measure, and exact-copy director. This skill should be used when setting typographic scale, headline measure, line breaks, text zones, contrast ratios, and layout boundaries, or protecting exact client copy strings.
---

# Typography Director

Typography Director governs typographic hierarchy, measure, line length, kerning, leading, and text legibility. It establishes dedicated, uncluttered text zones and protects exact user copy from being rewritten, fragmented, or lost against busy backgrounds.

---

## 1. Core Workflow

1. **Hierarchy & Scale Definition**:
   - **Headline**: High visual contrast, tight leading (1.05 - 1.15x), short line length (1-4 words per line).
   - **Subhead**: Supporting scale (0.4 - 0.6x headline size), comfortable leading (1.2 - 1.3x).
   - **Body / Callout**: High legibility, measure of 45-75 characters per line, generous leading (1.4 - 1.6x).
   - **CTA / Microcopy**: Distinct geometry, uppercase or balanced weight, isolated from decorative imagery.

2. **Semantic Line Breaking**:
   - Break lines strictly at natural grammatical and semantic boundaries.
   - Never leave single-word orphans or break hyphenated concepts awkwardly across lines.

3. **Text Zone & Contrast Protection**:
   - Designate clean, low-frequency background zones for text placement.
   - Ensure minimum contrast ratio:
     - Large text (headlines >= 24px): >= 3.0:1 (target >= 4.5:1).
     - Standard body text: >= 4.5:1 (target >= 7.0:1).
   - If the background is complex photographic imagery, specify solid scrims, soft directional vignettes, or clean flat containers behind the text.

4. **Arabic Copy Routing**:
   - If the text contains Arabic script, immediately route layout constraints to [Arabic RTL Director](../arabic-rtl-director/SKILL.md) to ensure proper right-to-left baseline flow and calligraphy rules.

5. **Output Contract**:
   - Return structured `typography_state` inside `DesignSignalPacket` containing font families, scale ratios, text zone coordinates, and exact copy locks.

---

## 2. Cross-Skill Neural Connections & References

### Peer & Downstream Skills
- [Arabic RTL Director](../arabic-rtl-director/SKILL.md) — RTL typography, glyph shaping & calligraphy fidelity
- [Composition Director](../composition-director/SKILL.md) — Grid placement, margins, and spatial hierarchy
- [Brand Intelligence](../brand-intelligence/SKILL.md) — Corporate typeface rules and brand lock alignment
- [Prompt Compiler](../prompt-compiler/SKILL.md) — Text zone protection in image generation instructions
- [Designly Director](../designly-director/SKILL.md) — Orchestrator and exact-copy lock manager

### Schemas & References
- [Signal Packet Schema](../../shared/contracts/signal-packet.schema.json) — Neural Mesh handoff
- [Typography Guide](../../shared/references/typography.md) — Typographic hierarchy and measure
- [Design Principles](../../shared/references/design-principles.md) — Core visual design rules
