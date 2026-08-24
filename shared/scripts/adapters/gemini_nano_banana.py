from __future__ import annotations
import json
from typing import Any
from .base import BaseAdapter, AdapterResult, CAMERA_DUMP

class GeminiNanoBananaAdapter(BaseAdapter):
    name = "gemini-nano-banana"
    display_name = "Gemini Nano Banana (NB2 / NB Pro)"
    category = "image"
    provider = "google"
    supported_aspect_ratios = [
        "1:1", "16:9", "9:16", "4:3", "3:4", "2:3", "3:2",
        "1:8", "8:1", "1:4", "4:1", "21:9"
    ]
    max_prompt_length = 5000
    max_references = 14

    def compile(self, spec: dict[str, Any]) -> AdapterResult:
        mode = spec.get("mode", "generate")
        ar = spec.get("aspect_ratio", "1:1")
        is_pro = spec.get("variant", "pro") == "pro" or spec.get("model") == "gemini-nano-banana-pro"
        model_name = "gemini-nano-banana-pro" if is_pro else "gemini-nano-banana-2"
        
        notes = []
        params = {
            "variant": "pro" if is_pro else "standard",
            "grounding": spec.get("grounding", True),
            "thinking_mode": spec.get("thinking_mode", is_pro)
        }

        # Check for multi-subject complexity (>=5 subjects) -> switch to structured JSON
        subjects = spec.get("subjects", [])
        if isinstance(subjects, list) and len(subjects) >= 5:
            notes.append("High subject density (>=5 elements): formatted as spatial JSON representation.")
            json_payload = {
                "scene_concept": spec.get("concept", spec.get("subject", "Scene")),
                "spatial_composition": spec.get("composition", "Balanced editorial hierarchy"),
                "lighting_and_atmosphere": spec.get("lighting", "Natural directional daylight"),
                "color_palette": spec.get("colors", ["#111111", "#FFFFFF"]),
                "elements": [
                    {"id": f"elem_{i+1}", "description": s, "position": spec.get("positions", {}).get(str(i), f"slot_{i+1}")}
                    for i, s in enumerate(subjects)
                ],
                "invariants": spec.get("invariants", ["High visual fidelity", "No synthetic artifacts"])
            }
            prompt = json.dumps(json_payload, indent=2, ensure_ascii=False)
            return AdapterResult(
                model=model_name,
                prompt=prompt,
                aspect_ratio=ar,
                mode=mode,
                parameters=params,
                notes=notes,
                raw_spec=spec
            )

        if mode == "edit":
            # Natural language bounded edit preservation
            target = spec.get("target", "target region")
            mutation = spec.get("mutation", "modify appearance")
            preserve = spec.get("preserve", ["subject identity", "lighting", "background", "framing"])
            if isinstance(preserve, list):
                preserve_str = ", ".join(preserve)
            else:
                preserve_str = str(preserve)
            
            prompt = (
                f"Keep {preserve_str} identical to the source image. "
                f"Change only the {target}: {mutation}. "
                f"Ensure seamless physical contact, natural edge blending, and preserve overall color grade."
            )
            notes.append("Bounded local edit: single atomic mutation with explicit preservation locks.")
            return AdapterResult(
                model=model_name,
                prompt=prompt,
                aspect_ratio=ar,
                mode=mode,
                parameters=params,
                notes=notes,
                raw_spec=spec
            )

        # Standard natural language descriptive paragraphs
        sections = []
        
        # 1. Subject & Core Action
        subject = spec.get("subject", "")
        action = spec.get("action", "")
        concept = spec.get("concept", "")
        
        core_line = f"{subject}. {action}".strip() if action else subject
        if concept and concept not in core_line:
            core_line = f"{concept}. {core_line}".strip()
        if core_line:
            sections.append(core_line)

        # 2. Environment & Spatial Depth
        env = spec.get("environment", "")
        comp = spec.get("composition", "")
        if env or comp:
            env_comp = f"{env} {comp}".strip()
            sections.append(env_comp)

        # 3. Optics & Lighting (Natural prose - purge raw camera dump numbers)
        light = spec.get("lighting", "")
        materials = spec.get("materials", "")
        optics = spec.get("optics", "")
        # Filter camera numbers from optics if present
        if optics:
            optics = CAMERA_DUMP.sub("", optics).strip()
            if optics:
                notes.append("Sanitized numeric camera specs into perceptual optical framing.")
        
        light_mat = f"{light} {optics} {materials}".strip()
        if light_mat:
            sections.append(light_mat)

        # 4. Typography & Exact Text Locks (quoted)
        text_copy = spec.get("copy", "")
        if text_copy:
            sections.append(f'Render exact text "{text_copy}" integrated naturally into the composition with clean typography.')

        # 5. References
        refs = spec.get("references", [])
        if refs:
            ref_notes = []
            for i, r in enumerate(refs[:14]):
                ref_notes.append(f"[Ref {i+1}: {r}]")
            sections.append("Reference grounding: " + " ".join(ref_notes))
            params["reference_count"] = len(refs)

        prompt = "\n\n".join(sections)
        return AdapterResult(
            model=model_name,
            prompt=prompt,
            aspect_ratio=ar,
            mode=mode,
            parameters=params,
            notes=notes,
            raw_spec=spec
        )

    def lint(self, text: str) -> list[tuple[str, str]]:
        issues = super().lint(text)
        if CAMERA_DUMP.search(text):
            issues.append(("minor", "Gemini Nano Banana ignores numeric camera focal lengths (e.g. 50mm, f/1.4); use natural perceptual optics language."))
        return issues
