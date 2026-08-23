# Graph Report - .  (2026-08-23)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 1556 nodes · 1915 edges · 156 communities (144 shown, 12 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 32 edges (avg confidence: 0.52)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6bd69fb9`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- enum
- enum
- properties
- properties
- properties
- taste-mix.schema.json
- properties
- campaign-canon/scripts/generate_mocs.py
- creative-director/scripts/generate_mocs.py
- slop_finding
- revision_routes
- MeshRouter
- required
- properties
- reference_memory.py
- enum
- properties
- properties
- properties
- properties
- sanitize_edit.py
- type
- brand_state
- properties
- properties
- required
- creative-brief.schema.json
- required
- required
- nodes
- properties
- required
- reads
- campaign-canon/scripts/test_creative_director.py
- properties
- properties
- creative-director/scripts/test_creative_director.py
- properties
- required
- required
- properties
- properties
- enum
- required
- reads
- required
- ambiguity
- properties
- composition_state
- reference-memory.schema.json
- properties
- writes
- required
- required
- required
- enum
- type
- properties
- type
- enum
- reference-memory
- taste-engine
- properties
- type
- properties
- applicability
- brand-intelligence
- manipulation-director
- enum
- test_campaign_canon.py
- items
- enum
- arabic-rtl-director
- similarity_guard
- photography-director
- enum
- enum
- enum
- enum
- visual-storytelling
- parse_schema
- type
- parse_schema
- test_insight_mining.py
- enum
- enum
- source
- visual-qa
- insight-mining
- validate_mesh.py
- test_brand_activation.py
- campaign-canon/scripts/generate_links.py
- visual-dna.schema.json
- art-direction.schema.json
- creative-director/scripts/generate_links.py
- test_visual_storytelling.py
- validate_public_plugin.py
- enum
- requested_mutations
- confidence
- validate_agent_configs.py
- validate_skill_interfaces.py
- alignment_anchors
- design_lint.py
- jobs
- taste_merge.py
- test_contracts.py
- acceptance_checks
- iteration
- priority
- focal_points
- restraints
- style_families
- prompt_lint.py
- signature
- test_skill_catalog.py
- forbidden_mutations
- geometry_locks
- style_locks
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
- background_character
- product_scale_range
- audience
- awareness
- language
- obstacle_or_objection
- Path
- Path
- Path

## God Nodes (most connected - your core abstractions)
1. `enum` - 21 edges
2. `enum` - 21 edges
3. `nodes` - 20 edges
4. `revision_routes` - 20 edges
5. `required` - 19 edges
6. `enum` - 17 edges
7. `required` - 17 edges
8. `enum` - 14 edges
9. `enum` - 12 edges
10. `required` - 12 edges

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

## Communities (156 total, 12 thin omitted)

### Community 0 - "enum"
Cohesion: 0.04
Nodes (48): annotation_guided, applicability, background_extend, composition-revision, concept-revision, defects, fail, family (+40 more)

### Community 1 - "enum"
Cohesion: 0.07
Nodes (48): arabic_visual_director, brand_guardian, craft_director, edit-sanitizer, reference-memory, strategy_planner, structure_critic, taste_analyst (+40 more)

### Community 2 - "properties"
Cohesion: 0.04
Nodes (46): additionalProperties, type, type, type, type, type, type, type (+38 more)

### Community 3 - "properties"
Cohesion: 0.05
Nodes (44): accent_strategy, alignment, class, exact_copy_locked, ltr, mixed, roles, rtl (+36 more)

### Community 4 - "properties"
Cohesion: 0.05
Nodes (43): height, kind, string, width, maximum, minimum, type, type (+35 more)

### Community 5 - "taste-mix.schema.json"
Cohesion: 0.06
Nodes (36): ref, additionalProperties, additionalProperties, properties, required, type, items, type (+28 more)

### Community 6 - "properties"
Cohesion: 0.06
Nodes (35): brand_rule, director, immutable, lock_id, locked_by, locked_value, priority, safety_gate (+27 more)

### Community 7 - "campaign-canon/scripts/generate_mocs.py"
Cohesion: 0.15
Nodes (27): format_card_line(), generate_moc_budget(), generate_moc_emotion(), generate_moc_format(), generate_moc_index(), generate_moc_industry(), generate_moc_pattern(), get() (+19 more)

