# Designly Workflow Prompt Library

<p>
  <img src="../../../assets/badges/prompt-playground.svg" alt="Designly Workflow Prompt Library" />
  <img src="../../../assets/badges/prompts.svg" alt="16 production workflows" />
  <img src="../../../assets/badges/skills.svg" alt="21 Designly Skills" />
  <img src="../../../assets/badges/arabic-rtl.svg" alt="Arabic RTL" />
  <img src="../../../assets/badges/ai-film.svg" alt="AI Film" />
  <img src="../../../assets/badges/visual-qa.svg" alt="Visual QA" />
</p>

This is not a gallery of fictional briefs. It is a copy-ready operating layer for the real Designly mesh.

Each Workflow Prompt is built around existing Designly Skills, their ownership boundaries, typed contracts, role-aware pipelines, feedback loops, model-physics rules, and release gates. Replace the `{{PLACEHOLDERS}}`, paste the prompt into ChatGPT with `@Designly`, attach the relevant assets, and let Designly execute the job through the smallest useful route.

<p>
  <a href="#core-orchestration-workflows"><img src="../../../assets/badges/section-start.svg" alt="Core Routes" /></a>
  <a href="#image--design-execution-workflows"><img src="../../../assets/badges/section-learn.svg" alt="Image Workflows" /></a>
  <a href="#video--narrative-workflows"><img src="../../../assets/badges/section-advanced.svg" alt="Video Workflows" /></a>
  <a href="#review-repair--specialist-workflows"><img src="../../../assets/badges/section-chatgpt.svg" alt="Review and Repair" /></a>
  <a href="#workflow-coverage-map"><img src="../../../assets/badges/section-coverage.svg" alt="Route Map" /></a>
</p>

## Production rules

Every workflow in this library follows these rules:

1. **Route, do not decorate.** Start with `designly-director`, classify the job, and use the smallest useful route that can complete it. Do not activate all 21 Skills for ceremony.
2. **Do not invent Skills, tools, models, memory, or execution capabilities.** Use only Designly capabilities that exist in the repository and host capabilities that are actually available in the current session.
3. **Respect ownership.** A specialist writes only the state it owns. `creative-director` owns ideation; `composition-director` owns spatial hierarchy; `prompt-compiler` compiles approved decisions; `visual-qa` independently reviews the actual output.
4. **Use real contracts.** Maintain `DesignContext`, specialist `DesignSignalPacket` handoffs, `generation_state`, `EditContract` for bounded edits, and `RevisionRequest` for failed release dimensions.
5. **Locks outrank taste.** User exact constraints, official brand assets, exact copy, cultural correctness, and protected edit regions cannot be overwritten by inferred taste or decorative preference.
6. **Compile only approved upstream work.** Do not let `prompt-compiler` invent a concept or repair hierarchy. Route incomplete state back to its owner first.
7. **Execute when execution is available.** If the host exposes a host-native image generation or editing tool, use it only after the generation state is ready. If no compatible execution tool exists, return the ready model-specific instruction and state that execution was not performed.
8. **Review reality, not intention.** When an actual output exists, `visual-qa` must inspect the actual output before signoff. A good Art Direction Spec is not evidence that the render passed.
9. **Fail locally.** QA failures return one `RevisionRequest` to the smallest responsible Skill. Do not restart the whole workflow unless the concept or brief itself failed.
10. **Do not expose private chain-of-thought.** Show decisions, routes, evidence, scores, contracts, and deliverables in a concise user-facing form.

---

<a id="core-orchestration-workflows"></a>
## Core orchestration workflows

### WF-01 Auto-route any Designly job

**Use when:** you have a design task and want Designly to decide the correct internal pipeline instead of blindly running every Skill.

**Required inputs:** `{{BRIEF}}`, `{{DELIVERABLES}}`; optional `{{BRAND_ASSETS}}`, `{{REFERENCES}}`, `{{EXACT_COPY}}`, `{{LANGUAGE}}`, `{{TARGET_MODEL}}`.

**Route:** `designly-director` → smallest applicable role-aware pipeline or Pathway → relevant specialists → `prompt-compiler` when generation/edit execution is required → `visual-qa` when an actual visual exists.

**Copy prompt**

```text
@Designly

Treat this as a production Designly job, not as a request for generic design advice.

INPUTS
- Brief: {{BRIEF}}
- Deliverables / formats: {{DELIVERABLES}}
- Brand assets or guidelines: {{BRAND_ASSETS}}
- Visual references: {{REFERENCES}}
- Exact copy that must not be rewritten: {{EXACT_COPY}}
- Language / cultural context: {{LANGUAGE}}
- Preferred target model, only if I specified one: {{TARGET_MODEL}}

OPERATING INSTRUCTIONS
1. Use `designly-director` as the state owner. Create the working DesignContext first: task type, objective, audience, primary communication job, desired action, platform/ratio, cultural context, supplied assets, and immutable locks.
2. Classify the task against the actual Designly routing graph and choose the smallest useful route. Do not run every Skill automatically. Briefly tell me which route is active and why.
3. Use only existing Designly Skills. Do not invent a new specialist because the brief uses unfamiliar terminology.
4. Each specialist must stay inside its ownership. Preserve important outputs as DesignSignalPacket-style handoffs rather than letting downstream Skills silently reinterpret upstream decisions.
5. If important information is absent but not blocking, continue with an explicit assumption. Ask only when the missing fact materially changes the output or a fail-close Skill such as `edit-sanitizer` returns clarify.
6. If the job ends in image/video generation, do not jump to a generator prompt. Finish the required strategy, brand/taste, composition, craft, and model-physics stages first. Only then let `prompt-compiler` create generation_state.
7. If a compatible host-native image or editing tool is actually available, execute the approved generation_state. If execution is unavailable, return the compiled instruction without pretending that a render happened.
8. If an actual visual is produced or supplied for review, run `visual-qa` on the actual output. On failure, create one targeted RevisionRequest to the smallest responsible Skill, repair that dimension, recompile if needed, and re-check.
9. Return a concise production report: active route, immutable locks, material decisions, final deliverable or executable prompt, QA verdict, and any unresolved risk. Do not expose private chain-of-thought.

Now execute the workflow on my inputs.
```

### WF-02 Full new commercial campaign

**Use when:** turning a business/marketing brief into a campaign idea, hero visual direction, and production-ready execution without skipping strategy or originality checks.

