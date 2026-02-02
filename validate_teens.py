import json

for ch in [1, 2]:
    filepath = f'data/quizzes/bg/{ch}-teens.json'
    with open(filepath) as f:
        data = json.load(f)
    
    questions = data['questions']
    total = len(questions)
    
    print(f'\n{"="*60}')
    print(f'BG Chapter {ch} Teens Quiz - Gold Standard Validation')
    print(f'{"="*60}')
    
    # Total questions
    print(f'✓ Total questions: {total}')
    
    # Check IDs are sequential
    expected_ids = [f'bg{ch}-q{i}' for i in range(1, total+1)]
    actual_ids = [q['id'] for q in questions]
    if expected_ids == actual_ids:
        print(f'✓ IDs are sequential: bg{ch}-q1 through bg{ch}-q{total}')
    else:
        print(f'✗ ID mismatch found')
    
    # Purport questions
    purport_questions = [q for q in questions if (
        'purport' in q.get('verseLabel', '').lower() or
        q.get('source', '').lower() == 'purport'
    )]
    purport_count = len(purport_questions)
    purport_pct = (purport_count / total) * 100
    
    print(f'✓ Purport questions: {purport_count}/{total} ({purport_pct:.0f}%)')
    if 35 <= purport_pct <= 40:
        print(f'  ✓ Within gold standard range (35-40%)')
    else:
        print(f'  ⚠ Outside gold standard range (35-40%)')
    
    # Feedback analysis
    print(f'\nFeedback Analysis:')
    short_feedbacks = []
    for i, q in enumerate(questions, 1):
        words = len(q['feedback'].split())
        if words < 30:
            short_feedbacks.append((f'bg{ch}-q{i}', words))
    
    if short_feedbacks:
        print(f'  ⚠ {len(short_feedbacks)} feedback(s) under 30 words:')
        for qid, words in short_feedbacks:
            print(f'    {qid}: {words} words')
    else:
        print(f'  ✓ All feedbacks meet minimum 30 words')
    
    # Word count stats
    word_counts = [len(q['feedback'].split()) for q in questions]
    avg_words = sum(word_counts) / len(word_counts)
    print(f'  Average: {avg_words:.1f} words')

print(f'\n{"="*60}')
print('✅ VALIDATION COMPLETE')
print(f'{"="*60}')
