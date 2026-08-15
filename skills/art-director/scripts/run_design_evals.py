#!/usr/bin/env python3
import json, importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("design_lint",ROOT/"scripts/design_lint.py")
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
cases=json.loads((ROOT/"evals/design-evals.json").read_text(encoding="utf-8"))
failed=0
for case in cases:
    data=json.loads((ROOT/"evals"/case["file"]).read_text(encoding="utf-8"))
    findings=mod.lint(data)
    got=any(f["severity"] in {"major","critical"} for f in findings)
    exp=case["expect_major_or_critical"]
    if got==exp: print(f"PASS {case['id']}")
    else:
        failed+=1; print(f"FAIL {case['id']}: got blocker={got}, expected={exp}; findings={findings}")
print(f"\n{len(cases)-failed} passed, {failed} failed")
raise SystemExit(1 if failed else 0)
