# Designly Prompt Playground

<p>
  <img src="../../../assets/badges/prompt-playground.svg" alt="Prompt Playground" />
  <img src="../../../assets/badges/prompts.svg" alt="20 Prompt Cards" />
  <img src="../../../assets/badges/skills.svg" alt="21 Skills" />
  <img src="../../../assets/badges/arabic-rtl.svg" alt="Arabic RTL" />
  <img src="../../../assets/badges/ai-film.svg" alt="AI Film" />
  <img src="../../../assets/badges/visual-qa.svg" alt="Visual QA" />
</p>

A copy-first onboarding surface for learning Designly by using it.

The Playground does not explain the 21 Skills as a catalog first. It turns capabilities into small, observable jobs. Each card gives the user a prompt they can paste into ChatGPT with `@Designly`, a concrete result to inspect, and the specialist Skills that should become visible through the work.

## Product rule

Every card must pass four checks:

1. **Copyable**: usable as-is with no setup beyond an optional attachment.
2. **Observable**: the result demonstrates a capability, not merely describes it.
3. **Teachable**: after the result, Designly briefly names what it did and which Skills mattered.
4. **Expandable**: the user can continue from the result into a deeper Designly workflow.

When presenting cards in chat, show 3 to 6 cards at a time unless the user explicitly asks for the full catalog. Put the copyable prompt first, then one short line describing what the user will learn. Do not dump internal architecture unless asked.

## Start here

### 1. See Designly think like an art director

**Copy prompt**

```text
@Designly Take this simple brief: "Launch a premium sparkling water for people who are bored with wellness clichés." Show me 3 genuinely different creative directions. For each direction, find the human or category tension, explain the core idea in one sentence, define the visual territory, and score it using your creative-direction criteria. Then choose one direction and turn it into a polished key-visual art direction spec. At the end, tell me which Designly Skills did the important work and why.
```

**Shows**: insight mining, creative direction, campaign canon, composition, image direction, QA.

### 2. Turn a reference into reusable taste rules

**Copy prompt**

```text
@Designly Analyze the reference image I attached. Do not copy the subject or layout literally. Extract the transferable taste rules: composition, lighting, material feel, palette behavior, typography relationship, negative space, visual tension, and what makes the reference feel expensive or distinctive. Save those reusable rules in Reference Memory under a stable REF-#### ID and show me the ID plus a one-line prompt I could use in a later chat to recall it. Then use the saved rules to create a completely new visual direction for a different brand category. Finish by showing me what came from Taste Engine, Reference Memory, Composition, Photography, and Brand Intelligence.
```

**Shows**: taste engine, reference memory, reference deconstruction, composition, photography, brand intelligence.

### 3. Build a campaign key visual from a raw brief

**Copy prompt**

```text
@Designly I need a campaign key visual for a fictional event company called NORTH. The message is: "We make complex live events feel perfectly controlled." Do the full Designly process: clarify the communication job from the information available, find a useful tension, generate structurally different concepts using SIT/TRIZ or another appropriate method, reject weak or familiar routes, select the strongest concept, define composition and photographic treatment, compile the final image-generation direction, then run Visual QA on the result or spec. Show me the decisions, not generic brainstorming.
```

**Shows**: end-to-end orchestration and quality gates.

### 4. Design Arabic-first, not translated-left-to-right

**Copy prompt**

```text
@Designly Create an Arabic-first social poster for the message: "فكرتك تبدأ من هنا". Treat Arabic as the primary visual language. Build the hierarchy, reading gravity, line breaks, spacing, focal point, and composition from right to left. Keep the Arabic copy exact. Explain the RTL decisions, then produce the final art direction and image-generation prompt. Before finishing, run an Arabic glyph and RTL QA pass and list any risk you would refuse to ship.
```

**Shows**: Arabic RTL direction, typography, composition, exact-copy gates, visual QA.

### 5. Make a believable manipulation composite

**Copy prompt**

```text
@Designly Create a manipulation concept where a giant luxury wristwatch appears physically integrated into a real city plaza as a temporary public installation. I want the result to feel photographed, not pasted. Work through perspective, scale references, lens choice, contact shadows, occlusion, reflections, material response, ambient light, human scale, and depth. Then compile the final image prompt and give me a physical-believability checklist before execution.
```

