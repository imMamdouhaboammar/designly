from __future__ import annotations
import abc
import re
from dataclasses import dataclass, field
from typing import Any

SLOP_TERMS = [
    "neon", "glow", "hologram", "holographic", "particles", "chrome",
    "liquid metal", "lens flare", "cyberpunk", "floating objects",
    "futuristic ui", "glass panels", "sparks", "smoke"
]

VAGUE_TERMS = [
    "stunning", "eye-catching", "make it pop", "next-level",
    "visually captivating", "premium and modern", "bold and dynamic",
    "masterpiece", "epic", "cinematic lighting"
]

CAMERA_DUMP = re.compile(r"\b(24mm|35mm|50mm|85mm|105mm|f/1\.4|f/1\.8|f/2\.8|iso\s*\d+|1/\d+s)\b", re.I)

@dataclass
class AdapterResult:
    model: str
    prompt: str
    negative_prompt: str | None = None
    parameters: dict[str, Any] = field(default_factory=dict)
    aspect_ratio: str = "1:1"
    mode: str = "generate"
    notes: list[str] = field(default_factory=list)
    raw_spec: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "model": self.model,
            "aspect_ratio": self.aspect_ratio,
            "mode": self.mode,
            "prompt": self.prompt,
            "negative_prompt": self.negative_prompt,
            "parameters": self.parameters,
            "notes": self.notes
        }

    def format_text(self) -> str:
        lines = [
            f"Model: {self.model}",
            f"Aspect Ratio: {self.aspect_ratio}",
            f"Mode: {self.mode}"
        ]
        if self.parameters:
            params_str = ", ".join(f"{k}: {v}" for k, v in self.parameters.items())
            lines.append(f"Parameters: {params_str}")
        if self.negative_prompt:
            lines.append(f"Negative Prompt: {self.negative_prompt}")
        lines.append("")
        lines.append("Prompt:")
        lines.append(self.prompt)
        if self.notes:
            lines.append("")
            lines.append("Notes:")
            for note in self.notes:
                lines.append(f"- {note}")
        return "\n".join(lines)


class BaseAdapter(abc.ABC):
    name: str = "base"
    display_name: str = "Base Model Adapter"
    category: str = "image"  # image, video, design
    provider: str = "generic"
    supported_aspect_ratios: list[str] = ["1:1", "16:9", "9:16", "4:3", "3:4"]
    max_prompt_length: int = 4000
    max_references: int = 14

    @abc.abstractmethod
    def compile(self, spec: dict[str, Any]) -> AdapterResult:
        """Compile an Art Direction Spec or Edit Contract into model-ready instruction."""
        pass

    def validate(self, spec: dict[str, Any]) -> list[str]:
        """Validate that the input spec satisfies the model constraints."""
        errors = []
        ar = spec.get("aspect_ratio", "1:1")
        if ar not in self.supported_aspect_ratios and not any(ar.startswith(p) for p in ["1:", "8:", "4:", "16:", "9:", "3:", "2:"]):
            errors.append(f"Unsupported aspect ratio '{ar}' for {self.name}. Supported: {self.supported_aspect_ratios}")
        
        refs = spec.get("references", [])
        if len(refs) > self.max_references:
            errors.append(f"Too many references ({len(refs)}) for {self.name}. Max allowed: {self.max_references}")
        
        return errors

    def extract_negative_prompt(self, spec: dict[str, Any]) -> str:
        """Extract negative exclusions if applicable for this model."""
        exclusions = spec.get("exclusions", [])
        if isinstance(exclusions, list) and exclusions:
            return ", ".join(exclusions)
        return ""

    def lint(self, text: str) -> list[tuple[str, str]]:
        """Run anti-slop and model physics linting."""
        issues = []
        lower = text.lower()
        
        hits = [t for t in SLOP_TERMS if t in lower]
        if len(hits) >= 4:
            issues.append(("major", f"Synthetic slop effect-stack detected: {', '.join(hits)}"))
        elif len(hits) >= 2:
            issues.append(("minor", f"Multiple synthetic effects: {', '.join(hits)}"))
            
        vague = [t for t in VAGUE_TERMS if t in lower]
        if vague:
            issues.append(("minor", f"Vague marketing buzzwords detected: {', '.join(vague)}"))
            
        return issues
