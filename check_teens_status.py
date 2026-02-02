"""Check status of BG teens quizzes against gold standard"""
import json
import os

teens_files = [
    'data/quizzes/bg/1-teens.json',
    'data/quizzes/bg/2-teens.json'
]

for f in teens_files:
    if os.path.exists(f):
        with open(f) as file:
            data = json.load(file)
        
        total = len(data['questions'])
        
        # Check purport ratio
        purport_count = sum(1 for q in data['questions'] if q.get('questionType') == 'purport')
        purport_ratio = (purport_count / total) * 100
        
        # Check ASCII
        content_str = json.dumps(data)
        has_unicode = any(ord(c) > 127 for c in content_str)
        
        # Check feedback depth (teens should be 2-3 sentences, ~30-60 words)
        feedback_lengths = [len(q.get('feedback', '').split()) for q in data['questions']]
        avg_feedback_len = sum(feedback_lengths) / total if total > 0 else 0
        short_feedback = sum(1 for fl in feedback_lengths if fl < 20)
        
        # Check length balance (1.5x threshold)
        length_issues = []
        for i, q in enumerate(data['questions'], 1):
            opts = q.get('options', [])
            if len(opts) == 4:
                lengths = [len(opt.split()) for opt in opts]
                max_l = max(lengths)
                min_l = min(lengths)
                if min_l > 0:
                    ratio = max_l / min_l
                    if ratio > 1.5:
                        length_issues.append(f"q{i} ({min_l}-{max_l}w, {ratio:.1f}x)")
        length_balance = ((total - len(length_issues)) / total) * 100 if total > 0 else 0
        
        # Check question IDs
        expected_ids = [f"bg{data['chapter']}-q{i}" for i in range(1, total+1)]
        actual_ids = [q['id'] for q in data['questions']]
        id_issues = [f"Expected {exp}, got {act}" for exp, act in zip(expected_ids, actual_ids) if exp != act]
        
        print(f'\n{"="*60}')
        print(f'{f}')
        print(f'{"="*60}')
        print(f'Questions: {total} (Target: 15 for teens)')
        print(f'Purport ratio: {purport_count}/{total} ({purport_ratio:.0f}%) - Target: 35-40%')
        print(f'Length balance: {length_balance:.0f}% pass 1.5x threshold')
        if length_issues:
            print(f'  Issues: {", ".join(length_issues)}')
        print(f'Feedback depth: {avg_feedback_len:.1f} words avg (Target: 30-60 words for teens)')
        print(f'  Short feedback (<20w): {short_feedback}/{total}')
        print(f'ASCII: {"✅" if not has_unicode else "❌ Unicode found"}')
        if id_issues:
            print(f'ID Issues: {len(id_issues)}')
            for issue in id_issues[:3]:
                print(f'  - {issue}')
        else:
            print('IDs: ✅ Sequential')
        
        # Check specific teens criteria
        print(f'\nTEENS-SPECIFIC CRITERIA:')
        print(f'  - Philosophical depth with technical terms')
        print(f'  - Challenges assumptions')
        print(f'  - 2-3 sentence feedback')
        print(f'  - Synthesis questions recommended')