### Community 8 - "creative-director/scripts/generate_mocs.py"
Cohesion: 0.15
Nodes (27): format_card_line(), generate_moc_budget(), generate_moc_emotion(), generate_moc_format(), generate_moc_index(), generate_moc_industry(), generate_moc_pattern(), get() (+19 more)

### Community 9 - "slop_finding"
Cohesion: 0.07
Nodes (27): hard_gate, object, type, major, minor, null, family, severity (+19 more)

### Community 10 - "revision_routes"
Cohesion: 0.08
Nodes (25): name, primary_orchestrator, revision_routes, activation_mechanic, ai_slop, annotation_mapping, arabic_rtl, brand_fidelity (+17 more)

### Community 11 - "MeshRouter"
Cohesion: 0.12
Nodes (16): check(), main(), run_conflict_evals(), main(), test_ai_slop_vetoes(), test_category_floors(), test_targeted_revision_routing(), main() (+8 more)

### Community 12 - "required"
Cohesion: 0.09
Nodes (22): acceptance_checks, annotation_space, edit_id, execution_allowed, forbidden_mutations, geometry_locks, identity_locks, iteration (+14 more)

### Community 13 - "properties"
Cohesion: 0.10
Nodes (21): key_direction, shadow_behavior, softness, minLength, type, additionalProperties, properties, required (+13 more)

### Community 14 - "reference_memory.py"
Cohesion: 0.33
Nodes (19): blank(), cmd_add(), cmd_export(), cmd_feedback(), cmd_forget(), cmd_get(), cmd_init(), cmd_list() (+11 more)

### Community 15 - "enum"
Cohesion: 0.12
Nodes (19): brand-behavior, camera, crop, cultural-direction, grid, intent, material, restraint (+11 more)

### Community 16 - "properties"
Cohesion: 0.11
Nodes (19): creative_territory, visual_proof, visual_proposition, type, additionalProperties, properties, required, type (+11 more)

### Community 17 - "properties"
Cohesion: 0.11
Nodes (19): type, type, type, type, properties, camera_family, image_treatment, lighting_family (+11 more)

### Community 18 - "properties"
Cohesion: 0.11
Nodes (18): one_second_read, primary, secondary, additionalProperties, properties, required, type, minLength (+10 more)

### Community 19 - "properties"
Cohesion: 0.11
Nodes (18): minLength, type, minLength, type, minLength, type, properties, minLength (+10 more)

### Community 20 - "sanitize_edit.py"
Cohesion: 0.27
Nodes (15): base_request(), expect(), main(), schema_valid(), _base_result(), _fail(), main(), _mutation_conflict() (+7 more)

### Community 21 - "type"
Cohesion: 0.14
Nodes (16): geometry, region_id, semantic_target, target_id, additionalProperties, required, type, confidence (+8 more)

### Community 22 - "brand_state"
Cohesion: 0.17
Nodes (16): brand_state, brief, desired_action, primary_message, strategy_state, strategy_state.canon_benchmark, reads, agent (+8 more)

### Community 23 - "properties"
Cohesion: 0.12
Nodes (17): pattern, type, type, items, type, properties, edit_id, execution_allowed (+9 more)

### Community 24 - "properties"
Cohesion: 0.12
Nodes (16): minLength, type, type, additionalProperties, properties, required, type, minLength (+8 more)

### Community 25 - "required"
Cohesion: 0.13
Nodes (14): anti_rules, observations, profile_version, rules, signature, similarity_guard, source, additionalProperties (+6 more)

### Community 26 - "creative-brief.schema.json"
Cohesion: 0.16
Nodes (14): audience, cultural_context, objective, platform, reads, reads, reads, reads (+6 more)

### Community 27 - "required"
Cohesion: 0.13
Nodes (14): category_floor_failed, defect_description, failing_dimension, origin_packet_id, required_delta, revision_id, source_qa, target_node (+6 more)

### Community 28 - "required"
Cohesion: 0.13
Nodes (14): decisions, from, hard_vetoes, packet_id, recommended_next, soft_warnings, to, additionalProperties (+6 more)

### Community 29 - "nodes"
Cohesion: 0.13
Nodes (15): strategy_state.activation, agent, description, type, writes, agent, description, type (+7 more)

