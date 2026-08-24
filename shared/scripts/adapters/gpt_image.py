from __future__ import annotations
from typing import Any
from .base import BaseAdapter, AdapterResult

class GPTImageAdapter(BaseAdapter):
    name = "gpt-image-2"
    display_name = "OpenAI GPT Image 2"
    category = "image"
    provider = "openai"
    supported_aspect_ratios = ["1:1", "16:9", "9:16", "4:3", "3:4", "3:1", "1:3"]
    max_prompt_length = 4000
    max_references = 16

    def compile(self, spec: dict[str, Any]) -> AdapterResult:
        mode = spec.get("mode", "generate")
        model_name = "gpt-image-2"
        ar = spec.get("aspect_ratio", "1:1")
        quality = spec.get("quality", "medium")
        notes = []

        params = {
            "quality": quality,
            "size": spec.get("size", "1024x1024")
        }

        if mode == "edit":
            # Two-column preservation contract
            change = spec.get("mutation", "modify target area")
            target = spec.get("target", "target element")
            preserve = spec.get("preserve", ["subject face", "lighting", "framing", "camera angle", "background"])
            if isinstance(preserve, list):
                preserve_str = ", ".join(preserve)
            else:
                preserve_str = str(preserve)
            constraints = spec.get("constraints", "do not add extra objects, prevent face drift, maintain identical resolution")

            prompt = (
                f"Change: Modify only the {target}. {change}\n"
                f"Preserve: {preserve_str}\n"
                f"Constraints: {constraints}"
            )
            notes.append("GPT Image 2 bounded edit: two-column preservation contract.")
            return AdapterResult(
                model=model_name,
                prompt=prompt,
                aspect_ratio=ar,
                mode=mode,
                parameters=params,
                notes=notes,
                raw_spec=spec
            )

        # 5-slot structured generation template
        slot_scene = spec.get("scene", spec.get("environment", "Clean professional studio setting"))
        slot_subject = spec.get("subject", "Commercial product / subject")
        slot_details = spec.get("details", f"Lighting: {spec.get('lighting', 'Key 45 deg')}. Optics: {spec.get('optics', 'Crisp focus')}")
        slot_use_case = spec.get("use_case", "Commercial advertising and high-resolution art direction")
        slot_constraints = spec.get("constraints", "No synthetic artifacts, no distorted anatomy, crisp typography")

        copy = spec.get("copy", "")
        if copy:
            slot_details += f' Render exact text "{copy}" with zero spelling errors.'

        sections = [
            f"Scene: {slot_scene}",
            f"Subject: {slot_subject}",
            f"Important Details: {slot_details}",
            f"Use Case: {slot_use_case}",
            f"Constraints: {slot_constraints}"
        ]

        prompt = "\n".join(sections)
        notes.append(f"GPT Image 2 5-slot template compiled with quality={quality}.")

        return AdapterResult(
            model=model_name,
            prompt=prompt,
            aspect_ratio=ar,
            mode=mode,
            parameters=params,
            notes=notes,
            raw_spec=spec
        )
