# Graph Report - .  (2026-08-23)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 1574 nodes · 1971 edges · 171 communities (146 shown, 25 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 32 edges (avg confidence: 0.52)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `893a608d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- enum
- properties
- properties
- taste-mix.schema.json
- enum
- properties
- revision_routes
- properties
- campaign-canon/scripts/generate_mocs.py
- creative-director/scripts/generate_mocs.py
- MeshRouter
- reads
- required
- properties
- arabic-rtl-director
- reference_memory.py
- enum
- properties
- enum
- type
- properties
- properties
- properties
- sanitize_edit.py
- properties
- properties
- properties
- required
- required
- required
- properties
- properties
- brand-intelligence
- required
- taste-engine
- campaign-canon/scripts/test_creative_director.py
- properties
- properties
- creative-director/scripts/test_creative_director.py
- required
- required
- properties
- type
- properties
- properties
- required
- ambiguity
- properties
- properties
- type
- reference-memory.schema.json
- properties
- enum
- writes
- required
- required
- required
- enum
- required
- type
- enum
- reads
- reference-memory
- items
- properties
- applicability
- brand_state
- enum
- creative-brief.schema.json
- design-context.schema.json
- test_campaign_canon.py
- properties
- enum
- insight-mining
- similarity_guard
- photography-director
- enum
- enum
- enum
- enum
- parse_schema
- type
- parse_schema
- test_insight_mining.py
- enum
- campaign-dna
- manipulation-director
- enum
- source
- visual-qa
- brand-activation
- visual-storytelling
- validate_mesh.py
- test_brand_activation.py
- campaign-canon/scripts/generate_links.py
- visual-dna.schema.json
- art-direction.schema.json
- creative-director/scripts/generate_links.py
- test_visual_storytelling.py
- validate_public_plugin.py
- enum
- confidence
- validate_agent_configs.py
- validate_skill_interfaces.py
- alignment_anchors
- design_lint.py
- taste_merge.py
- test_contracts.py
- locks
- iteration
- priority
- focal_points
- restraints
- style_families
- prompt_lint.py
- nodes
- test_skill_catalog.py
- controlled_variables
- crop_rules
- spacing_rhythm
- typography_roles
- aspect_ratio
- crop_logic
- eye_path
- hero
- negative_space
- supporting_information
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
- prompt-compiler
- composition_state
- craft_state
- cultural_context
- desired_action
- generation_state
- platform
- session_id
- strategy_state
- taste_state
- typography_state
- background_character
- product_scale_range
- campaign-canon
- desired_action
- language
- obstacle_or_objection
- Path
- Path
- Path
- Any
- Path
- signature
- packet_id
- primary_message
- audience

## God Nodes (most connected - your core abstractions)
1. `enum` - 21 edges
2. `enum` - 21 edges
3. `nodes` - 20 edges
4. `revision_routes` - 20 edges
5. `required` - 19 edges
6. `enum` - 17 edges
7. `required` - 17 edges
8. `enum` - 14 edges
9. `new_commercial_campaign` - 13 edges
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

## Communities (171 total, 25 thin omitted)

### Community 0 - "enum"
Cohesion: 0.04
Nodes (48): annotation_guided, applicability, background_extend, composition-revision, concept-revision, defects, fail, family (+40 more)

### Community 1 - "properties"
Cohesion: 0.04
Nodes (47): category_floor_failed, defect_description, failing_dimension, origin_packet_id, required_delta, revision_id, source_qa, target_node (+39 more)

### Community 2 - "properties"
Cohesion: 0.05
Nodes (44): accent_strategy, alignment, class, exact_copy_locked, ltr, mixed, roles, rtl (+36 more)

### Community 3 - "taste-mix.schema.json"
Cohesion: 0.06
Nodes (36): ref, additionalProperties, additionalProperties, properties, required, type, items, type (+28 more)

### Community 4 - "enum"
Cohesion: 0.17
Nodes (36): arabic-rtl-director, arabic_visual_director, brand-activation, brand_guardian, brand-intelligence, campaign-canon, campaign-dna, composition-director (+28 more)

### Community 5 - "properties"
Cohesion: 0.06
Nodes (35): brand_rule, director, immutable, lock_id, locked_by, locked_value, priority, safety_gate (+27 more)

### Community 6 - "revision_routes"
Cohesion: 0.07
Nodes (28): architecture_layers, feedback_loops, name, primary_orchestrator, revision_routes, activation_mechanic, ai_slop, annotation_mapping (+20 more)

