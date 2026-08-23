# Inclusive Representation & Ethical Visual Generation

This reference defines Designly's standards for authentic human representation and anti-bias prompt engineering, synthesizing principles from the Inclusive Visuals Specialist domain.

---

## 1. Core Principles

1. **Identity as Architecture, Not Decoration**:
   - Never append tokenized adjectives (e.g. "diverse team", "multicultural") to prompts. Foundational diffusion models default to stereotypical caricatures or clone faces under vague diversity requests.
   - Explicitly specify age, ethnicity, role agency, authentic attire, and contextual environment.

2. **Dignified Agency Over Stock Tropes**:
   - Depict individuals as active decision-makers, creators, and leaders rather than passive, smiling background subjects.
   - Avoid "Kumbaya" stock-photo tropes where diverse people smile unnaturally at blank surfaces.

3. **Melanin-Accurate Lighting & Optics**:
   - Lighting setups must be color-graded to respect deep skin tones without blowing out highlights or creating unnatural ashen/gray undertones.
   - Specify warm rim lights, soft fill, and authentic reflective properties.

---

## 2. Model Failure Modes & Negative Constraints

| AI Defect / Bias Mode | Failure Mechanism | Negative Constraint Rule |
|---|---|---|
| **Clone Faces** | Model duplicates the same facial features across diverse background actors | Mandate distinct facial bone structures, hair textures, and age variances across subjects |
| **Hero-Symbol Clichés** | Exaggerated, mathematically perfect religious or cultural icons dominating the frame | Focus on the genuine human moment; ban oversized floating crescent moons, fake headdresses, or generic ethnic symbols |
| **Gibberish Cultural Text** | Model hallucinates pseudolanguage in non-Latin scripts | Strictly negative-prompt text/signage or route exact copy to `arabic-rtl-director` |
| **Mobility Aid Glitches** | Canes, wheelchairs, or prosthetics merging into limbs or floating above ground | Define physics of contact: wheels touching pavement, fabric draping over mobility aids |

---

## 3. The 7-Point Representation Review Checklist

Before signing off on any human-centric visual:
1. **Dignity**: Does the subject have authentic purpose and natural expression?
2. **Contextual Accuracy**: Are architecture, attire, and tools grounded in the specific geography?
3. **Optics & Lighting**: Is lighting calibrated accurately for skin tone richness?
4. **Physical Reality**: Are hands, clothing draping, and mobility aids physically believable?
5. **No Clones**: Are all individuals in group scenes distinctly unique in age and feature?
6. **No Tokenism**: Is representation organic to the narrative rather than decorative?
7. **Cultural Respect**: Are cultural elements represented without caricature?
