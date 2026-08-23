---
name: photography-director
description: Commercial photography, studio lighting, camera optics, and material physics director. This skill should be used when directing camera focal length, depth of field, 3-point studio lighting systems, shutter speed, color temperature, or realistic surface material finishes.
---

# Photography Director

Photography Director specifies realistic photographic optics, camera physics, studio lighting environments, and physical material behaviors. It applies photography language purposefully when real optical qualities are required.

---

## 1. Core Workflow

1. **Camera Optics & Lens Choice**:
   - **Wide (24mm - 35mm)**: Environmental context, architectural space, dramatic perspective.
   - **Standard (50mm)**: Natural human eye perspective, documentary realism, undistorted geometry.
   - **Telephoto / Portrait (85mm - 135mm)**: Compressed perspective, flattering facial proportions, clean product packshots, shallow depth-of-field separation.
   - **Macro (100mm+)**: Extreme texture detail, jewelry, watch dial craftsmanship, microscopic surfaces.

2. **Aperture & Depth of Field**:
   - `f/1.4 - f/2.8`: Pronounced optical bokeh, subject isolation, soft dreamy falloff.
   - `f/5.6 - f/8.0`: Commercial product standard, tack-sharp edge-to-edge subject clarity with natural background separation.
   - `f/11 - f/16`: Deep depth-of-field for landscapes and complex architectural scenes.

3. **3-Point Studio Lighting Architecture**:
   - **Key Light**: Primary illumination source, defines form, mood, and directional shadow angle (e.g. 45° overhead softbox).
   - **Fill Light**: Controls shadow contrast ratio (e.g. 2:1 for high-key commercial, 8:1 for moody dramatic).
   - **Rim / Kicker Light**: Edge illumination separating dark subjects from dark backgrounds.
   - **Color Temperature**: Specify Kelvin values (e.g. 3200K warm tungsten, 5600K clean daylight, 6500K cool overcast).

4. **Surface Material Physics & Inclusive Lighting**:
   - Specify material response accurately: diffuse reflection, specular roughness, anisotropy (brushed aluminum), translucency (subsurface scattering on skin/liquids), and index of refraction (glass/water).
   - Melanin-accurate color grading: avoid ashen undertones or blown-out highlights on deeper complexions.

5. **Output Contract**:
   - Return structured `craft_state.photography` inside `DesignSignalPacket`.

---

## 2. Cross-Skill Neural Connections & References

### Peer & Downstream Skills
- [Composition Director](../composition-director/SKILL.md) — Spatial framing, focal anchors, and scale relationships
- [Manipulation Director](../manipulation-director/SKILL.md) — Environmental lighting alignment in composites
- [Taste Engine](../taste-engine/SKILL.md) — Reference lighting extraction and aesthetic rules
- [Prompt Compiler](../prompt-compiler/SKILL.md) — Translation into provider optical syntax
- [Designly Director](../designly-director/SKILL.md) — Lead orchestrator and lock manager

### Schemas & References
- [Signal Packet Schema](../../shared/contracts/signal-packet.schema.json) — Signal handoff contract
- [Composition and Photography](../../shared/references/composition-and-photography.md) — Photographic mechanics
- [Color and Contrast](../../shared/references/color-and-contrast.md) — Value contrast & color temperature
- [Inclusive Representation](../../shared/references/inclusive-representation-and-ethics.md) — Skin tone lighting & anti-bias