### Community 7 - "properties"
Cohesion: 0.07
Nodes (28): height, kind, string, width, type, additionalProperties, properties, required (+20 more)

### Community 8 - "campaign-canon/scripts/generate_mocs.py"
Cohesion: 0.15
Nodes (27): format_card_line(), generate_moc_budget(), generate_moc_emotion(), generate_moc_format(), generate_moc_index(), generate_moc_industry(), generate_moc_pattern(), get() (+19 more)

### Community 9 - "creative-director/scripts/generate_mocs.py"
Cohesion: 0.15
Nodes (27): format_card_line(), generate_moc_budget(), generate_moc_emotion(), generate_moc_format(), generate_moc_index(), generate_moc_industry(), generate_moc_pattern(), get() (+19 more)

### Community 10 - "MeshRouter"
Cohesion: 0.11
Nodes (17): Any, check(), main(), run_conflict_evals(), main(), test_ai_slop_vetoes(), test_category_floors(), test_targeted_revision_routing() (+9 more)

### Community 11 - "reads"
Cohesion: 0.27
Nodes (10): audience, cultural_context, objective, agent, description, reads, type, reads (+2 more)

### Community 12 - "required"
Cohesion: 0.09
Nodes (22): acceptance_checks, annotation_space, edit_id, execution_allowed, forbidden_mutations, geometry_locks, identity_locks, iteration (+14 more)

### Community 13 - "properties"
Cohesion: 0.10
Nodes (21): key_direction, shadow_behavior, softness, minLength, type, additionalProperties, properties, required (+13 more)

### Community 14 - "arabic-rtl-director"
Cohesion: 0.13
Nodes (15): composition_state.rtl_flow, typography_state, typography_state.arabic_rtl, agent, description, reads, type, writes (+7 more)

### Community 15 - "reference_memory.py"
Cohesion: 0.33
Nodes (19): blank(), cmd_add(), cmd_export(), cmd_feedback(), cmd_forget(), cmd_get(), cmd_init(), cmd_list() (+11 more)

### Community 16 - "enum"
Cohesion: 0.12
Nodes (19): brand-behavior, camera, crop, cultural-direction, grid, intent, material, restraint (+11 more)

### Community 17 - "properties"
Cohesion: 0.11
Nodes (19): creative_territory, visual_proof, visual_proposition, type, additionalProperties, properties, required, type (+11 more)

### Community 18 - "enum"
Cohesion: 0.11
Nodes (19): hard_gate, major, minor, severity, enum, type, critical, severity (+11 more)

### Community 19 - "type"
Cohesion: 0.11
Nodes (19): items, minItems, type, items, type, items, type, minLength (+11 more)

### Community 20 - "properties"
Cohesion: 0.11
Nodes (19): type, type, type, type, properties, camera_family, image_treatment, lighting_family (+11 more)

### Community 21 - "properties"
Cohesion: 0.11
Nodes (18): one_second_read, primary, secondary, additionalProperties, properties, required, type, minLength (+10 more)

### Community 22 - "properties"
Cohesion: 0.11
Nodes (18): minLength, type, minLength, type, minLength, type, properties, minLength (+10 more)

### Community 23 - "sanitize_edit.py"
Cohesion: 0.27
Nodes (15): base_request(), expect(), main(), schema_valid(), _base_result(), _fail(), main(), _mutation_conflict() (+7 more)

### Community 24 - "properties"
Cohesion: 0.12
Nodes (17): pattern, type, type, items, type, properties, edit_id, execution_allowed (+9 more)

### Community 25 - "properties"
Cohesion: 0.12
Nodes (16): minLength, type, type, additionalProperties, properties, required, type, minLength (+8 more)

### Community 26 - "properties"
Cohesion: 0.12
Nodes (16): type, type, maximum, minimum, type, additionalProperties, type, const (+8 more)

### Community 27 - "required"
Cohesion: 0.13
Nodes (14): anti_rules, observations, profile_version, rules, signature, similarity_guard, source, additionalProperties (+6 more)

### Community 28 - "required"
Cohesion: 0.13
Nodes (14): decisions, from, hard_vetoes, packet_id, recommended_next, soft_warnings, to, additionalProperties (+6 more)

### Community 29 - "required"
Cohesion: 0.14
Nodes (15): geometry, region_id, semantic_target, target_id, additionalProperties, required, confidence, rule (+7 more)

### Community 30 - "properties"
Cohesion: 0.13
Nodes (15): maximum, minimum, type, properties, confidence, region_id, rule, semantic_target (+7 more)

