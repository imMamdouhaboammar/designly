from __future__ import annotations
from typing import Any
from .base import BaseAdapter, AdapterResult
from .gemini_nano_banana import GeminiNanoBananaAdapter
from .minimax_design import MiniMaxDesignAdapter
from .kimi_design import KimiDesignAdapter
from .claude_design import ClaudeDesignAdapter
from .seedance import SeedanceAdapter
from .kling import KlingAdapter
from .gpt_image import GPTImageAdapter
from .veo import VeoAdapter

ALIASES: dict[str, str] = {
    # Gemini / Nano Banana
    "gemini": "gemini-nano-banana",
    "gemini-nano": "gemini-nano-banana",
    "gemini-nano-banana": "gemini-nano-banana",
    "gemini-nano-banana-pro": "gemini-nano-banana",
    "nano-banana": "gemini-nano-banana",
    "nano-banana-2": "gemini-nano-banana",
    "nano-banana-pro": "gemini-nano-banana",
    "nb2": "gemini-nano-banana",
    "nbp": "gemini-nano-banana",

    # MiniMax / Hailuo
    "minimax": "minimax-design",
    "minimax-design": "minimax-design",
    "minimax-image": "minimax-design",
    "minimax-video": "minimax-design",
    "hailuo": "minimax-design",
    "hailuo-ai": "minimax-design",

    # Kimi / Moonshot
    "kimi": "kimi-design",
    "kimi-design": "kimi-design",
    "kimi-k1.5": "kimi-design",
    "moonshot": "kimi-design",

    # Claude Design
    "claude": "claude-design",
    "claude-design": "claude-design",
    "claude-3-7": "claude-design",
    "claude-artifacts": "claude-design",

    # Seedance
    "seedance": "seedance",
    "seedance-2.5": "seedance",
    "doubao-video": "seedance",

    # Kling
    "kling": "kling",
    "kling-3.0": "kling",
    "kling-2.6": "kling",
    "kling-pro": "kling",

    # GPT Image
    "gpt-image": "gpt-image-2",
    "gpt-image-2": "gpt-image-2",
    "openai-image": "gpt-image-2",

    # Veo
    "veo": "veo",
    "veo-3": "veo",
    "veo-3.1": "veo"
}

class AdapterRegistry:
    def __init__(self):
        self._adapters: dict[str, BaseAdapter] = {}
        self.register(GeminiNanoBananaAdapter())
        self.register(MiniMaxDesignAdapter())
        self.register(KimiDesignAdapter())
        self.register(ClaudeDesignAdapter())
        self.register(SeedanceAdapter())
        self.register(KlingAdapter())
        self.register(GPTImageAdapter())
        self.register(VeoAdapter())

    def register(self, adapter: BaseAdapter) -> None:
        self._adapters[adapter.name] = adapter

    def resolve_name(self, name: str) -> str:
        key = name.lower().strip()
        return ALIASES.get(key, key)

    def get(self, name: str) -> BaseAdapter | None:
        canonical = self.resolve_name(name)
        return self._adapters.get(canonical)

    def list_all(self) -> list[dict[str, Any]]:
        return [
            {
                "name": a.name,
                "display_name": a.display_name,
                "category": a.category,
                "provider": a.provider,
                "supported_aspect_ratios": a.supported_aspect_ratios,
                "max_references": a.max_references
            }
            for a in self._adapters.values()
        ]

    def compile(self, model_name: str, spec: dict[str, Any]) -> AdapterResult:
        adapter = self.get(model_name)
        if not adapter:
            raise ValueError(f"Unknown model adapter '{model_name}'. Available: {list(self._adapters.keys())}")
        
        errors = adapter.validate(spec)
        if errors:
            raise ValueError(f"Validation failed for {adapter.name}: {'; '.join(errors)}")
            
        return adapter.compile(spec)

# Global default instance
registry = AdapterRegistry()