**Required inputs:** `{{BRIEF}}`, `{{AUDIENCE}}`, `{{DELIVERABLES}}`; optional `{{BRAND_ASSETS}}`, `{{REFERENCES}}`, `{{COPY}}`, `{{TARGET_MODEL}}`.

**Route:** role-aware pipeline `new_commercial_campaign`: `designly-director` → `creative-strategy` → `insight-mining` → `creative-director` → `campaign-canon` → `brand-intelligence` → `taste-engine` → `composition-director` → `typography-director` → `photography-director` → `image-director` → `prompt-compiler` → `visual-qa`.

**Copy prompt**

```text
@Designly

Run the real `new_commercial_campaign` pipeline on this job.

INPUTS
- Brief: {{BRIEF}}
- Audience: {{AUDIENCE}}
- Deliverables / channels / ratios: {{DELIVERABLES}}
- Brand assets and guidelines: {{BRAND_ASSETS}}
- References, if any: {{REFERENCES}}
- Exact mandatory copy: {{COPY}}
- Preferred image model, if explicitly required: {{TARGET_MODEL}}

WORKFLOW
1. `designly-director`: lock the objective, audience, communication job, deliverables, language/culture, exact copy, brand constraints, and supplied assets in DesignContext.
2. `creative-strategy`: deconstruct the business objective into one primary message and desired audience action. Do not generate visual decoration yet.
3. `insight-mining`: derive the strongest useful tension using the actual methods available in the Skill: problem/insight/advantage/strategy, JTBD, cultural/category/human tension, and abstraction laddering. Distinguish evidence from assumption.
4. `creative-director`: choose the correct idea level, generate structurally different concepts using its real method catalog rather than free association, mark obvious warm-ups, evaluate with the configured Cannes/HumanKind criteria, and refine or restart if the strongest route does not clear the Skill's quality bar.
5. `campaign-canon`: benchmark the concept against the canonical campaign library and pattern taxonomy. Use the canon as anti-derivative evidence. Flag saturated patterns and force structural novelty instead of copying famous work.
6. `brand-intelligence`: audit logo, product, identity, brand-off specificity, and supplied guidelines. Convert hard brand constraints into locks.
7. `taste-engine`: only if references exist, extract Evidence → Observation → Transferable Rule → Anti-Rule. Assign each reference a non-overlapping job. Do not copy subject matter or proprietary composition. If there are no references, do not fabricate a Taste Profile.
8. `composition-director`: define the actual visual hierarchy, grid, focal anchor, grouping, negative space, crop behavior, and eye path for the hero asset.
9. `typography-director`: lock exact copy, text zones, measure, line breaks, type hierarchy, and spacing. If Arabic is primary, route the Arabic-specific decisions through `arabic-rtl-director` before release.
10. `photography-director`: define camera relationships, lighting geometry, material response, realism, subject treatment, and only the optical choices that materially affect the image.
11. `image-director`: select the correct supported model physics. Do not force GPT Image 2 syntax onto Nano Banana or vice versa. Load the matching task/industry pattern guidance.
12. `prompt-compiler`: compile only the approved upstream Art Direction state into generation_state. Preserve brand/product/copy locks verbatim and lint out vague effect stacks.
13. If a host-native image tool is available, execute. Then `visual-qa` must review the actual output against brief accuracy, concept strength, hierarchy, typography, brand/product fidelity, physical realism, cultural fit, representation, and AI-slop gates.
14. If QA fails, issue one RevisionRequest to the smallest responsible Skill and repair only that dimension. Do not regenerate the entire campaign unless the concept failed.

DELIVER TO ME
- Final campaign premise in one sentence
- The selected insight/tension
- The winning concept and why it survived canon/originality review
- Hero visual Art Direction Spec
- Exact active locks
- Final model-specific executable instruction or actual generated output
- Visual QA verdict and any targeted revision performed

Do not give me a feature tour. Execute the pipeline.
```

### WF-03 High-fidelity key visual from an approved idea

**Use when:** the campaign idea/message is already approved and the real job is to turn it into a strong key visual without reopening strategy unnecessarily.

**Required inputs:** `{{APPROVED_IDEA}}`, `{{PRIMARY_MESSAGE}}`, `{{DELIVERABLE}}`; optional `{{BRAND_ASSETS}}`, `{{REFERENCES}}`, `{{EXACT_COPY}}`, `{{TARGET_MODEL}}`.

**Route:** `designly-director` → `insight-mining` only if message rationale is missing → `brand-intelligence` when brand assets exist → `composition-director` → `typography-director` when text is present → `photography-director` and/or `manipulation-director` → `image-director` → `prompt-compiler` → host-native image generation if available → `visual-qa`.

**Copy prompt**

```text
@Designly

The concept is already approved. Do not restart campaign ideation unless you find a direct contradiction in the brief.

INPUTS
- Approved idea: {{APPROVED_IDEA}}
- Primary message: {{PRIMARY_MESSAGE}}
- Deliverable / aspect ratio: {{DELIVERABLE}}
- Brand assets: {{BRAND_ASSETS}}
- Reference images: {{REFERENCES}}
- Exact copy: {{EXACT_COPY}}
- Target model preference: {{TARGET_MODEL}}

Use `designly-director` to lock the approved idea as immutable strategy state, then build the visual through the smallest execution route.

1. If the primary message already explains the strategic job, do not rerun `creative-director`. Use `insight-mining` only if the visual tension still needs clarification.
2. If brand assets exist, use `brand-intelligence` to lock logo/product proportions, clearspace, official colors, and identity constraints before composition.
3. Use `taste-engine` only when references are supplied, and only for transferable rules. Never substitute reference imitation for the approved concept.
4. `composition-director` must lock one focal anchor, hierarchy, grid, negative space, crop, eye path, and protected text zones before surface styling.
5. `typography-director` owns exact copy, line breaks, measure, scale, and spacing. Route Arabic-first work through `arabic-rtl-director` rather than mirroring an LTR layout.
6. Use `photography-director` for camera/light/material physics. If the scene is a composite or impossible manipulation, add `manipulation-director` for horizon, scale, contact, occlusion, reflections, relighting, and believable integration.
7. `image-director` selects model physics based on the job and supplied assets. If I named a model, verify it is actually supported before using its syntax.
8. `prompt-compiler` receives only approved states and produces generation_state. It may not change the concept or repair weak composition on its own.
9. Use the host-native image tool if one exists. Then run `visual-qa` on the actual output. Route any failure to one responsible Skill and recompile only if that Skill changed an upstream state.

Return the final Art Direction Spec, the ready execution instruction or generated visual, and the QA verdict. Keep internal reasoning private.
```

