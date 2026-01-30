import json

def analyze_chapter_detailed(ch):
    with open(f'data/quizzes/bg/{ch}-adult.json') as f:
        data = json.load(f)
    
    print(f'\n=== CHAPTER {ch} - Remaining Issues ===\n')
    
    for i, q in enumerate(data['questions'], 1):
        wc = [len(c.split()) for c in q['choices']]
        max_wc = max(wc)
        min_wc = min(wc)
        ratio = max_wc / min_wc
        correct_wc = wc[q['correctIndex']]
        
        if ratio > 1.3:
            print(f"Q{i} [{q['id']}]: Ratio {ratio:.2f}")
            print(f"  Word counts: {wc}")
            print(f"  Correct idx: {q['correctIndex']}, Correct WC: {correct_wc}")
            for j, choice in enumerate(q['choices']):
                marker = " ← CORRECT" if j == q['correctIndex'] else ""
                marker += " (LONGEST)" if wc[j] == max_wc else ""
                print(f"  [{j}] ({wc[j]}w) {choice}{marker}")
            print()

for ch in [2, 3, 4, 5]:
    analyze_chapter_detailed(ch)
