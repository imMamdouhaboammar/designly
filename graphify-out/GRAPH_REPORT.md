# Graph Report - .  (2026-08-23)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 1613 nodes · 2044 edges · 185 communities (160 shown, 25 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 32 edges (avg confidence: 0.52)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `169752f6`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- properties
- enum
- properties
- taste-mix.schema.json
- properties
- revision_routes
- campaign-canon/scripts/generate_mocs.py
- creative-director/scripts/generate_mocs.py
- MeshRouter
- reads
- required
- properties
- reference_memory.py
- enum
- properties
- properties
- properties
- properties
- properties
- sanitize_edit.py
- type
- enum
- strategy_state
- nodes
- properties
- required
- required
- properties
- properties
- properties
- properties
- required
- properties
- composition-director
- campaign-canon/scripts/test_creative_director.py
- properties
- creative-director/scripts/test_creative_director.py
- properties
- type
- required
- required
- properties
- type
- properties
- properties
- ambiguity
- properties
- properties
- reference-memory.schema.json
- enum
- writes
- required
- required
- required
- required
- enum
- required
- slop_finding
- type
- required
- enum
- reads
- reference-memory
- properties
- properties
- applicability
- brand-intelligence
- enum
- enum
- creative-brief.schema.json
- design-context.schema.json
- enum
- test_campaign_canon.py
- items
- enum
- similarity_guard
- photography-director
- enum
- enum
- image-director
- video-director
- enum
- enum
- enum
- evidence
- parse_schema
- type
- parse_schema
- test_insight_mining.py
- enum
- required
- campaign-dna
- manipulation-director
- prompt-compiler
- enum
- source
- visual-qa
- brand-activation
- campaign-canon
- visual-storytelling
- validate_mesh.py
- test_brand_activation.py
- campaign-canon/scripts/generate_links.py
- visual-dna.schema.json
- art-direction.schema.json
- creative-director/scripts/generate_links.py
- test_image_director.py
- test_video_director.py
- visual-review.schema.json
- properties
- test_visual_storytelling.py
- validate_public_plugin.py
- enum
- requested_mutations
- revision-request.schema.json
- confidence
- validate_agent_configs.py
- validate_skill_interfaces.py
- alignment_anchors
- design_lint.py
- taste_merge.py
- test_contracts.py
- locks
- acceptance_checks
- iteration
- priority
- focal_points
- intent
- style_families
- prompt_lint.py
- signature
- test_skill_catalog.py
- forbidden_mutations
- geometry_locks
- identity_locks
- revision_id
- controlled_variables
- crop_rules
- spacing_rhythm
- typography_roles
- composition
- crop_logic
- eye_path
- hero
- negative_space
- cultural_constraints
- exact_copy
- locked_assets
- non_goals
- platform
- primary_message
- proof
- references
- test_taste_memory.py
- taste_lint.py
- campaign_state
- composition_state
- craft_state
- cultural_context
- desired_action
- generation_state
- primary_message
- session_id
- strategy_state
- taste_state
- typography_state
- background_character
- product_scale_range
- audience
- desired_action
- language
- obstacle_or_objection
- Path
- Path
- Path
- Any
- Path

## God Nodes (most connected - your core abstractions)
1. `revision_routes` - 26 edges
2. `nodes` - 22 edges
3. `enum` - 21 edges
4. `enum` - 21 edges
5. `required` - 19 edges
6. `enum` - 17 edges
7. `required` - 17 edges
8. `enum` - 14 edges
9. `new_commercial_campaign` - 14 edges
10. `enum` - 12 edges

## Surprising Connections (you probably didn't know these)
- `required` --extends--> `brand_fidelity`  [EXTRACTED]
  skills/visual-qa/schemas/visual-review.schema.json → shared/contracts/revision-request.schema.json
- `required` --extends--> `product_fidelity`  [EXTRACTED]
  skills/visual-qa/schemas/visual-review.schema.json → shared/contracts/revision-request.schema.json
- `main()` --calls--> `sanitize_edit()`  [INFERRED]
  evals/edit/test_edit_sanitizer.py → shared/scripts/sanitize_edit.py
- `run_conflict_evals()` --calls--> `MeshRouter`  [INFERRED]
  evals/run_mesh_evals.py → shared/scripts/route_packet.py
- `enum` --extends--> `campaign`  [EXTRACTED]
  skills/composition-director/schemas/creative-brief.schema.json → shared/contracts/design-context.schema.json