### WF-04 Arabic-first poster / campaign asset

**Use when:** Arabic is the primary visual language and correct RTL hierarchy, exact copy, native glyph shaping, and regional visual fit are hard requirements.

**Required inputs:** `{{BRIEF}}`, `{{ARABIC_COPY}}`, `{{DELIVERABLE}}`; optional `{{BRAND_ASSETS}}`, `{{REGION}}`, `{{REFERENCES}}`, `{{TARGET_MODEL}}`.

**Route:** role-aware pipeline `arabic_first_poster`: `designly-director` → `creative-strategy` → `insight-mining` → `creative-director` → `brand-intelligence` → `composition-director` → `arabic-rtl-director` → `typography-director` → `photography-director` → `prompt-compiler` → `visual-qa`; use `image-director` before compilation when generative image execution is required.

**Copy prompt**

```text
@Designly

Run this as an `arabic_first_poster` workflow. Arabic is the source layout language, not a translation layer added at the end.

INPUTS
- Brief: {{BRIEF}}
- Exact Arabic copy: {{ARABIC_COPY}}
- Deliverable / ratio: {{DELIVERABLE}}
- Brand assets: {{BRAND_ASSETS}}
- Regional context: {{REGION}}
- References: {{REFERENCES}}
- Target model: {{TARGET_MODEL}}

1. `designly-director`: put the Arabic Unicode string, brand marks, logos, dates, numbers, CTA, and any supplied wording into immutable locks.
2. `creative-strategy`, `insight-mining`, and `creative-director`: establish the communication job and concept only to the depth needed by the brief. Do not use English-first copy as the conceptual source unless I explicitly supplied it that way.
3. `brand-intelligence`: verify brand fidelity before visual construction.
4. `composition-director`: build the spatial architecture natively for RTL. The entry point, focal image, secondary information, and signoff must form a deliberate right-to-left eye path rather than a mechanically mirrored LTR template.
5. `arabic-rtl-director`: own RTL flow, correct contextual glyph shaping, ligatures, Unicode integrity, cultural authenticity, and Arabic/Latin balance. It has hard-veto authority for broken Arabic, reversed strings, malformed connections, or inappropriate symbolism.
6. `typography-director`: own measure, line breaks, scale, spacing, exact-copy zones, and optical relationship between Arabic and any Latin brand name.
7. `photography-director`: define image craft only after hierarchy and Arabic text zones are stable.
8. If image generation is required, `image-director` must select supported model physics and text-rendering guidance before `prompt-compiler` compiles generation_state.
9. Use a host-native image tool if available. `visual-qa` must perform character-by-character copy review, RTL flow review, hierarchy tests, brand fidelity, craft, and AI-slop gates on the actual output.
10. If Arabic glyphs or RTL flow fail, create a RevisionRequest to `arabic-rtl-director`, preserve the approved source/visual decisions, fix the text path, then recompile. Do not accept a visually attractive render with broken Arabic.

Return: locked Arabic copy, RTL composition map, typography spec, final execution instruction or output, and Arabic/Visual QA verdict.
```

### WF-05 References → Taste Profile → new design without imitation

**Use when:** you have one or more reference images and want Designly to use them as evidence for taste, not as layouts to copy.

**Required inputs:** `{{BRIEF}}`, `{{REFERENCES}}`; optional `{{REFERENCE_JOBS}}`, `{{BRAND_ASSETS}}`, `{{SAVE_TO_MEMORY}}`, `{{TARGET_MODEL}}`.

**Route:** `designly-director` → `taste-engine` → `reference-memory` when persistence is requested and available → `brand-intelligence` → `composition-director` → `photography-director` → `image-director` → `prompt-compiler` → `visual-qa`.

**Copy prompt**

```text
@Designly

Use the attached references as structured evidence, not as artwork to imitate.

INPUTS
- New brief: {{BRIEF}}
- Attached references: {{REFERENCES}}
- Optional assigned jobs per reference: {{REFERENCE_JOBS}}
- Brand assets: {{BRAND_ASSETS}}
- Save reusable rules to Reference Memory? {{SAVE_TO_MEMORY}}
- Target model: {{TARGET_MODEL}}

1. `designly-director`: lock the new brief and explicitly separate source reference content from the new subject/brand.
2. `taste-engine`: deconstruct each reference using its actual 5 dimensions: lighting, palette, texture/finish, spatial geometry, mood/tension. For every useful signal, return Evidence → Observation → Transferable Rule → Constraint/Anti-Rule.
3. Never merge references indiscriminately. Assign non-overlapping jobs such as lighting, composition, palette, texture, or typography relationship. If I supplied jobs, respect them. Discard source subject identity, proprietary artwork, and unique composition that would make the result derivative.
4. If persistence was requested, use `reference-memory` only if the runtime can actually perform the local memory operation. Create or update stable `REF-####` records with scoped job tags and feedback. If persistence is unavailable, return a portable Taste Profile without claiming it was saved.
5. `brand-intelligence`: reject any extracted rule that conflicts with official brand locks.
6. `composition-director` and `photography-director`: translate the surviving rules into a new spatial and craft solution for the new brief. The new composition must be independently justified by the communication job.
7. `image-director`: choose model physics and task-specific guidance, then `prompt-compiler` creates generation_state without copying the reference wording or layout.
8. Execute with a host-native image tool if available. `visual-qa` must run brand-off specificity, anti-derivative review, hierarchy/craft checks, and AI-slop gates on the actual output.

Return the Taste Profile, any real REF IDs created, the rules accepted/rejected by brand constraints, the new Art Direction Spec, final execution instruction/output, and QA verdict.
```

---

<a id="image--design-execution-workflows"></a>
## Image & design execution workflows

### WF-06 Bounded image edit with zero scope creep

**Use when:** changing one selected area, object, property, or text region in an existing image while keeping everything else materially stable.

**Required inputs:** `{{SOURCE_IMAGE}}`, `{{REQUESTED_CHANGE}}`, `{{TARGET_REGION}}`; optional `{{EXACT_REPLACEMENT_COPY}}`.

**Route:** role-aware pipeline `bounded_image_edit`: `designly-director` → `edit-sanitizer` → `arabic-rtl-director` when Arabic copy is involved → `image-director` → `prompt-compiler` → host-native image editor → `visual-qa`.

**Copy prompt**

```text
@Designly

