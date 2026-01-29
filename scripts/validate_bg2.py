#!/usr/bin/env python3
import json,re,sys
p='data/quizzes/bg/2-adult.json'
report=[]
try:
    with open(p,'r') as f:
        obj=json.load(f)
except Exception as e:
    print('ERROR: JSON parse failed:',e)
    sys.exit(1)
ok=True
required_top=['id','scripture','chapter','audience','title','difficulty','questions']
for k in required_top:
    if k not in obj:
        report.append(('TOP_MISSING',k))
        ok=False
if not isinstance(obj.get('questions'),list):
    report.append(('TOP_BAD','questions not list'))
    ok=False
qcount=len(obj.get('questions',[]))
if qcount!=25:
    report.append(('QCOUNT',qcount))
    ok=False
ids=set()
for i,q in enumerate(obj.get('questions',[]),start=1):
    prefix=f'Q{i}'
    if not isinstance(q,dict):
        report.append((prefix,'not_object'))
        ok=False
        continue
    if 'id' not in q:
        report.append((prefix,'missing_id'))
        ok=False
    else:
        if q['id'] in ids:
            report.append((prefix,'duplicate_id',q['id']))
            ok=False
        ids.add(q['id'])
    if 'prompt' not in q or not isinstance(q['prompt'],str) or not q['prompt'].strip():
        report.append((prefix,'bad_prompt'))
        ok=False
    ch=q.get('choices')
    if not isinstance(ch,list) or len(ch)<2:
        report.append((prefix,'bad_choices'))
        ok=False
    else:
        for c in ch:
            if isinstance(c,str) and re.search(r'(?i)all of the above|none of the above',c):
                report.append((prefix,'banned_choice',c))
                ok=False
    ci=q.get('correctIndex')
    if not isinstance(ci,int) or not (0 <= ci < (len(ch) if isinstance(ch,list) else 0)):
        report.append((prefix,'bad_correctIndex',ci))
        ok=False
    if 'feedback' not in q or not isinstance(q['feedback'],str) or not q['feedback'].strip():
        report.append((prefix,'missing_feedback'))
        ok=False
    if 'verdict' not in q:
        report.append((prefix,'missing_verdict'))
    else:
        if q['verdict'] not in ('Correct','Review'):
            report.append((prefix,'bad_verdict',q.get('verdict')))
            ok=False
    if 'verseLabel' not in q or not isinstance(q['verseLabel'],str):
        report.append((prefix,'missing_verseLabel'))
        ok=False
    vu=q.get('verseUrl','')
    if not isinstance(vu,str) or not vu.startswith('https://') or 'vedabase.io' not in vu:
        report.append((prefix,'bad_verseUrl',vu))
        ok=False
    def check_ascii(v,fieldname):
        if isinstance(v,str):
            try:
                v.encode('ascii')
            except Exception:
                report.append((prefix,'non_ascii',fieldname))
    for kk,vv in q.items():
        check_ascii(vv,kk)
try:
    obj.get('title','').encode('ascii')
except Exception:
    report.append(('TOP','non_ascii_title'))
print('VALID_JSON: OK' if ok else 'VALID_JSON: ISSUES')
print('TOTAL_QUESTIONS:',qcount)
if report:
    print('\nISSUES:')
    for r in report:
        print(' -'," ".join([str(x) for x in r]))
else:
    print('\nNo issues found')

# Exit with non-zero if hard failures (missing required fields or structural issues)
hard_fails=[r for r in report if r[1] in ('TOP_MISSING','TOP_BAD','QCOUNT','bad_choices','bad_correctIndex','missing_feedback','bad_verseUrl','non_ascii','not_object','missing_id')]
if hard_fails:
    sys.exit(2)
else:
    sys.exit(0)
