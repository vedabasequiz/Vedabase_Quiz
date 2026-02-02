import json

with open('data/quizzes/bg/7-adult.json', 'r') as f:
    quiz = json.load(f)

print('=== LENGTH VARIANCE ISSUES ===\n')
high_variance_qs = []
for i, q in enumerate(quiz['questions'], 1):
    lengths = [len(c.split()) for c in q['choices']]
    correct_len = lengths[q['correctIndex']]
    max_len = max(lengths)
    min_len = min(lengths)
    variance = max_len / min_len
    
    if variance > 1.5:
        high_variance_qs.append(i)
        print(f'Q{i} ({q["id"]}): Range {min_len}-{max_len} words (variance {variance:.1f}x)')
        for j, (choice, length) in enumerate(zip(q['choices'], lengths)):
            marker = ' ✓CORRECT' if j == q['correctIndex'] else ''
            print(f'  [{length:2d}w] {choice}{marker}')
        print()

print('\n=== CORRECT-IS-LONGEST ANALYSIS ===\n')
correct_longest = []
for i, q in enumerate(quiz['questions'], 1):
    lengths = [len(c.split()) for c in q['choices']]
    if lengths[q['correctIndex']] == max(lengths):
        correct_longest.append(i)

print(f'Correct is longest in: {correct_longest}')
print(f'Total: {len(correct_longest)}/25 = {len(correct_longest)/25*100:.0f}%')
print(f'Target: ~60% (15/25)')
print(f'Need to reduce by: {len(correct_longest) - 15} questions')
