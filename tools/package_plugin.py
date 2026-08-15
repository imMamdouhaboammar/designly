#!/usr/bin/env python3
from __future__ import annotations
import hashlib, os, stat, sys, zipfile
from pathlib import Path
FIXED=(1980,1,1,0,0,0)
def main():
    root=Path(sys.argv[1]).resolve(); out=Path(sys.argv[2]).resolve(); out.parent.mkdir(parents=True,exist_ok=True)
    dirs=set(); files=[]
    for cur,ds,fs in os.walk(root):
        ds[:]=sorted(d for d in ds if d!='__pycache__')
        for f in sorted(fs):
            p=Path(cur)/f
            if p.suffix in {'.pyc','.pyo'}: continue
            rel=p.relative_to(root).as_posix(); files.append(rel); parts=rel.split('/')[:-1]
            for n in range(1,len(parts)+1): dirs.add('/'.join(parts[:n])+'/')
    tmp=out.with_suffix(out.suffix+'.tmp')
    with zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for rel in sorted(dirs):
            i=zipfile.ZipInfo(rel,FIXED); i.create_system=3; i.external_attr=(stat.S_IFDIR|0o755)<<16; z.writestr(i,b'')
        for rel in sorted(files):
            p=root/rel; i=zipfile.ZipInfo(rel,FIXED); i.create_system=3; i.compress_type=zipfile.ZIP_DEFLATED; mode=0o755 if p.stat().st_mode & stat.S_IXUSR else 0o644; i.external_attr=(stat.S_IFREG|mode)<<16; z.writestr(i,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
    tmp.replace(out); print(hashlib.sha256(out.read_bytes()).hexdigest())
if __name__=='__main__': main()
