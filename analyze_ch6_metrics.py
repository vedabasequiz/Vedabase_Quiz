import json

with open('data/quizzes/bg/6-adult.json', 'r') as f:
    data = json.load(f)

questions = data['questions']
total = len(questions)

# Count purport questions
purport_count = sum(1 for q in questions if 'purport' in q['prompt'].lower())

# Check length balance issues
length_issues = []
for i, q in enumerate(questions, 1):
    lengths = [len(choice.split()) for choice in q['choices']]
    max_len = max(lengths)
    min_len = min(lengths)
    variance = max_len / min_len if min_len > 0 else 0
    if variance > 1.5:
        length_issues.append((i, variance, lengths))

# Count 'Why this matters'
why_matters_count = sum(1 for q in questions if 'Why this matters:' in q['feedback'])

print(f'Total questions: {total}')
print(f'Purport questions: {purport_count}/{total} ({purport_count*100//total}%)')
print(f'Length balance issues: {len(length_issues)}/{total} ({(total-len(length_issues))*100//total}% pass)')
print(f'"Why this matters": {why_matters_count}/{total} ({why_matters_count*100//total}%)')
print()
print('Length balance issues (variance > 1.5x):')
for q_num, var, lengths in length_issues:
    print(f'  Q{q_num}: {var:.2f}x variance, lengths: {lengths}')

print()
print('Questions by ID for purport analysis:')
for i, q in enumerate(questions, 1):
    is_purport = 'purport' in q['prompt'].lower()
    marker = '[P]' if is_purport else '   '
    print(f'{marker} Q{i:2d}: {q["id"]:10s} - {q["prompt"][:80]}...')