This is a bounded edit. Do not redesign the image.

INPUTS
- Approved source image / source checkpoint: {{SOURCE_IMAGE}}
- Requested atomic change: {{REQUESTED_CHANGE}}
- Target region, selection, annotation, or semantic object: {{TARGET_REGION}}
- Exact replacement copy if text is changing: {{EXACT_REPLACEMENT_COPY}}

Run the real `bounded_image_edit` route.

1. `designly-director`: establish the approved source checkpoint. The source must be the last approved image, never a previous failed edit.
2. `edit-sanitizer`: resolve annotation geometry against source dimensions, map it to one semantic target, split the request into atomic mutations, derive protected regions from the complement, lock crop/canvas/perspective/identity/text/lighting/composition unless explicitly targeted, and set a conservative mutation budget.
3. Require a typed EditContract. Do not continue until it is `status: ready` and `execution_allowed: true`. If the sanitizer returns clarify/reject/veto, obey it. Do not compile a best-effort edit around a failed contract.
4. If Arabic text is being corrected, `arabic-rtl-director` must verify the exact Unicode string and glyph behavior before execution.
5. `image-director`: load the bounded-edit guidance for the selected supported image model. Preserve one atomic change per iteration.
6. `prompt-compiler`: compile the ready EditContract in the required order: approved source checkpoint, exact target, one allowed mutation, identity/geometry/text/style locks, protected regions, minimal boundary blending allowance, acceptance checks, and retry rule.
7. Use the host-native image editor if available. Do not claim literal pixel identity outside the target; require material stability.
8. `visual-qa`: compare output against the approved source checkpoint, not against a failed intermediate. Check target accuracy, edit-scope accuracy, collateral drift, crop/canvas/camera/layout/lighting/text/identity/style locks.
9. On collateral drift or wrong target, issue a RevisionRequest to `edit-sanitizer`, reset to the approved source checkpoint, shrink/re-map the mutation scope, and retry. Never chain corrective edits from a drifted render. Stop after the configured retry limit.

Return the EditContract summary, execution verdict, edited result if a tool exists, and source-vs-output QA verdict.
```

### WF-07 Exact Arabic copy correction inside an existing design

**Use when:** the visual is approved but Arabic wording, one letter, diacritic, connection, or line of text must be corrected without changing the design.

**Required inputs:** `{{SOURCE_IMAGE}}`, `{{TARGET_TEXT_REGION}}`, `{{EXACT_ARABIC_COPY}}`.

**Route:** `designly-director` → `edit-sanitizer` → `arabic-rtl-director` → `image-director` → `prompt-compiler` → host-native editor → `visual-qa`.

**Copy prompt**

```text
@Designly

Perform a fail-close Arabic copy correction. The design itself is approved.

- Approved source checkpoint: {{SOURCE_IMAGE}}
- Exact target text region: {{TARGET_TEXT_REGION}}
- Exact replacement Arabic string: {{EXACT_ARABIC_COPY}}

1. Lock the source checkpoint and exact Unicode copy in `designly-director`.
2. `edit-sanitizer` must create an EditContract whose only mutation is the specified text replacement. Protect all non-target content including logo, background, layout, product, crop, colors, lighting, type treatment outside the target, and other copy.
3. `arabic-rtl-director` must verify character sequence, contextual letter forms, connections, diacritics, RTL order, and the relationship with neighboring text. A malformed glyph or reversed sequence is a hard veto.
4. If the image model cannot reliably render the exact Arabic string, do not invent copy. Prefer a deterministic text workflow if the host provides one; otherwise clearly return the approved visual foundation and the exact placement specification instead of pretending the model rendered correct Arabic.
5. `image-director` and `prompt-compiler` may only translate the ready EditContract into a provider-supported edit instruction. They may not restyle or recompose the design.
6. Execute only against the approved source. `visual-qa` performs a character-by-character copy pass and source-vs-output collateral review.
7. If anything outside the target changed materially, reject the output, reset to the approved source, and route a RevisionRequest to `edit-sanitizer`.

Return the exact copy lock, EditContract summary, execution result if available, and Arabic + collateral-drift QA verdict.
```

### WF-08 Photoreal manipulation / composite

**Use when:** integrating multiple photographic elements, inserting a product/object into a new environment, or creating an impossible scene that must still obey coherent physical rules.

**Required inputs:** `{{BRIEF}}`, `{{SOURCE_ELEMENTS}}`, `{{DELIVERABLE}}`; optional `{{BRAND_ASSETS}}`, `{{TARGET_MODEL}}`.

**Route:** `designly-director` → `brand-intelligence` when relevant → `composition-director` → `photography-director` ↔ `manipulation-director` → `image-director` → `prompt-compiler` → `visual-qa`.

**Copy prompt**

```text
@Designly

Build this as a physically believable composite, not as a stack of style adjectives.

INPUTS
- Brief / intended scene: {{BRIEF}}
- Source elements / plates / products: {{SOURCE_ELEMENTS}}
- Deliverable / ratio: {{DELIVERABLE}}
- Brand assets: {{BRAND_ASSETS}}
- Target model: {{TARGET_MODEL}}

1. `designly-director`: lock subject identities, product geometry, brand marks, source assets, intended scale relationship, deliverable, and any exact copy.
2. `brand-intelligence`: when branded assets exist, lock logo/product fidelity before compositing decisions.
3. `composition-director`: establish horizon, focal anchor, perspective regime, depth layers, crop, negative space, and viewer eye path.
4. `photography-director`: define the base plate camera logic, lighting direction/size/temperature, exposure relationship, material response, depth of field, and subject treatment.
5. `manipulation-director`: own compositing physics: perspective and scale alignment, contact points, ambient occlusion, cast/contact shadows, light wrap, reflections, refraction when applicable, edge integration, occlusion ordering, atmospheric depth, and color/contrast matching.
6. Use the craft-physics alignment feedback loop between `manipulation-director` and `photography-director` whenever perspective or lighting is inconsistent. Do not paper over a mismatch with grading effects.
7. `image-director`: select the supported model and relevant editing/generation guidance. `prompt-compiler` turns the approved craft state into generation_state while preserving source/product locks.
8. Execute via a host-native image tool when available.
9. `visual-qa`: run the physics pass, edge/tangency/crop test, product fidelity, hierarchy, brand, and AI-slop checks on the actual output. If physical integration fails, route one RevisionRequest to `manipulation-director` rather than re-ideating the whole piece.

