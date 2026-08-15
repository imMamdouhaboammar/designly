#!/usr/bin/env python3
import argparse, json, re, sys
from pathlib import Path

VAGUE_ADJECTIVES = {
    "premium", "modern", "bold", "cinematic", "futuristic", "luxury", "luxurious",
    "elegant", "stunning", "beautiful", "dynamic", "sleek", "sophisticated", "creative",
    "eye-catching", "impactful", "epic"
}
SLOP_EFFECTS = {
    "neon", "glow", "hologram", "holographic", "particles", "chrome", "liquid metal",
    "lens flare", "cyberpunk", "glass", "smoke", "sparks", "floating objects", "bokeh"
}


def norm_words(text):
    return re.findall(r"[a-zA-Z-]+", (text or "").lower())


def has_exception(data, needle):
    for item in data.get("heuristic_exceptions", []):
        if needle.lower() in str(item.get("heuristic", "")).lower():
            return True
    return False


def lint(data):
    findings=[]
    def add(sev, code, msg): findings.append({"severity":sev,"code":code,"message":msg})

    intent=data.get("intent",{})
    concept=data.get("concept",{})
    hierarchy=data.get("hierarchy",{})
    comp=data.get("composition",{})
    typ=data.get("typography",{})
    color=data.get("color",{})
    effects=data.get("effects",[])
    styles=data.get("style_families",[])

    primary=str(intent.get("primary_message","")).strip()
    if not primary:
        add("critical","missing-primary-message","No primary message is locked")

    prop=str(concept.get("visual_proposition","")).strip()
    words=norm_words(prop)
    meaningful=[w for w in words if w not in VAGUE_ADJECTIVES and w not in {"and","with","a","an","the","visual","image","design"}]
    vague=[w for w in words if w in VAGUE_ADJECTIVES]
    if not prop:
        add("critical","missing-visual-proposition","The concept has no executable visual proposition")
    elif len(meaningful) < 5 and len(vague) >= 2:
        add("major","adjective-only-concept","The concept depends on style adjectives more than visible subject/action/relationship")

    if not str(hierarchy.get("primary","")).strip() or not str(hierarchy.get("one_second_read","")).strip():
        add("major","weak-hierarchy-contract","Primary focal event and one-second read must be explicit")

    anchors=comp.get("alignment_anchors",[]) or []
    grid=comp.get("grid_type")
    if not grid:
        add("major","missing-grid-logic","No grid type or structural layout behavior is defined")
    if len(anchors) == 0:
        add("major","missing-alignment-anchors","No alignment anchors are defined")
    if grid == "freeform-anchors" and len(anchors) < 2:
        add("major","underdefined-freeform","Freeform composition needs at least two explicit anchors")
    if len(anchors) > 4 and not has_exception(data,"alignment"):
        add("minor","anchor-entropy","More than four alignment anchors may fragment the composition; justify the exception if intentional")

    focal=comp.get("focal_points",1)
    if isinstance(focal,int) and focal > 2 and not has_exception(data,"focal"):
        add("major","too-many-focal-points","More than two focal points are declared without an explicit multi-focal rationale")

    if not str(comp.get("negative_space","")).strip():
        add("minor","unassigned-negative-space","Negative space has no stated job")
    if not str(comp.get("crop_logic","")).strip():
        add("minor","missing-crop-logic","Crop behavior is not defined")
    if not str(comp.get("eye_path","")).strip():
        add("major","missing-eye-path","No eye path connects the focal event to supporting information")

    tclass=typ.get("class")
    roles=typ.get("roles",[]) or []
    if tclass in {"typography-heavy","poster-ad-layout"} and not typ.get("exact_copy_locked"):
        add("major","unlocked-exact-copy","Typography-heavy work should lock required copy before execution")
    if len(roles) > 4 and not has_exception(data,"type"):
        add("minor","type-role-proliferation","More than four type roles need a clear editorial or brand reason")
    if tclass != "image-only" and not str(color.get("contrast_target","")).strip():
        add("minor","missing-contrast-plan","Text-bearing work has no final contrast verification target")

    if len(styles) > 2 and not has_exception(data,"style"):
        add("major","style-family-entropy","More than two style families are mixed without an explicit reason")

    unpurposed=[e for e in effects if not str(e.get("purpose","")).strip()]
    if unpurposed:
        add("critical","effect-without-job","At least one effect has no stated communication, hierarchy, depth, material, or brand job")
    decorative_purposes=[]
    for e in effects:
        purpose=str(e.get("purpose","")).strip().lower()
        if purpose in {"decoration","decorative","aesthetic","visual interest","looks cool","make it pop"}:
            decorative_purposes.append(str(e.get("name","effect")))
    if len(decorative_purposes)>=2:
        add("major","effects-justified-only-as-decoration","Several effects exist only for decoration: " + ", ".join(decorative_purposes))
    elif len(decorative_purposes)==1:
        add("minor","effect-justified-only-as-decoration","Effect has no job beyond decoration: " + decorative_purposes[0])
    if len(effects) > 3 and not has_exception(data,"effect"):
        add("major","effect-stack","More than three explicit effects are stacked without an exception rationale")

    effect_names=" ".join(str(e.get("name","")) for e in effects).lower()
    slop_hits=sorted({term for term in SLOP_EFFECTS if term in effect_names})
    if len(slop_hits) >= 4:
        add("major","slop-effect-family-stack","Several common synthetic-effect families are stacked: " + ", ".join(slop_hits))

    roles_text=" ".join(color.get("roles",[]) or []).lower()
    accent=str(color.get("accent_strategy","")).lower()
    if "accent" in roles_text and not accent.strip():
        add("minor","undefined-accent-strategy","Accent color exists but its attention job is not defined")

    return findings


def main():
    ap=argparse.ArgumentParser(description="Lint a structured Art Direction Spec before generation")
    ap.add_argument("spec")
    ap.add_argument("--json", action="store_true", dest="as_json")
    args=ap.parse_args()
    data=json.loads(Path(args.spec).read_text(encoding="utf-8"))
    findings=lint(data)
    if args.as_json:
        print(json.dumps(findings, indent=2, ensure_ascii=False))
    elif not findings:
        print("PASS: design preflight found no deterministic structural issues")
    else:
        for f in findings:
            print(f"{f['severity'].upper()} [{f['code']}]: {f['message']}")
    return 1 if any(f["severity"] in {"critical","major"} for f in findings) else 0

if __name__ == "__main__":
    raise SystemExit(main())
