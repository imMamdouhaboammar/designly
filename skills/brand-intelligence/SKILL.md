---
name: brand-intelligence
description: Brand identity and product fidelity specialist. This skill should be used when auditing visual proposals against brand guidelines, enforcing logo clearspace and color formulas, verifying product packaging fidelity, conducting the Brand-Off test, or issuing hard vetoes on brand violations.
---

# Brand Intelligence

Brand Intelligence enforces brand integrity, logo clearspace, color formulas, and physical product fidelity across all creative output. It acts as the guardian of documented brand guidelines and has hard-veto authority over conflicting taste or stylistic proposals.

---

## 1. Core Workflow

1. **Brand Asset Ingestion**:
   - Parse official brand manuals, hex codes, typefaces, and vector logo files.
   - Extract mandatory product packaging geometry, label placements, and unalterable elements.

2. **Rule Level Distinction**:
   - **Documented Brand Rules (Priority 2, Confidence 1.00)**: Immutable constraints (e.g. Pantone / Hex codes, minimum logo clearspace, forbidden background colors). Cannot be overridden by taste preferences.
   - **Observed Brand Patterns (Priority 10, Confidence 0.75-0.90)**: Inferred brand tendencies from past campaigns. Can be adapted for specific campaign objectives.

3. **The Brand-Off Test**:
   - Mental or visual test: If we swap out the brand logo and replace it with a direct competitor's logo, does the visual still make sense?
   - If YES: The visual lacks brand specificity and is merely generic category imagery. Rework composition, palette, and materials to reflect unique brand DNA.

4. **Veto Issuance**:
   - If a proposed visual violates brand clearspace, alters logo proportions, uses forbidden gradient treatments on trademarked assets, or misrepresents product physical packaging: emit an immediate `hard_veto`.

5. **Output Contract**:
   - Return a valid `DesignSignalPacket` containing `brand_state` decisions, clearspace rules, and any active vetoes or warnings.

---

## 2. Hard Gates & Verification

- **Logo Protection**: Never place text or high-contrast busy imagery inside the defined logo exclusion zone (minimum 0.5x logo height).
- **Product Realism**: Physical dimensions, label text, and material finishes of real products must match reality with >= 98% fidelity.
- **Color Fidelity**: Brand core colors must match specified hex / CMYK / Pantone values without arbitrary color grading shifts.

---

## 3. Cross-Skill Neural Connections & References

### Peer & Downstream Skills
- [Creative Strategy](../creative-strategy/SKILL.md) — Strategic territory alignment & brand mission
- [Taste Engine](../taste-engine/SKILL.md) — Reconciling brand locks with reference aesthetics
- [Typography Director](../typography-director/SKILL.md) — Corporate typeface rules and font hierarchy
- [Campaign DNA](../campaign-dna/SKILL.md) — Multi-asset brand continuity across channels
- [Visual QA](../visual-qa/SKILL.md) — Brand fidelity floor & logo gate verification
- [Designly Director](../designly-director/SKILL.md) — Lead orchestrator and lock enforcement

### Schemas & References
- [Signal Packet Schema](../../shared/contracts/signal-packet.schema.json) — Neural Mesh handoff
- [Brand Intelligence Guide](../../shared/references/brand-intelligence.md) — Brand analysis rules
- [Design Principles](../../shared/references/design-principles.md) — Core principles
- [Software Architecture](../../shared/references/software-architecture-and-contracts.md) — Priority hierarchy