Return the composite construction plan, physical locks, final execution instruction/output, and physics QA verdict.
```

### WF-09 Product / e-commerce packshot

**Use when:** creating a product hero, e-commerce image, beauty shot, or branded packshot where product identity and material realism matter more than concept invention.

**Required inputs:** `{{PRODUCT_ASSETS}}`, `{{PRODUCT_SPECS}}`, `{{DELIVERABLE}}`; optional `{{BRAND_ASSETS}}`, `{{COPY}}`, `{{TARGET_MODEL}}`.

**Route:** `designly-director` → `brand-intelligence` → `composition-director` → `typography-director` when copy exists → `photography-director` → `image-director` using the relevant e-commerce/product pattern → `prompt-compiler` → `visual-qa`.

**Copy prompt**

```text
@Designly

Treat this as product-fidelity production, not as open-ended concept ideation.

- Product reference assets: {{PRODUCT_ASSETS}}
- Product dimensions / packaging facts / materials: {{PRODUCT_SPECS}}
- Brand assets and official colors: {{BRAND_ASSETS}}
- Deliverable / ratio / marketplace or channel: {{DELIVERABLE}}
- Exact copy if any: {{COPY}}
- Target model: {{TARGET_MODEL}}

1. `designly-director`: lock product silhouette, proportions, packaging geometry, label/logo placement, exact copy, official colors, and channel requirements.
2. `brand-intelligence`: audit source assets and produce hard product/brand fidelity constraints. Never let a taste reference override packaging identity.
3. `composition-director`: choose the product scale, crop, grounding, whitespace, supporting props only if useful, and text zones.
4. `typography-director`: if text exists, lock exact wording and hierarchy separately from the generated product image.
5. `photography-director`: specify studio setup in physical terms: camera relationship, key/fill/rim or other justified lighting geometry, shadow behavior, background depth, surface finish, reflections, specular response, translucency, and material realism.
6. `image-director`: use the actual e-commerce/product pattern guidance and choose model physics based on reference count, text fidelity needs, and editing/generation mode.
7. `prompt-compiler`: compile approved state; do not embellish the product with invented packaging details.
8. Execute if a host-native image tool exists.
9. `visual-qa`: hard-fail materially changed packaging, malformed logo, wrong product proportions, invented text, impossible reflections, bad grounding, or AI-slop. Route repair to the owning Skill only.

Return the product lock sheet, photography/art-direction spec, executable prompt/output, and fidelity QA verdict.
```

### WF-10 Multi-panel / multi-asset visual campaign

**Use when:** producing several related assets, panels, social posts, or format adaptations that must share a visual family without becoming duplicate layouts.

**Required inputs:** `{{BRIEF}}`, `{{ASSET_LIST}}`, `{{BRAND_ASSETS}}`; optional `{{REFERENCES}}`, `{{COPY_BY_ASSET}}`, `{{TARGET_MODEL}}`.

**Route:** role-aware pipeline `multi_panel_visual_campaign`: `designly-director` → `creative-strategy` → `brand-intelligence` → `taste-engine` → `campaign-dna` for multi-asset continuity → `image-director` → `composition-director` → `typography-director` → `prompt-compiler` → `visual-qa`.

**Copy prompt**

```text
@Designly

Run this as a `multi_panel_visual_campaign` production workflow.

INPUTS
- Brief: {{BRIEF}}
- Required assets / panels / formats / ratios: {{ASSET_LIST}}
- Brand assets: {{BRAND_ASSETS}}
- References: {{REFERENCES}}
- Exact copy per asset: {{COPY_BY_ASSET}}
- Target model: {{TARGET_MODEL}}

1. `designly-director`: create one shared campaign context plus per-asset constraints.
2. `creative-strategy`: lock one campaign communication premise and define the role of each asset. Do not make every panel perform the same job.
3. `brand-intelligence`: lock brand/product identity across the set.
4. `taste-engine`: if references exist, extract job-based transferable rules only. Keep the shared taste layer compact.
5. `campaign-dna`: define invariants that make the family recognizable and explicit variation axes that prevent clone layouts. State what must stay constant and what should intentionally change across assets.
6. `image-director`: choose the appropriate multi-panel / grid / social-format guidance and model physics. Maintain identity and visual continuity where shared characters or products appear.
7. `composition-director`: design each panel's hierarchy and crop for its actual ratio; do not simply resize a hero layout.
8. `typography-director`: preserve exact copy per asset and adapt measure/line breaks by format while maintaining the campaign type hierarchy.
9. `prompt-compiler`: produce per-asset generation_state with a shared continuity block plus asset-specific instructions.
10. Execute through the host if available. `visual-qa` must review both individual quality and family continuity. If one asset fails, issue a RevisionRequest only for that asset/owner unless the Campaign DNA itself is defective.

Return: Campaign DNA, per-asset role matrix, per-asset Art Direction Specs, executable prompts/outputs, and continuity QA verdict.
```

---

<a id="video--narrative-workflows"></a>
## Video & narrative workflows

### WF-11 Narrative storyboard / sequential visual story

**Use when:** creating a storyboard, sequential panels, animatic frames, or visual narrative before motion generation.

**Required inputs:** `{{BRIEF}}`, `{{STORY_LENGTH}}`, `{{FORMAT}}`; optional `{{BRAND_ASSETS}}`, `{{CHARACTER_REFERENCES}}`, `{{TARGET_MODEL}}`.

**Route:** role-aware pipeline `narrative_storyboard`: `designly-director` → `creative-strategy` → `insight-mining` → `visual-storytelling` → `campaign-dna` → `composition-director` → `photography-director` → `image-director` → `prompt-compiler` → `visual-qa`.

**Copy prompt**

```text
@Designly

Run the `narrative_storyboard` pipeline. The goal is a coherent sequence, not isolated pretty frames.

INPUTS
- Brief / narrative goal: {{BRIEF}}
- Number of panels or intended duration: {{STORY_LENGTH}}
- Final format / ratio: {{FORMAT}}
- Brand assets: {{BRAND_ASSETS}}
- Character/product references: {{CHARACTER_REFERENCES}}
- Target image model for keyframes: {{TARGET_MODEL}}

