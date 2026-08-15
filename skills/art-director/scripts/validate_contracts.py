#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PAIRS=[
(ROOT/"schemas/creative-brief.schema.json",ROOT/"assets/creative-brief.template.json"),
(ROOT/"schemas/art-direction.schema.json",ROOT/"assets/art-direction.template.json"),
(ROOT/"schemas/visual-review.schema.json",ROOT/"assets/visual-review.template.json"),
]
def type_ok(v,e):
    if isinstance(e,list): return any(type_ok(v,x) for x in e)
    return {"object":lambda x:isinstance(x,dict),"array":lambda x:isinstance(x,list),"string":lambda x:isinstance(x,str),"number":lambda x:isinstance(x,(int,float)) and not isinstance(x,bool),"integer":lambda x:isinstance(x,int) and not isinstance(x,bool),"boolean":lambda x:isinstance(x,bool),"null":lambda x:x is None}.get(e,lambda x:True)(v)
def validate(inst,schema,path="$",errors=None):
    if errors is None: errors=[]
    exp=schema.get("type")
    if exp and not type_ok(inst,exp): errors.append(f"{path}: expected {exp}, got {type(inst).__name__}"); return errors
    if "enum" in schema and inst not in schema["enum"]: errors.append(f"{path}: value {inst!r} not in enum")
    if "const" in schema and inst != schema["const"]: errors.append(f"{path}: value does not equal const")
    if isinstance(inst,str):
        if "minLength" in schema and len(inst)<schema["minLength"]: errors.append(f"{path}: shorter than minLength")
        if "maxLength" in schema and len(inst)>schema["maxLength"]: errors.append(f"{path}: longer than maxLength")
    if isinstance(inst,(int,float)) and not isinstance(inst,bool):
        if "minimum" in schema and inst<schema["minimum"]: errors.append(f"{path}: below minimum")
        if "maximum" in schema and inst>schema["maximum"]: errors.append(f"{path}: above maximum")
    if isinstance(inst,dict):
        for k in schema.get("required",[]):
            if k not in inst: errors.append(f"{path}: missing required property {k}")
        props=schema.get("properties",{}); addl=schema.get("additionalProperties",True)
        for k,v in inst.items():
            if k in props: validate(v,props[k],f"{path}.{k}",errors)
            elif isinstance(addl,dict): validate(v,addl,f"{path}.{k}",errors)
            elif addl is False: errors.append(f"{path}: unexpected property {k}")
    if isinstance(inst,list):
        if "minItems" in schema and len(inst)<schema["minItems"]: errors.append(f"{path}: fewer than minItems")
        if "maxItems" in schema and len(inst)>schema["maxItems"]: errors.append(f"{path}: more than maxItems")
        if schema.get("uniqueItems"):
            try:
                if len({json.dumps(x,sort_keys=True) for x in inst})!=len(inst): errors.append(f"{path}: items are not unique")
            except TypeError: pass
        item=schema.get("items")
        if item:
            for i,v in enumerate(inst): validate(v,item,f"{path}[{i}]",errors)
    return errors

def main():
    failed=False
    for sp,ip in PAIRS:
        schema=json.loads(sp.read_text(encoding="utf-8")); inst=json.loads(ip.read_text(encoding="utf-8")); errors=validate(inst,schema)
        if errors:
            failed=True; print(f"FAIL {ip.name}")
            for e in errors: print("  "+e)
        else: print(f"PASS {ip.name}")
    return 1 if failed else 0
if __name__=="__main__": raise SystemExit(main())