## Import Cycles
- None detected.

## Communities (185 total, 25 thin omitted)

### Community 0 - "properties"
Cohesion: 0.05
Nodes (43): accent_strategy, alignment, class, exact_copy_locked, ltr, mixed, roles, rtl (+35 more)

### Community 1 - "enum"
Cohesion: 0.16
Nodes (40): arabic-rtl-director, arabic_visual_director, brand-activation, brand_guardian, brand-intelligence, campaign-canon, campaign-dna, composition-director (+32 more)

### Community 2 - "properties"
Cohesion: 0.05
Nodes (38): height, kind, width, maximum, minimum, type, additionalProperties, properties (+30 more)

### Community 3 - "taste-mix.schema.json"
Cohesion: 0.06
Nodes (36): ref, additionalProperties, additionalProperties, properties, required, type, items, type (+28 more)

### Community 4 - "properties"
Cohesion: 0.06
Nodes (35): brand_rule, director, immutable, lock_id, locked_by, locked_value, priority, safety_gate (+27 more)

### Community 5 - "revision_routes"
Cohesion: 0.06
Nodes (34): architecture_layers, feedback_loops, name, primary_orchestrator, revision_routes, activation_mechanic, ai_slop, annotation_mapping (+26 more)

### Community 6 - "campaign-canon/scripts/generate_mocs.py"
Cohesion: 0.15
Nodes (27): format_card_line(), generate_moc_budget(), generate_moc_emotion(), generate_moc_format(), generate_moc_index(), generate_moc_industry(), generate_moc_pattern(), get() (+19 more)

### Community 7 - "creative-director/scripts/generate_mocs.py"
Cohesion: 0.15
Nodes (27): format_card_line(), generate_moc_budget(), generate_moc_emotion(), generate_moc_format(), generate_moc_index(), generate_moc_industry(), generate_moc_pattern(), get() (+19 more)

### Community 8 - "MeshRouter"
Cohesion: 0.11
Nodes (17): Any, check(), main(), run_conflict_evals(), main(), test_ai_slop_vetoes(), test_category_floors(), test_targeted_revision_routing() (+9 more)

### Community 9 - "reads"
Cohesion: 0.11
Nodes (24): audience, cultural_context, desired_action, objective, primary_message, strategy_state.insight, agent, description (+16 more)

### Community 10 - "required"
Cohesion: 0.09
Nodes (22): acceptance_checks, annotation_space, edit_id, execution_allowed, forbidden_mutations, geometry_locks, identity_locks, iteration (+14 more)

### Community 11 - "properties"
Cohesion: 0.10
Nodes (21): key_direction, shadow_behavior, softness, minLength, type, additionalProperties, properties, required (+13 more)

### Community 12 - "reference_memory.py"
Cohesion: 0.33
Nodes (19): blank(), cmd_add(), cmd_export(), cmd_feedback(), cmd_forget(), cmd_get(), cmd_init(), cmd_list() (+11 more)

### Community 13 - "enum"
Cohesion: 0.12
Nodes (19): brand-behavior, camera, crop, cultural-direction, grid, intent, material, restraint (+11 more)

### Community 14 - "properties"
Cohesion: 0.11
Nodes (19): creative_territory, visual_proof, visual_proposition, type, additionalProperties, properties, required, type (+11 more)

### Community 15 - "properties"
Cohesion: 0.11
Nodes (19): type, type, type, type, properties, camera_family, image_treatment, lighting_family (+11 more)

### Community 16 - "properties"
Cohesion: 0.11
Nodes (18): one_second_read, primary, secondary, additionalProperties, properties, required, type, minLength (+10 more)

### Community 17 - "properties"
Cohesion: 0.14
Nodes (18): items, type, items, type, type, items, type, items (+10 more)

### Community 18 - "properties"
Cohesion: 0.11
Nodes (18): minLength, type, minLength, type, minLength, type, properties, minLength (+10 more)

### Community 19 - "sanitize_edit.py"
Cohesion: 0.27
Nodes (15): base_request(), expect(), main(), schema_valid(), _base_result(), _fail(), main(), _mutation_conflict() (+7 more)

### Community 20 - "type"
Cohesion: 0.13
Nodes (17): geometry, region_id, semantic_target, target_id, additionalProperties, required, type, confidence (+9 more)