### Community 31 - "properties"
Cohesion: 0.13
Nodes (15): type, type, properties, minLength, type, benefit, heuristic, name (+7 more)

### Community 32 - "brand-intelligence"
Cohesion: 0.25
Nodes (8): brand_assets, product_specs, agent, description, reads, type, writes, brand-intelligence

### Community 33 - "required"
Cohesion: 0.15
Nodes (14): dimension, interpretation, strength, transferable, additionalProperties, required, evidence, job (+6 more)

### Community 34 - "taste-engine"
Cohesion: 0.29
Nodes (7): references, taste-engine, agent, description, reads, type, writes

### Community 35 - "campaign-canon/scripts/test_creative_director.py"
Cohesion: 0.21
Nodes (13): calculate_weighted_score(), main(), Calculate weighted score from the 6 Cannes/D&AD calibration criteria., Verify that tag-schema.md is successfully parsed into non-empty enum sets., Verify that every campaign card in legendary-campaigns/cards passes schema…, Verify weighted score calculation against known score combinations., Verify that saturated patterns (P09, P11, P16) cap default originality at 7…, Verify all MOC index files exist and have non-empty markdown content. (+5 more)

### Community 36 - "properties"
Cohesion: 0.18
Nodes (14): items, type, items, type, type, items, type, items (+6 more)

### Community 37 - "properties"
Cohesion: 0.14
Nodes (14): type, type, minLength, type, type, type, properties, awareness (+6 more)

### Community 38 - "creative-director/scripts/test_creative_director.py"
Cohesion: 0.21
Nodes (13): calculate_weighted_score(), main(), Calculate weighted score from the 6 Cannes/D&AD calibration criteria., Verify that tag-schema.md is successfully parsed into non-empty enum sets., Verify that every campaign card in legendary-campaigns/cards passes schema…, Verify weighted score calculation against known score combinations., Verify that saturated patterns (P09, P11, P16) cap default originality at 7…, Verify all MOC index files exist and have non-empty markdown content. (+5 more)

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
Cohesion: 0.20
Nodes (10): items, type, type, evidence, soft_warnings, unresolved, items, type (+2 more)

### Community 43 - "properties"
Cohesion: 0.15
Nodes (13): type, pattern, type, properties, minLength, type, $ref, created_at (+5 more)

### Community 44 - "properties"
Cohesion: 0.15
Nodes (13): type, minLength, type, type, fingerprint, label, name, ref_id (+5 more)

### Community 45 - "required"
Cohesion: 0.17
Nodes (12): alignment_anchors, aspect_ratio, crop_logic, eye_path, grid_type, hero, negative_space, reading_direction (+4 more)

### Community 46 - "ambiguity"
Cohesion: 0.17
Nodes (12): reasons, additionalProperties, properties, required, type, unresolved, ambiguity, reasons (+4 more)

### Community 47 - "properties"
Cohesion: 0.20
Nodes (10): type, type, properties, from, job, recommended_next, to, items (+2 more)

### Community 48 - "properties"
Cohesion: 0.17
Nodes (12): properties, type, key, rationale, reason, remediation, rule, value (+4 more)

### Community 49 - "type"
Cohesion: 0.18
Nodes (12): items, minLength, type, items, minItems, type, uniqueItems, jobs (+4 more)

### Community 50 - "reference-memory.schema.json"
Cohesion: 0.18
Nodes (10): mixes, next_ref, schema_version, additionalProperties, $id, references, required, $schema (+2 more)

### Community 51 - "properties"
Cohesion: 0.18
Nodes (11): type, properties, type, type, background, foreground, middle_ground, secondary_mass (+3 more)

### Community 52 - "enum"
Cohesion: 0.20
Nodes (10): ai_slop, annotation_mapping, arabic_rtl, collateral_change, edit_scope, prompt_execution, strategy, enum (+2 more)

### Community 53 - "writes"
Cohesion: 0.20
Nodes (10): all_packets, qa_state.final_approval, session_id, task_type, agent, description, reads, type (+2 more)

### Community 54 - "required"
Cohesion: 0.20
Nodes (10): brief_accuracy, concept_strength, craft, cultural_fit, grouping_alignment, lighting_materials, marketing_clarity, platform_fit (+2 more)

### Community 55 - "required"
Cohesion: 0.20
Nodes (10): controlled_variables, crop_rules, image_treatment, lighting_family, locked_invariants, palette_roles, spacing_rhythm, typography_roles (+2 more)

