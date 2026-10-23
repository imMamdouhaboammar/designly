/** Run from the repository root: bun examples/creative-intent-demo.ts */
import {
  compileCreativeIntentPlan,
  createCreativeIntentPlan,
  evaluateCreativeIntent
} from "../src/index.ts";

const brief = {
  id: "after-rain-launch",
  brand: "NOVA",
  objective: "Introduce a premium amber fragrance",
  subject: "Amber perfume bottle on wet volcanic stone",
  keyMessage: "Warmth after the storm",
  exactCopy: "AFTER RAIN",
  visualAnchors: ["amber glass bottle", "wet basalt", "warm rim light"],
  avoid: ["additional logos", "unapproved packaging"],
  targets: [
    { id: "portrait", model: "gpt-image-2", aspectRatio: "9:16" },
    { id: "reveal", model: "veo", aspectRatio: "9:16", durationSeconds: 6 }
  ]
};

const plan = createCreativeIntentPlan(brief);

// In a real workflow, collect an actual editorial decision before this call.
// This demo approval is illustrative provenance, not authenticated identity.
const compiled = await compileCreativeIntentPlan(plan, {
  decision: "approved",
  reviewer: "demo-editor"
});

// No media were generated or inspected. The report MUST remain unverified.
const report = evaluateCreativeIntent(plan, []);

console.log(JSON.stringify({
  briefId: plan.briefId,
  locks: plan.locks,
  outputs: compiled.outputs.map(output => ({
    taskId: output.taskId,
    model: output.model,
    status: output.status,
    missingLockIds: output.missingLockIds,
    prompt: output.prompt
  })),
  evidenceReport: report
}, null, 2));
