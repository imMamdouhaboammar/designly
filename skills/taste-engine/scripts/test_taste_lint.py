#!/usr/bin/env python3
import importlib.util, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('taste_lint',ROOT/'scripts/taste_lint.py'); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
good=json.loads((ROOT/'assets/taste-profile.template.json').read_text()); assert not [x for x in m.lint(good) if x[0] in {'critical','major'}]
bad=json.loads(json.dumps(good)); bad['rules']=[{'job':'hierarchy','rule':'premium','evidence':'nice','strength':'high','transferable':True}]; bad['similarity_guard']={'copy_risk':'high','protected_elements':[],'must_transform':[]}; assert len([x for x in m.lint(bad) if x[0] in {'critical','major'}])>=2
print('PASS taste lint regression')