### Community 56 - "required"
Cohesion: 0.20
Nodes (10): created_at, feedback, id, note, profile, signal, updated_at, required (+2 more)

### Community 57 - "enum"
Cohesion: 0.20
Nodes (10): exploration, quick, reference_replication, single_asset, taste_extraction, edit, review, task_type (+2 more)

### Community 58 - "required"
Cohesion: 0.18
Nodes (12): key, value, reason, items, type, items, type, additionalProperties (+4 more)

### Community 59 - "type"
Cohesion: 0.20
Nodes (10): items, type, items, minItems, type, items, minItems, type (+2 more)

### Community 60 - "enum"
Cohesion: 0.22
Nodes (9): brand-guideline, design, image, other, video-frame, campaign, enum, type (+1 more)

### Community 61 - "reads"
Cohesion: 0.22
Nodes (9): edit_request, generation_state.approved_checkpoint, locks, agent, description, reads, type, writes (+1 more)

### Community 62 - "reference-memory"
Cohesion: 0.22
Nodes (9): reference_records, taste_state.reference_memory, user_feedback, reference-memory, agent, description, reads, type (+1 more)

### Community 63 - "items"
Cohesion: 0.25
Nodes (9): items, type, additionalProperties, type, items, feedback, references, items (+1 more)

### Community 64 - "properties"
Cohesion: 0.22
Nodes (9): type, items, type, copy_risk, must_transform, protected_elements, items, type (+1 more)

### Community 65 - "applicability"
Cohesion: 0.22
Nodes (9): maximum, minimum, type, additionalProperties, type, applicability, scores, additionalProperties (+1 more)

### Community 66 - "brand_state"
Cohesion: 0.24
Nodes (16): brand_state, brief, composition_state, craft_state, edit_state, strategy_state, taste_state, reads (+8 more)

### Community 67 - "enum"
Cohesion: 0.25
Nodes (8): custom, freeform-anchors, modular, radial-centered, single-axis, split-field, enum, grid_type

### Community 68 - "creative-brief.schema.json"
Cohesion: 0.25
Nodes (7): platform, additionalProperties, $id, required, $schema, title, type

### Community 69 - "design-context.schema.json"
Cohesion: 0.25
Nodes (7): additionalProperties, locks, taste_state, required, $schema, title, type

### Community 70 - "test_campaign_canon.py"
Cohesion: 0.36
Nodes (7): main(), Verify that saturated patterns P09, P11, and P16 are identified., Verify that the 571 campaign card library is present., Verify all 6 MOC files exist., test_campaign_cards_are_present_and_valid(), test_moc_index_files_are_accessible(), test_pattern_saturation_classification()

### Community 71 - "properties"
Cohesion: 0.25
Nodes (8): type, minimum, type, properties, mixes, next_ref, schema_version, const

### Community 72 - "enum"
Cohesion: 0.29
Nodes (7): clarify, ready, reject, veto, status, enum, type

### Community 73 - "insight-mining"
Cohesion: 0.22
Nodes (10): desired_action, primary_message, strategy_state.insight, writes, writes, agent, description, type (+2 more)

### Community 74 - "similarity_guard"
Cohesion: 0.29
Nodes (7): copy_risk, must_transform, protected_elements, similarity_guard, additionalProperties, required, type

### Community 75 - "photography-director"
Cohesion: 0.33
Nodes (6): craft_state.photography, photography-director, agent, description, type, writes

### Community 76 - "enum"
Cohesion: 0.29
Nodes (7): generate, reference, edit, review, task_type, enum, manipulation

### Community 77 - "enum"
Cohesion: 0.38
Nodes (7): high, enum, low, medium, strength, enum, type

### Community 78 - "enum"
Cohesion: 0.29
Nodes (7): licensed, owned, public-reference, unknown, enum, type, ownership

### Community 79 - "enum"
Cohesion: 0.29
Nodes (7): mask, normalized, pixels, semantic, enum, type, annotation_space

### Community 80 - "parse_schema"
Cohesion: 0.43
Nodes (6): main(), parse_schema(), Path, Validate a single card's frontmatter. Returns list of error strings., Parse tag-schema.md and return field -> set of allowed enum values., validate_card()

### Community 81 - "type"
Cohesion: 0.29
Nodes (7): items, type, type, constraints, supporting_information, items, type

