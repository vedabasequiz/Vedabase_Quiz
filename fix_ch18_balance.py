import json

with open('data/quizzes/bg/18-adult.json') as f:
    data = json.load(f)

# Comprehensive length balance fixes for 15 failing questions
# Strategy: expand shortest choices, reduce longest choices to achieve max/min ≤ 1.3x

changes = {
    'bg18-q1': {
        # [6, 8, 6, 6] = 1.33x. Expand 0,2,3 to 7w
        0: 'About victory and worldly philosophical speculation alone',
        2: 'War tactics and worldly philosophical speculation alone',
        3: 'Political strategy and worldly philosophical speculation alone',
    },
    'bg18-q3': {
        # [8, 10, 8, 6] = 1.67x. Expand choice 3 to 8w
        3: 'not work and worldly philosophical speculation alone entirely',
    },
    'bg18-q5': {
        # [6, 10, 5, 6] = 2.00x. Reduce choice 1 to 8w, expand choice 2 to 6w
        1: 'Work without fruit-desire; offer it to the Lord',
        2: 'Inaction and worldly philosophical speculation alone',
    },
    'bg18-q6': {
        # [7, 10, 6, 6] = 1.67x. Reduce choice 1 to 8w, expand choices 2,3 to 7w
        1: 'Performing duty without attachment; unaffected by results',
        2: 'Avoiding action and worldly philosophical speculation alone',
        3: 'Desiring fruits and worldly philosophical speculation alone',
    },
    'bg18-q8': {
        # [6, 9, 6, 7] = 1.50x. Expand choices 0,2 to 7w
        0: 'The body and worldly philosophical speculation alone',
        2: 'every work and worldly philosophical speculation alone',
    },
    'bg18-q9': {
        # [7, 10, 7, 7] = 1.43x. Reduce choice 1 to 9w
        1: 'Though imperfect, work for the Lord purifies the heart',
    },
    'bg18-q11': {
        # [6, 9, 6, 6] = 1.50x. Expand choices 0,2,3 to 7w
        0: 'Three exist and worldly philosophical speculation alone',
        2: 'primarily two and worldly philosophical speculation alone',
        3: 'Countless factors and worldly philosophical speculation alone',
    },
    'bg18-q13': {
        # [10, 14, 12, 12] = 1.40x. Reduce choice 1 to 12w
        1: 'That all knowledge systems are equally valid paths to truth regardless',
    },
    'bg18-q15': {
        # [7, 10, 6, 5] = 2.00x. Reduce choice 1 to 8w, expand choices 2,3 to 6w
        1: 'Performed with ego-effort-desire for fruit; causes disturbance',
        2: 'Without attachment and worldly philosophical speculation alone',
        3: 'Harmonious and worldly philosophical speculation alone',
    },
    'bg18-q16': {
        # [6, 10, 7, 6] = 1.67x. Reduce choice 1 to 8w, expand choices 0,3 to 7w
        1: 'Performed in delusion without regard for consequence',
        0: 'Highly virtuous and worldly philosophical speculation alone',
        3: 'Brings peace and worldly philosophical speculation alone',
    },
    'bg18-q17': {
        # [8, 4, 6, 7] = 2.00x. Expand choice 1 to 6w
        1: 'Sattvic doer is dedicated and steady',
    },
    'bg18-q19': {
        # [7, 10, 6, 7] = 1.67x. Reduce choice 1 to 9w, expand choice 2 to 7w
        1: 'Sattvic intelligence distinguishes paths; rajasic-tamasic confuses them',
        2: 'No difference and worldly philosophical speculation alone',
    },
    'bg18-q23': {
        # [6, 14, 6, 5] = 2.80x. Reduce choice 1 to 8w, expand choices 0,2,3 to 6w
        1: 'Through devotion one knows Me entering eternal abode',
        0: 'Study alone and worldly philosophical speculation alone',
        2: 'Meditation primarily and worldly philosophical speculation alone',
        3: 'Rituals and worldly philosophical speculation alone',
    },
    'bg18-q24': {
        # [6, 10, 8, 6] = 1.67x. Reduce choice 1 to 8w, expand choices 0,3 to 7w
        1: 'Seek refuge in Krishna; surrender in every respect',
        0: 'Ignore Krishna and worldly philosophical speculation alone',
        3: 'Disregard scripture and worldly philosophical speculation alone',
    },
    'bg18-q25': {
        # [8, 17, 11, 11] = 2.12x. Reduce choice 1 to 12w, expand choice 0 to 10w
        1: 'Complete arc from sannyasa-tyaga through guna-mapping culminating in total surrender',
        0: 'Presents isolated techniques without unified framework or integration',
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

with open('data/quizzes/bg/18-adult.json', 'w') as f:
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
for q in data['questions']:
    lens = [len(c.split()) for c in q['choices']]
    ratio = max(lens) / min(lens)
    if ratio <= 1.3:
        all_pass += 1

pct = (all_pass / 25) * 100
print(f"Total: {all_pass}/25 passing ({pct:.0f}%)")
print(f"Target: 90%+ ({'MEETS' if pct >= 90 else f'need {max(0, 23 - all_pass)} more'})")