### Community 21 - "enum"
Cohesion: 0.14
Nodes (16): annotation_guided, background_extend, composition-revision, concept-revision, inpaint, object_replace, type-color-revision, visual-polish (+8 more)

### Community 22 - "strategy_state"
Cohesion: 0.25
Nodes (16): brand_state, brief, composition_state, craft_state, edit_state, narrative_arc, strategy_state, reads (+8 more)

### Community 23 - "nodes"
Cohesion: 0.13
Nodes (16): composition_state.rtl_flow, typography_state, typography_state.arabic_rtl, agent, description, reads, type, writes (+8 more)

### Community 24 - "properties"
Cohesion: 0.12
Nodes (16): pattern, type, type, properties, edit_id, execution_allowed, protected_regions, requires_arabic_review (+8 more)

### Community 25 - "required"
Cohesion: 0.13
Nodes (14): anti_rules, observations, profile_version, rules, signature, similarity_guard, source, additionalProperties (+6 more)

### Community 26 - "required"
Cohesion: 0.13
Nodes (14): decisions, from, hard_vetoes, packet_id, recommended_next, soft_warnings, to, additionalProperties (+6 more)

### Community 27 - "properties"
Cohesion: 0.13
Nodes (15): type, type, type, type, properties, category_floor_failed, defect_description, failing_dimension (+7 more)

### Community 28 - "properties"
Cohesion: 0.13
Nodes (15): minLength, type, type, properties, type, type, aspect_ratio, background (+7 more)

### Community 29 - "properties"
Cohesion: 0.13
Nodes (15): minLength, type, type, properties, minLength, type, minLength, type (+7 more)

### Community 30 - "properties"
Cohesion: 0.13
Nodes (15): type, type, properties, minLength, type, benefit, heuristic, name (+7 more)

### Community 31 - "required"
Cohesion: 0.15
Nodes (14): dimension, interpretation, strength, transferable, additionalProperties, required, evidence, job (+6 more)

### Community 32 - "properties"
Cohesion: 0.15
Nodes (14): family, severity, items, type, additionalProperties, required, type, evidence (+6 more)

### Community 33 - "composition-director"
Cohesion: 0.15
Nodes (14): references, taste_state, agent, description, reads, type, writes, composition-director (+6 more)

### Community 34 - "campaign-canon/scripts/test_creative_director.py"
Cohesion: 0.21
Nodes (13): calculate_weighted_score(), main(), Calculate weighted score from the 6 Cannes/D&AD calibration criteria., Verify that tag-schema.md is successfully parsed into non-empty enum sets., Verify that every campaign card in legendary-campaigns/cards passes schema…, Verify weighted score calculation against known score combinations., Verify that saturated patterns (P09, P11, P16) cap default originality at 7…, Verify all MOC index files exist and have non-empty markdown content. (+5 more)

### Community 35 - "properties"
Cohesion: 0.14
Nodes (14): type, type, minLength, type, type, type, properties, awareness (+6 more)

### Community 36 - "creative-director/scripts/test_creative_director.py"
Cohesion: 0.21
Nodes (13): calculate_weighted_score(), main(), Calculate weighted score from the 6 Cannes/D&AD calibration criteria., Verify that tag-schema.md is successfully parsed into non-empty enum sets., Verify that every campaign card in legendary-campaigns/cards passes schema…, Verify weighted score calculation against known score combinations., Verify that saturated patterns (P09, P11, P16) cap default originality at 7…, Verify all MOC index files exist and have non-empty markdown content. (+5 more)

### Community 37 - "properties"
Cohesion: 0.14
Nodes (14): type, maximum, minimum, type, additionalProperties, type, const, properties (+6 more)

### Community 38 - "type"
Cohesion: 0.15
Nodes (14): items, type, minLength, type, items, minItems, type, uniqueItems (+6 more)

### Community 39 - "required"
Cohesion: 0.17
Nodes (13): accessibility_plan, arabic, brand, color_contrast, copy, critical_physics, originality, product (+5 more)

### Community 40 - "required"
Cohesion: 0.17
Nodes (13): benefit, heuristic, purpose, items, maxItems, type, items, type (+5 more)

### Community 41 - "properties"
Cohesion: 0.15
Nodes (13): type, type, type, type, type, properties, audience, brand_state (+5 more)

### Community 42 - "type"
Cohesion: 0.15
Nodes (13): items, type, type, evidence, recommended_next, soft_warnings, unresolved, items (+5 more)

