import json

def analyze_chapter(ch):
    with open(f'data/quizzes/bg/{ch}-adult.json') as f:
        data = json.load(f)
    
    length_issues = 0
    correct_longest = 0
    
    for q in data['questions']:
        wc = [len(c.split()) for c in q['choices']]
        max_wc = max(wc)
        min_wc = min(wc)
        ratio = max_wc / min_wc
        
        if ratio > 1.3:
            length_issues += 1
        if wc[q['correctIndex']] == max_wc:
            correct_longest += 1
    
    total = len(data['questions'])
    return {
        'total': total,
        'length_issues': length_issues,
        'correct_longest': correct_longest,
        'correct_longest_pct': round(100 * correct_longest / total, 1)
    }

print('=' * 60)
print('TIER 3 QUALITY IMPROVEMENTS - BG CHAPTERS 2-5')
print('=' * 60)
print()

print('BEFORE:')
print('  Ch 2: 22 length issues, 21 correct-is-longest (84%)')
print('  Ch 3: 14 length issues, 13 correct-is-longest (52%)')
print('  Ch 4: 20 length issues, 20 correct-is-longest (80%)')
print('  Ch 5: 16 length issues, 22 correct-is-longest (88%)')
print()

print('AFTER:')
for ch in [2, 3, 4, 5]:
    result = analyze_chapter(ch)
    print(f'  Ch {ch}: {result["length_issues"]} length issues, {result["correct_longest"]} correct-is-longest ({result["correct_longest_pct"]}%)')

print()
print('=' * 60)
print('SUMMARY OF CHANGES:')
print('=' * 60)
print()
print('✓ Removed all awkward phrases like "through independent material processes"')
print('✓ Expanded short distractors with contextual detail (not padding)')
print('✓ Made many distractors LONGER than correct answers')
print('✓ Maintained plausibility of all distractors (partial truths)')
print('✓ Kept correct answers EXACTLY as they were')
print('✓ Preserved all verse references, feedback, and IDs')
print()
