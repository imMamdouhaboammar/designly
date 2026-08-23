# Graph Report - .  (2026-08-23)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 1443 nodes · 1742 edges · 159 communities (136 shown, 23 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 17 edges (avg confidence: 0.54)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- enum
- properties
- properties
- taste-mix.schema.json
- properties
- enum
- skills/creative-director/scripts/generate_mocs.py
- properties
- MeshRouter
- required
- revision_routes
- properties
- properties
- reference_memory.py
- properties
- enum
- properties
- properties
- properties
- properties
- sanitize_edit.py
- reads
- enum
- requested_mutations
- required
- required
- required
- type
- properties
- required
- properties
- properties
- test_creative_director.py
- properties
- type
- required
- required
- composition-director
- properties
- type
- properties
- enum
- ambiguity
- properties
- properties
- properties
- writes
- enum
- reference-memory.schema.json
- applicability
- reads
- required
- required
- required
- required
- nodes
- type
- required
- strategy_state
- reference-memory
- properties
- jobs
- brand-intelligence
- enum
- items
- required
- creative-brief.schema.json
- design-context.schema.json
- items
- enum
- arabic-rtl-director
- similarity_guard
- photography-director
- enum
- enum
- enum
- type
- parse_schema
- enum
- required
- manipulation-director
- prompt-compiler
- enum
- visual-qa
- validate_mesh.py
- visual-dna.schema.json
- art-direction.schema.json
- skills/creative-director/scripts/generate_links.py
- visual-review.schema.json
- validate_public_plugin.py
- typography-director
- confidence
- validate_agent_configs.py
- validate_skill_interfaces.py
- alignment_anchors
- design_lint.py
- taste_merge.py
- test_contracts.py
- locks
- priority
- focal_points
- intent
- restraints
- prompt_lint.py
- acceptance_checks
- properties
- test_skill_catalog.py
- forbidden_mutations
- iteration
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
- signature
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
- awareness
- desired_action
- language
- obstacle_or_objection
- Path
- Path
- Path
- geometry_locks
- identity_locks
- platform

## God Nodes (most connected - your core abstractions)
1. `enum` - 21 edges
2. `enum` - 21 edges
3. `required` - 19 edges
4. `enum` - 17 edges
5. `required` - 17 edges
6. `revision_routes` - 17 edges
7. `nodes` - 16 edges
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
- `required` --extends--> `reason`  [EXTRACTED]
  skills/composition-director/schemas/art-direction.schema.json → shared/contracts/design-lock.schema.json

## Import Cycles
- None detected.

## Communities (159 total, 23 thin omitted)

### Community 0 - "enum"
Cohesion: 0.06
Nodes (56): arabic_visual_director, brand_guardian, craft_director, edit-sanitizer, reference-memory, strategy_planner, structure_critic, taste_analyst (+48 more)

### Community 1 - "properties"
Cohesion: 0.05
Nodes (44): accent_strategy, alignment, class, exact_copy_locked, ltr, mixed, roles, rtl (+36 more)

### Community 2 - "properties"
Cohesion: 0.05
Nodes (43): height, kind, string, width, maximum, minimum, type, type (+35 more)

### Community 3 - "taste-mix.schema.json"
Cohesion: 0.06
Nodes (36): ref, additionalProperties, additionalProperties, properties, required, type, items, type (+28 more)

### Community 4 - "properties"
Cohesion: 0.06
Nodes (35): brand_rule, director, immutable, lock_id, locked_by, locked_value, priority, safety_gate (+27 more)

### Community 5 - "enum"
Cohesion: 0.07
Nodes (31): brand-guideline, design, exploration, generate, image, image-only, other, poster-ad-layout (+23 more)

### Community 6 - "skills/creative-director/scripts/generate_mocs.py"
Cohesion: 0.15
Nodes (27): format_card_line(), generate_moc_budget(), generate_moc_emotion(), generate_moc_format(), generate_moc_index(), generate_moc_industry(), generate_moc_pattern(), get() (+19 more)

