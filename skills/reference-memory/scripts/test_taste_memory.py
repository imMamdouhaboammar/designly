#!/usr/bin/env python3
import json, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; py=sys.executable; script=ROOT/'scripts/reference_memory.py'; profile=ROOT/'assets/taste-profile.template.json'
def run(*args): return subprocess.run([py,str(script),*map(str,args)],capture_output=True,text=True)
with tempfile.TemporaryDirectory() as td:
    mem=Path(td)/'memory.json'
    assert run('--memory',mem,'init').returncode==0
    a=run('--memory',mem,'add',profile); assert a.returncode==0, a.stderr
    rec=json.loads(a.stdout); assert rec['id']=='REF-0001'
    assert run('--memory',mem,'get','REF-0001').returncode==0
    out=run('--memory',mem,'list','--job','hierarchy'); assert 'REF-0001' in out.stdout
    out=run('--memory',mem,'search','editorial'); assert 'REF-0001' in out.stdout
    assert run('--memory',mem,'feedback','REF-0001','--signal','like','--note','keep crop').returncode==0
    assert run('--memory',mem,'promote','REF-0001','--status','canonical').returncode==0
    data=json.loads(mem.read_text()); assert data['references'][0]['status']=='canonical' and len(data['references'][0]['feedback'])==1
    assert run('--memory',mem,'forget','REF-0001','--yes').returncode==0
    assert json.loads(mem.read_text())['references']==[]
print('PASS reference memory CRUD')