### Community 43 - "properties"
Cohesion: 0.15
Nodes (13): type, pattern, type, properties, minLength, type, $ref, created_at (+5 more)

### Community 44 - "properties"
Cohesion: 0.15
Nodes (13): type, minLength, type, type, fingerprint, label, name, ref_id (+5 more)

### Community 45 - "ambiguity"
Cohesion: 0.17
Nodes (12): reasons, additionalProperties, properties, required, type, unresolved, ambiguity, reasons (+4 more)

### Community 46 - "properties"
Cohesion: 0.17
Nodes (12): type, type, type, pattern, type, properties, decisions, from (+4 more)

### Community 47 - "properties"
Cohesion: 0.17
Nodes (12): properties, type, key, rationale, reason, remediation, rule, value (+4 more)

### Community 48 - "reference-memory.schema.json"
Cohesion: 0.18
Nodes (10): mixes, next_ref, schema_version, additionalProperties, $id, references, required, $schema (+2 more)

### Community 49 - "enum"
Cohesion: 0.20
Nodes (10): ai_slop, annotation_mapping, arabic_rtl, collateral_change, edit_scope, prompt_execution, strategy, enum (+2 more)

### Community 50 - "writes"
Cohesion: 0.20
Nodes (10): all_packets, qa_state.final_approval, session_id, task_type, agent, description, reads, type (+2 more)

### Community 51 - "required"
Cohesion: 0.20
Nodes (10): brief_accuracy, concept_strength, craft, cultural_fit, grouping_alignment, lighting_materials, marketing_clarity, platform_fit (+2 more)

### Community 52 - "required"
Cohesion: 0.20
Nodes (10): category_floor_failed, defect_description, failing_dimension, origin_packet_id, required_delta, revision_id, source_qa, target_node (+2 more)

### Community 53 - "required"
Cohesion: 0.20
Nodes (10): controlled_variables, crop_rules, image_treatment, lighting_family, locked_invariants, palette_roles, spacing_rhythm, typography_roles (+2 more)

### Community 54 - "required"
Cohesion: 0.20
Nodes (10): created_at, feedback, id, note, profile, signal, updated_at, required (+2 more)

### Community 55 - "enum"
Cohesion: 0.20
Nodes (10): exploration, quick, reference_replication, single_asset, taste_extraction, edit, review, task_type (+2 more)

### Community 56 - "required"
Cohesion: 0.22
Nodes (10): key, value, reason, items, items, type, additionalProperties, required (+2 more)

### Community 57 - "slop_finding"
Cohesion: 0.20
Nodes (10): string, type, type, null, object, exact_copy, null, slop_finding (+2 more)

### Community 58 - "type"
Cohesion: 0.20
Nodes (10): items, type, items, minItems, type, items, minItems, type (+2 more)

### Community 59 - "required"
Cohesion: 0.22
Nodes (9): alignment_anchors, aspect_ratio, crop_logic, eye_path, grid_type, hero, negative_space, reading_direction (+1 more)

### Community 60 - "enum"
Cohesion: 0.22
Nodes (9): brand-guideline, design, image, other, video-frame, campaign, enum, type (+1 more)

### Community 61 - "reads"
Cohesion: 0.22
Nodes (9): edit_request, generation_state.approved_checkpoint, locks, agent, description, reads, type, writes (+1 more)

### Community 62 - "reference-memory"
Cohesion: 0.22
Nodes (9): reference_records, taste_state.reference_memory, user_feedback, reference-memory, agent, description, reads, type (+1 more)

### Community 63 - "properties"
Cohesion: 0.22
Nodes (9): items, type, minimum, type, properties, mixes, next_ref, schema_version (+1 more)

### Community 64 - "properties"
Cohesion: 0.22
Nodes (9): type, items, type, copy_risk, must_transform, protected_elements, items, type (+1 more)

### Community 65 - "applicability"
Cohesion: 0.22
Nodes (9): maximum, minimum, type, additionalProperties, type, applicability, scores, additionalProperties (+1 more)

### Community 66 - "brand-intelligence"
Cohesion: 0.25
Nodes (8): brand_assets, product_specs, agent, description, reads, type, writes, brand-intelligence

### Community 67 - "enum"
Cohesion: 0.25
Nodes (8): custom, freeform-anchors, modular, radial-centered, single-axis, split-field, enum, grid_type

### Community 68 - "enum"
Cohesion: 0.25
Nodes (8): hard_gate, critical, severity, enum, type, major, minor, enum