### Community 7 - "properties"
Cohesion: 0.08
Nodes (26): licensed, owned, ownership, public-reference, unknown, type, label, minLength (+18 more)

### Community 8 - "MeshRouter"
Cohesion: 0.12
Nodes (16): check(), main(), run_conflict_evals(), main(), test_ai_slop_vetoes(), test_category_floors(), test_targeted_revision_routing(), main() (+8 more)

### Community 9 - "required"
Cohesion: 0.09
Nodes (22): acceptance_checks, annotation_space, edit_id, execution_allowed, forbidden_mutations, geometry_locks, identity_locks, iteration (+14 more)

### Community 10 - "revision_routes"
Cohesion: 0.09
Nodes (22): name, primary_orchestrator, revision_routes, ai_slop, annotation_mapping, arabic_rtl, brand_fidelity, collateral_change (+14 more)

### Community 11 - "properties"
Cohesion: 0.10
Nodes (21): key_direction, shadow_behavior, softness, minLength, type, additionalProperties, properties, required (+13 more)

### Community 12 - "properties"
Cohesion: 0.11
Nodes (21): items, type, items, type, type, items, type, items (+13 more)

### Community 13 - "reference_memory.py"
Cohesion: 0.33
Nodes (19): blank(), cmd_add(), cmd_export(), cmd_feedback(), cmd_forget(), cmd_get(), cmd_init(), cmd_list() (+11 more)

### Community 14 - "properties"
Cohesion: 0.11
Nodes (19): creative_territory, visual_proof, visual_proposition, type, additionalProperties, properties, required, type (+11 more)

### Community 15 - "enum"
Cohesion: 0.11
Nodes (19): hard_gate, major, minor, severity, enum, type, critical, severity (+11 more)

### Community 16 - "properties"
Cohesion: 0.11
Nodes (19): type, type, type, type, properties, camera_family, image_treatment, lighting_family (+11 more)

### Community 17 - "properties"
Cohesion: 0.11
Nodes (18): one_second_read, primary, secondary, additionalProperties, properties, required, type, minLength (+10 more)

### Community 18 - "properties"
Cohesion: 0.12
Nodes (16): pattern, type, type, properties, edit_id, execution_allowed, protected_regions, requires_arabic_review (+8 more)

### Community 19 - "properties"
Cohesion: 0.11
Nodes (18): minLength, type, minLength, type, minLength, type, properties, minLength (+10 more)

### Community 20 - "sanitize_edit.py"
Cohesion: 0.27
Nodes (15): base_request(), expect(), main(), schema_valid(), _base_result(), _fail(), main(), _mutation_conflict() (+7 more)

### Community 21 - "reads"
Cohesion: 0.18
Nodes (17): brand_state, campaign_state, composition_state, craft_state, edit_request, edit_state, generation_state.approved_checkpoint, locks (+9 more)

### Community 22 - "enum"
Cohesion: 0.14
Nodes (16): annotation_guided, background_extend, composition-revision, concept-revision, inpaint, object_replace, type-color-revision, visual-polish (+8 more)

### Community 23 - "requested_mutations"
Cohesion: 0.40
Nodes (5): minLength, requested_mutations, items, minItems, type

### Community 24 - "required"
Cohesion: 0.13
Nodes (14): anti_rules, observations, profile_version, rules, signature, similarity_guard, source, additionalProperties (+6 more)

### Community 25 - "required"
Cohesion: 0.13
Nodes (14): category_floor_failed, defect_description, failing_dimension, origin_packet_id, required_delta, revision_id, source_qa, target_node (+6 more)

### Community 26 - "required"
Cohesion: 0.13
Nodes (14): decisions, from, hard_vetoes, packet_id, recommended_next, soft_warnings, to, additionalProperties (+6 more)

### Community 27 - "type"
Cohesion: 0.13
Nodes (17): geometry, region_id, semantic_target, target_id, additionalProperties, required, type, confidence (+9 more)

