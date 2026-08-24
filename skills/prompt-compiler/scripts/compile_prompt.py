#!/usr/bin/env python3
"""
CLI Prompt Compiler using Designly Model Adapters.
"""
from __future__ import annotations
import argparse
import json
import os
import select
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SHARED_SCRIPTS = ROOT / "shared/scripts"
sys.path.insert(0, str(SHARED_SCRIPTS))

from adapters import registry

def main() -> int:
    parser = argparse.ArgumentParser(description="Designly Model Prompt Compiler")
    parser.add_argument("--model", "-m", default="gemini-nano-banana", help="Target model adapter")
    parser.add_argument("--input", "-i", help="Path to JSON spec file or JSON string")
    parser.add_argument("--format", "-f", choices=["text", "json"], default="text", help="Output format")
    parser.add_argument("--list-models", action="store_true", help="List all supported model adapters")
    args = parser.parse_args()

    if args.list_models:
        print("=== Supported Designly Model Adapters ===")
        for a in registry.list_all():
            print(f"- {a['name']} ({a['display_name']}) [{a['category']}] -> Provider: {a['provider']}")
        return 0

    spec = None
    if args.input:
        in_path = Path(args.input)
        if in_path.is_file():
            spec = json.loads(in_path.read_text(encoding="utf-8"))
        else:
            try:
                spec = json.loads(args.input)
            except Exception:
                spec = {"subject": args.input}

    if spec is None:
        # Check if stdin has data without blocking
        has_stdin = False
        try:
            if not sys.stdin.isatty():
                r, _, _ = select.select([sys.stdin], [], [], 0.05)
                if r:
                    raw = sys.stdin.read().strip()
                    if raw:
                        has_stdin = True
                        try:
                            spec = json.loads(raw)
                        except Exception:
                            spec = {"subject": raw}
        except Exception:
            pass

    if spec is None:
        # Default sample specification
        spec = {
            "subject": "Minimalist luxury fragrance bottle on wet black obsidian rock",
            "lighting": "Sharp rim lighting with subtle warm fill",
            "aspect_ratio": "16:9",
            "copy": "EUPHORIA"
        }

    try:
        result = registry.compile(args.model, spec)
        if args.format == "json":
            print(json.dumps(result.to_dict(), indent=2, ensure_ascii=False))
        else:
            print(result.format_text())
        return 0
    except Exception as e:
        print(f"Error compiling prompt: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