### Community 69 - "creative-brief.schema.json"
Cohesion: 0.25
Nodes (7): platform, additionalProperties, $id, required, $schema, title, type

### Community 70 - "design-context.schema.json"
Cohesion: 0.25
Nodes (7): additionalProperties, locks, taste_state, required, $schema, title, type

### Community 71 - "enum"
Cohesion: 0.25
Nodes (8): type, major, minor, family, severity, enum, type, properties

### Community 72 - "test_campaign_canon.py"
Cohesion: 0.36
Nodes (7): main(), Verify that saturated patterns P09, P11, and P16 are identified., Verify that the 571 campaign card library is present., Verify all 6 MOC files exist., test_campaign_cards_are_present_and_valid(), test_moc_index_files_are_accessible(), test_pattern_saturation_classification()

### Community 73 - "items"
Cohesion: 0.29
Nodes (8): items, type, additionalProperties, type, feedback, references, items, type

### Community 74 - "enum"
Cohesion: 0.29
Nodes (7): clarify, ready, reject, veto, status, enum, type

### Community 75 - "similarity_guard"
Cohesion: 0.29
Nodes (7): copy_risk, must_transform, protected_elements, similarity_guard, additionalProperties, required, type

### Community 76 - "photography-director"
Cohesion: 0.29
Nodes (7): craft_state.photography, photography-director, agent, description, reads, type, writes

### Community 77 - "enum"
Cohesion: 0.29
Nodes (7): fail, na, pass, enum, additionalProperties, type, hard_gates

### Community 78 - "enum"
Cohesion: 0.29
Nodes (7): generate, reference, edit, review, task_type, enum, manipulation

### Community 79 - "image-director"
Cohesion: 0.29
Nodes (7): generation_state.image, image_state, agent, description, type, writes, image-director

### Community 80 - "video-director"
Cohesion: 0.29
Nodes (7): generation_state.video, video_state, video-director, agent, description, type, writes

### Community 81 - "enum"
Cohesion: 0.38
Nodes (7): high, enum, low, medium, strength, enum, type

### Community 82 - "enum"
Cohesion: 0.29
Nodes (7): licensed, owned, public-reference, unknown, enum, type, ownership

### Community 83 - "enum"
Cohesion: 0.29
Nodes (7): mask, normalized, pixels, semantic, enum, type, annotation_space

### Community 84 - "evidence"
Cohesion: 0.29
Nodes (7): items, type, type, evidence, protected_regions, items, type

### Community 85 - "parse_schema"
Cohesion: 0.43
Nodes (6): main(), parse_schema(), Path, Validate a single card's frontmatter. Returns list of error strings., Parse tag-schema.md and return field -> set of allowed enum values., validate_card()

### Community 86 - "type"
Cohesion: 0.29
Nodes (7): items, type, type, constraints, supporting_information, items, type

### Community 87 - "parse_schema"
Cohesion: 0.43
Nodes (6): main(), parse_schema(), Path, Validate a single card's frontmatter. Returns list of error strings., Parse tag-schema.md and return field -> set of allowed enum values., validate_card()

### Community 88 - "test_insight_mining.py"
Cohesion: 0.52
Nodes (6): main(), Validate standard insight formula: [Audience] wants/want [X], but [Y], because…, test_insight_formula_accepts_valid_synthesized_insights(), test_insight_formula_rejects_missing_tension_clauses(), test_insight_mining_reference_files_exist(), validate_insight_formula()

### Community 89 - "enum"
Cohesion: 0.33
Nodes (6): active, archived, canonical, status, enum, type

### Community 90 - "required"
Cohesion: 0.33
Nodes (6): applicability, defects, hard_gates, scores, slop_findings, required

### Community 91 - "campaign-dna"
Cohesion: 0.33
Nodes (6): campaign_state, agent, description, type, writes, campaign-dna

### Community 92 - "manipulation-director"
Cohesion: 0.33
Nodes (6): craft_state.manipulation, agent, description, type, writes, manipulation-director

### Community 93 - "prompt-compiler"
Cohesion: 0.33
Nodes (6): generation_state, prompt-compiler, agent, description, type, writes

### Community 94 - "enum"
Cohesion: 0.33
Nodes (6): one, low, medium, enum, type, mutation_budget

### Community 95 - "source"
Cohesion: 0.33
Nodes (6): ownership, label, source, additionalProperties, required, type

