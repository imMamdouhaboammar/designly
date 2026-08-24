#!/usr/bin/env python3
import copy, json, importlib.util
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("score_review",ROOT/"scripts/score_review.py")
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
base=json.loads((ROOT/"assets/visual-review.template.json").read_text(encoding="utf-8"))

cases=[]
def case(name, mutate, expected):
    x=copy.deepcopy(base); mutate(x); cases.append((name,x,expected))

cases.append(("clean-review-approves",copy.deepcopy(base),True))
case("arabic-na-does-not-block",lambda x:x["hard_gates"].update({"arabic":"na"}),True)
case("high-average-low-hierarchy-blocks",lambda x: x["scores"].update({"hierarchy":80}),False)
case("high-average-low-composition-blocks",lambda x: x["scores"].update({"composition":87}),False)
case("low-typography-allowed-when-not-applicable",lambda x:(x["applicability"].update({"typography":False}),x["scores"].update({"typography":20})),True)
case("brand-floor-blocks-when-applicable",lambda x:x["scores"].update({"brand_fidelity":91}),False)
case("product-floor-blocks",lambda x:x["scores"].update({"product_fidelity":94}),False)
case("physical-floor-blocks-manipulation",lambda x:x["scores"].update({"physical_believability":87}),False)
case("arabic-hard-gate-blocks",lambda x:x["hard_gates"].update({"arabic":"fail"}),False)
case("accessibility-plan-gate-blocks",lambda x:x["hard_gates"].update({"accessibility_plan":"fail"}),False)
case("one-critical-slop-blocks",lambda x:x["slop_findings"].append({"family":"concept","severity":"critical","evidence":"effect stack is the concept"}),False)
case("two-major-slop-blocks",lambda x:x["slop_findings"].extend([{"family":"composition","severity":"major","evidence":"equal emphasis"},{"family":"effects","severity":"major","evidence":"stacked finish"}]),False)
case("four-minor-slop-blocks",lambda x:x["slop_findings"].extend([{"family":str(i),"severity":"minor","evidence":"localized"} for i in range(4)]),False)
case("pressure-six-blocks",lambda x:x["slop_findings"].extend([{"family":"effects","severity":"major","evidence":"stack"}]+[{"family":str(i),"severity":"minor","evidence":"noise"} for i in range(3)]),False)
case("weighted-below-92-blocks",lambda x:[x["scores"].__setitem__(k,91) for k in x["scores"]],False)

def main() -> int:
    failed = 0
    for name, data, expected in cases:
        got = mod.evaluate(data)["approved"]
        if got == expected:
            print(f"PASS {name}")
        else:
            failed += 1
            print(f"FAIL {name}: got {got}, expected {expected}")
    print(f"\n{len(cases)-failed} passed, {failed} failed")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
