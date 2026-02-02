import json

with open('data/quizzes/bg/17-adult.json') as f:
    data = json.load(f)

# Batch 2: Reduce longest choices to get under 1.3x
changes = {
    'bg17-q1': {
        # [7, 13, 7, 7] = 1.86x. Need choice 1 from 13w -> 9w (7*1.3=9.1)
        1: 'Those who disregard scripture but worship with shraddha - their status?',  # 13->10
    },
    'bg17-q3': {
        # [7, 13, 6, 6] = 2.17x. Need choice 1 from 13w -> 9w max
        1: 'They worship demigods in sattva; demons in rajas; ghosts in tamas',  # 13->11
        2: 'Impure desire and worldly philosophical speculation alone',  # 6->7
    },
    'bg17-q5': {
        # [7, 11, 6, 6] = 1.83x. Need choice 1 from 11w -> 9w
        1: 'Worship of pretas and bhutas - spirits in ignorance',  # 11->9
    },
    'bg17-q8': {
        # [7, 13, 6, 6] = 2.17x. Need choice 1 from 13w -> 9w
        1: 'Performed as duty according to scripture without desire for result',  # 13->10
    },
    'bg17-q11': {
        # [7, 10, 7, 6] = 1.67x. Need choice 1 from 10w -> 8w; expand choice 3 to 7w
        1: 'Discipline of body-mind-speech without desire for results',  # 10->7
        3: 'Ego-driven and worldly philosophical speculation alone',  # 6->7
    },
    'bg17-q14': {
        # [8, 15, 7, 7] = 2.14x. Need choice 1 from 15w -> 10w max
        1: 'Sattvic given to worthy at proper time-place without expectation; rajasic for return',  # 15->12
        0: 'No difference exists through independent material processes',  # 8->7
    },
    'bg17-q15': {
        # [7, 10, 7, 7] = 1.43x. Need choice 1 from 10w -> 9w
        1: 'Om designates Supreme; Tat signifies transcendence; Sat denotes existence',  # 10->9
    },
    'bg17-q16': {
        # [7, 10, 7, 7] = 1.43x. Need choice 1 from 10w -> 9w
        1: 'Given at wrong time-place to unworthy person; disrespectfully',  # 10->8
    },
    'bg17-q22': {
        # [9, 12, 11, 9] = 1.33x. Need choice 1 from 12w -> 11w
        1: 'That actions without faith in Krishna are asat bringing no benefit',  # 12->11
    },
}

for q in data['questions']:
    if q['id'] in changes:
        for idx, new_text in changes[q['id']].items():
            old = q['choices'][idx]
            old_len = len(old.split())
            new_len = len(new_text.split())
            q['choices'][idx] = new_text
            print(f"Updated {q['id']} choice {idx}: {old_len}w -> {new_len}w")

with open('data/quizzes/bg/17-adult.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\n=== VALIDATION ===")
print("Checking new ratios:\n")

for qid in sorted(changes.keys()):
    q = [x for x in data['questions'] if x['id'] == qid][0]
    lens = [len(c.split()) for c in q['choices']]
    ratio = max(lens) / min(lens)
    status = "✅" if ratio <= 1.3 else "❌"
    print(f"{status} {qid}: {lens} = {ratio:.2f}x")

print("\n=== FULL SUMMARY ===")
all_pass = 0
all_fail = 0
for q in data['questions']:
    lens = [len(c.split()) for c in q['choices']]
    ratio = max(lens) / min(lens)
    if ratio <= 1.3:
        all_pass += 1
    else:
        all_fail += 1
        print(f"❌ {q['id']}: {lens} = {ratio:.2f}x")

pct = (all_pass / 25) * 100
print(f"\nTotal: {all_pass}/25 passing ({pct:.0f}%)")
print(f"Target: 90%+ ({'MEETS' if pct >= 90 else f'need {max(0, 23 - all_pass)} more'})")
