# Routing, State & Orchestration Architecture

This reference defines the multi-tier Orchestration Graph, role-aware execution pipelines, recursive feedback loops, and verification gates of the Designly Art Direction Neural Mesh.

---

## 1. Multi-Tier Architecture

The Neural Mesh organizes 19 specialist Skills into 6 distinct cognitive layers:

```text
+-------------------------------------------------------------------------------+
| Tier 1: Strategy & Ideation                                                  |
| [creative-strategy] [insight-mining] [creative-director]                     |
| [campaign-canon]    [brand-activation]                                        |
+-------------------------------------------------------------------------------+
                                      |
                                      v
+-------------------------------------------------------------------------------+
| Tier 2: Visual Architecture & Representation                                 |
| [visual-storytelling] [composition-director] [typography-director]           |
| [arabic-rtl-director] (Inclusive Representation & Anti-Bias Standards)       |
+-------------------------------------------------------------------------------+
                                      |
                                      v
+-------------------------------------------------------------------------------+
| Tier 3: Brand Identity & Taste Intelligence                                  |
| [brand-intelligence] [taste-engine] [reference-memory]                       |
+-------------------------------------------------------------------------------+
                                      |
                                      v
+-------------------------------------------------------------------------------+
| Tier 4: Craft Physics & Optics                                               |
| [photography-director] [manipulation-director] [campaign-dna]                |
+-------------------------------------------------------------------------------+
                                      |
                                      v
+-------------------------------------------------------------------------------+
| Tier 5: Sanitization & Model Compilation                                     |
| [edit-sanitizer] [prompt-compiler]                                           |
+-------------------------------------------------------------------------------+
                                      |
                                      v
+-------------------------------------------------------------------------------+
| Tier 6: Verification & QA Release Gates                                      |
| [visual-qa]                                                                   |
+-------------------------------------------------------------------------------+
```

---

## 2. Role-Aware Execution Pipelines

Depending on the classified task, the orchestrator invokes a specialized sequence:

### A. New Commercial Campaign (`new_commercial_campaign`)
`designly-director` $\rightarrow$ `creative-strategy` $\rightarrow$ `insight-mining` $\rightarrow$ `creative-director` $\rightarrow$ `campaign-canon` $\rightarrow$ `brand-intelligence` $\rightarrow$ `taste-engine` $\rightarrow$ `composition-director` $\rightarrow$ `typography-director` $\rightarrow$ `photography-director` $\rightarrow$ `prompt-compiler` $\rightarrow$ `visual-qa`

### B. Brand Activation / PR Stunt (`brand_activation_stunt`)
`designly-director` $\rightarrow$ `insight-mining` $\rightarrow$ `brand-activation` $\rightarrow$ `campaign-canon` $\rightarrow$ `brand-intelligence` $\rightarrow$ `manipulation-director` $\rightarrow$ `prompt-compiler` $\rightarrow$ `visual-qa`

### C. Arabic-First Poster / MENA Campaign (`arabic_first_poster`)
`designly-director` $\rightarrow$ `creative-strategy` $\rightarrow$ `insight-mining` $\rightarrow$ `creative-director` $\rightarrow$ `brand-intelligence` $\rightarrow$ `composition-director` $\rightarrow$ `arabic-rtl-director` $\rightarrow$ `typography-director` $\rightarrow$ `photography-director` $\rightarrow$ `prompt-compiler` $\rightarrow$ `visual-qa`

### D. Bounded Image Edit (`bounded_image_edit`)
`designly-director` $\rightarrow$ `edit-sanitizer` $\rightarrow$ `arabic-rtl-director` (if text changes) $\rightarrow$ `prompt-compiler` $\rightarrow$ `visual-qa`

---

## 3. Recursive Feedback Loops

When a stage fails quality criteria, it triggers an explicit feedback loop:

1. **Cannes Ideation Refinement Loop**:
   - *Condition*: `concept_score < 9.0` or `humankind_score < 7`.
   - *Loop*: Rotate ideation methods in `methods-catalog` (SIT $\rightarrow$ Bisociation $\rightarrow$ Inversion), re-mine tensions with `insight-mining`, re-score (up to 5 passes).
2. **Craft Physics Alignment Loop**:
   - *Condition*: Horizon, perspective, or lighting mismatch between composite element and background plate.
   - *Loop*: `manipulation-director` $\leftrightarrow$ `photography-director` realign vanishing points and Kelvin color temperatures.
3. **Bounded Edit Containment Loop**:
   - *Condition*: Collateral drift detected or wrong target mutated in output.
   - *Loop*: `visual-qa` rejects output, resets to approved source checkpoint, shrinks mutation polygon via `edit-sanitizer`, and re-issues `EditContract`.
4. **Arabic Glyph Integrity Loop**:
   - *Condition*: Arabic ligature corruption, disconnected glyphs, or reversed RTL flow.
   - *Loop*: `visual-qa` $\rightarrow$ `arabic-rtl-director` issues hard veto, extracts exact Unicode, and passes strict negative constraints to `prompt-compiler`.
5. **Anti-Bias Representation Loop**:
   - *Condition*: Clone faces or stereotypical tokenism detected in group visuals.
   - *Loop*: `visual-qa` $\rightarrow$ `prompt-compiler` injects explicit facial bone structure variance, melanin-calibrated lighting, and negative stock-photo constraints.

---

## 4. Multi-Stage Verification Gates

- **GATE-0 (Intake & Brief Invariants)**: Brief lock, objective, primary message, deliverables.
- **GATE-1 (Ideation & Originality)**: Cannes score $\ge 8.5$, Pollard taxonomy match, pattern saturation cap $\le 6.0$ for P09/P11/P16 without structural novelty.
- **GATE-2 (Representation & Inclusivity)**: 7-point representation checklist, no clone faces, melanin-calibrated lighting, no gibberish cultural symbols.
- **GATE-3 (Spatial & Typographic Preflight)**: 1-second thumbnail test, grayscale value mass, exact copy locked, Arabic glyphs shaped.
- **GATE-4 (Craft Realism & Physics)**: Consistent horizon, ambient occlusion contact shadows, directional reflections, and physical light wrap.
- **GATE-5 (Bounded-Edit Containment)**: Mutation budget = 1, protected complement locked, approved source checkpoint verified.
- **GATE-6 (Post-Generation Visual Signoff)**: Weighted score $\ge 92$, all applicable category floors met, AI-slop veto clear, collateral drift zero.