1. `designly-director`: lock story objective, audience, final image requirement, identities, brand/product details, panel count, and exact copy.
2. `creative-strategy` + `insight-mining`: establish the message and tension without over-expanding into a new campaign if the concept is already supplied.
3. `visual-storytelling`: choose the narrative framework that actually fits the job. Define the arc, emotional tiers, scene purpose, escalation, and payoff. Every panel must perform a narrative job.
4. `campaign-dna`: define continuity invariants for characters, product, world, palette behavior, and recurring motifs across panels.
5. `composition-director`: define readable staging and eye path for each frame while maintaining sequence continuity.
6. `photography-director`: lock visual grammar, camera relationships, lighting progression, and material/character treatment.
7. `image-director`: use storyboard/multi-panel/character-continuity guidance, choose model physics, and create keyframe instructions that repeat identity anchors where required.
8. `prompt-compiler`: compile per-frame generation_state without losing shared continuity constraints.
9. Execute stills if a host-native image tool is available.
10. `visual-qa`: inspect the actual panels for story readability, continuity, hierarchy, identity drift, exact copy, and AI-slop. Repair only failing frames or the responsible shared state.

Return the narrative arc, panel function table, continuity locks, final storyboard/keyframe instructions or generated panels, and sequence QA verdict.
```

### WF-12 Cinematic AI video spot

**Use when:** directing a commercial, product film, short narrative, music-video sequence, or AI video spot using Seedance, Kling, Veo, or another model supported by the Video Director.

**Required inputs:** `{{BRIEF}}`, `{{DURATION}}`, `{{ASPECT_RATIO}}`; optional `{{SCRIPT}}`, `{{CHARACTER_PRODUCT_ASSETS}}`, `{{TARGET_MODEL}}`.

**Route:** role-aware pipeline `cinematic_video_spot`: `designly-director` → `creative-strategy` → `insight-mining` → `creative-director` → `visual-storytelling` → `image-director` → `video-director` → `prompt-compiler` → `visual-qa`.

**Copy prompt**

```text
@Designly

Run the real `cinematic_video_spot` route. Prompt engineering comes after dramaturgy.

INPUTS
- Brief: {{BRIEF}}
- Duration: {{DURATION}}
- Aspect ratio / platform: {{ASPECT_RATIO}}
- Existing script or approved campaign idea: {{SCRIPT}}
- Character/product/brand assets: {{CHARACTER_PRODUCT_ASSETS}}
- Preferred video model if required: {{TARGET_MODEL}}

1. `designly-director`: lock duration, platform, identities, exact dialogue/VO, product and logo constraints, and any approved campaign premise.
2. `creative-strategy` and `insight-mining`: establish the communication job and tension. If an approved idea/script already exists, preserve it rather than reopening the campaign.
3. `creative-director`: only if concept generation is still required, create/refine the commercial idea using its real structured methods and configured quality bar.
4. `visual-storytelling`: convert the approved idea into a narrative arc with clear emotional progression and final image.
5. `image-director`: create the necessary still keyframes, character/product anchors, and continuity sheets using the actual image-model physics and storyboard guidance.
6. `video-director`: follow its mandatory reading order. Define the scene formula `desire + obstacle + geometry + gaze + rhythm`; enforce the Three-Jobs Rule; give every shot environmental pressure + body micro-action + sound anchor; use Walter Murch priorities for cuts; and design the montage staircase where relevant.
7. Select one supported video model based on the job. Load exactly that model's physics. Do not write a generic prompt and relabel it for Seedance/Kling/Veo. Respect actual duration, dialogue, reference, JSON, negative-prompt, or element-binding behavior of the chosen engine.
8. Create the appropriate output form: single prompt, multi-clip sequence, 14-field storyboard, or director treatment. Use motivated camera language, not phrases such as “dynamic camera” or generic cinematic adjectives.
9. `prompt-compiler`: compile approved model-specific video generation_state without changing the story.
10. If the host can execute the selected video model, execute. Otherwise return the production-ready model prompt package and state that video execution was not performed.
11. `visual-qa`: review actual motion if available; otherwise review the shot/prompt package for dramaturgy, three-detail completeness, continuity, identity, brand, exact dialogue, and slop. Use the video dramaturgy feedback loop for failures.

Return: chosen route/model and why, director treatment, shot structure, continuity anchors, final model-native prompts, and QA verdict.
```

### WF-13 Turn an approved campaign concept into film without re-ideating it

**Use when:** the campaign platform/idea is already signed off and you need a film treatment, keyframes, shot cards, and video prompts that faithfully express it.

**Required inputs:** `{{APPROVED_CAMPAIGN_IDEA}}`, `{{FILM_OBJECTIVE}}`, `{{DURATION}}`; optional `{{SCRIPT_COPY}}`, `{{ASSETS}}`, `{{TARGET_MODEL}}`.

**Route:** `designly-director` → `visual-storytelling` → `campaign-dna` → `image-director` → `video-director` → `prompt-compiler` → `visual-qa`.

**Copy prompt**

```text
@Designly

The campaign concept below is approved and locked. Do not generate replacement Big Ideas.

- Approved campaign idea: {{APPROVED_CAMPAIGN_IDEA}}
- Film objective: {{FILM_OBJECTIVE}}
- Duration / format: {{DURATION}}
- Exact script / VO / supers: {{SCRIPT_COPY}}
- Brand, product, character, or location assets: {{ASSETS}}
- Target model: {{TARGET_MODEL}}

1. `designly-director`: store the approved campaign premise, exact copy, identities, and brand/product rules as immutable locks.
2. Skip `creative-director` unless the approved concept contains a direct contradiction that makes filming impossible. This workflow is adaptation, not re-ideation.
3. `visual-storytelling`: choose a narrative architecture that dramatizes the approved premise, define the emotional arc, turning point, final image, and role of each beat.
4. `campaign-dna`: translate the existing campaign's invariant visual cues into film continuity rules without forcing every frame to look identical.
5. `image-director`: create character/product sheets and keyframe directions required for continuity.
6. `video-director`: create the director treatment and shot cards using its actual dramaturgy laws, Three-Jobs Rule, three-detail audit, Murch priorities, and one selected model's physics.
7. `prompt-compiler`: compile the approved film state. Preserve exact dialogue/VO and all campaign locks.
8. Execute if the host supports the selected model. `visual-qa` checks whether the film still expresses the approved campaign idea, plus dramaturgy, continuity, brand/product fidelity, copy, and AI-slop.
9. Any failing dimension receives one RevisionRequest to its owner. Do not solve a camera failure by changing the campaign concept.

