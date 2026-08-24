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
  });

  it("test_supported_adapters_contains_required_six_models", () => {
    const names = SUPPORTED_ADAPTERS.map((a) => a.name);
    expect(names).toContain("gemini-nano-banana");
    expect(names).toContain("minimax-design");
    expect(names).toContain("kimi-design");
    expect(names).toContain("claude-design");
    expect(names).toContain("seedance");
    expect(names).toContain("kling");
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
});

describe("Designly CLI Binary Execution", () => {
  it("test_cli_version_flag_returns_semver_5_0_0", () => {
    const res = spawnSync("bun", ["./bin/designly.js", "--version"], { encoding: "utf-8" });
    expect(res.status).toBe(0);
    expect(res.stdout.trim()).toBe("designly v5.0.0");
  });

  it("test_cli_list_models_returns_all_adapters", () => {
    const res = spawnSync("bun", ["./bin/designly.js", "list-models"], { encoding: "utf-8" });
    expect(res.status).toBe(0);
    expect(res.stdout).toContain("gemini-nano-banana");
    expect(res.stdout).toContain("kling");
    expect(res.stdout).toContain("minimax-design");
  });

  it("test_cli_skills_list_outputs_21_skills", () => {
    const res = spawnSync("bun", ["./bin/designly.js", "skills", "list"], { encoding: "utf-8" });
    expect(res.status).toBe(0);
    expect(res.stdout).toContain("Designly 21 Modular Skills");
    expect(res.stdout).toContain("designly-director");
    expect(res.stdout).toContain("arabic-rtl-director");
  });
});
