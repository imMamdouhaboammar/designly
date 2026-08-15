#!/usr/bin/env python3
import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("prompt_lint",ROOT/"scripts/prompt_lint.py")
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
cases=[
("active-effect-stack","Create a futuristic ad with neon glow particles chrome holograms lens flare and smoke",True),
("negative-list","Create a restrained product photograph. Avoid neon, glow, particles, chrome, holograms, lens flare, smoke, and fake dashboards.",False),
("contrast-clause","Avoid neon and particles, but add one subtle glow behind the product for figure-ground separation.",False),
("camera-dump","Use 24mm 35mm 50mm 85mm f/1.8 ISO 100",False),
]
failed=0
for name,text,expect_major in cases:
    issues=mod.lint(text); got=any(s=="major" for s,_ in issues)
    if got==expect_major: print(f"PASS {name}")
    else: failed+=1; print(f"FAIL {name}: {issues}")
print(f"\n{len(cases)-failed} passed, {failed} failed")
raise SystemExit(1 if failed else 0)
