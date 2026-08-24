from __future__ import annotations
from typing import Any
from .base import BaseAdapter, AdapterResult

class ClaudeDesignAdapter(BaseAdapter):
    name = "claude-design"
    display_name = "Claude 3.7 Design & Artifacts"
    category = "design"
    provider = "anthropic"
    supported_aspect_ratios = ["1:1", "16:9", "9:16", "4:3", "3:4", "custom"]
    max_prompt_length = 8000
    max_references = 16

    ANTI_SLOP_FORBIDDEN = [
        "generic purplish gradients",
        "floating 3d glass spheres",
        "decorative blobs without semantic function",
        "cookie-cutter SaaS card layouts",
        "unmotivated drop shadows"
    ]

    def compile(self, spec: dict[str, Any]) -> AdapterResult:
        mode = spec.get("mode", "generate")
        model_name = "claude-3-7-sonnet-design"
        ar = spec.get("aspect_ratio", "16:9")
        notes = []

        is_svg = spec.get("output_format") == "svg" or spec.get("target_type") == "vector"
        is_interactive = spec.get("interactive", False)

        sections = [
            "### Claude Design System & Artifact Contract",
            "",
            "#### 1. Creative Direction & Intent",
            f"- **Component / Interface**: {spec.get('subject', 'Design System Component')}",
            f"- **Aesthetic Altitude**: Editorial, intentional typography, bespoke palette, high polish",
            f"- **Tone & Purpose**: {spec.get('concept', 'Production-grade visual craft with uncompromising quality')}",
            "",
            "#### 2. Design Tokens & Palette",
            f"- **Backgrounds**: {spec.get('bg_token', 'bg-slate-950 / #0B0F19 dark, bg-slate-50 / #F8FAFC light')}",
            f"- **Primary Accent**: {spec.get('accent_token', '#2563EB (Electric Blue) / #10B981 (Emerald)')}",
            f"- **Typography Scale**: Display (font-display tracking-tight), Body (font-sans antialiased), Micro (font-mono uppercase)",
            f"- **Radius & Elevation**: {spec.get('radii', 'rounded-xl')}, subtle border highlight (border border-slate-800/80)",
            "",
            "#### 3. Anti-Slop Finish Gate (Strict Invariants)",
            "- Zero unmotivated floating shapes or decorative blobs.",
            "- Zero stock purple-to-cyan gradient backgrounds.",
            "- Every element must have clear functional hierarchy and readable contrast.",
            "- Text measure clamped for effortless scanning (max 65ch for paragraphs)."
        ]

        if is_svg:
            sections.extend([
                "",
                "#### 4. SVG Vector Precision Specifications",
                "- Include exact `viewBox=\"0 0 800 600\"` (or matching canvas dimensions).",
                "- Use semantic SVG elements (`<defs>`, `<linearGradient>`, `<path>`, `<text>`).",
                "- Ensure all paths have explicit `fill`, `stroke`, `stroke-width`, and `stroke-linecap`.",
                "- Zero hard-clipped visual elements at canvas boundaries."
            ])
            notes.append("Claude Design: Standalone precision SVG vector mode.")

        if is_interactive:
            sections.extend([
                "",
                "#### 5. Interactive State Machine Matrix",
                "- **Default**: Rest state with calm contrast and balanced hierarchy.",
                "- **Hover**: Smooth transition (`transition-all duration-200 ease-out`), subtle scale or luminance shift.",
                "- **Active / Pressed**: Tactile feedback with slight inset or elevation drop.",
                "- **Focus-Visible**: High-contrast outline (`ring-2 ring-offset-2 ring-blue-500`).",
                "- **Disabled**: Clean reduced opacity (`opacity-40 pointer-events-none`) without layout shift."
            ])
            notes.append("Claude Design: Multi-state interactive UI matrix defined.")

        copy = spec.get("copy", "")
        if copy:
            sections.extend([
                "",
                "#### 6. Copy & Content Locks",
                f"- Exact Copy: \"{copy}\" (render verbatim, maintain hierarchy)."
            ])

        prompt = "\n".join(sections)

        return AdapterResult(
            model=model_name,
            prompt=prompt,
            aspect_ratio=ar,
            mode=mode,
            parameters={
                "is_svg": is_svg,
                "is_interactive": is_interactive,
                "framework": spec.get("framework", "Tailwind CSS / React / SVG")
            },
            notes=notes,
            raw_spec=spec
        )