Return the film treatment, beat/shot structure, continuity rules, keyframe prompts, final video prompts, and QA verdict.
```

---

<a id="review-repair--specialist-workflows"></a>
## Review, repair & specialist workflows

### WF-14 Brand activation / PR stunt / utility

**Use when:** creating an experiential idea, public act, brand utility, ambient execution, cultural object, packaging hack, or PR stunt that must work beyond a standard ad placement.

**Required inputs:** `{{BRIEF}}`, `{{AUDIENCE}}`, `{{CONSTRAINTS}}`; optional `{{BRAND_ASSETS}}`, `{{LOCATION_CONTEXT}}`.

**Route:** role-aware pipeline `brand_activation_stunt`: `designly-director` → `insight-mining` → `brand-activation` → `campaign-canon` → `brand-intelligence` → `manipulation-director` when physical visualization is needed → `prompt-compiler` when execution imagery is required → `visual-qa`.

**Copy prompt**

```text
@Designly

Run this as a `brand_activation_stunt` workflow, not as a list of ad executions.

INPUTS
- Brief / objective: {{BRIEF}}
- Audience: {{AUDIENCE}}
- Budget, timing, operational, legal, or location constraints: {{CONSTRAINTS}}
- Brand assets / brand promise: {{BRAND_ASSETS}}
- Cultural / location context: {{LOCATION_CONTEXT}}

1. `designly-director`: lock the objective, audience behavior, brand constraints, operational limits, and cultural context.
2. `insight-mining`: find the human/category/cultural tension and the behavior the activation should change or enable.
3. `brand-activation`: explore only its real activation formats: utility, PR/guerilla, cultural hijack, subversive demonstration, interactive/ambient installation, social experiment, product/packaging hack, digital-physical bridge, or cultural object. Use the 3-second participation floor where interaction is involved.
4. Apply the non-advertising diagnostic exactly: if the campaign media disappears, does the object/act still possess intrinsic utility or cultural meaning? Classify the idea honestly as `non_advertising` or `execution`.
5. `campaign-canon`: benchmark against known activation patterns and reject derivative mechanics rather than name-dropping cases.
6. `brand-intelligence`: verify the idea can still be recognized as this brand without depending on a pasted logo.
7. If a physical visualization is needed, `manipulation-director` owns spatial/physical plausibility of the installation; use `image-director` as needed for model physics before `prompt-compiler` compiles visualization instructions.
8. `visual-qa` reviews any actual mockup, but also separate visual quality from activation viability. Do not let a beautiful mockup rescue a weak mechanic.

Return: insight, activation format, one-sentence mechanic, participant behavior, non-advertising diagnostic result, operational reality, earned-media logic, risks, visualization spec if needed, and QA/feasibility verdict.
```

### WF-15 Audit an existing design and repair only what failed

**Use when:** you already have a visual and want a rigorous Designly review followed by targeted repair, not a full redesign by default.

**Required inputs:** `{{EXISTING_VISUAL}}`, `{{ORIGINAL_BRIEF}}`; optional `{{BRAND_ASSETS}}`, `{{EXACT_COPY}}`, `{{SOURCE_CHECKPOINT}}`.

**Route:** `designly-director` → `visual-qa` first → exactly one smallest responsible specialist per failing dimension → `prompt-compiler` or `edit-sanitizer` when execution requires it → actual output → `visual-qa` again.

**Copy prompt**

```text
@Designly

Review and repair this visual using Designly's real release and revision model. Do not redesign it before diagnosis.

INPUTS
- Existing visual: {{EXISTING_VISUAL}}
- Original brief / communication job: {{ORIGINAL_BRIEF}}
- Brand/product assets: {{BRAND_ASSETS}}
- Exact copy: {{EXACT_COPY}}
- Approved source checkpoint if this is an edit: {{SOURCE_CHECKPOINT}}

1. `designly-director`: reconstruct the relevant locks from the brief and supplied assets.
2. Run `visual-qa` on the actual visual first. Evaluate only applicable categories: brief/message accuracy, concept strength, hierarchy/composition, grouping/spacing/crop, typography/exact copy, color/contrast, brand/product fidelity, physical realism, cultural/platform fit, inclusive representation, craft, and AI-slop.
3. Apply hard gates. Separate critical/major/minor defects from taste preferences. Do not fail a design merely because a reviewer would personally style it differently.
4. For each actual failure, identify the owner using Designly's revision map. Prioritize the single defect with the highest release impact and issue one typed RevisionRequest to the smallest responsible Skill.
5. The receiving specialist may modify only its owned state. Examples: concept → `creative-director`; insight → `insight-mining`; hierarchy → `composition-director`; type → `typography-director`; Arabic → `arabic-rtl-director`; brand/product → `brand-intelligence`; physical integration → `manipulation-director`; provider instruction → `prompt-compiler`.
6. If repair is a bounded mutation on an existing image, route the request through `edit-sanitizer` and require a ready EditContract before execution.
7. Recompile only if an upstream state changed. Execute with a host-native image/edit tool if available.
8. Re-run `visual-qa` on the actual repaired output. Continue targeted revision only while failures remain and within the applicable retry limits.

Return: QA scorecard, hard-gate verdict, prioritized defects, RevisionRequest, exact repair performed, before/after QA comparison, and final release verdict. Keep private reasoning private.
```

### WF-16 Compile an approved Art Direction Spec for the correct image model

**Use when:** strategy, concept, composition, and craft are already approved and you need Designly to convert them into the correct GPT Image 2 or Nano Banana instruction without changing the art direction.

**Required inputs:** `{{APPROVED_ART_DIRECTION_SPEC}}`, `{{TARGET_MODEL}}`, `{{DELIVERABLE}}`; optional `{{REFERENCE_ASSETS}}`, `{{PRESERVATION_LOCKS}}`.

**Route:** `designly-director` → `image-director` → `prompt-compiler`; add `visual-qa` only after an actual output exists.

**Copy prompt**

```text
@Designly