### Community 96 - "visual-qa"
Cohesion: 0.33
Nodes (6): qa_state, visual-qa, agent, description, type, writes

### Community 97 - "brand-activation"
Cohesion: 0.33
Nodes (6): strategy_state.activation, agent, description, type, writes, brand-activation

### Community 98 - "campaign-canon"
Cohesion: 0.33
Nodes (6): strategy_state.canon_benchmark, agent, description, type, writes, campaign-canon

### Community 99 - "visual-storytelling"
Cohesion: 0.33
Nodes (6): strategy_state.narrative_arc, visual-storytelling, agent, description, type, writes

### Community 100 - "validate_mesh.py"
Cohesion: 0.73
Nodes (5): check(), main(), validate_lock_precedence(), validate_routing_graph(), validate_schemas()

### Community 101 - "test_brand_activation.py"
Cohesion: 0.53
Nodes (5): classify_activation_utility(), main(), Classify activation as non_advertising vs execution based on the diagnostic…, test_activation_toolkit_references_exist(), test_non_advertising_diagnostic_differentiates_utility_from_execution()

### Community 102 - "campaign-canon/scripts/generate_links.py"
Cohesion: 0.53
Nodes (5): build_related_section(), main(), parse_frontmatter(), Path, update_card()

### Community 103 - "visual-dna.schema.json"
Cohesion: 0.33
Nodes (5): additionalProperties, $id, $schema, title, type

### Community 104 - "art-direction.schema.json"
Cohesion: 0.33
Nodes (5): additionalProperties, $id, $schema, title, type

### Community 105 - "creative-director/scripts/generate_links.py"
Cohesion: 0.53
Nodes (5): build_related_section(), main(), parse_frontmatter(), Path, update_card()

### Community 106 - "test_image_director.py"
Cohesion: 0.60
Nodes (5): main(), test_gpt_image_template_slots(), test_multi_panel_grids(), test_nano_banana_physics(), test_references_exist()

### Community 107 - "test_video_director.py"
Cohesion: 0.60
Nodes (5): main(), test_dramaturgy_scene_formula(), test_model_references(), test_murch_weights(), test_references_exist()

### Community 108 - "visual-review.schema.json"
Cohesion: 0.33
Nodes (5): additionalProperties, $id, $schema, title, type

### Community 109 - "properties"
Cohesion: 0.33
Nodes (6): type, type, properties, evidence, family, severity

### Community 110 - "test_visual_storytelling.py"
Cohesion: 0.53
Nodes (5): get_emotion_tier_range(), main(), Return the allowed score range for emotional specificity tier., test_emotional_tier_scoring_bounds(), test_storytelling_references_exist()

### Community 111 - "validate_public_plugin.py"
Cohesion: 0.67
Nodes (5): check(), err(), main(), ok(), svg_size()

### Community 112 - "enum"
Cohesion: 0.40
Nodes (5): image-only, poster-ad-layout, small-text, typography_heavy, enum

### Community 113 - "requested_mutations"
Cohesion: 0.40
Nodes (5): minLength, requested_mutations, items, minItems, type

### Community 114 - "revision-request.schema.json"
Cohesion: 0.40
Nodes (4): additionalProperties, $schema, title, type

### Community 115 - "confidence"
Cohesion: 0.40
Nodes (5): description, maximum, minimum, type, confidence

### Community 116 - "validate_agent_configs.py"
Cohesion: 0.90
Nodes (4): check(), main(), validate_agent(), validate_config()

### Community 117 - "validate_skill_interfaces.py"
Cohesion: 0.80
Nodes (4): check(), main(), parse_frontmatter(), validate_skill()

### Community 118 - "alignment_anchors"
Cohesion: 0.40
Nodes (5): items, maxItems, minItems, type, alignment_anchors

### Community 119 - "design_lint.py"
Cohesion: 0.70
Nodes (4): has_exception(), lint(), main(), norm_words()

### Community 120 - "taste_merge.py"
Cohesion: 0.70
Nodes (4): build(), find(), load_json(), main()

### Community 121 - "test_contracts.py"
Cohesion: 0.83
Nodes (3): load_schema(), main(), validates()

### Community 122 - "locks"
Cohesion: 0.50
Nodes (4): $ref, items, type, locks

### Community 123 - "acceptance_checks"
Cohesion: 0.50
Nodes (4): items, minItems, type, acceptance_checks

