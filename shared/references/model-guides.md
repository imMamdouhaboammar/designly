# Model Guides

Provider behavior changes over time, so use this as routing guidance rather than immutable capability claims

Verified against current public OpenAI image documentation on 2026-08-15

## OpenAI GPT Image 2

`gpt-image-2` is the current OpenAI state-of-the-art image generation and editing model

Use concise natural instructions that describe the intended image and only the details that materially affect it

It supports text and image input, image output, flexible sizes, image generation, and image editing

For API implementations

- use the Image API for a straightforward generation or edit request
- use the Responses API when the experience benefits from conversational or multi-turn image editing and context

For ChatGPT/Codex hosts with a built-in image tool, use the host tool rather than constructing API code

## Generic multimodal image model

If exact provider behavior is unknown

- keep the prompt concrete and visual
- provide reference images explicitly when supported
- use protected-region language for edits
- avoid unsupported parameter assumptions
- inspect output rather than trusting prompt compliance

## Typography caution

Even capable image models can make text mistakes

When exact typography matters, use the two-pass foundation plus text-correction workflow and inspect the result

## Capability fallback

If a requested operation is not supported by the available image tool

- do not pretend it is supported
- return the Art Direction Spec and an executable prompt/edit contract for a capable tool
