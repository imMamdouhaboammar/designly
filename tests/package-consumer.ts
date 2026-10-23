/** Minimal public TypeScript consumer contract (compiled during CI). */
import {
  compilePrompt,
  compileCreativeIntentPlan,
  createCreativeIntentPlan,
  evaluateCreativeIntent,
  getSkills,
  SUPPORTED_ADAPTERS,
  type CreativeIntentBrief
} from "../dist/index.js";

const skills: string[] = getSkills().map((skill) => skill.name);
const models: string[] = SUPPORTED_ADAPTERS.map((adapter) => adapter.name);

void skills;
void models;
void compilePrompt({ model: "veo", spec: { subject: "Macro product reveal" } });

// @ts-expect-error A creative spec is required by the published API.
void compilePrompt({ model: "veo" });

const campaign: CreativeIntentBrief = {
  id: "typescript-consumer",
  brand: "Sample Brand",
  objective: "Introduce a new product",
  subject: "Product on a neutral studio background",
  keyMessage: "Built with care",
  targets: [{ id: "hero", model: "gpt-image-2", aspectRatio: "1:1" }]
};

const plan = createCreativeIntentPlan(campaign);
void compileCreativeIntentPlan(plan, { decision: "approved", reviewer: "Editor" });
void evaluateCreativeIntent(plan, []);

// @ts-expect-error An intent plan cannot be compiled with a rejected approval.
void compileCreativeIntentPlan(plan, { decision: "rejected", reviewer: "Editor" });
