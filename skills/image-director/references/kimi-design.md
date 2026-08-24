# Kimi Design (Moonshot Multimodal UI & Visual Systems) Reference Guide

Kimi Design emphasizes structured visual architecture, layout coordinate zoning, and exact typography bounds.

## Core Rules

1. **Layout-First Coordinate Zoning**: Divide screen space into explicit zones: `[ZONE_TOP]`, `[ZONE_HERO]`, `[ZONE_BODY]`, `[ZONE_FOOTER]`.
2. **Design System Token Contracts**: Define `#HEX` palettes, typography scales, corner radii (`rounded-xl`), elevation shadows, and spacing rhythm (4/8/16/24/32/48px).
3. **Exact Copy Locks**: Bounding boxes lock text strings to prevent character morphing.
4. **Paired Code / Visual Output**: Generates both visual art direction and matching Tailwind / HTML / SVG markup.

## Output Example

```text
Model: kimi-k1.5-design
Aspect Ratio: 16:9
Mode: generate

Prompt:
=== KIMI MULTIMODAL DESIGN SYSTEM SPECIFICATION ===

[1. CONCEPT & VISUAL OBJECTIVE]
Objective: Luxury E-Commerce Product Launch Art Direction
Primary Message: Sophisticated minimalism with high-contrast typography

[2. SPATIAL & COORDINATE GRID ZONING]
- ZONE_TOP: Brand mark left, minimalist navigation items right, 64px height
- ZONE_HERO: High-impact hero flacon on wet obsidian stone, dramatic lighting
- ZONE_BODY: 3-column product specification cards with 24px gap
- ZONE_FOOTER: Subtle editorial credits and purchase action

[3. DESIGN TOKENS & SYSTEM CONTRACT]
- Palette: #0B0F19 (Obsidian), #F8FAFC (Pure White), #D97706 (Amber Accent)
- Typography Hierarchy: Headline (Geist Display / Bold), Body (Inter / 400), RTL (IBM Plex Sans Arabic)
- Spacing Grid: [4, 8, 16, 24, 32, 48, 64] px standard
- Corner Radius: 12px
- Elevation: 0 4px 6px -1px rgb(0 0 0 / 0.1)

[4. EXACT COPY LOCKS & TYPOGRAPHIC BOUNDS]
- Lock 1: "EUPHORIA" (Immutable characters, exact glyph bounding box)
```
