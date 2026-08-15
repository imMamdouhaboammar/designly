#!/usr/bin/env python3
import argparse, re, sys

SLOP_TERMS=["neon","glow","hologram","holographic","particles","chrome","liquid metal","lens flare","cyberpunk","floating objects","futuristic ui","glass panels","sparks","smoke"]
VAGUE=["stunning","eye-catching","make it pop","next-level","visually captivating","premium and modern","bold and dynamic"]
CAMERA_DUMP=re.compile(r"\b(24mm|35mm|50mm|85mm|105mm|f/1\.4|f/1\.8|f/2\.8|iso\s*\d+|1/\d+s)\b",re.I)
NEG=re.compile(r"\b(no|avoid|without|exclude|remove|omit|do not|don't)\b",re.I)
POS=re.compile(r"\b(use|add|include|with|feature|apply|make|create)\b",re.I)
BOUNDARY=re.compile(r"(?:[.;!?]|\bbut\b|\bhowever\b|\binstead\b)",re.I)

def active_term(text,term):
    lower=text.lower(); start=0
    while True:
        i=lower.find(term,start)
        if i<0: return False
        prefix=lower[:i]
        matches=list(BOUNDARY.finditer(prefix))
        clause_start=matches[-1].end() if matches else 0
        clause=lower[clause_start:i]
        neg=list(NEG.finditer(clause)); pos=list(POS.finditer(clause))
        last_neg=neg[-1].start() if neg else -1
        last_pos=pos[-1].start() if pos else -1
        if not (last_neg > last_pos):
            return True
        start=i+len(term)

def lint(text):
    lower=text.lower(); issues=[]
    hits=[t for t in SLOP_TERMS if active_term(text,t)]
    if len(hits)>=5: issues.append(("major",f"effect-stack pressure: {', '.join(hits)}"))
    elif len(hits)>=3: issues.append(("minor",f"several synthetic-effect families active: {', '.join(hits)}"))
    vague=[t for t in VAGUE if t in lower]
    if vague: issues.append(("minor",f"vague visual language: {', '.join(vague)}"))
    cam=CAMERA_DUMP.findall(text)
    if len(cam)>=4: issues.append(("minor","camera-spec dump may be replacing perceptual direction"))
    if len(text.split())>420: issues.append(("minor","prompt is unusually long; remove instructions that do not materially change the image"))
    if "preserve" in lower and "edit" in lower and not any(x in lower for x in ["protected","outside","unchanged","locked"]):
        issues.append(("minor","edit preservation is underspecified"))
    return issues

def main():
    p=argparse.ArgumentParser(); p.add_argument("text",nargs="?"); args=p.parse_args()
    text=args.text if args.text is not None else sys.stdin.read(); issues=lint(text)
    if not issues: print("PASS: no deterministic prompt-lint findings"); return 0
    for sev,msg in issues: print(f"{sev.upper()}: {msg}")
    return 1 if any(sev=="major" for sev,_ in issues) else 0
if __name__=="__main__": raise SystemExit(main())
