---
name: video-director
description: Dramaturgy-first AI video directing, shot lists, pacing, and multi-model video prompting. This skill should be used when creating, auditing, or splitting prompts for AI video generators (Seedance 2.5, Kling 3.0, MiniMax Hailuo Video, Veo 3/3.1, Runway Gen-4, Luma, Pika, Sora), building 14-field shot cards, Murch's Rule of Six montage cuts, animatic keyframes, race/speed sequences, or fixing broken video prompts.
---

# AI Video Director, Screenwriter & Editor

Direct, write, and edit AI video sequences with dramaturgy-first discipline. Prompt engineering serves cinema: frame, emotion, motivated camera, and cut rhythm come before model syntax.

## Mandatory Process & Reading Order

Do not write a prompt from memory. Each model has its own physics; load these references in order:

### 1. Dramaturgy & Core Laws → [dramaturgy.md](references/dramaturgy.md)
- **Scene Formula**: `desire + obstacle + geometry + gaze + rhythm` (named in 1 sentence before prompting).
- **Details Law**: Every shot must own three physical facts: environmental pressure + body micro-action + sound anchor/visual motif.
- **Walter Murch's Rule of Six**: Emotion (51%), Story (23%), Rhythm (10%), Eye-trace (7%), Screen plane (5%), 3D space (4%).
- **Three-Jobs Rule**: A shot must change emotion, advance action, or increase pressure. If none, delete.
- **Staging**: Fincher (camera moves only on change), Spielberg (readable geometry), Kurosawa (weather pressure).
- **Montage Staircase**: `long → shorter → shorter → pause → impact`. Never skip the Crack.

### 2. Universal Rules → [universal-rules.md](references/universal-rules.md)
- Universal U1–U12 rules: prompt skeleton, weight-at-start, show-don't-tell, lens language, character anchors, duration discipline, final-image rule.

### 3. Model Physics Selection (Read Exactly One)
- **Seedance 2.5 / Doubao** → [seedance.md](references/seedance.md) & [seedance-25.md](references/seedance-25.md): 30s single-pass, 50-slot reference kits, dialogue markers `{ }`, video editing, 3D blockout.
- **Kling 3.0 / 2.6 Pro** → [kling.md](references/kling.md): `[Character A: ...]` labels, native dialogue + lip-sync, Element Binding, Motion Brush, negative prompt field.
- **MiniMax Video (Hailuo)** → [minimax-video.md](references/minimax-video.md): Volumetric physics, motion intensity `1-10`, camera vectors (`pan`, `tilt`, `zoom`, `dolly`, `orbit`), and bilingual tags.
- **Veo 3 / 3.1** → [veo.md](references/veo.md): JSON prompts, dialogue / synchronized SFX, commercial polish with voiceover.
- Other engines (Runway Gen-4, Luma, Pika, Sora) follow [universal-rules.md](references/universal-rules.md).

### 4. Task-Specific Specialized Modules
- Storyboards, shot lists, role modes → [role-modes.md](references/role-modes.md)
- Animatic keyframes & still pitch panels → [animatic-keyframes.md](references/animatic-keyframes.md)
- Race, drift, chase, dynamic kinetic montage → [race-and-speed.md](references/race-and-speed.md)
- Commercial, music video, drama, action, UGC, product film → [patterns-and-genres.md](references/patterns-and-genres.md)
- Prompt audit, failure fixes, melted hands, face drift → [fixes-and-skeletons.md](references/fixes-and-skeletons.md)
- Studio camera, lens, movement, lighting & sound terms → [camera-lighting-vocabulary.md](references/camera-lighting-vocabulary.md)

---

## Preflight Verification Gates

Before outputting any prompt or shot list, execute:
1. **Dramaturgy Check**: Scene formula complete, motivated camera, readable geometry, five anchors named (emotion, motif, object, break, final image).
2. **Three-Detail Audit**: Environmental pressure + physical micro-action + sound anchor on every shot.
3. **Slop & Banned Word Filter**: Purge `cinematic`, `epic`, `stunning`, `masterpiece`, `beautiful lighting`, `dynamic camera`.

---

## Output Formats

- **A. Single Prompt**: Header (`Model`, `Quality`, `Duration`, `Aspect Ratio`) + prompt text + notes.
- **B. Multi-Clip Sequence**: Prompts with repeating identity / style / continuity blocks.
- **C. 14-Field Storyboard**: Time, Shot, Function, Action, Camera, Light, Sound, Emotion.
- **D. Prompt Audit**: Working points, broken elements, missing direction, continuity risks, rewritten prompt.
- **E. Director Treatment**: Core idea, emotional arc, visual motif, rhythm, camera language, ending image.

---

## Cross-Skill Neural Connections & References

### Peer & Downstream Skills
- [Image Director](../image-director/SKILL.md) — Keyframes, character sheets, and still panels
- [Creative Director](../creative-director/SKILL.md) — Upstream Big Idea and commercial script
- [Visual Storytelling](../visual-storytelling/SKILL.md) — Narrative arcs and story structures
- [Prompt Compiler](../prompt-compiler/SKILL.md) — Multi-model prompt compilation
- [Visual QA](../visual-qa/SKILL.md) — Motion critique and dramaturgy gate
- [Designly Director](../designly-director/SKILL.md) — Orchestrator and state owner

### Schemas & Contracts
- [Signal Packet](../../shared/contracts/signal-packet.schema.json) — Neural Mesh handoff
- [Routing Graph](../../shared/contracts/routing-graph.json) — Orchestration graph

---
*Attribution: Dramaturgy and model synthesis created by Serge Shima ([github.com/smixs/visual-skills](https://github.com/smixs/visual-skills)), licensed under CC BY 4.0.*
