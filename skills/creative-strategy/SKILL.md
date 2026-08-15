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

## 3. References & Schemas

- Shared Contract: [Signal Packet Schema](../../shared/contracts/signal-packet.schema.json)
- Shared Reference: [Marketing Brief Guide](../../shared/references/marketing-brief.md)
- Shared Reference: [Design Principles](../../shared/references/design-principles.md)
