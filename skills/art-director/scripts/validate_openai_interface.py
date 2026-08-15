#!/usr/bin/env python3
from pathlib import Path
import re, sys

ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT/'SKILL.md'
YAML=ROOT/'agents'/'openai.yaml'
REQUIRED_INTERFACE=['display_name','short_description','icon_small','icon_large','brand_color','default_prompt']

def fail(msg):
    print('FAIL '+msg)
    return False

def main():
    ok=True
    text=SKILL.read_text(encoding='utf-8')
    end=text.find('\n---\n',4)
    fm=text[4:end] if text.startswith('---\n') and end>=0 else ''
    top=[]
    for line in fm.splitlines():
        if line and not line.startswith((' ','\t')) and ':' in line:
            top.append(line.split(':',1)[0].strip())
    if set(top)!={'name','description'}:
        ok=fail(f'SKILL.md frontmatter must contain only name and description; found {top}') and ok
    else: print('PASS SKILL.md frontmatter contains only name and description')
    if re.search(r'(?m)^metadata\s*:',fm):
        ok=fail('SKILL.md must not use metadata for interface settings') and ok
    else: print('PASS no metadata block in SKILL.md')
    if not YAML.is_file():
        ok=fail('agents/openai.yaml exists') and ok
        return 1
    y=YAML.read_text(encoding='utf-8')
    if not re.search(r'(?m)^interface:\s*$',y):
        ok=fail('agents/openai.yaml has interface block') and ok
    else: print('PASS agents/openai.yaml has interface block')
    for key in REQUIRED_INTERFACE:
        if not re.search(rf'(?m)^\s{{2}}{re.escape(key)}:\s*.+$',y):
            ok=fail(f'interface.{key} is configured in agents/openai.yaml') and ok
        else: print(f'PASS interface.{key} configured in agents/openai.yaml')
    m=re.search(r'(?m)^\s{2}display_name:\s*["\']?([^"\'\n]+)',y)
    if not m or m.group(1).strip()!='Designly':
        ok=fail('interface.display_name is Designly') and ok
    else: print('PASS interface.display_name is Designly')
    for field in ('icon_small','icon_large'):
        m=re.search(rf'(?m)^\s{{2}}{field}:\s*["\']?([^"\'\n]+)',y)
        if m:
            path=(ROOT/m.group(1).strip()).resolve()
            if not path.is_file(): ok=fail(f'{field} asset exists: {m.group(1).strip()}') and ok
            else: print(f'PASS {field} asset exists')
    print('\nOpenAI skill interface validation: '+('PASS' if ok else 'FAIL'))
    return 0 if ok else 1

if __name__=='__main__': raise SystemExit(main())
