import { describe, it, expect } from "bun:test";
import * as designly from "../src/index.ts";

const makeBrief = () => ({
  id: "after-rain-01",
  brand: "NOVA",
  objective: "Introduce a new amber fragrance",
  subject: "Amber glass perfume bottle resting on black stone",
  keyMessage: "Warmth after the storm",
  exactCopy: "AFTER RAIN",
  visualAnchors: ["amber glass bottle", "wet basalt"],
  avoid: ["extra logos"],
  targets: [
    { id: "hero-image", model: "gpt-image-2", aspectRatio: "9:16" },
    { id: "hero-video", model: "veo", aspectRatio: "9:16", durationSeconds: 6 }
  ]
});

describe("Creative Intent Engine", () => {
  it("turns one creative brief into explicit shared locks and model-specific tasks without mutating it", () => {
    const createPlan = (designly as Record<string, any>).createCreativeIntentPlan;
    expect(typeof createPlan).toBe("function");
    const brief = makeBrief();
    const original = JSON.stringify(brief);

    const plan = createPlan(brief);

    expect(plan.briefId).toBe("after-rain-01");
    expect(plan.status).toBe("review_required");
    expect(plan.locks.map((lock: any) => [lock.id, lock.value])).toEqual([
      ["brand", "NOVA"],
      ["key_message", "Warmth after the storm"],
      ["exact_copy", "AFTER RAIN"],
      ["visual_anchor_1", "amber glass bottle"],
      ["visual_anchor_2", "wet basalt"],
      ["avoid_1", "extra logos"]
    ]);
    expect(plan.tasks.map((task: any) => [task.id, task.model, task.aspectRatio])).toEqual([
      ["hero-image", "gpt-image-2", "9:16"],
      ["hero-video", "veo", "9:16"]
    ]);
    expect(plan.tasks[0].spec.copy).toBe("AFTER RAIN");
    expect(plan.tasks[0].spec.subject).toContain("NOVA");
    expect(plan.tasks[0].spec.subject).toContain("wet basalt");
    expect(plan.tasks[0].spec.negative_prompt).toBe("extra logos");
    expect(plan.tasks[1].spec.duration).toBe(6);
    expect(JSON.stringify(brief)).toBe(original);
  });

  it("refuses to plan an unqualified brief with no actual campaign objective", () => {
    expect(() => designly.createCreativeIntentPlan({ ...makeBrief(), objective: "  " }))
      .toThrow(/objective/i);
  });

  it("rejects unsupported model and aspect ratio combinations before invoking a compiler", () => {
    expect(() => designly.createCreativeIntentPlan({
      ...makeBrief(), targets: [{ id: "hero", model: "imaginary-model", aspectRatio: "9:16" }]
    })).toThrow(/imaginary-model/);

    expect(() => designly.createCreativeIntentPlan({
      ...makeBrief(), targets: [{ id: "hero", model: "gpt-image-2", aspectRatio: "21:9" }]
    })).toThrow(/21:9/);
  });

  it("rejects duplicate target IDs and empty visual anchor locks", () => {
    const brief = makeBrief();
    expect(() => designly.createCreativeIntentPlan({
      ...brief, targets: [{ id: "repeat", model: "veo", aspectRatio: "9:16" }, { id: "repeat", model: "veo", aspectRatio: "9:16" }]
    })).toThrow(/duplicate/i);

    expect(() => designly.createCreativeIntentPlan({ ...brief, visualAnchors: [" "] }))
      .toThrow(/visual anchor/i);
  });

  it("keeps excluded visual elements as explicit requirements for later media review", () => {
    const plan = designly.createCreativeIntentPlan(makeBrief());
    expect(plan.locks).toContainEqual({
      id: "avoid_1", value: "extra logos", expectation: "must_be_absent"
    });
  });

  it("requires explicit creative approval before compiling model instructions", async () => {
    const compile = (designly as Record<string, any>).compileCreativeIntentPlan;
    expect(typeof compile).toBe("function");
    const plan = designly.createCreativeIntentPlan(makeBrief());

    await expect(compile(plan, { decision: "rejected", reviewer: "Creative Director" }))
      .rejects.toThrow(/approv/i);
    await expect(compile(plan, { decision: "approved", reviewer: " " }))
      .rejects.toThrow(/reviewer/i);
  });

  it("compiles one approved intent for image and video and reports missing exact-copy instructions", async () => {
    const plan = designly.createCreativeIntentPlan(makeBrief());
    const compiled = await (designly as Record<string, any>).compileCreativeIntentPlan(plan, {
      decision: "approved", reviewer: "Creative Director"
    });

    expect(compiled.briefId).toBe("after-rain-01");
    expect(compiled.outputs.map((output: any) => [output.taskId, output.model])).toEqual([
      ["hero-image", "gpt-image-2"],
      ["hero-video", "veo"]
    ]);
    expect(compiled.outputs[0].prompt).toContain("NOVA");
    expect(compiled.outputs[0].prompt).toContain("AFTER RAIN");
    expect(compiled.outputs[0].missingLockIds).toEqual(["avoid_1"]);
    expect(compiled.outputs[0].status).toBe("needs_review");
    expect(compiled.outputs[1].prompt).toContain("Warmth after the storm");
    expect(compiled.outputs[1].missingLockIds).toContain("exact_copy");
    expect(compiled.outputs[1].missingLockIds).toContain("avoid_1");
    expect(compiled.outputs[1].status).toBe("needs_review");
    expect(compiled.outputs[1].assetUrl).toBeUndefined();
  });

  it("keeps visual and brand claims unverified until actual observations are supplied", () => {
    const evaluate = (designly as Record<string, any>).evaluateCreativeIntent;
    expect(typeof evaluate).toBe("function");
    const report = evaluate(designly.createCreativeIntentPlan(makeBrief()), []);

    expect(report.status).toBe("needs_review");
    expect(report.scope).toBe("caller_supplied_observations");
    expect(report.findings).toHaveLength(12);
    expect(report.findings.every((finding: any) => finding.result === "unverified")).toBe(true);
  });

  it("blocks an observed exact-copy failure and only reports pass for complete positive evidence", () => {
    const plan = designly.createCreativeIntentPlan(makeBrief());
    const checks = {
      brand: true,
      key_message: true,
      exact_copy: true,
      visual_anchor_1: true,
      visual_anchor_2: true,
      avoid_1: true
    };
    const observations = [
      { taskId: "hero-image", source: "editor-review", checks },
      { taskId: "hero-video", source: "editor-review", checks: { ...checks, exact_copy: false } }
    ];

    const blocked = (designly as Record<string, any>).evaluateCreativeIntent(plan, observations);
    expect(blocked.status).toBe("blocked");
    expect(blocked.findings.find((finding: any) => finding.taskId === "hero-video" && finding.lockId === "exact_copy"))
      .toMatchObject({ result: "reported_fail", source: "editor-review" });

    const accepted = (designly as Record<string, any>).evaluateCreativeIntent(plan, [
      observations[0], { taskId: "hero-video", source: "editor-review", checks }
    ]);
    expect(accepted.status).toBe("reported_pass");
    expect(accepted.findings).toHaveLength(12);
  });

  it("rejects evidence for an unknown task or unknown creative lock", () => {
    expect(typeof (designly as Record<string, any>).evaluateCreativeIntent).toBe("function");
    const plan = designly.createCreativeIntentPlan(makeBrief());
    expect(() => (designly as Record<string, any>).evaluateCreativeIntent(plan, [
      { taskId: "phantom", source: "editor-review", checks: { brand: true } }
    ])).toThrow(/phantom/);
    expect(() => (designly as Record<string, any>).evaluateCreativeIntent(plan, [
      { taskId: "hero-image", source: "editor-review", checks: { imaginary_lock: true } }
    ])).toThrow(/imaginary_lock/);
  });

  it("does not report a vacuous pass when a caller removes all identity locks", () => {
    const plan = designly.createCreativeIntentPlan(makeBrief());
    plan.locks = [];
    expect(() => designly.evaluateCreativeIntent(plan, [])).toThrow(/lock/i);
  });
});
