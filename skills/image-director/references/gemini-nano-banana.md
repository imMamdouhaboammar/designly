# Gemini Nano Banana (NB2 / NB Pro) Reference Guide

Gemini Nano Banana models operate on descriptive visual relationships and spatial reasoning rather than tokenized keyword tags.

## Core Rules

1. **Natural Language Prose**: Write 1-2 coherent paragraphs describing subject, lighting, environment, materials, and composition.
2. **Do Not Specify Numeric Camera Settings**: Avoid `50mm`, `f/1.4`, `ISO 100`. NB2 ignores these numbers. Instead, describe visual perspective: "shallow focus with soft foreground bokeh", "wide expansive angle capturing the full architectural facade".
3. **Extreme Aspect Ratios**: Native support for `1:8`, `8:1`, `1:4`, `4:1`, `16:9`, `9:16`, `1:1`, `21:9`.
4. **Image Grounding**: Queries real-world knowledge for accurate depiction of cultural landmarks, specific flora/fauna, and mechanical components.
5. **Thinking Mode & Spatial JSON**: For multi-element scenes (5+ subjects), format as JSON to guarantee clean spatial separation without crowding.
6. **Reference Images**: Up to 14 references can be indexed (`[Ref 1: ...]`).

## Generation Example

```text
Model: gemini-nano-banana-pro
Aspect Ratio: 16:9
Mode: generate
Parameters: variant: pro, grounding: True, thinking_mode: True

Prompt:
A minimalist luxury glass fragrance bottle resting on wet black obsidian rock in Iceland during late dusk. The surface reflects deep indigo sky tones with sharp rim lighting accentuating the bevelled edges of the flacon. Fine condensation droplets cling to the amber glass.

In the background, basalt columns recede into a soft atmospheric mist with gentle ambient ocean spray. Clean negative space fills the upper third of the frame.

Render exact text "EUPHORIA" embossed cleanly on the lower center label.
```