**Shows**: manipulation physics, photography direction, composition, prompt compilation.

### 6. Direct a 15-second AI film

**Copy prompt**

```text
@Designly Direct a 15-second cinematic film for a premium coffee brand around the idea "the quiet minute before the day begins." Build the emotional arc first, then create the shot sequence using your video dramaturgy method and Walter Murch priorities. Give every shot a precise visual job, camera behavior, performance note, lighting state, continuity requirement, transition logic, and generation instruction for the best-fitting supported video model. Finish with a continuity and edit-rhythm QA pass.
```

**Shows**: visual storytelling, video director, dramaturgy, image keyframes, continuity.

## Learn one capability by doing it

### 7. Consumer tension and insight mining

```text
@Designly Teach me your Insight Mining capability by doing it on this category: food-delivery apps. Do not give me a theory lecture first. Find cultural, category, and human tensions, run JTBD and the Pollard-style problem/insight/advantage/strategy logic, distinguish observation from insight, then show me which insight is strongest and how it changes the creative brief. End with a short explanation of the method I just watched you use.
```

### 8. Cannes-calibrated ideation

```text
@Designly Teach me Creative Director by doing it. Brief: convince young professionals to take a real lunch break instead of eating at their desks. Generate ideas using at least three structurally different ideation methods, mark the obvious warm-up ideas, push past them, score the stronger ideas for originality, strategic fit, emotional response, feasibility, scalability, and simplicity, then improve the best idea until it clears your quality threshold.
```

### 9. Campaign canon without copying famous work

```text
@Designly Use Campaign Canon as an anti-copy tool on this brief: launch a new running shoe around injury prevention. Show me the familiar campaign patterns this category is likely to fall into, explain which patterns are saturated, identify the white-space opportunity, then propose 3 concept territories that deliberately avoid derivative routes. I want to see how the canon changes the ideas rather than a list of famous campaigns.
```

### 10. Brand activation that works without an ad

```text
@Designly Create a non-advertising brand activation for a sunscreen brand. Apply the test: if the campaign media disappears, the activation should still be useful or meaningful. Generate several routes across utility, experiential, ambient, or public participation, reject stunts that are just photo opportunities, then develop the strongest route into a one-page activation concept with mechanism, audience behavior, operational reality, and measurement.
```

### 11. Composition before decoration

```text
@Designly Teach me Composition Director on a fictional 4:5 product poster. The poster must contain one product bottle, one six-word headline, one supporting line, and one CTA. Show me 3 layout structures, explain focal anchors, eye path, negative space, crop logic, hierarchy, and text zones, then select one and describe it precisely enough that another designer could rebuild it. Do not discuss surface styling until the structure is locked.
```

### 12. Photography direction that specifies real optics

```text
@Designly Art-direct a premium skincare packshot as if you are briefing a real photographer. Specify focal length, camera height and distance, aperture intent, key/fill/rim relationship, light size and direction, shadow softness, surface material, reflections, background depth, color temperature, and the reason for each choice. Then translate that photographic direction into a model-ready image prompt without losing the physical logic.
```

### 13. Image model physics comparison

```text
@Designly Take one visual idea: "a translucent perfume bottle on black volcanic glass at blue hour." Show me how you would direct the same image differently for GPT Image 2 versus Nano Banana. Keep the art direction constant but adapt the instruction structure to each model's preferred prompting behavior. Explain only the differences that materially affect the result, then give me both copy-ready prompts.
```

### 14. Bounded image correction without collateral drift

```text
@Designly I attached an existing design. Change only the product label text to "NOVA" and keep everything else unchanged. Before editing, create a strict change-versus-preserve contract, identify protected regions and possible collateral risks, sanitize the edit request, then give the execution instruction. After the edit, inspect whether anything outside the intended target drifted. If it did, reject the result and route the correction from the original source rather than from the failed edit.
```

### 15. Multi-asset campaign DNA

```text
@Designly Build a visual DNA for a 5-post social campaign about a new design conference. I want all posts to feel unmistakably related without becoming five copies of the same layout. Define the invariant DNA, the allowed variation axes, typography behavior, palette behavior, image treatment, recurring structural cue, and what must deliberately change from asset to asset. Then outline five distinct posts and run a continuity check.
```

### 16. Critique a design without vague taste language

