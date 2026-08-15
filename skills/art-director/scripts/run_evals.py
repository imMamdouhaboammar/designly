#!/usr/bin/env python3
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals/evals.jsonl"


def classify(prompt):
    p = prompt.lower()
    if any(x in p for x in ["remember this visual reference", "use ref-", "build my taste profile", "recall my reference", "forget ref-", "taste memory"]):
        task = "taste-memory"
    elif any(x in p for x in ["review this", "critique this", "blocks approval"]):
        task = "review"
    elif any(x in p for x in ["edit this image", "change only", "preserve everything", "fix this poster"]):
        task = "edit"
    elif any(x in p for x in ["composite", "insert this", "manipulation", "replace this object"]):
        task = "manipulation"
    elif any(x in p for x in ["reference", "recreate the visual logic", "match this visual"]):
        task = "reference"
    elif any(x in p for x in ["exact headline", "arabic poster", "typography-heavy", "poster with exact"]):
        task = "typography-heavy"
    elif any(x in p for x in ["campaign", "related social assets", "visual dna", "series"]):
        task = "campaign"
    else:
        task = "generate"

    if task == "taste-memory":
        mode = "taste-profile"
    elif any(x in p for x in ["only the final image generation prompt", "prompt only"]):
        mode = "quick"
    elif task == "edit":
        mode = "edit"
    elif task == "manipulation":
        mode = "manipulation"
    elif task == "reference":
        mode = "reference-replication"
    elif task == "campaign":
        mode = "campaign"
    elif any(x in p for x in ["three genuinely different", "three different visual concepts", "explore three"]):
        mode = "exploration"
    else:
        mode = "director"
    return task, mode


def main():
    failures = 0
    skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    refs = {p.name for p in (ROOT / "references").glob("*.md")}
    for line in EVALS.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        case = json.loads(line)
        task, mode = classify(case["prompt"])
        case_fail = []
        if task != case["expected_task"]:
            case_fail.append(f"task={task}, expected={case['expected_task']}")
        if mode != case["expected_mode"]:
            case_fail.append(f"mode={mode}, expected={case['expected_mode']}")
        for ref in case.get("requires", []):
            if ref not in refs:
                case_fail.append(f"missing reference file {ref}")
            elif f"references/{ref}" not in skill_text:
                case_fail.append(f"reference not discoverable from SKILL.md: {ref}")
        if case_fail:
            failures += 1
            print(f"FAIL {case['id']}: " + "; ".join(case_fail))
        else:
            print(f"PASS {case['id']}")
    print(f"\n{len(EVALS.read_text(encoding='utf-8').splitlines()) - failures} passed, {failures} failed")
    return 1 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
