import { describe, it, expect } from "bun:test";
import { spawnSync } from "node:child_process";
import { getSkills, SUPPORTED_ADAPTERS, compilePrompt } from "../src/index.ts";

describe("Designly Core Library Exports", () => {
  it("test_get_skills_returns_all_21_declared_skills", () => {
    const skills = getSkills();
    expect(skills.length).toBe(21);
    const names = skills.map((s) => s.name);
    expect(names).toContain("designly-director");
    expect(names).toContain("image-director");
    expect(names).toContain("video-director");
    expect(names).toContain("prompt-compiler");
    expect(names).toContain("arabic-rtl-director");
    expect(names).toContain("visual-qa");
    expect(names).toContain("taste-engine");
  });

  it("test_supported_adapters_contains_all_8_models", () => {
    const names = SUPPORTED_ADAPTERS.map((a) => a.name);
    expect(names).toContain("gemini-nano-banana");
    expect(names).toContain("minimax-design");
    expect(names).toContain("kimi-design");
    expect(names).toContain("claude-design");
    expect(names).toContain("seedance");
    expect(names).toContain("kling");
    expect(names).toContain("gpt-image-2");
    expect(names).toContain("veo");
  });

  it("test_compile_prompt_generates_valid_gemini_prose", async () => {
    const output = await compilePrompt({
      model: "gemini-nano-banana",
      spec: {
        subject: "Minimalist titanium wristwatch",
        lighting: "Diffused soft studio lighting",
        aspect_ratio: "16:9",
        copy: "HOROLOGY"
      }
    });

    expect(output).toContain("Model: gemini-nano-banana-pro");
    expect(output).toContain("Minimalist titanium wristwatch");
    expect(output).toContain('"HOROLOGY"');
  });

  it("test_compile_prompt_generates_valid_kling_lip_sync", async () => {
    const output = await compilePrompt({
      model: "kling",
      spec: {
        characters: ["Commander Shepard"],
        subject: "Spaceship bridge",
        speaker: "Character A",
        dialogue: "Engage warp drive!"
      }
    });

    expect(output).toContain("Model: kling-3.0-pro");
    expect(output).toContain("[Character A: Commander Shepard]");
    expect(output).toContain('Native Lip-Sync Dialogue: [Character A] "Engage warp drive!"');
  });

  it("test_compile_prompt_generates_valid_seedance_timeline", async () => {
    const output = await compilePrompt({
      model: "seedance",
      spec: {
        dramaturgy: "Astronaut exploring crystal cave",
        duration: 20,
        shots: [
          { start: "00:00", end: "00:10", camera: "Wide tracking", action: "Steps onto reflective crystals" },
          { start: "00:10", end: "00:20", camera: "Close-up", action: "Reaches out hand", speaker: "Astronaut", dialogue: "Incredible." }
        ]
      }
    });

    expect(output).toContain("Model: seedance-2.5-pro");
    expect(output).toContain("SEEDANCE 2.5 DRAMATURGY");
    expect(output).toContain('{ Astronaut: "Incredible." }');
  });

  it("test_compile_prompt_generates_valid_claude_design_svg", async () => {
    const output = await compilePrompt({
      model: "claude-design",
      spec: {
        subject: "Interactive Analytics Metric Card",
        output_format: "svg",
        interactive: true,
        copy: "99.98% SUCCESS RATE"
      }
    });

    expect(output).toContain("Model: claude-3-7-sonnet-design");
    expect(output).toContain("Claude Design System & Artifact Contract");
    expect(output).toContain("viewBox=");
    expect(output).toContain("Interactive State Machine Matrix");
    expect(output).toContain('"99.98% SUCCESS RATE"');
  });

  it("test_compile_prompt_generates_valid_kimi_design_spec", async () => {
    const output = await compilePrompt({
      model: "kimi-design",
      spec: {
        concept: "E-Commerce Checkout Flow",
        colors: ["#1E293B", "#38BDF8"],
        copy: "CHECKOUT COMPLETED"
      }
    });

    expect(output).toContain("Model: kimi-k1.5-design");
    expect(output).toContain("KIMI MULTIMODAL DESIGN SYSTEM");
    expect(output).toContain("#38BDF8");
    expect(output).toContain('"CHECKOUT COMPLETED"');
  });

  it("test_compile_prompt_generates_valid_minimax_design_spec", async () => {
    const output = await compilePrompt({
      model: "minimax-design",
      spec: {
        subject: "Supercar drifting around sharp curve",
        action: "Tires smoking on asphalt under sunset light",
        camera_motion: "orbit_counterclockwise",
        duration: 5
      }
    });

    expect(output).toContain("Model: minimax-video-01");
    expect(output).toContain("Subject: Supercar drifting around sharp curve");
    expect(output).toContain("orbit_counterclockwise");
  });

  it("test_compile_prompt_generates_valid_gpt_image_template", async () => {
    const output = await compilePrompt({
      model: "gpt-image-2",
      spec: {
        subject: "Modern architectural villa",
        scene: "Coastal cliffside at twilight",
        copy: "HORIZON RESIDENCES"
      }
    });

    expect(output).toContain("Model: gpt-image-2");
    expect(output).toContain("Scene: Coastal cliffside at twilight");
    expect(output).toContain("Subject: Modern architectural villa");
    expect(output).toContain('"HORIZON RESIDENCES"');
  });

  it("test_compile_prompt_generates_valid_veo_json_spec", async () => {
    const output = await compilePrompt({
      model: "veo",
      format: "text",
      spec: {
        concept: "Macro dew drop falling from lush monstera leaf",
        camera_motion: "Extreme macro slow push-in",
        duration: 6
      }
    });

    expect(output).toContain("Model: veo-3.1");
    expect(output).toContain("veo-3.1");
    expect(output).toContain("Macro dew drop falling from lush monstera leaf");
  });

  it("test_compile_prompt_rejects_unknown_model", async () => {
    expect(
      compilePrompt({
        model: "non-existent-unknown-model",
        spec: { subject: "Test" }
      })
    ).rejects.toThrow();
  });
});

