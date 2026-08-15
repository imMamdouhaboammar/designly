#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys
from pathlib import Path
VAGUE={"premium","modern","cinematic","cool","luxury","elegant","stunning","beautiful","bold","futuristic"}

def lint(p):
    f=[]
    if p.get("profile_version")!="1.0": f.append(("critical","profile_version must be 1.0"))
    if not p.get("jobs"): f.append(("critical","at least one job is required"))
    if not p.get("observations"): f.append(("major","observations are required"))
    for i,o in enumerate(p.get("observations",[])):
        if len(o.get("evidence","").split())<3: f.append(("major",f"observation {i} lacks concrete evidence"))
        if o.get("confidence",0)<0.5: f.append(("minor",f"observation {i} confidence is below promotion threshold"))
    for i,r in enumerate(p.get("rules",[])):
        words=set(re.findall(r"[a-z]+",r.get("rule","").lower()))
        if words and words <= VAGUE: f.append(("major",f"rule {i} is adjective-only"))
        if r.get("transferable") and r.get("strength")=="high" and len(r.get("evidence","").split())<4: f.append(("major",f"high-strength rule {i} lacks evidence"))
    sg=p.get("similarity_guard",{})
    if sg.get("copy_risk") in {"medium","high"} and not sg.get("must_transform"): f.append(("major","copy risk requires at least one must_transform item"))
    if p.get("confidence",0)>0.9 and len(p.get("observations",[]))<2: f.append(("minor","very high confidence from too little evidence"))
    return f

def main():
    p=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")); f=lint(p)
    for s,m in f: print(f"{s.upper()}: {m}")
    blockers=[x for x in f if x[0] in {"critical","major"}]
    print(f"Taste lint: {'FAIL' if blockers else 'PASS'}")
    return 1 if blockers else 0
if __name__=="__main__": raise SystemExit(main())
