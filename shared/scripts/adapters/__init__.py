from .base import BaseAdapter, AdapterResult
from .gemini_nano_banana import GeminiNanoBananaAdapter
from .minimax_design import MiniMaxDesignAdapter
from .kimi_design import KimiDesignAdapter
from .claude_design import ClaudeDesignAdapter
from .seedance import SeedanceAdapter
from .kling import KlingAdapter
from .gpt_image import GPTImageAdapter
from .veo import VeoAdapter
from .registry import AdapterRegistry, registry

__all__ = [
    "BaseAdapter",
    "AdapterResult",
    "GeminiNanoBananaAdapter",
    "MiniMaxDesignAdapter",
    "KimiDesignAdapter",
    "ClaudeDesignAdapter",
    "SeedanceAdapter",
    "KlingAdapter",
    "GPTImageAdapter",
    "VeoAdapter",
    "AdapterRegistry",
    "registry"
]