describe("Designly CLI Binary Execution", () => {
  it("test_cli_version_flag_returns_semver_5_0_1", () => {
    const res = spawnSync("bun", ["./bin/designly.js", "--version"], { encoding: "utf-8" });
    expect(res.status).toBe(0);
    expect(res.stdout.trim()).toBe("designly v5.0.2");
  });

  it("test_cli_help_flag_displays_usage_guide", () => {
    const res = spawnSync("bun", ["./bin/designly.js", "--help"], { encoding: "utf-8" });
    expect(res.status).toBe(0);
    expect(res.stdout).toContain("Designly CLI");
    expect(res.stdout).toContain("COMMANDS:");
    expect(res.stdout).toContain("compile");
    expect(res.stdout).toContain("list-models");
  });

  it("test_cli_list_models_returns_all_adapters", () => {
    const res = spawnSync("bun", ["./bin/designly.js", "list-models"], { encoding: "utf-8" });
    expect(res.status).toBe(0);
    expect(res.stdout).toContain("gemini-nano-banana");
    expect(res.stdout).toContain("kling");
    expect(res.stdout).toContain("minimax-design");
    expect(res.stdout).toContain("claude-design");
    expect(res.stdout).toContain("kimi-design");
    expect(res.stdout).toContain("seedance");
    expect(res.stdout).toContain("gpt-image-2");
    expect(res.stdout).toContain("veo");
  });

  it("test_cli_skills_list_outputs_21_skills", () => {
    const res = spawnSync("bun", ["./bin/designly.js", "skills", "list"], { encoding: "utf-8" });
    expect(res.status).toBe(0);
    expect(res.stdout).toContain("Designly 21 Modular Skills");
    expect(res.stdout).toContain("designly-director");
    expect(res.stdout).toContain("arabic-rtl-director");
  });

  it("test_cli_skills_show_outputs_target_skill_details", () => {
    const res = spawnSync("bun", ["./bin/designly.js", "skills", "show", "image-director"], { encoding: "utf-8" });
    expect(res.status).toBe(0);
    expect(res.stdout).toContain("Skill: image-director");
    expect(res.stdout).toContain("Path:  skills/image-director");
  });

  it("test_cli_skills_show_unknown_skill_fails_gracefully", () => {
    const res = spawnSync("bun", ["./bin/designly.js", "skills", "show", "non-existent-skill"], { encoding: "utf-8" });
    expect(res.status).toBe(1);
    expect(res.stderr).toContain("Skill 'non-existent-skill' not found");
  });

  it("test_cli_compile_executes_prompt_compilation", () => {
    const res = spawnSync(
      "bun",
      ["./bin/designly.js", "compile", "-m", "gemini-nano-banana", "-i", '{"subject": "Diamond necklace on velvet"}'],
      { encoding: "utf-8" }
    );
    expect(res.status).toBe(0);
    expect(res.stdout).toContain("Diamond necklace on velvet");
  });
});
