from __future__ import annotations
from typing import Any
from .base import BaseAdapter, AdapterResult

class SeedanceAdapter(BaseAdapter):
    name = "seedance"
    display_name = "ByteDance Seedance 2.5"
    category = "video"
    provider = "bytedance"
    supported_aspect_ratios = ["16:9", "9:16", "1:1", "4:3", "21:9"]
    max_prompt_length = 6000
    max_references = 50

    def compile(self, spec: dict[str, Any]) -> AdapterResult:
        mode = spec.get("mode", "generate")
        model_name = "seedance-2.5-pro"
        ar = spec.get("aspect_ratio", "16:9")
        duration = spec.get("duration", 15)  # default 15s up to 30s
        notes = []

        shots = spec.get("shots", [])
        sections = [
            f"=== SEEDANCE 2.5 DRAMATURGY VIDEO DIRECTING SPEC (Duration: {duration}s | Ratio: {ar}) ===",
            "",
            "--- CORE SCENE DRAMATURGY ---",
            f"Desire + Obstacle: {spec.get('dramaturgy', spec.get('concept', 'Main character pursuit under environmental pressure'))}",
            f"Rule of Six Priority: Emotion (51%), Story (23%), Rhythm (10%), Eye-Trace (7%)",
            ""
        ]

        # Multi-Reference Kit (up to 50 slots)
        refs = spec.get("references", [])
        if refs:
            sections.append("--- REFERENCE KIT BINDING ---")
            for i, r in enumerate(refs[:50]):
                r_lower = str(r).lower()
                char_kw = ["char", "person", "man", "woman", "actor", "hero", "detective", "pilot", "portrait", "face"]
                env_kw = ["env", "interior", "exterior", "location", "room", "warehouse", "landscape", "street", "city", "building"]
                
                if any(kw in r_lower for kw in char_kw):
                    tag_role = "Character"
                elif any(kw in r_lower for kw in env_kw):
                    tag_role = "Environment"
                else:
                    tag_role = "Asset"
                sections.append(f"[{tag_role} ID-{i+1:02d}]: {r}")
            sections.append("")
            notes.append(f"Bound {len(refs)} reference kit anchors for temporal stability.")

        # Multi-Shot Timeline
        if shots:
            sections.append("--- MULTI-SHOT TIMELINE (SINGLE-PASS CONTINUITY) ---")
            for i, s in enumerate(shots):
                t_start = s.get("start", f"00:{(i*5):02d}")
                t_end = s.get("end", f"00:{((i+1)*5):02d}")
                cam = s.get("camera", "Motivated tracking push-in")
                act = s.get("action", "Character action progressing narrative")
                dialogue = s.get("dialogue", "")
                
                shot_desc = f"[Shot {i+1}: {t_start}-{t_end} | Camera: {cam}] Action: {act}"
                if dialogue:
                    char_name = s.get("speaker", "Character")
                    shot_desc += f' {{ {char_name}: "{dialogue}" }}'
                sections.append(shot_desc)
        else:
            subject = spec.get("subject", "Main subject")
            action = spec.get("action", "Dynamic cinematic movement")
            env = spec.get("environment", "Atmospheric photorealistic environment")
            cam = spec.get("camera", "Slow motivated push-in with stable horizon")
            dialogue = spec.get("dialogue", "")

            sections.extend([
                "--- SHOT DIRECTION ---",
                f"[Shot 01: 00:00-{duration:02d} | Camera: {cam}]",
                f"Subject & Staging: {subject} in {env}.",
                f"Action Physics: {action}."
            ])
            if dialogue:
                speaker = spec.get("speaker", "Protagonist")
                sections.append(f'Dialogue: {{ {speaker}: "{dialogue}" }}')

        spatial = spec.get("spatial_blockout", "Subject vector moving from midground to foreground, lighting key 45 degrees")
        sections.extend([
            "",
            "--- 3D SPATIAL BLOCKOUT & LIGHTING ---",
            f"Coordinates & Trajectory: {spatial}"
        ])

        prompt = "\n".join(sections)

        params = {
            "duration": duration,
            "aspect_ratio": ar,
            "temporal_interpolation": "high_smoothness",
            "dialogue_lip_sync": bool(spec.get("dialogue") or any(s.get("dialogue") for s in shots))
        }

        return AdapterResult(
            model=model_name,
            prompt=prompt,
            aspect_ratio=ar,
            mode=mode,
            parameters=params,
            notes=notes,
            raw_spec=spec
        )
