import json

with open('data/quizzes/bg/15-adult.json') as f:
    data = json.load(f)

fixes = {
    # q1: [6,7,6,5] -> expand shortest from 5 to 6 words
    'bg15-q1': {
        'Krishna is an eternal person in the spiritual realm': 'Krishna is eternally a person in the spiritual realm'
    },
    
    # q5: [8,6,8,7] -> expand shortest from 6 to 7 words
    'bg15-q5': {
        'Because the soul is part of the Supersoul': 'Because the soul is actually part of the Supersoul'
    },
    
    # q14: [8,6,9,8] -> expand shortest from 6 to 8 words (need 2 words)
    'bg15-q14': {
        'The three guṇas compel their actions': 'The three guṇas of nature compel their actions fully'
    },
    
    # q25: [15,17,15,13] -> expand shortest from 13 to 14 words
    'bg15-q25': {
        'The inverted tree shows that detaching from sense objects liberates from material bondage': 'The inverted tree clearly shows that detaching from sense objects liberates from material bondage'
    }
}

for q in data['questions']:
    if q['id'] in fixes:
        for i, choice in enumerate(q['choices']):
            if choice in fixes[q['id']]:
                q['choices'][i] = fixes[q['id']][choice]
                print(f"Fixed {q['id']}")

print("\nValidating new ratios:")
for qid in fixes.keys():
    q = [x for x in data['questions'] if x['id'] == qid][0]
    lens = [len(c.split()) for c in q['choices']]
    ratio = max(lens) / min(lens)
    status = "✓" if ratio <= 1.3 else "✗"
    print(f"{status} {qid}: {lens} = {ratio:.2f}x")

with open('data/quizzes/bg/15-adult.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
