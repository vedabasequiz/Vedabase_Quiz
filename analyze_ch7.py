import json

with open('data/quizzes/bg/7-adult.json', 'r') as f:
    data = json.load(f)

# Check length balance
length_issues = []
for q in data['questions']:
    lengths = [len(c) for c in q['choices']]
    max_len = max(lengths)
    min_len = min(lengths)
    ratio = max_len / min_len if min_len > 0 else 0
    if ratio > 1.6:
        length_issues.append({
            'id': q['id'],
            'ratio': ratio,
            'lengths': lengths
        })

print(f'Length balance issues (>1.6 ratio): {len(length_issues)}/25')
for issue in length_issues:
    print(f"  {issue['id']}: ratio {issue['ratio']:.2f}, lengths {issue['lengths']}")

# Check feedback depth
short_feedback = []
for q in data['questions']:
    sentences = q['feedback'].count('.') + q['feedback'].count('?') + q['feedback'].count('!')
    words = len(q['feedback'].split())
    if sentences < 2 or words < 20:
        short_feedback.append({
            'id': q['id'],
            'sentences': sentences,
            'words': words,
            'feedback': q['feedback'][:80] + '...' if len(q['feedback']) > 80 else q['feedback']
        })

print(f'\nShort feedback (<2 sentences or <20 words): {len(short_feedback)}/25')
for fb in short_feedback[:10]:
    print(f"  {fb['id']}: {fb['sentences']} sentences, {fb['words']} words")

# Check purport ratio
purport_count = sum(1 for q in data['questions'] if 'purport' in q['prompt'].lower())
print(f'\nPurport questions: {purport_count}/25 ({purport_count/25*100:.0f}%)')

# Check synthesis questions
synthesis_keywords = ['synthesize', 'how do', 'relate', 'connection between', 'compare', 'contrast']
synthesis_count = sum(1 for q in data['questions'] if any(kw in q['prompt'].lower() for kw in synthesis_keywords))
print(f'Synthesis questions: {synthesis_count}/25 ({synthesis_count/25*100:.0f}%)')

# Check for 'Why this matters'
why_matters_count = sum(1 for q in data['questions'] if 'why this matters' in q['feedback'].lower())
print(f'"Why this matters" in feedback: {why_matters_count}/25')

# Check false-path density
false_path_count = sum(1 for q in data['questions'] if 'false path' in q['feedback'].lower() or 'trap' in q['feedback'].lower())
print(f'False-path warnings: {false_path_count}/25')
