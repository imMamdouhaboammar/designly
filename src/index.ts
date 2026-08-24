/**
 * Designly Core Engine
 * Commercial Art Direction & Design Neural Mesh
 */
import { spawn } from "node:child_process";
import { fileURLToPath } from "node:url";
import { dirname, resolve } from "node:path";
import { readFileSync, existsSync } from "node:fs";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const ROOT_DIR = resolve(__dirname, "..");

export interface SkillManifest {
  name: string;
  path: string;
  entry: string;
  description: string;
}

export interface ModelAdapterInfo {
  name: string;
  displayName: string;
  category: "image" | "video" | "design";
  provider: string;
  supportedAspectRatios: string[];
}

export interface CompileOptions {
  model: string;
  spec: Record<string, unknown>;
  format?: "text" | "json";
}

export interface CompileResult {
  model: string;
  prompt: string;
  negativePrompt?: string;
  aspectRatio: string;
  mode: string;
  parameters: Record<string, unknown>;
  notes: string[];
}

/**
 * Load and return all 21 skills declared in skills.json
 */
export function getSkills(): SkillManifest[] {
  const skillsJsonPath = resolve(ROOT_DIR, "skills.json");
  if (!existsSync(skillsJsonPath)) {
    throw new Error(`skills.json not found at ${skillsJsonPath}`);
  }
  const data = JSON.parse(readFileSync(skillsJsonPath, "utf-8"));
  return data.skills || [];
}

/**
 * List all supported model adapters
 */
export const SUPPORTED_ADAPTERS: ModelAdapterInfo[] = [
  {
    name: "gemini-nano-banana",
    displayName: "Gemini Nano Banana (NB2 / NB Pro)",
    category: "image",
    provider: "google",
    supportedAspectRatios: ["1:1", "16:9", "9:16", "4:3", "3:4", "1:8", "8:1", "4:1", "1:4", "21:9"]
  },
  {
    name: "minimax-design",
    displayName: "MiniMax / Hailuo Design (Image & Video)",
    category: "image",
    provider: "minimax",
    supportedAspectRatios: ["1:1", "16:9", "9:16", "4:3", "3:4", "21:9"]
  },
  {
    name: "kimi-design",
    displayName: "Kimi Design (Moonshot Multimodal UI & Visual Systems)",
    category: "design",
    provider: "moonshot",
    supportedAspectRatios: ["1:1", "16:9", "9:16", "4:3", "3:4", "2:1", "1:2"]
  },
  {
    name: "claude-design",
    displayName: "Claude 3.7 Design & Artifacts",
    category: "design",
    provider: "anthropic",
    supportedAspectRatios: ["1:1", "16:9", "9:16", "4:3", "3:4", "custom"]
  },
  {
    name: "seedance",
    displayName: "ByteDance Seedance 2.5",
    category: "video",
    provider: "bytedance",
    supportedAspectRatios: ["16:9", "9:16", "1:1", "4:3", "21:9"]
  },
  {
    name: "kling",
    displayName: "Kuaishou Kling 3.0 / 2.6 Pro",
    category: "video",
    provider: "kuaishou",
    supportedAspectRatios: ["16:9", "9:16", "1:1", "4:3", "21:9"]
  },
  {
    name: "gpt-image-2",
    displayName: "OpenAI GPT Image 2",
    category: "image",
    provider: "openai",
    supportedAspectRatios: ["1:1", "16:9", "9:16", "4:3", "3:4", "3:1", "1:3"]
  },
  {
    name: "veo",
    displayName: "Google Veo 3 / 3.1",
    category: "video",
    provider: "google",
    supportedAspectRatios: ["16:9", "9:16", "1:1", "4:3"]
  }
];

/**
 * Programmatically compile a prompt using Designly model adapters
 */
export async function compilePrompt(options: CompileOptions): Promise<string> {
  const compilerScript = resolve(ROOT_DIR, "skills/prompt-compiler/scripts/compile_prompt.py");
  const specJson = JSON.stringify(options.spec || {});
  const args = ["-m", options.model || "gemini-nano-banana", "-f", options.format || "text", "-i", specJson];

  return new Promise((resolvePromise, rejectPromise) => {
    const child = spawn("python3", [compilerScript, ...args], {
      stdio: ["pipe", "pipe", "pipe"]
    });

    let stdout = "";
    let stderr = "";

    child.stdout.on("data", (chunk) => {
      stdout += chunk.toString();
    });
    child.stderr.on("data", (chunk) => {
      stderr += chunk.toString();
    });

    child.on("error", (err) => {
      rejectPromise(err);
    });

    child.on("close", (code) => {
      if (code === 0) {
        resolvePromise(stdout.trim());
      } else {
        rejectPromise(new Error(stderr.trim() || `Compiler exited with code ${code}`));
      }
    });
  });
}
