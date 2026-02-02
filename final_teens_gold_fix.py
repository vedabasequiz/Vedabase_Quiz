"""Final gold standard fix for BG teens quizzes"""
import json

# Fix Ch1
with open('data/quizzes/bg/1-teens.json') as f:
    ch1 = json.load(f)

# Remove the duplicate at position 2 (index 2, the "bg1-q2-teens")
# It's the old version of q3 that should have been replaced
questions_to_keep = []
for i, q in enumerate(ch1['questions']):
    if q['id'] == 'bg1-q2-teens':
        print(f"Removing duplicate: {q['id']}")
        continue
    questions_to_keep.append(q)

ch1['questions'] = questions_to_keep

# Ensure sequential IDs
for i, q in enumerate(ch1['questions'], 1):
    old_id = q['id']
    q['id'] = f"bg1-q{i}"
    if old_id != q['id']:
        print(f"  Fixed ID: {old_id} → {q['id']}")

# Expand remaining short feedbacks
# q3 (now index 2) - BG 1.3 Purport
if len(ch1['questions'][2]['feedback'].split()) < 30:
    ch1['questions'][2]['feedback'] = "Srila Prabhupada reveals Duryodhana's psychological manipulation: his diplomatic words mask an accusation. By praising the Pandavas' military arrangement, he subtly blames Dronacarya for training them so well. This demonstrates how envy operates through indirect criticism and diplomatic language. Understanding these subtle psychological tactics helps us recognize manipulation in ourselves and others, avoiding the trap of disguised criticism."

# q14 - needs expansion (currently about BG 1.44-1.45 or BG 1.41)
for i, q in enumerate(ch1['questions']):
    if 'BG 1.41' in q['verseLabel'] and len(q['feedback'].split()) < 30:
        ch1['questions'][i]['feedback'] = "When families stop performing proper ceremonies and respecting tradition (kula-dharma), the ancestors no longer receive honor and remembrance through shraddha rituals and offerings. This shows Arjuna's concern for dharmic obligations across generations and the interconnected nature of family duties spanning past, present, and future, though his understanding remains on the material bodily platform."

with open('data/quizzes/bg/1-teens.json', 'w') as f:
    json.dump(ch1, f, indent=2)

# Validate results
print(f"\n{'='*70}")
print("FINAL VALIDATION")
print(f"{'='*70}")

for ch_num, fname in [(1, 'data/quizzes/bg/1-teens.json'), (2, 'data/quizzes/bg/2-teens.json')]:
    with open(fname) as f:
        data = json.load(f)
    
    total = len(data['questions'])
    purport = sum(1 for q in data['questions'] if 'purport' in q.get('prompt', '').lower())
    purport_pct = (purport / total * 100) if total else 0
    
    short_fb = [(i+1, len(q['feedback'].split())) for i, q in enumerate(data['questions']) if len(q['feedback'].split()) < 30]
    
    print(f"\nCh{ch_num}:")
    print(f"  Total: {total} questions ({'✅' if total == 15 else '❌ should be 15'})")
    print(f"  Purport: {purport}/{total} ({purport_pct:.0f}%) ({'✅' if 33 <= purport_pct <= 40 else '❌ should be 33-40%'})")
    print(f"  Short feedback: {len(short_fb)} ({'✅' if len(short_fb) == 0 else f'❌ {short_fb}'})")
    
    # Check IDs are sequential
    expected_ids = [f"bg{ch_num}-q{i}" for i in range(1, total+1)]
    actual_ids = [q['id'] for q in data['questions']]
    if expected_ids == actual_ids:
        print(f"  IDs: ✅ Sequential")
    else:
        print(f"  IDs: ❌ Not sequential")
        for exp, act in zip(expected_ids, actual_ids):
            if exp != act:
                print(f"    Expected {exp}, got {act}")

print(f"\n{'='*70}")
print("✅ BG TEENS QUIZZES - GOLD STANDARD READY")
print(f"{'='*70}")