```text
@Designly Review the design I attached as an independent Visual QA reviewer. Do not start by redesigning it. Score communication accuracy, concept strength, composition, typography, brand fidelity, craft realism, accessibility, and AI-slop risks. Separate hard failures from taste preferences. Identify the single responsible specialist for each failing dimension, then give me the smallest revision sequence that would materially improve the work.
```

## Advanced combinations

### 17. Reference to campaign, not reference to imitation

```text
@Designly I attached 3 references and a short campaign brief. First extract only transferable rules from the references and identify where they conflict. Then find the campaign insight, create a new concept that could not be mistaken for any of the references, define a visual system that uses the extracted taste without copying composition or subject matter, and produce one hero key visual plus rules for three follow-up assets. End with an anti-derivative QA check.
```

### 18. Arabic premium brand launch

```text
@Designly Build a premium Arabic-first launch direction for a Saudi legal consultancy. The communication job is trust through precision, not prestige clichés. Develop the insight and concept, audit likely category clichés, create an Arabic typography and RTL composition direction, define photography and materials, preserve logo fidelity, then produce a hero visual specification and two supporting social adaptations. Run both Arabic QA and brand QA before signoff.
```

### 19. From campaign idea to 15-second film

```text
@Designly Brief: a travel brand wants to say "the best part of a trip begins before you arrive." First generate and score campaign ideas, choose one strong enough to become a film, then convert it into a 15-second narrative with shot cards, keyframe directions, continuity rules, transition logic, and model-ready video instructions. I want to see where Creative Director hands off to Visual Storytelling, Image Director, and Video Director.
```

### 20. Full Designly capability tour on one brief

```text
@Designly Give me a practical tour of your capabilities using one fictional brief instead of listing features. Brief: launch a new cultural festival called AFTER SIX for young adults in Cairo. Work in visible stages: insight, creative concept, campaign canon check, activation idea, visual storytelling, brand/taste decisions, composition, typography, photography, image direction, one manipulation option, campaign DNA, final prompt compilation, and Visual QA. Keep each stage concise but make the handoffs explicit so I can understand what each Designly specialist contributes.
```

## Prompt Card behavior in ChatGPT

When the user asks things like:

- "What can Designly do?"
- "Show me examples"
- "How do I use Designly?"
- "Give me prompts to try"
- "Teach me Designly"
- "I want to test the plugin"
- "Show me the playground"

Designly Director should open this module and respond with a compact menu, not a feature dump.

Recommended first response:

```text
Pick what you want to see Designly do:

1. Build a key visual from a raw brief
2. Learn a reference without copying it
3. Create an Arabic RTL design
4. Direct a 15-second AI film
5. Make a realistic manipulation composite
6. Critique an existing design with Visual QA

I can give you one copy-ready prompt, or the full Playground.
```

If the user chooses a card, provide the prompt exactly or adapt only the user-editable nouns such as brand, category, language, deliverable, or attached asset. Preserve the workflow clauses because they are the part that activates Designly's specialist behavior.

## Coverage map

The Playground should collectively expose all 21 Skills across its cards:

- `designly-director`: 1, 3, 20
- `creative-strategy`: 3, 18, 20
- `creative-director`: 1, 3, 8, 19, 20
- `insight-mining`: 1, 3, 7, 18, 20
- `campaign-canon`: 1, 3, 9, 18, 20
- `brand-activation`: 10, 20
- `visual-storytelling`: 6, 19, 20
- `brand-intelligence`: 2, 18, 20
- `taste-engine`: 2, 17, 20
- `reference-memory`: 2
- `composition-director`: 1, 3, 4, 5, 11, 20
- `typography-director`: 4, 11, 18, 20
- `photography-director`: 2, 5, 12, 20
- `manipulation-director`: 5, 20
- `arabic-rtl-director`: 4, 18, 20
- `campaign-dna`: 15, 17, 18, 20
- `video-director`: 6, 19, 20
- `image-director`: 1, 3, 6, 13, 19, 20
- `edit-sanitizer`: 14
- `prompt-compiler`: 3, 5, 12, 13, 20
- `visual-qa`: 1, 3, 4, 6, 14, 16, 18, 20

This file is the single source of truth for copy-ready onboarding prompts. Keep the top-level Skill focused on invocation and routing, and keep individual specialist mechanics in their own Skills.
