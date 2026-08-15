#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, shutil, sys
from datetime import datetime, timezone
from pathlib import Path

SCHEMA_VERSION = "1.0"
VALID_STATUS = {"active", "canonical", "archived"}
VALID_SIGNAL = {"like", "dislike", "correction", "neutral"}

def now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat()

def memory_path(explicit=None):
    if explicit: return Path(explicit).expanduser().resolve()
    if os.environ.get("ART_DIRECTOR_MEMORY"): return Path(os.environ["ART_DIRECTOR_MEMORY"]).expanduser().resolve()
    for env in ("PLUGIN_DATA", "CLAUDE_PLUGIN_DATA"):
        if os.environ.get(env): return Path(os.environ[env]).expanduser().resolve()/"reference-memory.json"
    return Path.cwd()/".designly/reference-memory.json"

def blank(): return {"schema_version":SCHEMA_VERSION,"next_ref":1,"references":[],"mixes":[]}

def load(path, create=True):
    if not path.exists():
        if not create: raise FileNotFoundError(path)
        path.parent.mkdir(parents=True, exist_ok=True); save(path, blank())
    data=json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version")!=SCHEMA_VERSION or not isinstance(data.get("references"),list): raise ValueError("unsupported or malformed reference memory")
    return data

def save(path,data):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp=path.with_suffix(path.suffix+".tmp")
    tmp.write_text(json.dumps(data,indent=2,ensure_ascii=False,sort_keys=True)+"\n",encoding="utf-8")
    tmp.replace(path)

def next_id(data):
    n=int(data.get("next_ref",1)); data["next_ref"]=n+1; return f"REF-{n:04d}"

def find(data, ref_id):
    for r in data["references"]:
        if r["id"]==ref_id: return r
    raise KeyError(ref_id)

def cmd_init(args):
    p=memory_path(args.memory); load(p); print(p); return 0

def cmd_path(args): print(memory_path(args.memory)); return 0

def cmd_add(args):
    p=memory_path(args.memory); data=load(p)
    profile=json.loads(Path(args.profile).read_text(encoding="utf-8"))
    ref=next_id(data); profile.setdefault("source",{})["ref_id"]=ref
    label=args.label or profile.get("source",{}).get("label") or ref
    t=now(); rec={"id":ref,"label":label,"status":"active","created_at":t,"updated_at":t,"profile":profile,"feedback":[]}
    data["references"].append(rec); save(p,data); print(json.dumps(rec,ensure_ascii=False,indent=2)); return 0

def cmd_list(args):
    data=load(memory_path(args.memory)); out=[]
    for r in data["references"]:
        if args.status and r["status"]!=args.status: continue
        prof=r.get("profile",{})
        if args.job and args.job not in prof.get("jobs",[]): continue
        if args.tag and args.tag not in prof.get("tags",[]): continue
        out.append({"id":r["id"],"label":r["label"],"status":r["status"],"jobs":prof.get("jobs",[]),"tags":prof.get("tags",[])})
    print(json.dumps(out,ensure_ascii=False,indent=2)); return 0

def cmd_get(args):
    r=find(load(memory_path(args.memory)),args.ref_id); print(json.dumps(r,ensure_ascii=False,indent=2)); return 0

def cmd_search(args):
    data=load(memory_path(args.memory)); q=" ".join(args.query).casefold(); terms=[t for t in q.split() if t]; scored=[]
    for r in data["references"]:
        blob=json.dumps(r,ensure_ascii=False).casefold(); score=sum(blob.count(t) for t in terms)
        if score: scored.append((score,r))
    scored.sort(key=lambda x:(-x[0], x[1]["id"]))
    print(json.dumps([{"score":s,"id":r["id"],"label":r["label"],"status":r["status"],"jobs":r.get("profile",{}).get("jobs",[])} for s,r in scored[:args.limit]],ensure_ascii=False,indent=2)); return 0

def cmd_feedback(args):
    if args.signal not in VALID_SIGNAL: raise ValueError("invalid signal")
    p=memory_path(args.memory); data=load(p); r=find(data,args.ref_id); t=now(); r["feedback"].append({"signal":args.signal,"note":args.note or "","scope":args.scope or "","created_at":t}); r["updated_at"]=t; save(p,data); print(args.ref_id); return 0

def cmd_promote(args):
    if args.status not in VALID_STATUS: raise ValueError("invalid status")
    p=memory_path(args.memory); data=load(p); r=find(data,args.ref_id); r["status"]=args.status; r["updated_at"]=now(); save(p,data); print(args.ref_id); return 0

def cmd_forget(args):
    if not args.yes: raise ValueError("forget requires --yes")
    p=memory_path(args.memory); data=load(p); before=len(data["references"]); data["references"]=[r for r in data["references"] if r["id"]!=args.ref_id]
    if len(data["references"])==before: raise KeyError(args.ref_id)
    for mix in data.get("mixes",[]):
        mix["jobs"]={k:v for k,v in mix.get("jobs",{}).items() if v.get("ref")!=args.ref_id}
    save(p,data); print(args.ref_id); return 0

def cmd_export(args):
    src=memory_path(args.memory); load(src); dst=Path(args.output).expanduser().resolve(); dst.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(src,dst); print(dst); return 0

def parser():
    ap=argparse.ArgumentParser(description="Deterministic local reference-memory CRUD for the Designly skill")
    ap.add_argument("--memory",help="override memory JSON path")
    sub=ap.add_subparsers(dest="cmd",required=True)
    sub.add_parser("init").set_defaults(func=cmd_init); sub.add_parser("path").set_defaults(func=cmd_path)
    a=sub.add_parser("add"); a.add_argument("profile"); a.add_argument("--label"); a.set_defaults(func=cmd_add)
    a=sub.add_parser("list"); a.add_argument("--job"); a.add_argument("--tag"); a.add_argument("--status",choices=sorted(VALID_STATUS)); a.set_defaults(func=cmd_list)
    a=sub.add_parser("get"); a.add_argument("ref_id"); a.set_defaults(func=cmd_get)
    a=sub.add_parser("search"); a.add_argument("query",nargs="+"); a.add_argument("--limit",type=int,default=10); a.set_defaults(func=cmd_search)
    a=sub.add_parser("feedback"); a.add_argument("ref_id"); a.add_argument("--signal",required=True,choices=sorted(VALID_SIGNAL)); a.add_argument("--note"); a.add_argument("--scope"); a.set_defaults(func=cmd_feedback)
    a=sub.add_parser("promote"); a.add_argument("ref_id"); a.add_argument("--status",required=True,choices=sorted(VALID_STATUS)); a.set_defaults(func=cmd_promote)
    a=sub.add_parser("forget"); a.add_argument("ref_id"); a.add_argument("--yes",action="store_true"); a.set_defaults(func=cmd_forget)
    a=sub.add_parser("export"); a.add_argument("output"); a.set_defaults(func=cmd_export)
    return ap

def main():
    args=parser().parse_args()
    try: return args.func(args)
    except Exception as e: print(f"ERROR: {e}",file=sys.stderr); return 1
if __name__=="__main__": raise SystemExit(main())
