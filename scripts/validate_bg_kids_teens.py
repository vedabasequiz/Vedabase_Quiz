#!/usr/bin/env python3
import json

files = [
    ('data/quizzes/bg/1-kids.json', 15, 5),
    ('data/quizzes/bg/2-kids.json', 15, 5),
    ('data/quizzes/bg/1-teens.json', 20, 8),
    ('data/quizzes/bg/2-teens.json', 20, 8)
]

for filepath, target_total, target_purport in files:
    with open(filepath) as f:
        data = json.load(f)
    
    questions = data['questions']
    total = len(questions)
    purport_qs = [q for q in questions if 'Purport' in q.get('verseLabel', '')]
    purport_count = len(purport_qs)
    purport_pct = (purport_count / total * 100) if total > 0 else 0
    
    # Length balance check
    def check_length_balance(q):
        choices = q['choices']
        wc = [len(c.split()) for c in choices]
        min_wc, max_wc = min(wc), max(wc)
        ratio = max_wc / min_wc if min_wc > 0 else 999
        return ratio <= 1.3
    
    # Correct-is-longest check
    def check_correct_longest(q):
        choices = q['choices']
        wc = [len(c.split()) for c in choices]
        correct_wc = wc[q['correctIndex']]
        return correct_wc == max(wc)
    
    lb_pass = sum(1 for q in questions if check_length_balance(q))
    lb_pct = (lb_pass / total * 100) if total > 0 else 0
    
    cil_count = sum(1 for q in questions if check_correct_longest(q))
    cil_pct = (cil_count / total * 100) if total > 0 else 0
    
    status = "PASS" if total == target_total and purport_count >= target_purport and lb_pct >= 90 and cil_pct < 70 else "NEEDS WORK"
    
    print(f"\n{filepath.split('/')[-1]}:")
    print(f"  Count: {total}Q (target: {target_total}Q)")
    print(f"  Purport: {purport_count}Q / {purport_pct:.1f}% (target: {target_purport}Q)")
    print(f"  Length balance: {lb_pass}/{total} ({lb_pct:.1f}%)")
    print(f"  Correct-is-longest: {cil_count}/{total} ({cil_pct:.1f}%)")
    print(f"  STATUS: {status}")
