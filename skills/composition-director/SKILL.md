---
name: composition-director
description: Spatial composition, grid layout, hierarchy, and structural preflight director. This skill should be used when establishing layout grids, visual hierarchy, focal anchors, negative space balance, eye paths, or conducting preflight tests to prevent equal-emphasis slop and clutter.
---

# Composition Director

Composition Director establishes the mathematical and perceptual skeleton of the visual before generation or rendering. It governs grid systems, focal hierarchy, eye paths, scale relationships, and negative space balance.

---

## 1. Core Workflow

1. **Format & Canvas Setup**:
   - Establish aspect ratio (e.g. 1:1, 4:5, 9:16, 16:9) and define outer margins and safety padding (minimum 6-8% margin).
   - Select grid system: Rule of Thirds, Golden Ratio, Diagonal Dynamic Grid, or Swiss Modular Grid.

2. **Focal Anchor Architecture**:
   - **Primary Focal Anchor (Single)**: The hero element capturing immediate attention (occupies primary visual weight).
   - **Secondary Anchor**: Supporting narrative element or product context.
   - **Tertiary Elements**: Text blocks, badge, brand mark, and secondary accents.
   - **Strict Rule**: Exactly ONE primary focal point. Reject "equal-emphasis" where 3+ elements compete equally.

3. **Perceptual Preflight Checks**:
   - **The Thumbnail Test**: Scaled down to 100x100px, is the silhouette and hierarchy immediately clear?
   - **The Grayscale Contrast Test**: Stripped of color, do value contrasts maintain readable depth and clear separation?
   - **Negative Space Audit**: Ensure negative space is active and intentional, not trapped dead space.
   - **Accidental Tangencies**: Ensure overlapping elements have decisive overlap or clear separation; eliminate ambiguous touching edges.

4. **Output Contract**:
   - Return structured `composition_state` inside `DesignSignalPacket` containing grid specs, anchor coordinates, and negative space ratios.

---

## 2. Tools & Scripts

- Run design lint on Art Direction spec:
  ```bash
  python3 scripts/design_lint.py assets/art-direction.template.json
  ```
- Run design structural evals:
  ```bash
  python3 scripts/run_design_evals.py
  ```

---

## 3. Schemas & References

- Local Schema: [Art Direction Schema](schemas/art-direction.schema.json)
- Local Schema: [Creative Brief Schema](schemas/creative-brief.schema.json)
- Shared Reference: [Layout, Grid, and Spacing](../../shared/references/layout-grid-and-spacing.md)
- Shared Reference: [Composition and Photography](../../shared/references/composition-and-photography.md)
- Shared Reference: [Design Preflight](../../shared/references/design-preflight.md)
- Shared Reference: [Gestalt and Perception](../../shared/references/gestalt-and-perception.md)
