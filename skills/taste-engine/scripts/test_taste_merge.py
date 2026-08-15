#!/usr/bin/env python3
import importlib.util, json, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('taste_merge',ROOT/'scripts/taste_merge.py'); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
base=json.loads((ROOT/'assets/taste-profile.template.json').read_text())
p1=json.loads(json.dumps(base)); p1['source']['ref_id']='REF-0001'; p1['jobs']=['hierarchy','restraint']; p1['rules']=[{'job':'hierarchy','rule':'Keep one dominant hero','evidence':'one large mass dominates','strength':'high','transferable':True}]
p2=json.loads(json.dumps(base)); p2['source']['ref_id']='REF-0002'; p2['jobs']=['lighting']; p2['rules']=[{'job':'lighting','rule':'Use controlled directional light','evidence':'one coherent light source','strength':'high','transferable':True}]
mem={'references':[{'id':'REF-0001','label':'A','status':'canonical','profile':p1},{'id':'REF-0002','label':'B','status':'active','profile':p2}]}
mix={'name':'x','jobs':{'hierarchy':{'ref':'REF-0001'},'lighting':{'ref':'REF-0002'}},'constraints':['exact product'], 'brand_overrides':['brand first']}
out=m.build(mem,mix); assert out['jobs']['hierarchy']['ref']=='REF-0001'; assert out['jobs']['lighting']['ref']=='REF-0002'; assert 'exact product' in out['constraints']
try: m.build(mem,{'name':'bad','jobs':{'typography':{'ref':'REF-0001'}}}); raise AssertionError('expected failure')
except ValueError: pass
print('PASS taste mix routing and conflict guard')
