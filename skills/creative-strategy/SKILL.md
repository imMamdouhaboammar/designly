---
name: creative-strategy
description: Marketing strategy and visual concept specialist. This skill should be used when deconstructing marketing briefs, defining target audience insights, establishing message hierarchy, developing distinct concept territories, or clarifying the single primary communication job before visual design begins.
---

# Creative Strategy

Creative Strategy deconstructs commercial marketing briefs into sharp communication objectives, audience insights, message hierarchies, and distinct visual concept territories.

---

## 1. Core Workflow

1. **Brief Deconstruction**:
   - Extract the core business objective (e.g. product launch, brand repositioning, direct conversion).
   - Identify the primary target persona (demographic, psychographic, pain points, motivations).
   - Isolate the single **Primary Communication Job** that must be communicated within 3 seconds.

2. **Message Hierarchy**:
   - **Primary Message**: The single indispensable claim or emotion (occupies 100% of initial viewer glance).
   - **Secondary Message**: Supporting reason-to-believe or value proposition.
   - **Tertiary Elements**: Call to action (CTA), legal disclaimers, or secondary brand proof points.

3. **Concept Territory Development**:
   - For exploratory briefs, define up to 3 genuinely distinct visual territories (e.g. Territory A: Minimalist Precision, Territory B: Organic Authenticity, Territory C: Dynamic Motion).
   - Never generate variations that are merely superficial color swaps.

4. **Output Contract**:
   - Return a valid `DesignSignalPacket` containing `strategy_state`, `primary_message`, and `desired_action` decisions with supporting evidence.

---

## 2. Rules & Hard Constraints

- **Single Core Job**: If a brief demands 5 simultaneous headlines, force a hierarchy: 1 primary, 2 secondary, 2 relegated to caption/metadata.
- **Audience Grounding**: Every visual metaphor must resonate with the target demographic's cultural and commercial context.
- **No Premature Execution**: Strategy does not dictate camera lens millimeter choices or hexadecimal color codes; it defines conceptual intent and hierarchy.

---

## 3. Cross-Skill Neural Connections & References

### Peer & Downstream Skills
- [Insight Mining](../insight-mining/SKILL.md) — Unearthing underlying consumer tensions & JTBD
- [Creative Director](../creative-director/SKILL.md) — Structural ideation (SIT/TRIZ) & Cannes scoring
- [Campaign Canon](../campaign-canon/SKILL.md) — Benchmarking against 571 canonical campaigns
- [Brand Intelligence](../brand-intelligence/SKILL.md) — Aligning strategic territories with brand identity
- [Composition Director](../composition-director/SKILL.md) — Translating message hierarchy into layout structure
- [Designly Director](../designly-director/SKILL.md) — Orchestrator and lock manager

### Schemas & References
- [Signal Packet Schema](../../shared/contracts/signal-packet.schema.json) — Neural Mesh handoff
- [Marketing Brief Guide](../../shared/references/marketing-brief.md) — Brief intake rules
- [Design Principles](../../shared/references/design-principles.md) — Core principles
- [Inclusive Representation](../../shared/references/inclusive-representation-and-ethics.md) — Anti-stereotype audience modeling
