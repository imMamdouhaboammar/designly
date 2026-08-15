#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

def load_json(path): return json.loads(Path(path).read_text(encoding="utf-8"))

def find(memory, ref):
    for r in memory.get("references",[]):
        if r.get("id")==ref: return r
    raise KeyError(f"unknown reference: {ref}")

def build(memory, spec):
    jobs=spec.get("jobs",{})
    if not jobs: raise ValueError("mix requires jobs")
    contract={"name":spec.get("name","Taste Contract"),"sources":{},"jobs":{},"constraints":list(spec.get("constraints",[])),"brand_overrides":list(spec.get("brand_overrides",[])),"anti_rules":[],"similarity_guard":{"protected_elements":[],"must_transform":[]}}
    for job, assignment in jobs.items():
        ref=assignment["ref"]; rec=find(memory,ref); profile=rec.get("profile",{})
        if job not in profile.get("jobs",[]): raise ValueError(f"{ref} is not profiled for job {job}")
        selected=[r for r in profile.get("rules",[]) if r.get("transferable") and r.get("job") in {job,"general","*"}]
        if not selected: raise ValueError(f"{ref} has no transferable rules for job {job}")
        contract["sources"][ref]={"label":rec.get("label",ref),"status":rec.get("status","active"),"confidence":profile.get("confidence")}
        contract["jobs"][job]={"ref":ref,"weight":assignment.get("weight",1.0),"note":assignment.get("note",""),"rules":selected}
        for ar in profile.get("anti_rules",[]):
            if ar not in contract["anti_rules"]: contract["anti_rules"].append(ar)
        sg=profile.get("similarity_guard",{})
        for k in ("protected_elements","must_transform"):
            for x in sg.get(k,[]):
                if x not in contract["similarity_guard"][k]: contract["similarity_guard"][k].append(x)
    return contract

def main():
    ap=argparse.ArgumentParser(description="Build a job-based Taste Contract from Reference Memory")
    ap.add_argument("--memory",required=True); ap.add_argument("--spec",required=True); ap.add_argument("--out")
    args=ap.parse_args()
    try:
        result=build(load_json(args.memory),load_json(args.spec)); text=json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True)+"\n"
        if args.out: Path(args.out).write_text(text,encoding="utf-8")
        else: print(text,end="")
        return 0
    except Exception as e: print(f"ERROR: {e}",file=sys.stderr); return 1
if __name__=="__main__": raise SystemExit(main())
