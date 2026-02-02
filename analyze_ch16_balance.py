import json

with open('data/quizzes/bg/16-adult.json') as f:
    data = json.load(f)

# Read current choices first to get exact text
for q in data['questions']:
    if q['id'] in ['bg16-q1', 'bg16-q5', 'bg16-q8', 'bg16-q9', 'bg16-q10', 'bg16-q11', 
                   'bg16-q12', 'bg16-q13', 'bg16-q14', 'bg16-q15', 'bg16-q16', 'bg16-q17',
                   'bg16-q19', 'bg16-q20', 'bg16-q23']:
        lens = [len(c.split()) for c in q['choices']]
        print(f"\n{q['id']} - {lens}:")
        for i, c in enumerate(q['choices']):
            print(f"  [{lens[i]}] {c[:80]}")
