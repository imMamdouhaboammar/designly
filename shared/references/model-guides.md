# Designly Model Adapters & Model Guides

Designly provides typed, model-physics-calibrated prompt adapters across premier image, video, and design AI generators.

---

## Model Selection Matrix

| Model / Adapter | Primary Use Case | Output Physics & Grammar | Native Parameters |
|---|---|---|---|
| **Gemini Nano Banana (NB2 / Pro)** | Photorealism, real-world grounding, spatial diagrams, extreme ratios | Natural-language prose, zero fake camera numbers, JSON for 5+ elements | `1:8` to `8:1`, thinking mode, 14 references |
| **MiniMax Design (Hailuo)** | Cinematic video & high-dynamic images | Bilingual syntax, volumetric lighting, motion vectors | Camera motions (`pan`, `tilt`, `zoom`, `dolly`, `orbit`), intensity `1-10` |
| **Kimi Design (Moonshot)** | Multimodal UI/UX, poster layouts, typography locks | Coordinate zoning (`[Top-Bar]`, `[Hero]`, `[Card-Grid]`), design tokens | Paired layout specifications, copy bounding boxes, `#HEX` palettes |
| **Claude Design (Anthropic 3.7)** | UI systems, precision vector SVG, clean interactive components | Anti-slop finish gate, Tailwind tokens, state machines | Semantic SVG `<viewBox>`, zero clipping, interactive states |
| **ByteDance Seedance 2.5** | 30s multi-shot cinematic film sequences | 14-field shot lists, `{ dialogue }` lip-sync, 3D blockout | 50-slot reference kit, multi-shot timeline |
| **Kuaishou Kling 3.0 / 2.6 Pro** | High-action video, multi-character continuity | `[Character A: ...]` tags, Motion Brush vectors | 6-region motion brush, negative prompt, camera matrix |
| **OpenAI GPT Image 2** | Precision typography, bounded 2-column edits | 5-slot template (`Scene/Subject/Details/Use/Constraints`) | `quality: low/medium/high`, 16 references |
| **Google Veo 3 / 3.1** | Commercial polish video with voiceover | Structured JSON schema prompt | Aspect ratio, duration, 24fps / 1080p |

---

## 1. Gemini Nano Banana Adapter (`gemini-nano-banana`)

### Physics & Syntax Rules
- **Natural Language Paragraphs**: Describe perceptual relationships rather than disconnected keywords.
- **Zero Camera Specs Dump**: NB2/Pro ignores numbers like `50mm f/1.4 ISO 100`. Use natural lighting and framing descriptions instead.
- **Extreme Aspect Ratios**: Native support for `1:8`, `8:1`, `1:4`, `4:1`, `16:9`, `9:16`, `1:1`, `21:9`.
- **Grounding Mode**: Leverages real-world visual knowledge for authentic landmarks, biological species, and architectural structures.
- **Thinking Mode & Spatial JSON**: When composing 5+ distinct elements, outputs structured JSON coordinates to prevent subject overlap.
- **Reference Binding**: Up to 14 reference images with indexed roles (`[Ref 1: ...]`).

---

## 2. MiniMax Design Adapter (`minimax-design`)

### Physics & Syntax Rules
- **Cinematic Lighting & Fluid Dynamics**: Dense atmospheric particles, volumetric rays, natural momentum.
- **Bilingual Nuance**: English and Chinese tag support for high aesthetic fidelity.
- **Camera Directives**:
  - `pan_left`, `pan_right`, `tilt_up`, `tilt_down`
  - `zoom_in`, `zoom_out`, `dolly_in`, `dolly_out`
  - `truck_left`, `truck_right`, `orbit_clockwise`, `crane_shot`
- **Video Motion Levers**: Motion intensity from `1` (subtle breathing) to `10` (high kinetic speed).

---

## 3. Kimi Design Adapter (`kimi-design`)

### Physics & Syntax Rules
- **Layout-First Coordinate Zoning**: Dividers and sections mapped to `[ZONE_TOP]`, `[ZONE_HERO]`, `[ZONE_BODY]`, `[ZONE_FOOTER]`.
- **Design Token Contract**: Explicit color palette (`#111111`, `#FFFFFF`, `#3B82F6`), typography hierarchy, border radii, and elevation shadows.
- **Exact Copy Locks**: Text strings in bounding boxes are preserved without font distortion or spelling hallucination.
- **Dual Vector / Code Mode**: Outputs both visual prompt guidance and paired SVG / Tailwind markup.

---

## 4. Claude Design Adapter (`claude-design`)

### Physics & Syntax Rules
- **Anti-Slop Finish Gate**: Forbids generic purple gradients, floating spheres, and decorative non-functional blobs.
- **Token-Driven Architecture**: Uses production Tailwind CSS / CSS variable tokens with strict typography scale.
- **Precision SVG Generation**: Standalone valid SVG with responsive `viewBox="0 0 800 600"`, semantic grouping, and zero clipping.
- **Interactive State Matrix**: Defines `default`, `hover`, `active`, `focus-visible`, and `disabled` states.

---

## 5. Seedance 2.5 Video Adapter (`seedance`)

### Physics & Syntax Rules
- **30s Single-Pass Multi-Shot**: Transitions across `[Shot 1] -> [Shot 2] -> [Shot 3]` in one continuous pass.
- **50-Slot Reference Kit**: Characters, environments, and style keys indexed `[Character ID-01]`, `[Environment ID-01]`.
- **Dialogue Lip-Sync Markers**: `{ Character Name: "Exact dialogue line" }`.
- **Walter Murch Rule of Six**: 51% Emotion, 23% Story, 10% Rhythm, 7% Eye-trace.

---

## 6. Kling 3.0 Pro Video Adapter (`kling`)

### Physics & Syntax Rules
- **Multi-Character Binding**: Tag characters as `[Character A: description]` and `[Character B: description]`.
- **6-Region Motion Brush**: Trajectory vectors and velocity sliders (`-10 to +10`) for localized motion control.
- **Native Negative Prompt**: Explicit exclusion field to eliminate anatomy morphing and camera jitter.
- **6-Axis Camera Control Matrix**: Horizontal, Vertical, Zoom, Tilt, Pan, Roll.