### Community 28 - "properties"
Cohesion: 0.13
Nodes (15): type, type, properties, minLength, type, benefit, heuristic, name (+7 more)

### Community 29 - "required"
Cohesion: 0.15
Nodes (14): dimension, interpretation, strength, transferable, additionalProperties, required, evidence, job (+6 more)

### Community 30 - "properties"
Cohesion: 0.14
Nodes (14): minLength, type, type, properties, type, type, aspect_ratio, background (+6 more)

### Community 31 - "properties"
Cohesion: 0.14
Nodes (14): type, type, minLength, type, type, type, properties, audience (+6 more)

### Community 32 - "test_creative_director.py"
Cohesion: 0.21
Nodes (13): calculate_weighted_score(), main(), Calculate weighted score from the 6 Cannes/D&AD calibration criteria., Verify that tag-schema.md is successfully parsed into non-empty enum sets., Verify that every campaign card in legendary-campaigns/cards passes schema…, Verify weighted score calculation against known score combinations., Verify that saturated patterns (P09, P11, P16) cap default originality at 7…, Verify all MOC index files exist and have non-empty markdown content. (+5 more)

### Community 33 - "properties"
Cohesion: 0.14
Nodes (14): type, maximum, minimum, type, additionalProperties, type, const, properties (+6 more)

### Community 34 - "type"
Cohesion: 0.18
Nodes (12): items, type, minLength, type, items, type, anti_rules, must_transform (+4 more)

### Community 35 - "required"
Cohesion: 0.17
Nodes (13): accessibility_plan, arabic, brand, color_contrast, copy, critical_physics, originality, product (+5 more)

### Community 36 - "required"
Cohesion: 0.17
Nodes (13): benefit, heuristic, purpose, items, maxItems, type, items, type (+5 more)

### Community 37 - "composition-director"
Cohesion: 0.17
Nodes (13): references, taste_state, agent, description, reads, type, composition-director, taste-engine (+5 more)

### Community 38 - "properties"
Cohesion: 0.15
Nodes (13): type, type, type, type, type, properties, audience, brand_state (+5 more)

### Community 39 - "type"
Cohesion: 0.15
Nodes (13): items, type, type, evidence, recommended_next, soft_warnings, unresolved, items (+5 more)

### Community 40 - "properties"
Cohesion: 0.15
Nodes (13): type, pattern, type, properties, minLength, type, $ref, created_at (+5 more)

### Community 41 - "enum"
Cohesion: 0.17
Nodes (12): ai_slop, annotation_mapping, arabic_rtl, collateral_change, edit_scope, prompt_execution, strategy, enum (+4 more)

### Community 42 - "ambiguity"
Cohesion: 0.17
Nodes (12): reasons, additionalProperties, properties, required, type, unresolved, ambiguity, reasons (+4 more)

### Community 43 - "properties"
Cohesion: 0.17
Nodes (12): type, type, type, pattern, type, properties, decisions, from (+4 more)

### Community 44 - "properties"
Cohesion: 0.17
Nodes (12): properties, type, key, rationale, reason, remediation, rule, value (+4 more)

### Community 45 - "properties"
Cohesion: 0.17
Nodes (12): minLength, type, type, properties, minLength, type, minLength, type (+4 more)

### Community 46 - "writes"
Cohesion: 0.18
Nodes (11): all_packets, brief, qa_state.final_approval, session_id, task_type, agent, description, reads (+3 more)

### Community 47 - "enum"
Cohesion: 0.18
Nodes (11): brand-behavior, camera, crop, cultural-direction, grid, material, restraint, spacing (+3 more)

### Community 48 - "reference-memory.schema.json"
Cohesion: 0.18
Nodes (10): mixes, next_ref, schema_version, additionalProperties, $id, references, required, $schema (+2 more)

