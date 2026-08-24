# MiniMax / Hailuo Design Reference Guide

MiniMax Image & Video engines excel at high dynamic motion, fluid physics, and rich cinematic lighting.

## Core Rules

1. **Volumetric Lighting**: Emphasize natural light direction, light falloff, bounce light, and atmospheric particles.
2. **Subject Action Dynamics**: Specify physical momentum, fabric movement, liquid splash, or facial expression nuances.
3. **Camera Directives**:
   - `Camera: pan_left / pan_right / tilt_up / tilt_down / zoom_in / dolly_in / orbit`
4. **Bilingual Tags**: Supports Chinese and English aesthetic qualifiers for enhanced material rendering.
5. **Negative Prompting**: Use explicit negative prompt exclusions to eliminate warped anatomy or synthetic noise.

## Output Example

```text
Model: minimax-image-01
Aspect Ratio: 1:1
Mode: generate
Parameters: prompt_optimizer: True, fidelity: high
Negative Prompt: low quality, distorted hands, morphing objects, jittery frame, oversaturated, blurry face

Prompt:
Subject: Minimalist luxury fragrance bottle on wet black obsidian rock
Action & Physics: subtle mist rising from water droplets, natural fluid surface tension
Environment & Light: Volumetric twilight with sharp directional rim lighting and dark indigo shadows
Composition: Centered balanced framing with strong focal isolation
Rendered Text: "EUPHORIA" with pristine sharpness and high legibility
```
