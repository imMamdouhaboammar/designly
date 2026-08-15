---
name: campaign-dna
description: Multi-asset campaign visual DNA and cross-format continuity director. This skill should be used when planning multi-asset campaigns, defining visual-family continuity rules across formats (1:1, 9:16, 16:9), creating deliberate variation across deliverables, or maintaining campaign brand consistency.
---

# Campaign DNA

Campaign DNA defines the visual genome for multi-asset commercial campaigns. It establishes unbreakable family resemblance across disparate formats and channels (social, digital OOH, print, performance ads) while introducing deliberate creative variation across individual assets.

---

## 1. Core Workflow

1. **Campaign Genome Definition**:
   - **Primary Palette DNA**: Core 2-3 colors that appear consistently in every asset.
   - **Lighting Signature**: Consistent light direction, contrast ratio, and color temperature across all campaign shots.
   - **Material & Texture DNA**: Common tactile finish (e.g. brushed metal, organic matte paper, high-gloss glass).
   - **Typographic Anchor**: Shared font pairing, tracking rules, and badge placement.

2. **Deliberate Variation Matrix**:
   - Never copy-paste the exact same layout across 5 assets.
   - Vary intentional dimensions while holding the genome locked:
     - Asset 1 (Hero / Brand): Macro product hero shot with dynamic dramatic lighting.
     - Asset 2 (Context / Lifestyle): Environmental wide shot showing product in real use.
     - Asset 3 (Detail / Feature): Close-up crop emphasizing tactile craft and engineering.
     - Asset 4 (Story / Conversion 9:16): Vertical composition with clear CTA zone.

3. **Multi-Format Responsive Adaptation**:
   - **1:1 Square (Feed)**: Centered or Rule-of-Thirds balance with equal margin breathing room.
   - **4:5 Portrait (Instagram Feed)**: Extended vertical hierarchy with upper headline and lower CTA.
   - **9:16 Vertical (Stories / TikTok)**: Top 15% and bottom 20% safe zone clearance for UI overlays.
   - **16:9 Landscape (YouTube / Desktop / DOOH)**: Dynamic horizontal eye path with distinct left/right narrative balance.

4. **Output Contract**:
   - Return structured `campaign_state` and `VisualDNA` JSON inside `DesignSignalPacket`.

---

## 2. References & Schemas

- Local Schema: [Visual DNA Schema](schemas/visual-dna.schema.json)
- Shared Reference: [Campaign Visual DNA](../../shared/references/campaign-visual-dna.md)
- Shared Reference: [Platform and Format Guide](../../shared/references/platform-and-format.md)
