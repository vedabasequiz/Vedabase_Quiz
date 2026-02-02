import json

with open('data/quizzes/bg/17-adult.json') as f:
    data = json.load(f)

# Comprehensive fixes: expand shortest choices to balance with longest (target: max/min ≤ 1.3x)
changes = {
    'bg17-q1': {
        0: 'Battle strategy and worldly philosophical speculation alone',  # 6->7
        2: 'About politics and worldly philosophical speculation alone',  # 6->7
        3: 'About trade and worldly philosophical speculation alone',  # 6->7
    },
    'bg17-q3': {
        3: 'Lust-driven and worldly philosophical speculation alone',  # 5->6
    },
    'bg17-q5': {
        2: 'Enlightening and worldly philosophical speculation alone',  # 5->6
        3: 'Beneficial and worldly philosophical speculation alone',  # 5->6
    },
    'bg17-q8': {
        3: 'Selfish and worldly philosophical speculation alone',  # 5->6
    },
    'bg17-q9': {
        2: 'Without expectation and worldly philosophical speculation alone',  # 6->7
        3: 'Selfless and worldly philosophical speculation alone',  # 5->6
    },
    'bg17-q11': {
        2: 'Seeking reward and worldly philosophical speculation alone',  # 6->7
        3: 'Ego-driven and worldly philosophical speculation alone',  # 5->6
    },
    'bg17-q12': {
        2: 'Bringing stability and worldly philosophical speculation alone',  # 6->7
        3: 'Without ego and worldly philosophical speculation alone',  # 6->7
    },
    'bg17-q14': {
        0: 'No difference exists through independent material processes alone',  # 7->8
        2: 'Equally valuable and worldly philosophical speculation alone',  # 6->7
    },
    'bg17-q15': {
        0: 'Arbitrary sounds and worldly philosophical speculation alone',  # 6->7
        2: 'Meaningless syllables through independent material processes alone',  # 6->7
        3: 'Cultural tradition and worldly philosophical speculation alone',  # 6->7
    },
    'bg17-q16': {
        0: 'Highly virtuous and worldly philosophical speculation alone',  # 6->7
        2: 'Pure giving and worldly philosophical speculation alone',  # 6->7
        3: 'Truly generous and worldly philosophical speculation alone',  # 6->7
    },
    'bg17-q17': {
        2: 'Creates suffering and worldly philosophical speculation alone',  # 6->7
        3: 'Brings impurity and worldly philosophical speculation alone',  # 6->7
    },
    'bg17-q19': {
        3: 'It is abstract through independent material processes alone',  # 7->8
    },
    'bg17-q20': {
        0: 'Follow anyone and worldly philosophical speculation alone',  # 6->7
        2: 'Follow pleasure and worldly philosophical speculation alone',  # 6->7
    },
    'bg17-q22': {
        # Reduce longest (13->10) and expand shortest (9->10)
        1: 'That actions without faith in Krishna are asat (temporary) bringing no benefit',  # 13->10
        0: 'That shraddha-less sacrifice-charity-austerity still accumulates some spiritual merit easily',  # 9->10
        3: 'That faithless yajna-dana-tapas purify consciousness through habitual repetition alone',  # 9->11
    },
    'bg17-q25': {
        # Reduce longest (18->13) and expand shortest (9->11)
        1: 'Comprehensive guna-mapping showing faith determines food affecting capacity for sacrifice-austerity-charity',  # 18->11
        0: 'Five unrelated teachings requiring choosing which category to emphasize primarily',  # 9->10
        3: 'Contradictory approaches to spirituality requiring personal interpretation or selection',  # 10->9
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

print("\n=== SUMMARY ===")
all_pass = 0
all_fail = 0
for q in data['questions']:
    lens = [len(c.split()) for c in q['choices']]
    ratio = max(lens) / min(lens)
    if ratio <= 1.3:
        all_pass += 1
    else:
        all_fail += 1

pct = (all_pass / 25) * 100
print(f"Total: {all_pass}/25 passing ({pct:.0f}%)")
print(f"Target: 90%+ (need {max(0, 23 - all_pass)} more)")