### Community 49 - "applicability"
Cohesion: 0.22
Nodes (9): maximum, minimum, type, additionalProperties, type, applicability, scores, additionalProperties (+1 more)

### Community 50 - "reads"
Cohesion: 0.24
Nodes (10): audience, cultural_context, objective, reads, agent, description, reads, type (+2 more)

### Community 51 - "required"
Cohesion: 0.20
Nodes (10): brief_accuracy, concept_strength, craft, cultural_fit, grouping_alignment, lighting_materials, marketing_clarity, platform_fit (+2 more)

### Community 52 - "required"
Cohesion: 0.20
Nodes (10): controlled_variables, crop_rules, image_treatment, lighting_family, locked_invariants, palette_roles, spacing_rhythm, typography_roles (+2 more)

### Community 53 - "required"
Cohesion: 0.20
Nodes (10): created_at, feedback, id, note, profile, signal, updated_at, required (+2 more)

### Community 54 - "required"
Cohesion: 0.22
Nodes (10): key, value, reason, items, items, type, additionalProperties, required (+2 more)

### Community 55 - "nodes"
Cohesion: 0.20
Nodes (10): agent, description, type, writes, agent, description, type, nodes (+2 more)

### Community 56 - "type"
Cohesion: 0.20
Nodes (10): items, type, items, minItems, type, items, minItems, type (+2 more)

### Community 57 - "required"
Cohesion: 0.22
Nodes (9): alignment_anchors, aspect_ratio, crop_logic, eye_path, grid_type, hero, negative_space, reading_direction (+1 more)

### Community 58 - "strategy_state"
Cohesion: 0.28
Nodes (9): desired_action, primary_message, strategy_state, writes, agent, description, type, writes (+1 more)

### Community 59 - "reference-memory"
Cohesion: 0.22
Nodes (9): reference_records, taste_state.reference_memory, user_feedback, reference-memory, agent, description, reads, type (+1 more)

### Community 60 - "properties"
Cohesion: 0.22
Nodes (9): items, type, minimum, type, properties, mixes, next_ref, schema_version (+1 more)

### Community 61 - "jobs"
Cohesion: 0.40
Nodes (5): items, minItems, type, uniqueItems, jobs

### Community 62 - "brand-intelligence"
Cohesion: 0.25
Nodes (8): brand_assets, product_specs, agent, description, reads, type, writes, brand-intelligence

### Community 63 - "enum"
Cohesion: 0.25
Nodes (8): custom, freeform-anchors, modular, radial-centered, single-axis, split-field, enum, grid_type

### Community 64 - "items"
Cohesion: 0.25
Nodes (8): family, severity, items, additionalProperties, required, type, evidence, items

### Community 65 - "required"
Cohesion: 0.25
Nodes (8): intent, restraints, composition, hierarchy, color, required, concept, lighting

### Community 66 - "creative-brief.schema.json"
Cohesion: 0.25
Nodes (7): platform, additionalProperties, $id, required, $schema, title, type

### Community 67 - "design-context.schema.json"
Cohesion: 0.25
Nodes (7): additionalProperties, locks, taste_state, required, $schema, title, type

### Community 68 - "items"
Cohesion: 0.29
Nodes (8): items, type, additionalProperties, type, feedback, references, items, type

### Community 69 - "enum"
Cohesion: 0.29
Nodes (7): clarify, ready, reject, veto, status, enum, type

### Community 70 - "arabic-rtl-director"
Cohesion: 0.29
Nodes (7): composition_state.rtl_flow, typography_state.arabic_rtl, agent, description, type, writes, arabic-rtl-director

### Community 71 - "similarity_guard"
Cohesion: 0.29
Nodes (7): copy_risk, must_transform, protected_elements, similarity_guard, additionalProperties, required, type

### Community 72 - "photography-director"
Cohesion: 0.29
Nodes (7): craft_state.photography, photography-director, agent, description, reads, type, writes

### Community 73 - "enum"
Cohesion: 0.29
Nodes (7): fail, na, pass, enum, additionalProperties, type, hard_gates

