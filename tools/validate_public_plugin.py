#!/usr/bin/env python3
from __future__ import annotations
import json, os, re, sys, xml.etree.ElementTree as ET
from pathlib import Path
CATEGORIES={"Productivity","Creativity","Developer Tools","Business & Operations","Data & Analytics","Communication","Education & Research","Security","Finance","Healthcare","Travel","Entertainment","Other"}
SEMVER=re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
SECRET=re.compile(r"^(?:\.env(?:\..*)?|auth\.json|credentials?(?:\..*)?|secrets?(?:\..*)?|\.npmrc|\.pypirc)$",re.I)
def err(e,m): e.append(m); print('FAIL '+m)
def ok(m): print('PASS '+m)
def check(c,m,e): ok(m) if c else err(e,m)
def svg_size(p):
    r=ET.fromstring(p.read_text()); vb=r.attrib.get('viewBox') or r.attrib.get('viewbox'); a=[float(x) for x in re.split(r'[\s,]+',vb.strip())] if vb else [0,0,float(r.attrib['width']),float(r.attrib['height'])]; return a[2],a[3]
def main():
    root=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve(); e=[]; mp=root/'.codex-plugin/plugin.json'
    check(mp.is_file(),'manifest exists',e)
    if not mp.is_file(): return 1
    m=json.loads(mp.read_text()); i=m.get('interface',{})
    check(bool(re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,63}',m.get('name',''))),'plugin name valid',e)
    check(bool(SEMVER.fullmatch(m.get('version',''))),'strict semver',e)
    check(isinstance(m.get('author'),dict) and bool(m['author'].get('name')),'author.name present',e)
    check(m.get('skills','').startswith('./') and (root/m['skills'][2:]).is_dir(),'skills path valid',e)
    for f,n in [('displayName',30),('shortDescription',30),('longDescription',4000),('developerName',80)]: check(isinstance(i.get(f),str) and 0<len(i[f])<=n,f'interface.{f} within limit',e)
    check(i.get('category') in CATEGORIES,'public category supported',e)
    prompts=i.get('defaultPrompt',[]); check(isinstance(prompts,list) and len(prompts)<=3,'defaultPrompt count <= 3',e)
    for x in prompts: check(isinstance(x,str) and len(x)<=128 and '\n' not in x,'defaultPrompt one line <=128',e)
    for f in ('logo','composerIcon'):
        v=i.get(f); p=(root/v[2:]) if isinstance(v,str) and v.startswith('./') else None; check(p is not None and p.is_file(),f'{f} exists',e)
        if p and p.is_file():
            try: w,h=svg_size(p) if p.suffix.lower()=='.svg' else (0,1); check(w==h and w>=48,f'{f} square >=48',e)
            except Exception as ex: err(e,f'{f} readable: {ex}')
    count=0; total=0
    for cur,dirs,files in os.walk(root):
        dirs[:]=[d for d in dirs if d!='__pycache__']
        for name in files:
            p=Path(cur)/name; rel=p.relative_to(root); count+=1; total+=p.stat().st_size
            if p.is_symlink(): err(e,f'symlink not allowed: {rel}')
            if SECRET.match(name): err(e,f'secret-shaped file: {rel}')
            if name.endswith(('.pyc','.pyo')): err(e,f'bytecode not allowed: {rel}')
    check(count<5000,'entry count below 5000',e); check(total<512*1024*1024,'uncompressed size below 512 MiB',e)
    print('\nPublic plugin validation: '+('PASS' if not e else 'FAIL'))
    return 1 if e else 0
if __name__=='__main__': raise SystemExit(main())
