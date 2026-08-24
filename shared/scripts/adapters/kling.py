from __future__ import annotations
from typing import Any
from .base import BaseAdapter, AdapterResult

class KlingAdapter(BaseAdapter):
    name = "kling"
    display_name = "Kuaishou Kling 3.0 / 2.6 Pro"
    category = "video"
    provider = "kuaishou"
    supported_aspect_ratios = ["16:9", "9:16", "1:1", "4:3", "21:9"]
    max_prompt_length = 4500
    max_references = 10

    def compile(self, spec: dict[str, Any]) -> AdapterResult:
        mode = spec.get("mode", "generate")
        version = spec.get("version", "3.0")
        model_name = f"kling-{version}-pro"
        ar = spec.get("aspect_ratio", "16:9")
        duration = spec.get("duration", 10)  # 5s or 10s
        notes = []

        # Multi-Character Binding
        characters = spec.get("characters", [])
        char_sections = []
        if characters:
            for i, c in enumerate(characters):
                label = chr(65 + i)  # A, B, C...
                char_sections.append(f"[Character {label}: {c}]")

        # Camera Motion Matrix (-10 to +10)
        camera_matrix = spec.get("camera_matrix", {
            "horizontal": spec.get("cam_h", 0),
            "vertical": spec.get("cam_v", 0),
            "zoom": spec.get("cam_zoom", 3),
            "tilt": spec.get("cam_tilt", 0),
            "pan": spec.get("cam_pan", 0),
            "roll": spec.get("cam_roll", 0)
        })

        # Motion Brush Regions (up to 6 regions)
        motion_brushes = spec.get("motion_brushes", [])
        brush_sections = []
        if motion_brushes:
            for i, mb in enumerate(motion_brushes[:6]):
                brush_sections.append(f"Region {i+1} ({mb.get('target', 'subject')}): trajectory={mb.get('trajectory', 'forward')}, velocity={mb.get('velocity', '+5')}")
            notes.append(f"Configured {len(motion_brushes)} Motion Brush vector regions.")

        sections = [
            f"=== KLING {version} PRO VIDEO DIRECTING PROMPT (Duration: {duration}s | Ratio: {ar}) ==="
        ]

        if char_sections:
            sections.extend(["", "--- CHARACTER BINDINGS ---"] + char_sections)

        sections.extend([
            "",
            "--- SCENE & ACTION SCRIPT ---",
            f"Subject & Staging: {spec.get('subject', 'Protagonist in cinematic setting')}",
            f"Movement Physics: {spec.get('action', 'High-fidelity natural physical movement, realistic momentum and cloth physics')}",
            f"Lighting & Atmosphere: {spec.get('lighting', 'Volumetric cinematic lighting with realistic shadows')}"
        ])

        dialogue = spec.get("dialogue", "")
        if dialogue:
            speaker = spec.get("speaker", "Character A")
            sections.append(f'Native Lip-Sync Dialogue: [{speaker}] "{dialogue}"')
            notes.append(f"Kling native lip-sync dialogue enabled for {speaker}.")

        if brush_sections:
            sections.extend(["", "--- MOTION BRUSH VECTORS ---"] + brush_sections)

        sections.extend([
            "",
            "--- CAMERA CONTROL PARAMETERS ---",
            f"Matrix: Horizontal={camera_matrix.get('horizontal', 0)}, Vertical={camera_matrix.get('vertical', 0)}, "
            f"Zoom={camera_matrix.get('zoom', 3)}, Tilt={camera_matrix.get('tilt', 0)}, Pan={camera_matrix.get('pan', 0)}, Roll={camera_matrix.get('roll', 0)}"
        ])

        prompt = "\n".join(sections)
        neg_prompt = (
            self.extract_negative_prompt(spec) or 
            "distorted limbs, extra fingers, text jitter, warping background, morphing objects, inconsistent face, blur, low resolution, unnatural twitching"
        )

        params = {
            "version": version,
            "duration": duration,
            "mode": spec.get("quality_mode", "professional"),
            "camera_matrix": camera_matrix,
            "motion_brush_count": len(motion_brushes),
            "cfg_scale": spec.get("cfg_scale", 0.5)
        }

        return AdapterResult(
            model=model_name,
            prompt=prompt,
            negative_prompt=neg_prompt,
            aspect_ratio=ar,
            mode=mode,
            parameters=params,
            notes=notes,
            raw_spec=spec
        )
