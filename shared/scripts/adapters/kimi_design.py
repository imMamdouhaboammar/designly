from __future__ import annotations
import json
from typing import Any
from .base import BaseAdapter, AdapterResult

class KimiDesignAdapter(BaseAdapter):
    name = "kimi-design"
    display_name = "Kimi Design (Moonshot Multimodal UI & Visual Systems)"
    category = "design"
    provider = "moonshot"
    supported_aspect_ratios = ["1:1", "16:9", "9:16", "4:3", "3:4", "2:1", "1:2"]
    max_prompt_length = 6000
    max_references = 10

    def compile(self, spec: dict[str, Any]) -> AdapterResult:
        mode = spec.get("mode", "generate")
        ar = spec.get("aspect_ratio", "16:9")
        model_name = "kimi-k1.5-design"
        notes = []

        raw_typo = spec.get("typography", {})
        if isinstance(raw_typo, dict):
            headline_font = raw_typo.get("headline_font") or raw_typo.get("headline") or "Inter / Geist Display"
            body_font = raw_typo.get("body_font") or raw_typo.get("body") or "Inter"
            arabic_font = raw_typo.get("arabic_font") or raw_typo.get("arabic") or "IBM Plex Sans Arabic / Noto Sans Arabic"
        elif isinstance(raw_typo, str):
            headline_font = raw_typo
            body_font = raw_typo
            arabic_font = "IBM Plex Sans Arabic"
        else:
            headline_font = "Inter / Geist Display"
            body_font = "Inter"
            arabic_font = "IBM Plex Sans Arabic / Noto Sans Arabic"

        raw_colors = spec.get("colors", ["#0F172A", "#F8FAFC", "#3B82F6", "#64748B"])
        colors_str = ", ".join(raw_colors) if isinstance(raw_colors, list) else str(raw_colors)

        spacing_scale = spec.get("spacing_scale", [4, 8, 12, 16, 24, 32, 48, 64])
        radii = spec.get("radii", "12px")
        shadows = spec.get("shadows", "0 4px 6px -1px rgb(0 0 0 / 0.1)")

        # Layout Coordinate Zones
        layout_zones = spec.get("layout_zones", {
            "zone_top": spec.get("top_bar", "Brand mark left, navigation items right, 64px height"),
            "zone_hero": spec.get("hero", "Dominant visual focal point with primary message headline"),
            "zone_body": spec.get("body_content", "Structured grid cards with 24px gap"),
            "zone_footer": spec.get("footer", "Supporting metadata, regulatory tags, and secondary action")
        })

        sections = [
            "=== KIMI MULTIMODAL DESIGN SYSTEM SPECIFICATION ===",
            "",
            "[1. CONCEPT & VISUAL OBJECTIVE]",
            f"Objective: {spec.get('concept', spec.get('subject', 'Commercial Brand Design'))}",
            f"Primary Message: {spec.get('message', 'Clear value proposition and aesthetic balance')}",
            "",
            "[2. SPATIAL & COORDINATE GRID ZONING]"
        ]

        if isinstance(layout_zones, dict):
            for z_name, z_desc in layout_zones.items():
                sections.append(f"- {z_name.upper()}: {z_desc}")
        elif isinstance(layout_zones, list):
            for i, zone in enumerate(layout_zones):
                sections.append(f"- ZONE_{i+1}: {zone}")

        sections.extend([
            "",
            "[3. DESIGN TOKENS & SYSTEM CONTRACT]",
            f"- Palette: {colors_str}",
            f"- Typography Hierarchy: Headline ({headline_font}), Body ({body_font}), RTL/Arabic ({arabic_font})",
            f"- Spacing Grid: {spacing_scale} px standard",
            f"- Corner Radius: {radii}",
            f"- Elevation: {shadows}",
            "",
            "[4. EXACT COPY LOCKS & TYPOGRAPHIC BOUNDS]"
        ])

        copy_locks = spec.get("copy_locks", [spec.get("copy", "")] if spec.get("copy") else [])
        if copy_locks and any(copy_locks):
            for i, lock in enumerate(copy_locks):
                if lock:
                    sections.append(f"- Lock {i+1}: \"{lock}\" (Immutable characters, exact glyph bounding box)")
        else:
            sections.append("- No hard-coded text locks. Ensure visual breathing room for dynamic typography overlay.")

        sections.extend([
            "",
            "[5. PAIRED SVG / HTML SPECIFICATION]",
            "Render clean, modern, semantic container tags, responsive layout tokens, and zero visual slop."
        ])

        tokens = {
            "colors": raw_colors,
            "typography": {
                "headline_font": headline_font,
                "body_font": body_font,
                "arabic_font": arabic_font
            },
            "spacing_scale": spacing_scale,
            "radii": radii,
            "shadows": shadows
        }

        prompt = "\n".join(sections)
        notes.append("Kimi Design: layout-first coordinate zoning + design token contract paired.")

        return AdapterResult(
            model=model_name,
            prompt=prompt,
            aspect_ratio=ar,
            mode=mode,
            parameters={"tokens": tokens, "layout_zones": layout_zones},
            notes=notes,
            raw_spec=spec
        )
