# Model Selection — Gemini Nano Banana, MiniMax, Kimi, Claude & GPT Image 2

Designly provides typed prompt adapters tailored to the exact physics, parameters, and aesthetics of each generator.

## Comparison Matrix

| Use Case | Recommended Model Adapter | Model Strengths & Physics |
|---|---|---|
| Real places, architectural landmarks, biological grounding | **Gemini Nano Banana (NB2 / Pro)** | Web-grounded knowledge, descriptive paragraphs, 14 references |
| Complex multi-element compositions (5+ subjects) | **Gemini Nano Banana Pro** | Thinking mode & spatial JSON coordinate structuring |
| Extreme aspect ratios (`1:8`, `8:1`, `4:1`, `1:4`, `21:9`) | **Gemini Nano Banana** | Extreme ratio stability without edge warping |
| High-dynamic lighting, volumetric atmosphere, cinematic momentum | **MiniMax Design (Hailuo)** | Physics simulation, bilingual English/Chinese parsing, motion vectors |
| UI/UX design systems, poster layouts, typography bounding boxes | **Kimi Design (Moonshot)** | Layout coordinate zoning (`[Top-Bar]`, `[Hero]`, `[Cards]`), token contracts |
| Clean vector SVG, interactive component states, anti-slop finish | **Claude Design (Anthropic 3.7)** | Anti-slop finish gate, Tailwind tokens, precision `<viewBox>` |
| Micro-typography, brand polygraphy, two-column bounded edits | **GPT Image 2** | 5-slot template, `quality: high` text rendering, strict edit preservation |

---

## Model Syntax & Prompt Rules

### 1. Gemini Nano Banana
- **Style**: Natural language descriptive paragraphs.
- **Optics**: Do NOT use numeric focal lengths (`50mm f/1.4`); describe depth and lighting relationships naturally.
- **Extreme Ratios**: Supports `1:8`, `8:1`, `4:1`, `1:4`, `16:9`, `9:16`, `1:1`.
- **Grounding**: Queries real-world references for authentic landmarks and cultural motifs.
- **Reference Binding**: Up to 14 reference images with indexed roles (`[Ref 1: ...]`).

### 2. MiniMax Design
- **Style**: Direct sensory description with action mechanics and volumetric atmosphere.
- **Camera Directives**: `Camera: pan_left / tilt_up / zoom_in / dolly_in / orbit / crane`.
- **Negative Prompt**: Explicit negative exclusions field.

### 3. Kimi Design
- **Style**: Layout-first coordinate zoning + design token contracts.
- **Structure**: `[ZONE_TOP]`, `[ZONE_HERO]`, `[ZONE_BODY]`, `[ZONE_FOOTER]`.
- **Typography**: Exact copy locks with bounding box coordinates.

### 4. Claude Design
- **Style**: Component architecture contracts, design system tokens, and precision vector specs.
- **Anti-Slop**: Zero generic purple gradients or non-functional floating blobs.
- **Vectors**: Responsive SVG with clean `viewBox` and zero visual clipping.

### 5. GPT Image 2
- **Style**: 5-slot template (`Scene`, `Subject`, `Important Details`, `Use Case`, `Constraints`).
- **Edit**: Two-column contract (`Change: X`, `Preserve: Y`, `Constraints: Z`).