### Community 74 - "enum"
Cohesion: 0.18
Nodes (13): high, enum, type, low, medium, copy_risk, protected_elements, strength (+5 more)

### Community 75 - "enum"
Cohesion: 0.29
Nodes (7): mask, normalized, pixels, semantic, enum, type, annotation_space

### Community 76 - "type"
Cohesion: 0.29
Nodes (7): items, type, type, constraints, supporting_information, items, type

### Community 77 - "parse_schema"
Cohesion: 0.43
Nodes (6): main(), parse_schema(), Path, Validate a single card's frontmatter. Returns list of error strings., Parse tag-schema.md and return field -> set of allowed enum values., validate_card()

### Community 78 - "enum"
Cohesion: 0.33
Nodes (6): active, archived, canonical, status, enum, type

### Community 79 - "required"
Cohesion: 0.33
Nodes (6): applicability, defects, hard_gates, scores, slop_findings, required

### Community 80 - "manipulation-director"
Cohesion: 0.33
Nodes (6): craft_state.manipulation, agent, description, type, writes, manipulation-director

### Community 81 - "prompt-compiler"
Cohesion: 0.33
Nodes (6): generation_state, prompt-compiler, agent, description, type, writes

### Community 82 - "enum"
Cohesion: 0.33
Nodes (6): one, low, medium, enum, type, mutation_budget

### Community 83 - "visual-qa"
Cohesion: 0.33
Nodes (6): qa_state, visual-qa, agent, description, type, writes

### Community 84 - "validate_mesh.py"
Cohesion: 0.73
Nodes (5): check(), main(), validate_lock_precedence(), validate_routing_graph(), validate_schemas()

### Community 85 - "visual-dna.schema.json"
Cohesion: 0.33
Nodes (5): additionalProperties, $id, $schema, title, type

### Community 86 - "art-direction.schema.json"
Cohesion: 0.33
Nodes (5): additionalProperties, $id, $schema, title, type

### Community 87 - "skills/creative-director/scripts/generate_links.py"
Cohesion: 0.53
Nodes (5): build_related_section(), main(), parse_frontmatter(), Path, update_card()

### Community 88 - "visual-review.schema.json"
Cohesion: 0.33
Nodes (5): additionalProperties, $id, $schema, title, type

### Community 89 - "validate_public_plugin.py"
Cohesion: 0.67
Nodes (5): check(), err(), main(), ok(), svg_size()

### Community 90 - "typography-director"
Cohesion: 0.40
Nodes (5): typography-director, agent, description, reads, type

### Community 91 - "confidence"
Cohesion: 0.40
Nodes (5): description, maximum, minimum, type, confidence

### Community 92 - "validate_agent_configs.py"
Cohesion: 0.90
Nodes (4): check(), main(), validate_agent(), validate_config()

### Community 93 - "validate_skill_interfaces.py"
Cohesion: 0.80
Nodes (4): check(), main(), parse_frontmatter(), validate_skill()

### Community 94 - "alignment_anchors"
Cohesion: 0.40
Nodes (5): items, maxItems, minItems, type, alignment_anchors

### Community 95 - "design_lint.py"
Cohesion: 0.70
Nodes (4): has_exception(), lint(), main(), norm_words()

### Community 96 - "taste_merge.py"
Cohesion: 0.70
Nodes (4): build(), find(), load_json(), main()

### Community 97 - "test_contracts.py"
Cohesion: 0.83
Nodes (3): load_schema(), main(), validates()

### Community 98 - "locks"
Cohesion: 0.50
Nodes (4): $ref, items, type, locks

### Community 99 - "priority"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, priority

### Community 100 - "focal_points"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, focal_points

### Community 101 - "intent"
Cohesion: 0.50
Nodes (4): additionalProperties, required, type, intent

### Community 102 - "restraints"
Cohesion: 0.50
Nodes (4): restraints, items, minItems, type

