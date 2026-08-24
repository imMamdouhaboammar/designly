# MiniMax Video Directing Reference Guide

Directing high-motion AI video sequences for MiniMax Hailuo Video Engine (T2V-01 / I2V-01).

## Core Rules

1. **Shot Length & Motion Intensity**:
   - Duration: 6 seconds (default standard) or 10 seconds (extended action).
   - Motion Intensity slider: `1-3` for ambient/mood, `4-7` for character/dialogue, `8-10` for high-speed action/chase.
2. **Camera Syntax**:
   - `Camera Movement: pan_left | pan_right | tilt_up | tilt_down | zoom_in | zoom_out | dolly_in | dolly_out | truck_left | truck_right | orbit_clockwise | crane_shot`
3. **Physical Dynamics**:
   - Describe mass, weight, fluid drag, wind interaction, and footstep contact explicitly.
4. **Negative Prompting**:
   - Purge character face warping, extra limbs, frame jitter, and abrupt lighting flicker.
