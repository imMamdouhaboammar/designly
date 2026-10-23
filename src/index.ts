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

export interface CreativeIntentTarget {
  id: string;
  model: string;
  aspectRatio: string;
  durationSeconds?: number;
}

export interface CreativeIntentBrief {
  id: string;
  brand: string;
  objective: string;
  subject: string;
  keyMessage: string;
  exactCopy?: string;
  visualAnchors?: string[];
  avoid?: string[];
  targets: CreativeIntentTarget[];
}

export interface CreativeIntentLock {
  id: string;
  value: string;
  expectation: "must_be_present" | "must_be_absent";
}

export interface CreativeIntentTask {
  id: string;
  model: string;
  aspectRatio: string;
  spec: Record<string, unknown>;
}

export interface CreativeIntentPlan {
  briefId: string;
  status: "review_required";
  locks: CreativeIntentLock[];
  tasks: CreativeIntentTask[];
}

export interface CreativeIntentApproval {
  decision: "approved";
  reviewer: string;
}

export interface CompiledCreativeIntentOutput {
  taskId: string;
  model: string;
  prompt: string;
  status: "compiled" | "needs_review";
  missingLockIds: string[];
}

export interface CompiledCreativeIntent {
  briefId: string;
  approval: CreativeIntentApproval;
  outputs: CompiledCreativeIntentOutput[];
}

/** A caller's observation, not a claim that Designly inspected pixels or video. */
export interface CreativeIntentObservation {
  taskId: string;
  source: string;
  checks: Record<string, boolean | null>;
}

export interface CreativeIntentFinding {
  taskId: string;
  lockId: string;
  result: "reported_pass" | "reported_fail" | "unverified";
  source?: string;
}

export interface CreativeIntentReport {
  briefId: string;
  scope: "caller_supplied_observations";
  status: "reported_pass" | "needs_review" | "blocked";
  findings: CreativeIntentFinding[];
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

/** Derive a shared creative contract before selecting model-specific language. */
export function createCreativeIntentPlan(brief: CreativeIntentBrief): CreativeIntentPlan {
  for (const field of ["id", "brand", "objective", "subject", "keyMessage"] as const) {
    if (typeof brief?.[field] !== "string" || !brief[field].trim()) {
      throw new TypeError(`Creative brief ${field} must be a non-empty string`);
    }
  }
  if (!Array.isArray(brief.targets) || !brief.targets.length) {
    throw new TypeError("Creative brief targets must be a non-empty array");
  }
  for (const [field, values] of [["visual anchor", brief.visualAnchors], ["avoid", brief.avoid]] as const) {
    if (values !== undefined && (!Array.isArray(values) || values.some(value => typeof value !== "string" || !value.trim()))) {
      throw new TypeError(`Each ${field} must be a non-empty string`);
    }
  }
  if (brief.exactCopy !== undefined && (typeof brief.exactCopy !== "string" || !brief.exactCopy.trim())) {
    throw new TypeError("Exact copy must be a non-empty string when supplied");
  }
  const targetIds = new Set<string>();
  for (const target of brief.targets) {
    if (!target || typeof target.id !== "string" || !target.id.trim()) {
      throw new TypeError("Target id must be a non-empty string");
    }
    if (targetIds.has(target.id)) throw new TypeError(`Duplicate creative target ID: ${target.id}`);
    targetIds.add(target.id);
    const adapter = SUPPORTED_ADAPTERS.find(candidate => candidate.name === target.model);
    if (!adapter) throw new TypeError(`Unsupported creative model: ${target.model}`);
    if (!adapter.supportedAspectRatios.includes(target.aspectRatio)) {
      throw new TypeError(`Unsupported aspect ratio ${target.aspectRatio} for ${target.model}`);
    }
    if (target.durationSeconds !== undefined && (adapter.category !== "video" || !Number.isFinite(target.durationSeconds) || target.durationSeconds <= 0)) {
      throw new TypeError(`Invalid video duration for ${target.id}`);
    }
  }
  const locks: CreativeIntentLock[] = [
    { id: "brand", value: brief.brand, expectation: "must_be_present" },
    { id: "key_message", value: brief.keyMessage, expectation: "must_be_present" },
    ...(brief.exactCopy ? [{ id: "exact_copy", value: brief.exactCopy, expectation: "must_be_present" as const }] : []),
    ...(brief.visualAnchors ?? []).map((anchor, index) => ({ id: `visual_anchor_${index + 1}`, value: anchor, expectation: "must_be_present" as const })),
    ...(brief.avoid ?? []).map((element, index) => ({ id: `avoid_${index + 1}`, value: element, expectation: "must_be_absent" as const }))
  ];
  const subject = [
    brief.subject,
    `Brand: ${brief.brand}`,
    `Campaign objective: ${brief.objective}`,
    `Key message: ${brief.keyMessage}`,
    ...(brief.visualAnchors?.length ? [`Visual anchors: ${brief.visualAnchors.join(", ")}`] : [])
  ].join(". ");

  const tasks = brief.targets.map((target): CreativeIntentTask => {
    const spec: Record<string, unknown> = {
      subject,
      concept: subject,
      aspect_ratio: target.aspectRatio
    };
    if (brief.exactCopy) spec.copy = brief.exactCopy;
    if (brief.avoid?.length) spec.negative_prompt = brief.avoid.join(", ");
    if (target.durationSeconds !== undefined) spec.duration = target.durationSeconds;
    return { id: target.id, model: target.model, aspectRatio: target.aspectRatio, spec };
  });

  return { briefId: brief.id, status: "review_required", locks, tasks };
}

/**
 * Programmatically compile a prompt using Designly model adapters
 */
export async function compilePrompt(options: CompileOptions): Promise<string> {
  const compilerScript = resolve(ROOT_DIR, "skills/prompt-compiler/scripts/compile_prompt.py");
  const specJson = JSON.stringify(options.spec || {});
  // JSON belongs on stdin, not argv: large creative briefs can exceed OS arg limits.
  const args = ["-m", options.model || "gemini-nano-banana", "-f", options.format || "text"];

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

    child.stdin.on("error", (err) => {
      rejectPromise(err);
    });

    child.stdin.end(specJson);

    child.on("close", (code) => {
      if (code === 0) {
        resolvePromise(stdout.trim());
      } else {
        rejectPromise(new Error(stderr.trim() || `Compiler exited with code ${code}`));
      }
    });
  });
}

