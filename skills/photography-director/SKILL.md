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

4. **Surface Material Physics**:
   - Specify material response accurately: diffuse reflection, specular roughness, anisotropy (brushed aluminum), translucency (subsurface scattering on skin/liquids), and index of refraction (glass/water).

5. **Output Contract**:
   - Return structured `craft_state.photography` inside `DesignSignalPacket`.

---

## 2. References & Schemas

- Shared Contract: [Signal Packet Schema](../../shared/contracts/signal-packet.schema.json)
- Shared Reference: [Composition and Photography](../../shared/references/composition-and-photography.md)
- Shared Reference: [Color and Contrast](../../shared/references/color-and-contrast.md)
