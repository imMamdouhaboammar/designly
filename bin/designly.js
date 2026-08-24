#!/usr/bin/env node
/**
 * Designly CLI Binary
 * Commercial Art Direction & Design Neural Mesh
 */
import { spawn } from "node:child_process";
import { fileURLToPath } from "node:url";
import { dirname, resolve } from "node:path";
import { readFileSync, existsSync } from "node:fs";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const ROOT_DIR = resolve(__dirname, "..");

const VERSION = "5.0.2";

const HELP_TEXT = `
  Designly CLI v${VERSION}
  Commercial Art Direction & Design Neural Mesh Plugin

  USAGE:
    $ designly <command> [options]

  COMMANDS:
    compile                 Compile an Art Direction Spec into model-ready instructions
    list-models             List all 8 supported model adapters (Gemini, MiniMax, Kimi, Claude, etc.)
    skills <list|show>      Inspect the 21 modular Designly skills
    check                   Run skills.sh and Homebrew packaging validation
    version, -v, --version  Print current Designly version
    help, -h, --help        Show this help documentation

  OPTIONS for 'compile':
    -m, --model <name>      Target model adapter (default: gemini-nano-banana)
                            [gemini-nano-banana, minimax-design, kimi-design, claude-design, seedance, kling, gpt-image-2, veo]
    -i, --input <spec>      JSON specification string or path to JSON file
    -f, --format <text|json> Output format (default: text)

  EXAMPLES:
    $ designly list-models
    $ designly compile -m gemini-nano-banana -i '{"subject": "Obsidian flacon", "aspect_ratio": "16:9"}'
    $ designly compile -m kling -i '{"characters": ["Pilot A"], "speaker": "Pilot A", "dialogue": "Liftoff!"}'
    $ designly skills list
`;

async function main() {
  const args = process.argv.slice(2);
  const command = args[0] || "--help";

  if (command === "--help" || command === "-h" || command === "help") {
    console.log(HELP_TEXT);
    process.exit(0);
  }

  if (command === "--version" || command === "-v" || command === "version") {
    console.log(`designly v${VERSION}`);
    process.exit(0);
  }

  if (command === "list-models") {
    const script = resolve(ROOT_DIR, "skills/prompt-compiler/scripts/compile_prompt.py");
    runPythonScript(script, ["--list-models"]);
    return;
  }

  if (command === "skills") {
    const sub = args[1] || "list";
    const skillsJsonPath = resolve(ROOT_DIR, "skills.json");
    if (!existsSync(skillsJsonPath)) {
      console.error("Error: skills.json not found.");
      process.exit(1);
    }
    const data = JSON.parse(readFileSync(skillsJsonPath, "utf-8"));
    const skills = data.skills || [];

    if (sub === "list") {
      console.log(`\n=== Designly 21 Modular Skills (v${VERSION}) ===\n`);
      for (const s of skills) {
        console.log(`  * ${s.name.padEnd(24)} -> ${s.description}`);
      }
      console.log(`\nInstall via skills.sh: npx skills add imMamdouhaboammar/designly\n`);
      process.exit(0);
    } else if (sub === "show") {
      const target = args[2];
      if (!target) {
        console.error("Error: specify a skill name, e.g.: designly skills show image-director");
        process.exit(1);
      }
      const found = skills.find((s) => s.name === target);
      if (!found) {
        console.error(`Error: Skill '${target}' not found.`);
        process.exit(1);
      }
      console.log(`\nSkill: ${found.name}`);
      console.log(`Path:  ${found.path}`);
      console.log(`Entry: ${found.entry}`);
      console.log(`Desc:  ${found.description}\n`);
      process.exit(0);
    } else {
      console.error(`Unknown skills subcommand '${sub}'. Use 'list' or 'show'.`);
      process.exit(1);
    }
  }

  if (command === "check") {
    const pubScript = resolve(ROOT_DIR, "tools/publish_skills_sh.py");
    const brewScript = resolve(ROOT_DIR, "tools/homebrew_installer.py");
    runPythonScript(pubScript, ["--check"], () => {
      runPythonScript(brewScript, ["--check"]);
    });
    return;
  }

  if (command === "compile") {
    const script = resolve(ROOT_DIR, "skills/prompt-compiler/scripts/compile_prompt.py");
    const passArgs = args.slice(1);
    runPythonScript(script, passArgs);
    return;
  }

  // Fallback: pass directly to compile_prompt.py
  const script = resolve(ROOT_DIR, "skills/prompt-compiler/scripts/compile_prompt.py");
  runPythonScript(script, args);
}

function runPythonScript(scriptPath, scriptArgs, callback) {
  const child = spawn("python3", [scriptPath, ...scriptArgs], {
    stdio: "inherit"
  });

  child.on("close", (code) => {
    if (code === 0 && callback) {
      callback();
    } else {
      process.exit(code || 0);
    }
  });

  child.on("error", (err) => {
    console.error(`Failed to execute Python script: ${err.message}`);
    process.exit(1);
  });
}

main();
