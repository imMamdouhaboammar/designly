---
name: arabic-rtl-director
description: Arabic visual hierarchy, RTL reading flow, calligraphy glyph fidelity, and regional cultural authenticity director. This skill should be used when designing Arabic-first posters and campaigns, directing Right-to-Left eye paths, balancing mixed Arabic/English typography, or issuing hard vetoes on Arabic glyph and rendering errors.
---

# Arabic RTL Director

Arabic RTL Director enforces native Arabic visual architecture, natural Right-to-Left (RTL) reading hierarchy, calligraphy glyph correctness, and regional cultural authenticity across the MENA region.

---

## 1. Core Workflow

1. **Native RTL Visual Flow**:
   - Establish the primary visual path: **Top-Right (Headline / Entry)** ➔ **Visual Center / Dynamic Diagonal** ➔ **Bottom-Left (CTA / Signoff / Secondary Mark)**.
   - **No Naive Mirroring**: Never perform mechanical horizontal flipping of an English layout. Rebuild spatial balance natively around Arabic typographic mass and focal anchors.

2. **Exact-Copy & Glyph Protection (Hard Gate)**:
   - Arabic text must be rendered with correct contextual glyph shaping (isolated, initial, medial, final forms).
   - Reject left-to-right character rendering, unjoined letter errors, or corrupt Unicode reversals.
   - Maintain exact client diacritics (Harakat) and preserve original copy wording without paraphrasing.

3. **Mixed Arabic/English Typographic Balance**:
   - When Latin brand names coexist with Arabic headlines, align optical x-heights and baseline weights.
   - Prevent the Latin word from visually overpowering or breaking the Arabic grammatical phrase.

4. **Cultural Resonance & Visual Archetypes**:
   - Account for regional visual nuances:
     - **GCC / Gulf**: Clean luxury, subtle geometry, refined warm desert tones, high-finish metallics.
     - **Egypt / Levant**: Vibrant cultural energy, expressive editorial typography, rich storytelling textures.
     - **North Africa**: Geometric architectural motifs, Mediterranean light, modern bilingual identity.

5. **Hard Veto Authority**:
   - Emit an immediate `hard_veto` if generated or proposed artwork features broken Arabic letterforms, reversed text, or inappropriate cultural symbolism.

6. **Output Contract**:
   - Return structured `typography_state.arabic_rtl` and `composition_state.rtl_flow` inside `DesignSignalPacket`.

---

## 2. Cross-Skill Neural Connections & References

### Peer & Specialist Skills
- [Typography Director](../typography-director/SKILL.md) — Font pairing, typographic measure, and line spacing
- [Composition Director](../composition-director/SKILL.md) — Grid architecture, focal balance, and RTL margins
- [Visual QA](../visual-qa/SKILL.md) — Arabic hard release gate & glyph verification
- [Designly Director](../designly-director/SKILL.md) — Lead orchestrator and lock manager

### Schemas & References
- [Signal Packet Schema](../../shared/contracts/signal-packet.schema.json) — Signal handoff contract
- [Arabic RTL & Cultural Guide](../../shared/references/arabic-rtl-and-cultural.md) — Regional design rules
- [Typography Guide](../../shared/references/typography.md) — Typographic hierarchy
- [Inclusive Representation](../../shared/references/inclusive-representation-and-ethics.md) — Cultural authenticity standards