### Community 30 - "properties"
Cohesion: 0.13
Nodes (15): type, type, properties, minLength, type, benefit, heuristic, name (+7 more)

### Community 31 - "required"
Cohesion: 0.15
Nodes (14): dimension, interpretation, strength, transferable, additionalProperties, required, evidence, job (+6 more)

### Community 32 - "reads"
Cohesion: 0.16
Nodes (14): edit_request, edit_state, generation_state, generation_state.approved_checkpoint, locks, typography_state, agent, description (+6 more)

### Community 33 - "campaign-canon/scripts/test_creative_director.py"
Cohesion: 0.21
Nodes (13): calculate_weighted_score(), main(), Calculate weighted score from the 6 Cannes/D&AD calibration criteria., Verify that tag-schema.md is successfully parsed into non-empty enum sets., Verify that every campaign card in legendary-campaigns/cards passes schema…, Verify weighted score calculation against known score combinations., Verify that saturated patterns (P09, P11, P16) cap default originality at 7…, Verify all MOC index files exist and have non-empty markdown content. (+5 more)

### Community 34 - "properties"
Cohesion: 0.18
Nodes (14): items, type, items, type, type, items, type, items (+6 more)

### Community 35 - "properties"
Cohesion: 0.14
Nodes (14): type, type, minLength, type, type, type, properties, desired_action (+6 more)

### Community 36 - "creative-director/scripts/test_creative_director.py"
Cohesion: 0.21
Nodes (13): calculate_weighted_score(), main(), Calculate weighted score from the 6 Cannes/D&AD calibration criteria., Verify that tag-schema.md is successfully parsed into non-empty enum sets., Verify that every campaign card in legendary-campaigns/cards passes schema…, Verify weighted score calculation against known score combinations., Verify that saturated patterns (P09, P11, P16) cap default originality at 7…, Verify all MOC index files exist and have non-empty markdown content. (+5 more)

### Community 37 - "properties"
Cohesion: 0.14
Nodes (14): type, maximum, minimum, type, additionalProperties, type, minItems, type (+6 more)

### Community 38 - "required"
Cohesion: 0.17
Nodes (13): accessibility_plan, arabic, brand, color_contrast, copy, critical_physics, originality, product (+5 more)

### Community 39 - "required"
Cohesion: 0.17
Nodes (13): benefit, heuristic, purpose, items, maxItems, type, items, type (+5 more)

### Community 40 - "properties"
Cohesion: 0.15
Nodes (13): type, pattern, type, properties, minLength, type, $ref, created_at (+5 more)

### Community 41 - "properties"
Cohesion: 0.15
Nodes (13): type, minLength, type, type, fingerprint, label, name, ref_id (+5 more)

### Community 42 - "enum"
Cohesion: 0.17
Nodes (12): ai_slop, annotation_mapping, arabic_rtl, collateral_change, edit_scope, prompt_execution, strategy, enum (+4 more)

### Community 43 - "required"
Cohesion: 0.17
Nodes (12): alignment_anchors, aspect_ratio, crop_logic, eye_path, grid_type, hero, negative_space, reading_direction (+4 more)

### Community 44 - "reads"
Cohesion: 0.17
Nodes (12): campaign_state, agent, description, type, writes, campaign-dna, prompt-compiler, agent (+4 more)

### Community 45 - "required"
Cohesion: 0.22
Nodes (10): key, value, reason, items, items, type, additionalProperties, required (+2 more)

### Community 46 - "ambiguity"
Cohesion: 0.17
Nodes (12): reasons, additionalProperties, properties, required, type, unresolved, ambiguity, reasons (+4 more)

### Community 47 - "properties"
Cohesion: 0.17
Nodes (12): properties, type, key, rationale, reason, remediation, rule, value (+4 more)

### Community 48 - "composition_state"
Cohesion: 0.18
Nodes (11): composition_state, agent, description, type, writes, composition-director, typography-director, agent (+3 more)

### Community 49 - "reference-memory.schema.json"
Cohesion: 0.18
Nodes (10): mixes, next_ref, schema_version, additionalProperties, $id, references, required, $schema (+2 more)

