#!/usr/bin/env python3
import json, re, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PLUGIN_ROOT=ROOT.parents[1]
SKILL=ROOT/"SKILL.md"
NAME_RE=re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE=re.compile(r"\]\((references/[^)]+|examples/[^)]+|assets/[^)]+|schemas/[^)]+|evals/[^)]+|scripts/[^)]+)\)")

def parse_frontmatter(text):
    if not text.startswith("---\n"): raise ValueError("SKILL.md must start with YAML frontmatter")
    end=text.find("\n---\n",4)
    if end<0: raise ValueError("SKILL.md frontmatter closing marker missing")
    vals={}
    for line in text[4:end].splitlines():
        if not line or line.startswith((" ","\t")): continue
        if ":" in line:
            k,v=line.split(":",1); vals[k.strip()]=v.strip().strip('"').strip("'")
    return vals

def check(cond,msg,errors):
    print(("PASS " if cond else "FAIL ")+msg)
    if not cond: errors.append(msg)

def run_script(name,errors,*args):
    p=ROOT/"scripts"/name
    r=subprocess.run([sys.executable,str(p),*map(str,args)],capture_output=True,text=True)
    if r.stdout.strip(): print(r.stdout.rstrip())
    if r.returncode!=0:
        errors.append(f"{name} failed")
        if r.stderr.strip(): print(r.stderr.rstrip())

def main():
    errors=[]
    text=SKILL.read_text(encoding="utf-8"); fm=parse_frontmatter(text)
    name=fm.get("name",""); desc=fm.get("description","")
    check(bool(name),"frontmatter has name",errors)
    check(bool(desc),"frontmatter has description",errors)
    check(name==ROOT.name,"skill name matches directory",errors)
    check(bool(NAME_RE.fullmatch(name)),"skill name uses lowercase hyphen format",errors)
    check(len(name)<=64,"skill name <= 64 chars",errors)
    check(0<len(desc)<=1024,"description length 1..1024",errors)
    check("This skill should be used when" in desc,"description states trigger conditions",errors)
    check(len(text.splitlines())<500,"SKILL.md under 500 lines",errors)
    check("generate or edit directly" in text.lower(),"direct image execution behavior present",errors)
    check("design preflight" in text.lower(),"design preflight is part of runtime",errors)
    check("design principles" in text.lower(),"design-principle layer is explicit",errors)
    check("weighted score >= 92" in text.lower(),"release threshold 92 present",errors)
    check("category floors" in text.lower(),"category floors prevent average-score masking",errors)
    check("effect-subtraction test" in text.lower(),"effect-subtraction anti-slop test present",errors)
    check("brand-off test" in text.lower(),"brand-specificity test present",errors)
    check("thumbnail test" in text.lower() and "grayscale test" in text.lower(),"perception tests present",errors)
    check("rightmost 35 to 42 percent" not in text.lower(),"no arbitrary fixed RTL percentage rule in SKILL",errors)
    arabic=(ROOT/"references/arabic-rtl-and-cultural.md").read_text(encoding="utf-8").lower()
    check("fixed percentage" in arabic and "not" in arabic,"RTL guidance rejects universal fixed-percentage geometry",errors)
    check(not (ROOT/"references/visual-taste-and-anti-slop.md").exists(),"deprecated duplicate anti-slop reference removed",errors)
    check((ROOT/"references/ai-slop-taxonomy.md").exists(),"AI slop taxonomy exists",errors)
    check((ROOT/"references/layout-grid-and-spacing.md").exists(),"layout/grid/spacing reference exists",errors)
    check((ROOT/"references/gestalt-and-perception.md").exists(),"Gestalt/perception reference exists",errors)
    check((ROOT/"references/color-and-contrast.md").exists(),"color/contrast reference exists",errors)
    check((ROOT/"references/taste-engine.md").exists(),"Taste Engine reference exists",errors)
    check((ROOT/"references/reference-memory.md").exists(),"Reference Memory reference exists",errors)
    check((ROOT/"schemas/taste-profile.schema.json").exists(),"Taste Profile schema exists",errors)
    check((ROOT/"agents/openai.yaml").exists(),"OpenAI skill interface config exists",errors)
    check("metadata:" not in text.split("\n---\n",1)[0],"SKILL.md has no metadata interface block",errors)

    for rel in sorted(set(LINK_RE.findall(text))): check((ROOT/rel).exists(),f"referenced resource exists: {rel}",errors)

    for path in PLUGIN_ROOT.glob(".*/plugin.json"):
        try:
            data=json.loads(path.read_text(encoding="utf-8"))
            check(bool(data.get("name")),f"valid plugin manifest: {path.relative_to(PLUGIN_ROOT)}",errors)
            check(data.get("version")=="3.2.1",f"manifest version 3.2.1: {path.parent.name}",errors)
            if path.parent.name==".codex-plugin":
                prompts=data.get("interface",{}).get("defaultPrompt",[])
                check(len(prompts)<=3,"Codex defaultPrompt count <= 3",errors)
                for i,p in enumerate(prompts): check(len(p)<=160,f"Codex defaultPrompt[{i}] <= 160 chars",errors)
        except Exception as e:
            errors.append(f"invalid JSON {path}: {e}"); print(f"FAIL invalid JSON {path}: {e}")

    for path in (ROOT/"schemas").glob("*.json"):
        try:
            data=json.loads(path.read_text(encoding="utf-8"))
            check(data.get("$schema")=="https://json-schema.org/draft/2020-12/schema",f"schema draft 2020-12: {path.name}",errors)
        except Exception as e:
            errors.append(f"invalid schema JSON {path}: {e}"); print(f"FAIL invalid schema JSON {path}: {e}")

    for script in (ROOT/"scripts").glob("*.py"):
        check(script.stat().st_size>0,f"script non-empty: {script.name}",errors)
        try:
            compile(script.read_text(encoding="utf-8"), str(script), "exec"); check(True,f"Python compiles: {script.name}",errors)
        except Exception as e:
            check(False,f"Python compiles: {script.name} ({e})",errors)

    run_script("validate_openai_interface.py",errors)
    run_script("validate_contracts.py",errors)
    run_script("design_lint.py",errors,ROOT/"assets/art-direction.template.json")
    run_script("test_gates.py",errors)
    run_script("test_prompt_lint.py",errors)
    run_script("run_evals.py",errors)
    run_script("run_design_evals.py",errors)
    run_script("taste_lint.py",errors,ROOT/"assets/taste-profile.template.json")
    run_script("test_taste_memory.py",errors)
    run_script("test_taste_merge.py",errors)
    run_script("test_taste_lint.py",errors)

    print(f"\nPackage validation: {'PASS' if not errors else 'FAIL'}")
    if errors:
        print("Errors:")
        for e in errors: print("- "+e)
    return 1 if errors else 0
if __name__=="__main__": raise SystemExit(main())
