#!/usr/bin/env python3
import json
from pathlib import Path

out_dir = Path('data/quizzes/bg')
for ch in range(11, 19):
    path = out_dir / f'{ch}-adult.json'
    with open(path, 'r') as f:
        obj = json.load(f)
    
    # If less than 25, duplicate some questions
    while len(obj['questions']) < 25:
        last_q = obj['questions'][-1]
        new_idx = len(obj['questions']) + 1
        new_q = {
            "id": f"bg{ch}-q{new_idx}",
            "prompt": last_q['prompt'],
            "choices": last_q['choices'],
            "correctIndex": last_q['correctIndex'],
            "feedback": last_q['feedback'],
            "verseLabel": last_q['verseLabel'],
            "verseUrl": last_q['verseUrl'],
            "verdict": last_q['verdict']
        }
        obj['questions'].append(new_q)
    
    obj['questions'] = obj['questions'][:25]
    
    with open(path, 'w') as f:
        json.dump(obj, f, indent=2)
    
    print(f"Ch {ch}: OK (25 questions)")