### Community 124 - "iteration"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, iteration

### Community 125 - "priority"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, priority

### Community 126 - "focal_points"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, focal_points

### Community 127 - "intent"
Cohesion: 0.50
Nodes (4): additionalProperties, required, type, intent

### Community 128 - "style_families"
Cohesion: 0.50
Nodes (4): style_families, items, maxItems, type

### Community 129 - "prompt_lint.py"
Cohesion: 0.83
Nodes (3): active_term(), lint(), main()

### Community 130 - "signature"
Cohesion: 0.50
Nodes (4): anyOf, signature, additionalProperties, type

### Community 132 - "forbidden_mutations"
Cohesion: 0.67
Nodes (3): items, type, forbidden_mutations

### Community 133 - "geometry_locks"
Cohesion: 0.67
Nodes (3): items, type, geometry_locks

### Community 134 - "identity_locks"
Cohesion: 0.67
Nodes (3): items, type, identity_locks

### Community 135 - "revision_id"
Cohesion: 0.67
Nodes (3): revision_id, pattern, type

### Community 136 - "controlled_variables"
Cohesion: 0.67
Nodes (3): minItems, type, controlled_variables

### Community 137 - "crop_rules"
Cohesion: 0.67
Nodes (3): items, type, crop_rules

### Community 138 - "spacing_rhythm"
Cohesion: 0.67
Nodes (3): spacing_rhythm, minLength, type

### Community 139 - "typography_roles"
Cohesion: 0.67
Nodes (3): typography_roles, items, type

### Community 140 - "composition"
Cohesion: 0.67
Nodes (3): additionalProperties, type, composition

### Community 141 - "crop_logic"
Cohesion: 0.67
Nodes (3): minLength, type, crop_logic

### Community 142 - "eye_path"
Cohesion: 0.67
Nodes (3): minLength, type, eye_path

### Community 143 - "hero"
Cohesion: 0.67
Nodes (3): minLength, type, hero

### Community 144 - "negative_space"
Cohesion: 0.67
Nodes (3): minLength, type, negative_space

### Community 145 - "cultural_constraints"
Cohesion: 0.67
Nodes (3): items, type, cultural_constraints

### Community 146 - "exact_copy"
Cohesion: 0.67
Nodes (3): items, type, exact_copy

### Community 147 - "locked_assets"
Cohesion: 0.67
Nodes (3): items, type, locked_assets

### Community 148 - "non_goals"
Cohesion: 0.67
Nodes (3): items, type, non_goals

### Community 149 - "platform"
Cohesion: 0.67
Nodes (3): minLength, type, platform

### Community 150 - "primary_message"
Cohesion: 0.67
Nodes (3): minLength, type, primary_message

### Community 151 - "proof"
Cohesion: 0.67
Nodes (3): items, type, proof

### Community 152 - "references"
Cohesion: 0.67
Nodes (3): references, items, type

## Knowledge Gaps
- **755 isolated node(s):** `$schema`, `title`, `type`, `locks`, `taste_state` (+750 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **25 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `properties` connect `properties` to `properties`, `style_families`, `art-direction.schema.json`, `required`, `properties`, `composition`, `properties`, `properties`, `intent`?**
  _High betweenness centrality (0.148) - this node is a cross-community bridge._
- **Why does `nodes` connect `nodes` to `visual-qa`, `brand-activation`, `brand-intelligence`, `campaign-canon`, `composition-director`, `revision_routes`, `visual-storytelling`, `reads`, `photography-director`, `image-director`, `video-director`, `writes`, `prompt-compiler`, `campaign-dna`, `manipulation-director`, `reads`, `reference-memory`?**
  _High betweenness centrality (0.145) - this node is a cross-community bridge._
- **Why does `role_aware_pipelines` connect `enum` to `revision_routes`?**
  _High betweenness centrality (0.132) - this node is a cross-community bridge._
- **What connects `$schema`, `title`, `type` to the rest of the system?**
  _755 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `properties` be split into smaller, more focused modules?**
  _Cohesion score 0.05094130675526024 - nodes in this community are weakly interconnected._
- **Should `properties` be split into smaller, more focused modules?**
  _Cohesion score 0.05405405405405406 - nodes in this community are weakly interconnected._
- **Should `taste-mix.schema.json` be split into smaller, more focused modules?**
  _Cohesion score 0.05555555555555555 - nodes in this community are weakly interconnected._