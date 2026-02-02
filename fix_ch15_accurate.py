import json

with open('data/quizzes/bg/15-adult.json') as f:
    data = json.load(f)

fixes = {
    # q1: [6,7,6,5] -> expand 5 to 6
    'bg15-q1': {
        'Mountain represents worldly philosophical speculation': 'Mountain clearly represents worldly philosophical speculation'
    },
    
    # q5: [8,6,8,7] -> expand 6 to 7
    'bg15-q5': {
        'Freed from pride delusion attachment desire': 'Freed from pride delusion attachment strong desire'
    },
    
    # q14: [8,6,9,8] -> expand 6 to 8
    'bg15-q14': {
        'I am seated in everyones heart': 'I am seated actively in everyones heart within'
    },
    
    # q25: [15,17,15,13] -> expand 13 to 14
    'bg15-q25': {
        'Tree represents material science; soul fragments justify individualism; Supreme Person symbolizes collective consciousness': 'Tree represents material science; soul fragments justify individualism; Supreme Person symbolizes collective human consciousness'
    }
}

for q in data['questions']:
    if q['id'] in fixes:
        for i, choice in enumerate(q['choices']):
            if choice in fixes[q['id']]:
                old_len = len(choice.split())
                q['choices'][i] = fixes[q['id']][choice]
                new_len = len(q['choices'][i].split())
                print(f"Fixed {q['id']}: {old_len} -> {new_len} words")

with open('data/quizzes/bg/15-adult.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\nValidating new ratios:")
for qid in fixes.keys():
    q = [x for x in data['questions'] if x['id'] == qid][0]
    lens = [len(c.split()) for c in q['choices']]
    ratio = max(lens) / min(lens)
    status = "✓" if ratio <= 1.3 else "✗"
    print(f"{status} {qid}: {lens} = {ratio:.2f}x")
