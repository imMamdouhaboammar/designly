/** Minimal public TypeScript consumer contract (compiled during CI). */
import { compilePrompt, getSkills, SUPPORTED_ADAPTERS } from "../dist/index.js";

const skills: string[] = getSkills().map((skill) => skill.name);
const models: string[] = SUPPORTED_ADAPTERS.map((adapter) => adapter.name);

void skills;
void models;
void compilePrompt({ model: "veo", spec: { subject: "Macro product reveal" } });

// @ts-expect-error A creative spec is required by the published API.
void compilePrompt({ model: "veo" });
