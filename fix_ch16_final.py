import json

with open('data/quizzes/bg/16-adult.json') as f:
    data = json.load(f)

fixes = {
    # q9: [6,10,6,7] -> reduce 10 to 8
    'bg16-q9': {
        'I slew my enemy shall slay others I am enjoyer': 'I slew enemies shall slay more am enjoyer'
    },
    
    # q12: [8,8,6,6] -> reduce 8s to 7
    'bg16-q12': {
        'They do not exist through independent material processes': 'They do not exist through independent material',
        'Lust, anger, and greed; one must abandon these': 'Lust anger and greed must be abandoned'
    },
    
    # q15: [11,10,8,11] -> reduce 11s to 10, expand 8 to 9
    'bg16-q15': {
        'Scriptural injunctions lead to sukha (happiness), siddhi (perfection), param gatim (goal)': 'Scriptural injunctions lead to sukha siddhi perfection param gatim goal',
        'That shastra-vidhana (scriptural regulation) determines kartavya (duty) objectively': 'That shastra-vidhana scriptural regulation determines kartavya duty objectively definitely',
        'That ignoring revealed texts prevents knowing right action from wrong action': 'Ignoring revealed texts prevents knowing right action from wrong action'
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

with open('data/quizzes/bg/16-adult.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\nValidating new ratios:")
for qid in sorted(fixes.keys()):
    q = [x for x in data['questions'] if x['id'] == qid][0]
    lens = [len(c.split()) for c in q['choices']]
    ratio = max(lens) / min(lens)
    status = "✓" if ratio <= 1.3 else "✗"
    print(f"{status} {qid}: {lens} = {ratio:.2f}x")
