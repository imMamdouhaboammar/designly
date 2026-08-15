---
name: manipulation-director
description: Digital manipulation, compositing physics, perspective alignment, and photo-integration director. This skill should be used when combining multiple image elements, planning compositing perspective and scale, enforcing realistic contact shadows and reflections, or directing impossible/surreal advertising scenes with internal physical consistency.
---

# Manipulation Director

Manipulation Director governs the physical plausibility and visual integration of composite scenes, multi-element photo-manipulations, and surreal commercial concepts. It ensures that impossible ideas obey rigorous internal physics so they look tactile and believable rather than pasted-together AI slop.

---

## 1. Core Workflow

1. **Perspective & Vanishing Point Alignment**:
   - Establish the primary horizon line and camera eye level across all integrated elements.
   - Ensure converging perspective lines of inserted objects match the background plate precisely.

2. **Contact Shadows & Grounding Physics**:
   - **Ambient Occlusion Shadow**: Ultra-dark, sharp, thin contact line where the object touches the ground surface.
   - **Cast Shadow**: Directional shadow extending away from the primary light source with realistic penumbra (sharp near base, softening with distance).
   - **Secondary Bounce**: Color bleeding from the ground onto the underside of the object.

3. **Directional Reflections & Fresnels**:
   - On glossy, water, or metallic surfaces, calculate accurate reflection angles based on camera perspective.
   - Apply Fresnel falloff (reflections strengthen at grazing angles).

4. **Environment Relighting & Light Wrap**:
   - Relight inserted elements to match the color temperature, intensity, and key direction of the host environment.
   - Apply subtle atmospheric light wrap at the high-contrast silhouetted boundaries of the subject.

5. **Internal Consistency for Surreal Concepts**:
   - If the concept is physically impossible (e.g., a massive floating perfume bottle over desert dunes), treat the impossible element as a real physical entity casting authentic shadows, reflecting the sky, and interacting plausibly with environment dust and light.

6. **Output Contract**:
   - Return structured `craft_state.manipulation` inside `DesignSignalPacket`.

---

## 2. References & Schemas

- Shared Contract: [Signal Packet Schema](../../shared/contracts/signal-packet.schema.json)
- Shared Reference: [Advertising Manipulation](../../shared/references/advertising-manipulation.md)
- Shared Reference: [Image Editing Guide](../../shared/references/image-editing.md)
