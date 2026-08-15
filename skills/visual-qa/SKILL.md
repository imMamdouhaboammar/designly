---
name: visual-qa
description: Independent visual quality assurance, hard-gate auditor, and targeted revision router. This skill should be used when reviewing rendered images or designs, scoring category floors, testing against AI-slop anti-patterns, issuing approval verdicts, or routing targeted RevisionRequests to specialist skills.
---

# Visual QA

Visual QA provides rigorous, independent critique of generated or edited visual outputs. It scores across 6 distinct dimensions, enforces strict category floors to prevent high-average score masking, triggers hard-gate vetoes for AI-slop anti-patterns, and routes repairs exclusively to the single failing specialist.

---

## 1. Core Workflow

1. **Independent Evaluation (Weighted Threshold >= 92)**:
   - Evaluates the visual across weighted categories:
     - **Hierarchy (Floor: 85)**: Eye path, focal clarity, 1 hero anchor.
     - **Composition (Floor: 90)**: Balance, grid stability, negative space.
     - **Typography (Floor: 88, if applicable)**: Contrast, measure, line breaks, exact copy.
     - **Brand Fidelity (Floor: 95, if applicable)**: Logo clearspace, color formulas.
     - **Product Fidelity (Floor: 98, if applicable)**: Physical packaging accuracy.
     - **Physical Believability (Floor: 90, if applicable)**: Plausible contact shadows, lighting consistency.
   - **Category Floor Rule**: If ANY applicable category falls below its floor, the entire visual fails, regardless of whether the overall average is >= 92.

2. **Hard Gate Checks**:
   - **Arabic Copy Gate**: If Arabic text has broken glyphs, reversed letters, or incorrect connections: FAIL.
   - **Accessibility Contrast Gate**: Text contrast must meet >= 4.5:1 against background.
   - **Protected Region Gate**: In edit mode, non-target regions must remain 100% untouched.

3. **AI-Slop Hard Veto Policy**:
   - Critical Slop finding (e.g. effect stack replaces concept): 0 allowed (immediate FAIL).
   - Major Slop findings (e.g. equal emphasis across 3 subjects): max 1 allowed (>= 2 FAILS).
   - Minor Slop findings: max 3 allowed (>= 4 FAILS).
   - Cumulative Slop Pressure: >= 6 FAILS.

4. **Targeted Revision Routing**:
   - If the review fails, do NOT restart the entire pipeline.
   - Produce a structured `RevisionRequest` specifying the single target specialist:
     - Hierarchy / Grid defect ➔ `composition-director`
     - Text / Readability defect ➔ `typography-director`
     - Arabic glyph / RTL defect ➔ `arabic-rtl-director`
     - Brand / Packaging defect ➔ `brand-intelligence`
     - Physics / Shadow defect ➔ `manipulation-director`
     - Concept / Message defect ➔ `creative-strategy`
     - Model execution defect ➔ `prompt-compiler`

5. **Output Contract**:
   - Return structured `qa_state`, `VisualReview` JSON, and `RevisionRequest` inside `DesignSignalPacket`.

---

## 2. Tools & Scripts

- Score a Visual Review and evaluate all gates:
  ```bash
  python3 scripts/score_review.py assets/visual-review.template.json
  ```
- Run gate regression tests:
  ```bash
  python3 scripts/test_gates.py
  ```

---

## 3. Schemas & References

- Local Schema: [Visual Review Schema](schemas/visual-review.schema.json)
- Shared Contract: [Revision Request Schema](../../shared/contracts/revision-request.schema.json)
- Shared Reference: [Visual QA & Revisions Guide](../../shared/references/visual-qa-and-revisions.md)
- Shared Reference: [AI Slop Taxonomy](../../shared/references/ai-slop-taxonomy.md)