### Community 82 - "parse_schema"
Cohesion: 0.43
Nodes (6): main(), parse_schema(), Path, Validate a single card's frontmatter. Returns list of error strings., Parse tag-schema.md and return field -> set of allowed enum values., validate_card()

### Community 83 - "test_insight_mining.py"
Cohesion: 0.52
Nodes (6): main(), Validate standard insight formula: [Audience] wants/want [X], but [Y], because…, test_insight_formula_accepts_valid_synthesized_insights(), test_insight_formula_rejects_missing_tension_clauses(), test_insight_mining_reference_files_exist(), validate_insight_formula()

### Community 84 - "enum"
Cohesion: 0.33
Nodes (6): active, archived, canonical, status, enum, type

### Community 85 - "campaign-dna"
Cohesion: 0.33
Nodes (6): campaign_state, agent, description, type, writes, campaign-dna

### Community 86 - "manipulation-director"
Cohesion: 0.33
Nodes (6): craft_state.manipulation, agent, description, type, writes, manipulation-director

### Community 87 - "enum"
Cohesion: 0.33
Nodes (6): one, low, medium, enum, type, mutation_budget

### Community 88 - "source"
Cohesion: 0.33
Nodes (6): ownership, label, source, additionalProperties, required, type

### Community 89 - "visual-qa"
Cohesion: 0.33
Nodes (6): qa_state, visual-qa, agent, description, type, writes

### Community 90 - "brand-activation"
Cohesion: 0.33
Nodes (6): strategy_state.activation, agent, description, type, writes, brand-activation

### Community 91 - "visual-storytelling"
Cohesion: 0.33
Nodes (6): strategy_state.narrative_arc, visual-storytelling, agent, description, type, writes

### Community 92 - "validate_mesh.py"
Cohesion: 0.73
Nodes (5): check(), main(), validate_lock_precedence(), validate_routing_graph(), validate_schemas()

### Community 93 - "test_brand_activation.py"
Cohesion: 0.53
Nodes (5): classify_activation_utility(), main(), Classify activation as non_advertising vs execution based on the diagnostic…, test_activation_toolkit_references_exist(), test_non_advertising_diagnostic_differentiates_utility_from_execution()

### Community 94 - "campaign-canon/scripts/generate_links.py"
Cohesion: 0.53
Nodes (5): build_related_section(), main(), parse_frontmatter(), Path, update_card()

### Community 95 - "visual-dna.schema.json"
Cohesion: 0.33
Nodes (5): additionalProperties, $id, $schema, title, type

### Community 96 - "art-direction.schema.json"
Cohesion: 0.33
Nodes (5): additionalProperties, $id, $schema, title, type

### Community 97 - "creative-director/scripts/generate_links.py"
Cohesion: 0.53
Nodes (5): build_related_section(), main(), parse_frontmatter(), Path, update_card()

### Community 98 - "test_visual_storytelling.py"
Cohesion: 0.53
Nodes (5): get_emotion_tier_range(), main(), Return the allowed score range for emotional specificity tier., test_emotional_tier_scoring_bounds(), test_storytelling_references_exist()

### Community 99 - "validate_public_plugin.py"
Cohesion: 0.67
Nodes (5): check(), err(), main(), ok(), svg_size()

### Community 100 - "enum"
Cohesion: 0.40
Nodes (5): image-only, poster-ad-layout, small-text, typography_heavy, enum

### Community 101 - "confidence"
Cohesion: 0.40
Nodes (5): description, maximum, minimum, type, confidence

### Community 102 - "validate_agent_configs.py"
Cohesion: 0.90
Nodes (4): check(), main(), validate_agent(), validate_config()

### Community 103 - "validate_skill_interfaces.py"
Cohesion: 0.80
Nodes (4): check(), main(), parse_frontmatter(), validate_skill()

### Community 104 - "alignment_anchors"
Cohesion: 0.40
Nodes (5): items, maxItems, minItems, type, alignment_anchors

### Community 105 - "design_lint.py"
Cohesion: 0.70
Nodes (4): has_exception(), lint(), main(), norm_words()

### Community 106 - "taste_merge.py"
Cohesion: 0.70
Nodes (4): build(), find(), load_json(), main()

### Community 107 - "test_contracts.py"
Cohesion: 0.83
Nodes (3): load_schema(), main(), validates()

### Community 108 - "locks"
Cohesion: 0.50
Nodes (4): $ref, items, type, locks

### Community 109 - "iteration"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, iteration

### Community 110 - "priority"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, priority

### Community 111 - "focal_points"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, focal_points

