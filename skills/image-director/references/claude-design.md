# Claude 3.7 Design & UI Artifacts Reference Guide

Claude Design enforces high aesthetic altitude, anti-slop visual contracts, precision SVG vector graphics, and production UI components.

## Core Rules

1. **Anti-Slop Finish Gate**: Rejects generic purple gradients, floating spheres, and decorative non-functional blobs.
2. **Token-Driven Design**: Full Tailwind CSS / CSS variable token contracts.
3. **Precision SVG Vector Standards**: Standalone valid SVG with responsive `viewBox="0 0 800 600"`, semantic `<defs>`, `<linearGradient>`, and zero edge clipping.
4. **State Machine Matrix**: Covers `default`, `hover`, `active`, `focus-visible`, and `disabled` states.

## Output Example

```text
Model: claude-3-7-sonnet-design
Aspect Ratio: 16:9
Mode: generate

Prompt:
### Claude Design System & Artifact Contract

#### 1. Creative Direction & Intent
- Component / Interface: Editorial Luxury Product Presentation Card
- Aesthetic Altitude: Editorial, intentional typography, bespoke palette, high polish
- Tone & Purpose: Commercial luxury launch with understated elegance

#### 2. Design Tokens & Palette
- Backgrounds: bg-slate-950 dark, bg-slate-50 light
- Primary Accent: #D97706 (Warm Amber) / #2563EB (Electric Blue)
- Typography Scale: Display (font-display tracking-tight), Body (font-sans antialiased), Micro (font-mono uppercase)
- Radius & Elevation: rounded-xl, subtle border highlight (border border-slate-800/80)

#### 3. Anti-Slop Finish Gate (Strict Invariants)
- Zero unmotivated floating shapes or decorative blobs.
- Zero stock purple-to-cyan gradient backgrounds.
- Every element must have clear functional hierarchy and readable contrast.
- Text measure clamped for effortless scanning (max 65ch for paragraphs).

#### 4. SVG Vector Precision Specifications
- Include exact viewBox="0 0 800 600".
- Use semantic SVG elements (<defs>, <linearGradient>, <path>, <text>).
- Ensure all paths have explicit fill, stroke, stroke-width, and stroke-linecap.
- Zero hard-clipped visual elements at canvas boundaries.
```
