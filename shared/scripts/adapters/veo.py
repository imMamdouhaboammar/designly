from __future__ import annotations
import json
from typing import Any
from .base import BaseAdapter, AdapterResult

class VeoAdapter(BaseAdapter):
    name = "veo"
    display_name = "Google Veo 3 / 3.1"
    category = "video"
    provider = "google"
    supported_aspect_ratios = ["16:9", "9:16", "1:1", "4:3"]
    max_prompt_length = 5000
    max_references = 8

    def compile(self, spec: dict[str, Any]) -> AdapterResult:
        mode = spec.get("mode", "generate")
        model_name = "veo-3.1"
        ar = spec.get("aspect_ratio", "16:9")
        duration = spec.get("duration", 8)
        notes = []

        payload = {
            "version": "veo-3.1",
            "prompt": {
                "visual_concept": spec.get("concept", spec.get("subject", "Cinematic Scene")),
                "subject": spec.get("subject", ""),
                "action": spec.get("action", "Smooth cinematic movement"),
                "cinematography": {
                    "camera_angle": spec.get("camera_angle", "Eye-level"),
                    "camera_motion": spec.get("camera_motion", "Subtle tracking forward"),
                    "lighting": spec.get("lighting", "Natural golden hour directional light"),
                    "depth_of_field": spec.get("depth_of_field", "Shallow background bokeh")
                },
                "sound_and_dialogue": {
                    "dialogue": spec.get("dialogue", ""),
                    "ambient_sfx": spec.get("ambient_sfx", "Subtle environmental room tone")
                }
            },
            "parameters": {
                "duration_seconds": duration,
                "aspect_ratio": ar,
                "frame_rate": spec.get("fps", 24),
                "resolution": spec.get("resolution", "1080p")
            }
        }

        prompt = json.dumps(payload, indent=2, ensure_ascii=False)
        notes.append("Google Veo: compiled into native JSON schema format.")

        return AdapterResult(
            model=model_name,
            prompt=prompt,
            aspect_ratio=ar,
            mode=mode,
            parameters=payload["parameters"],
            notes=notes,
            raw_spec=spec
        )
