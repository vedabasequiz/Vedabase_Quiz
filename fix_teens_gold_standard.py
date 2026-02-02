"""
Fix BG Teens quizzes to meet Gold Standard:
1. Sequential IDs (bg1-q1, bg1-q2, ... not bg1-q1-teens, bg1-q1p-teens)
2. 35-40% purport questions
3. 90%+ length balance (1.5x threshold)
4. 2-3 sentence feedback (30-60 words)
5. Philosophical depth with technical terms
"""
import json

def fix_teens_quiz(chapter):
    filename = f'data/quizzes/bg/{chapter}-teens.json'
    
    with open(filename) as f:
        data = json.load(f)
    
    # Fix IDs to sequential format (bg1-q1, bg1-q2, etc.)
    for i, q in enumerate(data['questions'], 1):
        old_id = q['id']
        q['id'] = f"bg{chapter}-q{i}"
        print(f"  Fixed ID: {old_id} → {q['id']}")
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    
    # Analyze quality
    total = len(data['questions'])
    purport = sum(1 for q in data['questions'] if q.get('questionType') == 'purport')
    purport_pct = (purport / total * 100) if total else 0
    
    # Check feedback depth
    feedback_lens = [len(q.get('feedback', '').split()) for q in data['questions']]
    avg_fb = sum(feedback_lens) / len(feedback_lens) if feedback_lens else 0
    short_fb = sum(1 for fl in feedback_lens if fl < 30)
    
    # Check length balance
    issues = []
    for i, q in enumerate(data['questions'], 1):
        opts = q.get('choices', []) or q.get('options', [])
        if len(opts) == 4:
            lens = [len(o.split()) for o in opts]
            if min(lens) > 0:
                ratio = max(lens) / min(lens)
                if ratio > 1.5:
                    issues.append(f"q{i}")
    
    balance = ((total - len(issues)) / total * 100) if total else 0
    
    print(f"\nCh{chapter} Teens Quality:")
    print(f"  Questions: {total}")
    print(f"  Purport: {purport}/{total} ({purport_pct:.0f}%) - Target: 35-40%")
    print(f"  Length balance: {balance:.0f}% - Target: 90%+")
    if issues:
        print(f"    Issues in: {', '.join(issues)}")
    print(f"  Feedback: {avg_fb:.1f}w avg - Target: 30-60w")
    print(f"    Short (<30w): {short_fb}/{total}")
    
    return {
        'chapter': chapter,
        'total': total,
        'purport': purport,
        'purport_pct': purport_pct,
        'balance': balance,
        'avg_feedback': avg_fb,
        'short_feedback': short_fb
    }

print("=" * 70)
print("FIXING BG TEENS QUIZZES TO GOLD STANDARD")
print("=" * 70)

print("\n=== CHAPTER 1 TEENS ===")
ch1_results = fix_teens_quiz(1)

print("\n=== CHAPTER 2 TEENS ===")
ch2_results = fix_teens_quiz(2)

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
for result in [ch1_results, ch2_results]:
    ch = result['chapter']
    needs_work = []
    
    if result['purport_pct'] < 35:
        needs_work.append(f"purport too low ({result['purport_pct']:.0f}%)")
    if result['balance'] < 90:
        needs_work.append(f"length balance ({result['balance']:.0f}%)")
    if result['short_feedback'] > 3:
        needs_work.append(f"{result['short_feedback']} short feedbacks")
    
    if needs_work:
        print(f"\nCh{ch} - NEEDS WORK: {', '.join(needs_work)}")
    else:
        print(f"\nCh{ch} - ✅ GOLD STANDARD")

print("\n✅ IDs fixed to sequential format (bg{ch}-q1, bg{ch}-q2, etc.)")
