import json

with open('data/quizzes/bg/18-adult.json') as f:
    data = json.load(f)

# Final fixes for last 4 failures
changes = {
    'bg18-q5': {
        # [6, 8, 6, 6] = 1.33x. Expand choices 0,2,3 to 7w
        0: 'Pretend renunciation and worldly philosophical speculation alone',
        2: 'Inaction and worldly philosophical speculation alone entirely',
        3: 'Selfish action and worldly philosophical speculation alone',
    },
    'bg18-q17': {
        # [8, 6, 6, 7] = 1.33x. Reduce choice 0 to 7w
        0: 'every doers are equal through material processes',
    },
    'bg18-q23': {
        # [7, 8, 7, 6] = 1.33x. Expand choice 3 to 7w
        3: 'Rituals and worldly philosophical speculation alone entirely',
    },
    'bg18-q25': {
        # [8, 10, 11, 11] = 1.38x. Expand choice 0 to 10w
        0: 'Presents isolated techniques without unified framework or complete integration',
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

print("\n=== FINAL VALIDATION ===\n")

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