Compile this approved Art Direction Spec. Do not improve, reinterpret, or replace the creative idea.

INPUTS
- Approved Art Direction Spec: {{APPROVED_ART_DIRECTION_SPEC}}
- Target model: {{TARGET_MODEL}}
- Deliverable / size / ratio: {{DELIVERABLE}}
- Reference assets: {{REFERENCE_ASSETS}}
- Preservation / exact-copy / brand locks: {{PRESERVATION_LOCKS}}

1. `designly-director`: verify that the upstream strategy/composition/craft state is actually approved and sufficiently complete. If a required state is missing, route back to its owner instead of asking `prompt-compiler` to guess.
2. `image-director`: verify the target model is one Designly supports and load the correct physics in its mandatory reading order.
   - For GPT Image 2, use its 5-slot structure, quality lever, supported size logic, reference behavior, and two-column edit logic where applicable.
   - For Nano Banana, use natural-language/model-specific behavior and do not inject camera numbers that its guidance explicitly rejects.
   - Load task-specific modules such as text rendering, editing, characters, storyboards, structural, dimensional, vision decomposition, multi-panel, or the relevant industry pattern only when the job needs them.
3. Preserve the approved art direction. Model adaptation may change instruction syntax and explicitness, not concept, hierarchy, copy, logo, product identity, or protected content.
4. `prompt-compiler`: compile generation_state. State invariants first, express composition as relationships, preserve exact locks verbatim, include only likely failure exclusions, and use the host's native image interface rather than invented API parameters.
5. Run prompt lint / anti-slop rules conceptually or with available repo scripts when the runtime supports them. Reject vague quality adjectives that replace actual visual decisions.
6. If a host-native image generator is available, execute the compiled state. Only after actual output exists, run `visual-qa`. Otherwise stop at a ready executable instruction and explicitly say execution was not performed.

Return only: verified model choice, any model-physics adaptation that materially changed the instruction structure, final generation_state, ready copyable model prompt, and QA result if an actual image was generated. Do not expose private chain-of-thought.
```

---

## Prompt behavior in ChatGPT

When a user asks `@Designly` for prompts, examples, a guide, or help using the plugin, do not invent a fictional brief to demonstrate a Skill.

First classify the user's real job and show the smallest relevant workflow menu. Recommended menu:

```text
What are you trying to ship with Designly?

1. Auto-route a design brief
2. Build a full campaign
3. Turn an approved idea into a key visual
4. Create Arabic-first artwork
5. Use references without copying them
6. Make a bounded edit
7. Build a realistic composite
8. Produce a multi-asset campaign
9. Build a storyboard or AI film
10. Audit and repair an existing visual
11. Create a brand activation
12. Compile an approved spec for the right image model

Tell me the job number, or give me your real brief and I will choose the workflow.
```

When returning a Workflow Prompt:

- Give the prompt itself before lengthy explanation
- Preserve routing, ownership, contracts, gates, and fail-close clauses
- Adapt placeholders and obviously user-editable inputs only
- Do not shorten away the clauses that make the workflow reliable
- Do not substitute a capability description for execution

## Workflow coverage map

| Workflow | Primary route | Existing Skills materially exercised |
|---|---|---|
| WF-01 | Auto-route | `designly-director` + smallest applicable route |
| WF-02 | `new_commercial_campaign` | `creative-strategy`, `insight-mining`, `creative-director`, `campaign-canon`, `brand-intelligence`, `taste-engine`, `composition-director`, `typography-director`, `photography-director`, `image-director`, `prompt-compiler`, `visual-qa` |
| WF-03 | Key visual execution | `brand-intelligence`, `composition-director`, `typography-director`, `photography-director`, `manipulation-director`, `image-director`, `prompt-compiler`, `visual-qa` |
| WF-04 | `arabic_first_poster` | `creative-strategy`, `insight-mining`, `creative-director`, `brand-intelligence`, `composition-director`, `arabic-rtl-director`, `typography-director`, `photography-director`, `image-director`, `prompt-compiler`, `visual-qa` |
| WF-05 | Reference/taste | `taste-engine`, `reference-memory`, `brand-intelligence`, `composition-director`, `photography-director`, `image-director`, `prompt-compiler`, `visual-qa` |
| WF-06 | `bounded_image_edit` | `edit-sanitizer`, `arabic-rtl-director`, `image-director`, `prompt-compiler`, `visual-qa` |
| WF-07 | Arabic bounded copy repair | `edit-sanitizer`, `arabic-rtl-director`, `image-director`, `prompt-compiler`, `visual-qa` |
| WF-08 | Composite craft | `composition-director`, `photography-director`, `manipulation-director`, `image-director`, `prompt-compiler`, `visual-qa` |
| WF-09 | Product packshot | `brand-intelligence`, `composition-director`, `typography-director`, `photography-director`, `image-director`, `prompt-compiler`, `visual-qa` |
| WF-10 | `multi_panel_visual_campaign` | `creative-strategy`, `brand-intelligence`, `taste-engine`, `campaign-dna`, `image-director`, `composition-director`, `typography-director`, `prompt-compiler`, `visual-qa` |
| WF-11 | `narrative_storyboard` | `creative-strategy`, `insight-mining`, `visual-storytelling`, `campaign-dna`, `composition-director`, `photography-director`, `image-director`, `prompt-compiler`, `visual-qa` |
| WF-12 | `cinematic_video_spot` | `creative-strategy`, `insight-mining`, `creative-director`, `visual-storytelling`, `image-director`, `video-director`, `prompt-compiler`, `visual-qa` |
| WF-13 | Approved concept → film | `visual-storytelling`, `campaign-dna`, `image-director`, `video-director`, `prompt-compiler`, `visual-qa` |
| WF-14 | `brand_activation_stunt` | `insight-mining`, `brand-activation`, `campaign-canon`, `brand-intelligence`, `manipulation-director`, `prompt-compiler`, `visual-qa` |
| WF-15 | QA + targeted revision | `visual-qa` + exactly one responsible specialist + `edit-sanitizer`/`prompt-compiler` when required |
| WF-16 | Model-physics compilation | `image-director`, `prompt-compiler`, `visual-qa` after actual output |

All 21 existing Designly Skills are represented across the workflow library. This file is the single source of truth for user-facing production prompts. The top-level Director owns invocation and routing; specialist implementation details remain in their own Skill files.
