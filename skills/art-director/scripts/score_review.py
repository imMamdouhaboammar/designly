#!/usr/bin/env python3
import json, sys
from pathlib import Path

WEIGHTS = {
    "brief_accuracy": 8,
    "concept_strength": 10,
    "marketing_clarity": 8,
    "hierarchy": 10,
    "composition": 10,
    "grouping_alignment": 6,
    "spacing_density": 5,
    "typography": 8,
    "color_contrast": 5,
    "brand_fidelity": 8,
    "product_fidelity": 6,
    "physical_believability": 5,
    "lighting_materials": 4,
    "cultural_fit": 3,
    "platform_fit": 2,
    "craft": 2,
}
THRESHOLD = 92.0
FLOORS = {
    "brief_accuracy": (85, None),
    "concept_strength": (85, None),
    "marketing_clarity": (85, None),
    "hierarchy": (88, None),
    "composition": (88, None),
    "grouping_alignment": (82, None),
    "typography": (88, "typography"),
    "color_contrast": (85, "color_contrast"),
    "brand_fidelity": (92, "brand"),
    "product_fidelity": (95, "product"),
    "physical_believability": (88, "physical_believability"),
}


def evaluate(data):
    scores=data.get("scores",{})
    missing=[k for k in WEIGHTS if k not in scores]
    if missing:
        raise ValueError("Missing scores: " + ", ".join(missing))
    applicability=data.get("applicability",{})
    optional_flags={
        "typography":"typography",
        "color_contrast":"color_contrast",
        "brand_fidelity":"brand",
        "product_fidelity":"product",
        "physical_believability":"physical_believability",
    }
    active_weights={}
    for k,w in WEIGHTS.items():
        flag=optional_flags.get(k)
        if flag is None or bool(applicability.get(flag,False)):
            active_weights[k]=w
    denom=sum(active_weights.values())
    weighted=sum(float(scores[k])*w for k,w in active_weights.items())/denom if denom else 0.0
    floor_failures=[]
    for key,(minimum,flag) in FLOORS.items():
        applies=True if flag is None else bool(applicability.get(flag,False))
        if applies and float(scores[key]) < minimum:
            floor_failures.append({"category":key,"score":float(scores[key]),"minimum":minimum})

    hard=data.get("hard_gates",{})
    valid_status={"pass","fail","na"}
    invalid_hard=[k for k,v in hard.items() if v not in valid_status]
    hard_failures=[k for k,v in hard.items() if v == "fail"]
    hard_ok=bool(hard) and not invalid_hard and not hard_failures

    findings=data.get("slop_findings",[]) or []
    counts={"minor":0,"major":0,"critical":0}
    for f in findings:
        sev=f.get("severity")
        if sev in counts: counts[sev]+=1
    pressure=counts["minor"] + 3*counts["major"]
    slop_ok=counts["critical"] == 0 and counts["major"] < 2 and counts["minor"] < 4 and pressure < 6

    approved=weighted >= THRESHOLD and not floor_failures and hard_ok and slop_ok
    return {
        "weighted_score": round(weighted,2),
        "threshold": THRESHOLD,
        "category_floors_pass": not floor_failures,
        "floor_failures": floor_failures,
        "hard_gates_pass": hard_ok,
        "hard_gate_failures": hard_failures,
        "invalid_hard_gate_status": invalid_hard,
        "slop_veto_pass": slop_ok,
        "slop_counts": counts,
        "slop_pressure": pressure,
        "approved": approved,
    }


def main():
    if len(sys.argv)!=2:
        print("Usage: score_review.py <visual-review.json>",file=sys.stderr); return 2
    data=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    result=evaluate(data)
    print(json.dumps(result,indent=2))
    return 0 if result["approved"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
