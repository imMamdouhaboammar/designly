#!/usr/bin/env python3
"""
Deterministic plugin ZIP packager for Designly.
"""
from __future__ import annotations
import hashlib
import json
import os
import stat
import sys
import zipfile
from pathlib import Path

FIXED_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
EXCLUDE_DIRS = {".git", ".superpowers", ".planning", "__pycache__", ".pytest_cache", ".ruff_cache", "dist", "build"}
EXCLUDE_EXTS = {".pyc", ".pyo", ".tmp", ".zip", ".tar.gz"}
EXCLUDE_FILES = {".DS_Store", ".gitignore", "Designly-Multi-Skill-Neural-Mesh-Implementation-Plan.md"}

def get_current_version(root: Path) -> str:
    pkg = root / "package.json"
    if pkg.is_file():
        try:
            return json.loads(pkg.read_text(encoding="utf-8")).get("version", "5.0.1")
        except Exception:
            pass
    return "5.0.1"

def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    ver = get_current_version(root)
    out = Path(sys.argv[2] if len(sys.argv) > 2 else f"dist/designly-v{ver}.zip").resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    
    dirs = set()
    files = []
    
    for cur, ds, fs in os.walk(root):
        # Exclude directories
        ds[:] = sorted([d for d in ds if d not in EXCLUDE_DIRS and not d.startswith(".tmp")])
        for f in sorted(fs):
            if f in EXCLUDE_FILES or f.startswith(".DS_Store"):
                continue
            p = Path(cur) / f
            if p.suffix in EXCLUDE_EXTS:
                continue
            rel = p.relative_to(root).as_posix()
            files.append(rel)
            parts = rel.split("/")[:-1]
            for n in range(1, len(parts) + 1):
                dirs.add("/".join(parts[:n]) + "/")

    tmp = out.with_suffix(out.suffix + ".tmp")
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for rel in sorted(dirs):
            i = zipfile.ZipInfo(rel, FIXED_TIMESTAMP)
            i.create_system = 3
            i.external_attr = (stat.S_IFDIR | 0o755) << 16
            z.writestr(i, b"")
        for rel in sorted(files):
            p = root / rel
            i = zipfile.ZipInfo(rel, FIXED_TIMESTAMP)
            i.create_system = 3
            i.compress_type = zipfile.ZIP_DEFLATED
            mode = 0o755 if (p.stat().st_mode & stat.S_IXUSR) else 0o644
            i.external_attr = (stat.S_IFREG | mode) << 16
            z.writestr(i, p.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

    tmp.replace(out)
    sha = hashlib.sha256(out.read_bytes()).hexdigest()
    print(f"Archive written: {out}")
    print(f"SHA256: {sha}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