### Community 112 - "restraints"
Cohesion: 0.50
Nodes (4): restraints, items, minItems, type

### Community 113 - "style_families"
Cohesion: 0.50
Nodes (4): style_families, items, maxItems, type

### Community 114 - "prompt_lint.py"
Cohesion: 0.83
Nodes (3): active_term(), lint(), main()

### Community 115 - "nodes"
Cohesion: 0.20
Nodes (10): agent, description, type, writes, agent, description, type, nodes (+2 more)

### Community 117 - "controlled_variables"
Cohesion: 0.67
Nodes (3): minItems, type, controlled_variables

### Community 118 - "crop_rules"
Cohesion: 0.67
Nodes (3): items, type, crop_rules

### Community 119 - "spacing_rhythm"
Cohesion: 0.67
Nodes (3): spacing_rhythm, minLength, type

### Community 120 - "typography_roles"
Cohesion: 0.67
Nodes (3): typography_roles, items, type

### Community 121 - "aspect_ratio"
Cohesion: 0.67
Nodes (3): minLength, type, aspect_ratio

### Community 122 - "crop_logic"
Cohesion: 0.67
Nodes (3): minLength, type, crop_logic

### Community 123 - "eye_path"
Cohesion: 0.67
Nodes (3): minLength, type, eye_path

### Community 124 - "hero"
Cohesion: 0.67
Nodes (3): minLength, type, hero

### Community 125 - "negative_space"
Cohesion: 0.67
Nodes (3): minLength, type, negative_space

### Community 126 - "supporting_information"
Cohesion: 0.67
Nodes (3): supporting_information, items, type

### Community 127 - "cultural_constraints"
Cohesion: 0.67
Nodes (3): items, type, cultural_constraints

### Community 128 - "exact_copy"
Cohesion: 0.67
Nodes (3): items, type, exact_copy

### Community 129 - "locked_assets"
Cohesion: 0.67
Nodes (3): items, type, locked_assets

### Community 130 - "non_goals"
Cohesion: 0.67
Nodes (3): items, type, non_goals

### Community 131 - "platform"
Cohesion: 0.67
Nodes (3): minLength, type, platform

### Community 132 - "primary_message"
Cohesion: 0.67
Nodes (3): minLength, type, primary_message

### Community 133 - "proof"
Cohesion: 0.67
Nodes (3): items, type, proof

### Community 134 - "references"
Cohesion: 0.67
Nodes (3): references, items, type

### Community 139 - "prompt-compiler"
Cohesion: 0.33
Nodes (6): generation_state, prompt-compiler, agent, description, type, writes

### Community 152 - "campaign-canon"
Cohesion: 0.33
Nodes (6): strategy_state.canon_benchmark, agent, description, type, writes, campaign-canon

### Community 167 - "signature"
Cohesion: 0.50
Nodes (4): anyOf, signature, additionalProperties, type

### Community 168 - "packet_id"
Cohesion: 0.67
Nodes (3): pattern, type, packet_id

## Knowledge Gaps
- **740 isolated node(s):** `$schema`, `title`, `type`, `locks`, `taste_state` (+735 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **25 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `properties` connect `properties` to `art-direction.schema.json`, `properties`, `required`, `required`, `properties`, `restraints`, `properties`, `style_families`, `properties`, `properties`?**
  _High betweenness centrality (0.148) - this node is a cross-community bridge._
- **Why does `nodes` connect `nodes` to `brand-intelligence`, `taste-engine`, `revision_routes`, `insight-mining`, `reads`, `photography-director`, `prompt-compiler`, `arabic-rtl-director`, `campaign-dna`, `writes`, `manipulation-director`, `campaign-canon`, `visual-qa`, `brand-activation`, `visual-storytelling`, `reads`, `reference-memory`?**
  _High betweenness centrality (0.129) - this node is a cross-community bridge._
- **Why does `role_aware_pipelines` connect `enum` to `revision_routes`?**
  _High betweenness centrality (0.114) - this node is a cross-community bridge._
- **What connects `$schema`, `title`, `type` to the rest of the system?**
  _740 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `enum` be split into smaller, more focused modules?**
  _Cohesion score 0.04336734693877551 - nodes in this community are weakly interconnected._
- **Should `properties` be split into smaller, more focused modules?**
  _Cohesion score 0.04343971631205674 - nodes in this community are weakly interconnected._
- **Should `properties` be split into smaller, more focused modules?**
  _Cohesion score 0.049682875264270614 - nodes in this community are weakly interconnected._