### Community 103 - "prompt_lint.py"
Cohesion: 0.83
Nodes (3): active_term(), lint(), main()

### Community 104 - "acceptance_checks"
Cohesion: 0.50
Nodes (4): items, minItems, type, acceptance_checks

### Community 105 - "properties"
Cohesion: 0.33
Nodes (6): type, properties, defects, revision_mode, slop_findings, type

### Community 107 - "forbidden_mutations"
Cohesion: 0.67
Nodes (3): items, type, forbidden_mutations

### Community 108 - "iteration"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, iteration

### Community 109 - "controlled_variables"
Cohesion: 0.67
Nodes (3): minItems, type, controlled_variables

### Community 110 - "crop_rules"
Cohesion: 0.67
Nodes (3): items, type, crop_rules

### Community 111 - "spacing_rhythm"
Cohesion: 0.67
Nodes (3): spacing_rhythm, minLength, type

### Community 112 - "typography_roles"
Cohesion: 0.67
Nodes (3): typography_roles, items, type

### Community 113 - "composition"
Cohesion: 0.67
Nodes (3): additionalProperties, type, composition

### Community 114 - "crop_logic"
Cohesion: 0.67
Nodes (3): minLength, type, crop_logic

### Community 115 - "eye_path"
Cohesion: 0.67
Nodes (3): minLength, type, eye_path

### Community 116 - "hero"
Cohesion: 0.67
Nodes (3): minLength, type, hero

### Community 117 - "negative_space"
Cohesion: 0.67
Nodes (3): minLength, type, negative_space

### Community 118 - "cultural_constraints"
Cohesion: 0.67
Nodes (3): items, type, cultural_constraints

### Community 119 - "exact_copy"
Cohesion: 0.67
Nodes (3): items, type, exact_copy

### Community 120 - "locked_assets"
Cohesion: 0.67
Nodes (3): items, type, locked_assets

### Community 121 - "non_goals"
Cohesion: 0.67
Nodes (3): items, type, non_goals

### Community 122 - "platform"
Cohesion: 0.67
Nodes (3): minLength, type, platform

### Community 123 - "primary_message"
Cohesion: 0.67
Nodes (3): minLength, type, primary_message

### Community 124 - "proof"
Cohesion: 0.67
Nodes (3): items, type, proof

### Community 125 - "references"
Cohesion: 0.67
Nodes (3): references, items, type

### Community 132 - "signature"
Cohesion: 0.50
Nodes (4): anyOf, signature, additionalProperties, type

### Community 156 - "geometry_locks"
Cohesion: 0.67
Nodes (3): items, type, geometry_locks

### Community 157 - "identity_locks"
Cohesion: 0.67
Nodes (3): items, type, identity_locks

## Knowledge Gaps
- **718 isolated node(s):** `$schema`, `title`, `type`, `locks`, `taste_state` (+713 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **23 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `enum` connect `enum` to `jobs`, `required`, `required`, `enum`?**
  _High betweenness centrality (0.206) - this node is a cross-community bridge._
- **Why does `properties` connect `properties` to `properties`, `required`, `intent`, `restraints`, `properties`, `properties`, `composition`, `properties`, `art-direction.schema.json`?**
  _High betweenness centrality (0.187) - this node is a cross-community bridge._
- **What connects `$schema`, `title`, `type` to the rest of the system?**
  _718 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `enum` be split into smaller, more focused modules?**
  _Cohesion score 0.05714285714285714 - nodes in this community are weakly interconnected._
- **Should `properties` be split into smaller, more focused modules?**
  _Cohesion score 0.049682875264270614 - nodes in this community are weakly interconnected._
- **Should `properties` be split into smaller, more focused modules?**
  _Cohesion score 0.047619047619047616 - nodes in this community are weakly interconnected._
- **Should `taste-mix.schema.json` be split into smaller, more focused modules?**
  _Cohesion score 0.05555555555555555 - nodes in this community are weakly interconnected._