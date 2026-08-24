from __future__ import annotations
from typing import Any
from .base import BaseAdapter, AdapterResult

class MiniMaxDesignAdapter(BaseAdapter):
    name = "minimax-design"
    display_name = "MiniMax / Hailuo Design (Image & Video)"
    category = "image"
    provider = "minimax"
    supported_aspect_ratios = ["1:1", "16:9", "9:16", "4:3", "3:4", "21:9"]
    max_prompt_length = 3500
    max_references = 8

    VALID_CAMERA_MOTIONS = [
        "static", "pan_left", "pan_right", "tilt_up", "tilt_down",
        "zoom_in", "zoom_out", "dolly_in", "dolly_out",
        "truck_left", "truck_right", "orbit_clockwise", "orbit_counterclockwise", "crane_shot"
    ]

    def compile(self, spec: dict[str, Any]) -> AdapterResult:
        mode = spec.get("mode", "generate")
        is_video = spec.get("media_type") == "video" or spec.get("duration") is not None
        model_name = "minimax-video-01" if is_video else "minimax-image-01"
        ar = spec.get("aspect_ratio", "16:9" if is_video else "1:1")
        notes = []

        params = {
            "prompt_optimizer": spec.get("prompt_optimizer", True),
            "fidelity": spec.get("fidelity", "high")
        }

        if is_video:
            duration = spec.get("duration", 6)
            motion_intensity = spec.get("motion_intensity", 6)
            camera_motion = spec.get("camera_motion", "dolly_in")
            params["duration"] = duration
            params["motion_intensity"] = min(max(int(motion_intensity), 1), 10)
            params["camera_motion"] = camera_motion
            notes.append(f"MiniMax Video: duration={duration}s, motion_intensity={params['motion_intensity']}")

        # Build prompt sections
        parts = []
        
        # 1. Subject & Action Mechanics
        subject = spec.get("subject", "")
        action = spec.get("action", "")
        dynamics = spec.get("dynamics", "natural realistic movement, accurate physical momentum")
        if subject:
            parts.append(f"Subject: {subject}")
        if action:
            parts.append(f"Action & Physics: {action}, {dynamics}")

        # 2. Atmospheric & Volumetric Lighting
        lighting = spec.get("lighting", "Cinematic atmospheric lighting with realistic volumetric depth and soft shadows")
        environment = spec.get("environment", "")
        if environment or lighting:
            parts.append(f"Environment & Light: {environment}. {lighting}".strip())

        # 3. Camera Directives
        if is_video:
            cam = params.get("camera_motion", "smooth subtle push-in")
            parts.append(f"Camera Movement: {cam}, stable trajectory, no jitter")
        else:
            framing = spec.get("composition", "Balanced cinematic framing with clear focal hierarchy")
            parts.append(f"Composition: {framing}")

        # 4. Bilingual Keywords / Quality Enhancers
        bilingual = spec.get("bilingual_tags", [])
        if bilingual:
            parts.append(f"Tags: {', '.join(bilingual)}")

        # 5. Exact copy lock if present
        copy = spec.get("copy", "")
        if copy:
            parts.append(f'Rendered Text: "{copy}" with pristine sharpness and high legibility')

        prompt = "\n".join(parts)
        neg_prompt = self.extract_negative_prompt(spec) or "low quality, distorted hands, morphing objects, jittery frame, oversaturated, blurry face"

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

    def validate(self, spec: dict[str, Any]) -> list[str]:
        errors = super().validate(spec)
        motion = spec.get("camera_motion")
        if motion and motion not in self.VALID_CAMERA_MOTIONS:
            errors.append(f"Invalid camera motion '{motion}' for MiniMax. Valid: {self.VALID_CAMERA_MOTIONS}")
        return errors