### Community 50 - "properties"
Cohesion: 0.18
Nodes (11): type, properties, type, type, background, foreground, middle_ground, secondary_mass (+3 more)

### Community 51 - "writes"
Cohesion: 0.20
Nodes (10): all_packets, qa_state.final_approval, session_id, task_type, agent, description, reads, type (+2 more)

### Community 52 - "required"
Cohesion: 0.20
Nodes (10): brief_accuracy, concept_strength, craft, cultural_fit, grouping_alignment, lighting_materials, marketing_clarity, platform_fit (+2 more)

### Community 53 - "required"
Cohesion: 0.20
Nodes (10): controlled_variables, crop_rules, image_treatment, lighting_family, locked_invariants, palette_roles, spacing_rhythm, typography_roles (+2 more)

### Community 54 - "required"
Cohesion: 0.20
Nodes (10): created_at, feedback, id, note, profile, signal, updated_at, required (+2 more)

### Community 55 - "enum"
Cohesion: 0.20
Nodes (10): exploration, quick, reference_replication, single_asset, taste_extraction, edit, review, task_type (+2 more)

### Community 56 - "type"
Cohesion: 0.15
Nodes (13): items, type, type, evidence, recommended_next, soft_warnings, unresolved, items (+5 more)

### Community 57 - "properties"
Cohesion: 0.17
Nodes (12): type, type, type, pattern, type, properties, decisions, from (+4 more)

### Community 58 - "type"
Cohesion: 0.20
Nodes (10): items, type, items, minItems, type, items, minItems, type (+2 more)

### Community 59 - "enum"
Cohesion: 0.22
Nodes (9): brand-guideline, design, image, other, video-frame, campaign, enum, type (+1 more)

### Community 60 - "reference-memory"
Cohesion: 0.22
Nodes (9): reference_records, taste_state.reference_memory, user_feedback, reference-memory, agent, description, reads, type (+1 more)

### Community 61 - "taste-engine"
Cohesion: 0.25
Nodes (9): references, taste_state, reads, taste-engine, agent, description, reads, type (+1 more)

### Community 62 - "properties"
Cohesion: 0.22
Nodes (9): items, type, minimum, type, properties, mixes, next_ref, schema_version (+1 more)

### Community 63 - "type"
Cohesion: 0.25
Nodes (9): items, type, minLength, type, anti_rules, tags, items, type (+1 more)

### Community 64 - "properties"
Cohesion: 0.22
Nodes (9): type, items, type, copy_risk, must_transform, protected_elements, items, type (+1 more)

### Community 65 - "applicability"
Cohesion: 0.22
Nodes (9): maximum, minimum, type, additionalProperties, type, applicability, scores, additionalProperties (+1 more)

### Community 66 - "brand-intelligence"
Cohesion: 0.25
Nodes (8): brand_assets, product_specs, agent, description, reads, type, writes, brand-intelligence

### Community 67 - "manipulation-director"
Cohesion: 0.25
Nodes (8): craft_state, craft_state.manipulation, agent, description, reads, type, writes, manipulation-director

### Community 68 - "enum"
Cohesion: 0.25
Nodes (8): custom, freeform-anchors, modular, radial-centered, single-axis, split-field, enum, grid_type

### Community 69 - "test_campaign_canon.py"
Cohesion: 0.36
Nodes (7): main(), Verify that saturated patterns P09, P11, and P16 are identified., Verify that the 571 campaign card library is present., Verify all 6 MOC files exist., test_campaign_cards_are_present_and_valid(), test_moc_index_files_are_accessible(), test_pattern_saturation_classification()

### Community 70 - "items"
Cohesion: 0.29
Nodes (8): items, type, additionalProperties, type, feedback, references, items, type

### Community 71 - "enum"
Cohesion: 0.29
Nodes (7): clarify, ready, reject, veto, status, enum, type

### Community 72 - "arabic-rtl-director"
Cohesion: 0.29
Nodes (7): composition_state.rtl_flow, typography_state.arabic_rtl, agent, description, type, writes, arabic-rtl-director

### Community 73 - "similarity_guard"
Cohesion: 0.29
Nodes (7): copy_risk, must_transform, protected_elements, similarity_guard, additionalProperties, required, type

### Community 74 - "photography-director"
Cohesion: 0.29
Nodes (7): craft_state.photography, photography-director, agent, description, reads, type, writes