/** Compile only an explicitly reviewed plan. Does not generate or inspect media assets. */
export async function compileCreativeIntentPlan(
  plan: CreativeIntentPlan,
  approval: CreativeIntentApproval
): Promise<CompiledCreativeIntent> {
  if (approval?.decision !== "approved") {
    throw new TypeError("Creative approval is required before compilation");
  }
  if (typeof approval.reviewer !== "string" || !approval.reviewer.trim()) {
    throw new TypeError("Creative approval reviewer must be identified");
  }
  if (!plan || !Array.isArray(plan.tasks) || !Array.isArray(plan.locks) || !plan.tasks.length || !plan.locks.length) {
    throw new TypeError("A valid creative intent plan is required");
  }

  const outputs = await Promise.all(plan.tasks.map(async (task): Promise<CompiledCreativeIntentOutput> => {
    const prompt = await compilePrompt({ model: task.model, spec: task.spec });
    const missingLockIds = plan.locks.filter(lock => !prompt.includes(lock.value)).map(lock => lock.id);
    return {
      taskId: task.id,
      model: task.model,
      prompt,
      status: missingLockIds.length ? "needs_review" : "compiled",
      missingLockIds
    };
  }));

  return { briefId: plan.briefId, approval: { ...approval }, outputs };
}

/** Compare declared review observations against every locked creative requirement. */
export function evaluateCreativeIntent(
  plan: CreativeIntentPlan,
  observations: CreativeIntentObservation[]
): CreativeIntentReport {
  if (!plan || !Array.isArray(plan.tasks) || !Array.isArray(plan.locks) || !plan.tasks.length || !plan.locks.length || !Array.isArray(observations)) {
    throw new TypeError("A creative plan with identity locks and an observations array are required");
  }
  const knownTasks = new Set(plan.tasks.map(task => task.id));
  const knownLocks = new Set(plan.locks.map(lock => lock.id));
  const evidence = new Map<string, CreativeIntentObservation>();
  for (const observation of observations) {
    if (!observation || !knownTasks.has(observation.taskId)) {
      throw new TypeError(`Unknown creative task: ${observation?.taskId}`);
    }
    if (evidence.has(observation.taskId)) {
      throw new TypeError(`Duplicate observations for task: ${observation.taskId}`);
    }
    if (typeof observation.source !== "string" || !observation.source.trim()) {
      throw new TypeError(`Observation source is required for ${observation.taskId}`);
    }
    if (!observation.checks || Array.isArray(observation.checks) || typeof observation.checks !== "object") {
      throw new TypeError(`Observation checks must be an object for ${observation.taskId}`);
    }
    for (const [lockId, value] of Object.entries(observation.checks)) {
      if (!knownLocks.has(lockId)) throw new TypeError(`Unknown creative lock: ${lockId}`);
      if (value !== null && typeof value !== "boolean") {
        throw new TypeError(`Observation for ${lockId} must be true, false, or null`);
      }
    }
    evidence.set(observation.taskId, observation);
  }

  const findings = plan.tasks.flatMap((task): CreativeIntentFinding[] => {
    const observation = evidence.get(task.id);
    return plan.locks.map(lock => {
      const value = observation?.checks[lock.id];
      if (value === undefined || value === null) {
        return { taskId: task.id, lockId: lock.id, result: "unverified" };
      }
      return {
        taskId: task.id,
        lockId: lock.id,
        result: value ? "reported_pass" : "reported_fail",
        source: observation!.source
      };
    });
  });

  const status = findings.some(finding => finding.result === "reported_fail")
    ? "blocked"
    : findings.some(finding => finding.result === "unverified")
      ? "needs_review"
      : "reported_pass";
  return { briefId: plan.briefId, scope: "caller_supplied_observations", status, findings };
}
