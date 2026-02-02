import json

for ch in [1, 2]:
    with open(f'data/quizzes/bg/{ch}-kids.json') as f:
        data = json.load(f)
    
    print(f'\nCh{ch}:')
    for i, q in enumerate(data['questions'], 1):
        words = len(q['feedback'].split())
        if words > 20:
            print(f'  q{i}: {words}w - {q["feedback"][:60]}...')