### Community 75 - "enum"
Cohesion: 0.29
Nodes (7): generate, reference, edit, review, task_type, enum, manipulation

### Community 76 - "enum"
Cohesion: 0.38
Nodes (7): high, enum, low, medium, strength, enum, type

### Community 77 - "enum"
Cohesion: 0.29
Nodes (7): licensed, owned, public-reference, unknown, enum, type, ownership

### Community 78 - "enum"
Cohesion: 0.29
Nodes (7): mask, normalized, pixels, semantic, enum, type, annotation_space

### Community 79 - "visual-storytelling"
Cohesion: 0.29
Nodes (7): strategy_state.narrative_arc, visual-storytelling, agent, description, reads, type, writes

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

### Community 85 - "enum"
Cohesion: 0.33
Nodes (6): one, low, medium, enum, type, mutation_budget

### Community 86 - "source"
Cohesion: 0.33
Nodes (6): ownership, label, source, additionalProperties, required, type

### Community 87 - "visual-qa"
Cohesion: 0.33
Nodes (6): qa_state, visual-qa, agent, description, type, writes

### Community 88 - "insight-mining"
Cohesion: 0.33
Nodes (6): strategy_state.insight, agent, description, type, writes, insight-mining

### Community 89 - "validate_mesh.py"
Cohesion: 0.73
Nodes (5): check(), main(), validate_lock_precedence(), validate_routing_graph(), validate_schemas()

### Community 90 - "test_brand_activation.py"
Cohesion: 0.53
Nodes (5): classify_activation_utility(), main(), Classify activation as non_advertising vs execution based on the diagnostic…, test_activation_toolkit_references_exist(), test_non_advertising_diagnostic_differentiates_utility_from_execution()

### Community 91 - "campaign-canon/scripts/generate_links.py"
Cohesion: 0.53
Nodes (5): build_related_section(), main(), parse_frontmatter(), Path, update_card()

### Community 92 - "visual-dna.schema.json"
Cohesion: 0.33
Nodes (5): additionalProperties, $id, $schema, title, type

### Community 93 - "art-direction.schema.json"
Cohesion: 0.33
Nodes (5): additionalProperties, $id, $schema, title, type

### Community 94 - "creative-director/scripts/generate_links.py"
Cohesion: 0.53
Nodes (5): build_related_section(), main(), parse_frontmatter(), Path, update_card()

### Community 95 - "test_visual_storytelling.py"
Cohesion: 0.53
Nodes (5): get_emotion_tier_range(), main(), Return the allowed score range for emotional specificity tier., test_emotional_tier_scoring_bounds(), test_storytelling_references_exist()

### Community 96 - "validate_public_plugin.py"
Cohesion: 0.67
Nodes (5): check(), err(), main(), ok(), svg_size()

### Community 97 - "enum"
Cohesion: 0.40
Nodes (5): image-only, poster-ad-layout, small-text, typography_heavy, enum

### Community 98 - "requested_mutations"
Cohesion: 0.40
Nodes (5): minLength, requested_mutations, items, minItems, type

### Community 99 - "confidence"
Cohesion: 0.40
Nodes (5): description, maximum, minimum, type, confidence

### Community 100 - "validate_agent_configs.py"
Cohesion: 0.90
Nodes (4): check(), main(), validate_agent(), validate_config()

### Community 101 - "validate_skill_interfaces.py"
Cohesion: 0.80
Nodes (4): check(), main(), parse_frontmatter(), validate_skill()

### Community 102 - "alignment_anchors"
Cohesion: 0.40
Nodes (5): items, maxItems, minItems, type, alignment_anchors

### Community 103 - "design_lint.py"
Cohesion: 0.70
Nodes (4): has_exception(), lint(), main(), norm_words()

### Community 104 - "jobs"
Cohesion: 0.40
Nodes (5): items, minItems, type, uniqueItems, jobs

### Community 105 - "taste_merge.py"
Cohesion: 0.70
Nodes (4): build(), find(), load_json(), main()

### Community 106 - "test_contracts.py"
Cohesion: 0.83
Nodes (3): load_schema(), main(), validates()

### Community 107 - "acceptance_checks"
Cohesion: 0.50
Nodes (4): items, minItems, type, acceptance_checks

