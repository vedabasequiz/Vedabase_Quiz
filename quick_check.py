import json

for ch in [1, 2]:
    with open(f'data/quizzes/bg/{ch}-kids.json') as f:
        data = json.load(f)
    
    print(f'Ch{ch}: {len(data["questions"])} questions')
    
    feedback_lens = [len(q['feedback'].split()) for q in data['questions']]
    avg = sum(feedback_lens) / len(feedback_lens)
    over20 = sum(1 for w in feedback_lens if w > 20)
    
    print(f'  Feedback: {avg:.1f}w avg, {over20} over 20w')
    
    purport = sum(1 for q in data['questions'] if 'prabhupada' in q['prompt'].lower())
    print(f'  Purport: {purport}/10')
    print()
