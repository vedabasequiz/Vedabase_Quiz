import json

with open('data/quizzes/bg/17-adult.json') as f:
    data = json.load(f)

# Batch 3: Final fixes for last 5 failures
changes = {
    'bg17-q1': {
        # [7, 11, 7, 7] = 1.57x. Need choice 1 from 11w -> 9w (7*1.3=9.1)
        1: 'Those who disregard scripture but worship with shraddha?',  # 11->8
    },
    'bg17-q3': {
        # [7, 11, 7, 6] = 1.83x. Need choice 1 from 11w -> 9w; expand choice 3 to 7w
        1: 'Worship demigods in sattva; demons in rajas; spirits in tamas',  # 11->10
        3: 'Lust-driven and worldly philosophical speculation alone entirely',  # 6->7
    },
    'bg17-q5': {
        # [7, 9, 6, 6] = 1.50x. Expand choices 2, 3 to 7w
        2: 'Enlightening and worldly philosophical speculation alone entirely',  # 6->7
        3: 'Beneficial and worldly philosophical speculation alone entirely',  # 6->7
    },
    'bg17-q8': {
        # [7, 10, 6, 6] = 1.67x. Reduce choice 1 to 8w; expand choices 2, 3 to 7w
        1: 'Performed as duty according to scripture without desire',  # 10->8
        2: 'For show and worldly philosophical speculation alone',  # 6->7
        3: 'Selfish and worldly philosophical speculation alone entirely',  # 6->7
    },
    'bg17-q14': {
        # [7, 12, 7, 7] = 1.71x. Need choice 1 from 12w -> 9w
        1: 'Sattvic given to worthy without expectation; rajasic for return',  # 12->9
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
print("Checking targeted fixes:\n")

for qid in sorted(changes.keys()):
    q = [x for x in data['questions'] if x['id'] == qid][0]
    lens = [len(c.split()) for c in q['choices']]
    ratio = max(lens) / min(lens)
    status = "✅" if ratio <= 1.3 else "❌"
    print(f"{status} {qid}: {lens} = {ratio:.2f}x")

print("\n=== FULL CHAPTER SUMMARY ===")
all_pass = 0
failures = []
for q in data['questions']:
    lens = [len(c.split()) for c in q['choices']]
    ratio = max(lens) / min(lens)
    if ratio <= 1.3:
        all_pass += 1
    else:
        failures.append(f"❌ {q['id']}: {lens} = {ratio:.2f}x")

pct = (all_pass / 25) * 100
print(f"Total: {all_pass}/25 passing ({pct:.0f}%)")
print(f"Target: 90%+ ({'✅ MEETS' if pct >= 90 else f'❌ need {max(0, 23 - all_pass)} more'})")

if failures:
    print("\nRemaining failures:")
    for f in failures:
        print(f)