### Community 108 - "iteration"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, iteration

### Community 109 - "priority"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, priority

### Community 110 - "focal_points"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, focal_points

### Community 111 - "restraints"
Cohesion: 0.50
Nodes (4): restraints, items, minItems, type

### Community 112 - "style_families"
Cohesion: 0.50
Nodes (4): style_families, items, maxItems, type

### Community 113 - "prompt_lint.py"
Cohesion: 0.83
Nodes (3): active_term(), lint(), main()

### Community 114 - "signature"
Cohesion: 0.50
Nodes (4): anyOf, signature, additionalProperties, type

### Community 116 - "forbidden_mutations"
Cohesion: 0.67
Nodes (3): items, type, forbidden_mutations

### Community 117 - "geometry_locks"
Cohesion: 0.67
Nodes (3): items, type, geometry_locks

### Community 118 - "style_locks"
Cohesion: 0.67
Nodes (3): style_locks, items, type

### Community 120 - "controlled_variables"
Cohesion: 0.67
Nodes (3): minItems, type, controlled_variables

### Community 121 - "crop_rules"
Cohesion: 0.67
Nodes (3): items, type, crop_rules

### Community 122 - "spacing_rhythm"
Cohesion: 0.67
Nodes (3): spacing_rhythm, minLength, type

### Community 123 - "typography_roles"
Cohesion: 0.67
Nodes (3): typography_roles, items, type

### Community 124 - "aspect_ratio"
Cohesion: 0.67
Nodes (3): minLength, type, aspect_ratio

### Community 125 - "crop_logic"
Cohesion: 0.67
Nodes (3): minLength, type, crop_logic

### Community 126 - "eye_path"
Cohesion: 0.67
Nodes (3): minLength, type, eye_path

### Community 127 - "hero"
Cohesion: 0.67
Nodes (3): minLength, type, hero

### Community 128 - "negative_space"
Cohesion: 0.67
Nodes (3): minLength, type, negative_space

### Community 129 - "supporting_information"
Cohesion: 0.67
Nodes (3): supporting_information, items, type

### Community 130 - "cultural_constraints"
Cohesion: 0.67
Nodes (3): items, type, cultural_constraints

### Community 131 - "exact_copy"
Cohesion: 0.67
Nodes (3): items, type, exact_copy

### Community 132 - "locked_assets"
Cohesion: 0.67
Nodes (3): items, type, locked_assets

### Community 133 - "non_goals"
Cohesion: 0.67
Nodes (3): items, type, non_goals

### Community 134 - "platform"
Cohesion: 0.67
Nodes (3): minLength, type, platform

### Community 135 - "primary_message"
Cohesion: 0.67
Nodes (3): minLength, type, primary_message

### Community 136 - "proof"
Cohesion: 0.67
Nodes (3): items, type, proof

### Community 137 - "references"
Cohesion: 0.67
Nodes (3): references, items, type

## Knowledge Gaps
- **736 isolated node(s):** `$schema`, `title`, `type`, `locks`, `taste_state` (+731 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **12 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `enum` connect `enum` to `jobs`, `enum`, `required`?**
  _High betweenness centrality (0.207) - this node is a cross-community bridge._
- **Why does `enum` connect `enum` to `enum`, `enum`?**
  _High betweenness centrality (0.192) - this node is a cross-community bridge._
- **Why does `properties` connect `properties` to `cultural_constraints`, `exact_copy`, `locked_assets`, `non_goals`, `platform`, `primary_message`, `proof`, `references`, `enum`, `audience`, `awareness`, `type`, `language`, `obstacle_or_objection`, `creative-brief.schema.json`?**
  _High betweenness centrality (0.172) - this node is a cross-community bridge._
- **What connects `$schema`, `title`, `type` to the rest of the system?**
  _736 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `enum` be split into smaller, more focused modules?**
  _Cohesion score 0.04336734693877551 - nodes in this community are weakly interconnected._
- **Should `enum` be split into smaller, more focused modules?**
  _Cohesion score 0.0700354609929078 - nodes in this community are weakly interconnected._
- **Should `properties` be split into smaller, more focused modules?**
  _Cohesion score 0.0425531914893617 - nodes in this community are weakly interconnected._