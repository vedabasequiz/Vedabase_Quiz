"""Analyze BG teens quizzes for gold standard compliance"""
import json

def analyze_quiz(ch):
    filename = f'data/quizzes/bg/{ch}-teens.json'
    
    with open(filename) as f:
        data = json.load(f)
    
    print(f"\n{'='*70}")
    print(f"CHAPTER {ch} TEENS - DETAILED ANALYSIS")
    print(f"{'='*70}")
    
    total = len(data['questions'])
    purport_qs = []
    verse_qs = []
    short_feedback_qs = []
    
    for i, q in enumerate(data['questions'], 1):
        qtype = q.get('questionType', 'verse')
        feedback = q.get('feedback', '')
        fb_words = len(feedback.split())
        
        if qtype == 'purport':
            purport_qs.append(f"q{i}")
        else:
            verse_qs.append(f"q{i}")
        
        if fb_words < 30:
            short_feedback_qs.append((i, fb_words, q['verseLabel']))
    
    purport_pct = (len(purport_qs) / total * 100) if total else 0
    
    print(f"\nTotal questions: {total}")
    print(f"Purport questions: {len(purport_qs)}/{total} ({purport_pct:.0f}%)")
    print(f"  Target: 5-6 questions (33-40%)")
    print(f"  Purport Qs: {', '.join(purport_qs)}")
    
    if purport_pct < 33:
        print(f"  ⚠️ TOO LOW - need {6 - len(purport_qs)} more purport questions")
    elif purport_pct > 40:
        print(f"  ⚠️ TOO HIGH - need to convert {len(purport_qs) - 6} to verse questions")
    else:
        print(f"  ✅ GOLD STANDARD")
    
    print(f"\nShort feedback (<30 words): {len(short_feedback_qs)}")
    if short_feedback_qs:
        print(f"  Questions needing expansion:")
        for qnum, words, verse in short_feedback_qs:
            print(f"    q{qnum}: {words}w ({verse})")
    else:
        print(f"  ✅ All feedback meets 30+ word minimum")
    
    return {
        'chapter': ch,
        'total': total,
        'purport_count': len(purport_qs),
        'purport_pct': purport_pct,
        'purport_qs': purport_qs,
        'short_feedback': short_feedback_qs
    }

ch1 = analyze_quiz(1)
ch2 = analyze_quiz(2)

print(f"\n{'='*70}")
print("GOLD STANDARD FIXES NEEDED")
print(f"{'='*70}")

print(f"\nCh1: Convert 2 purport questions to verse questions")
print(f"Ch2: Convert 1 purport question to verse questions")
print(f"\nTotal: Expand {len(ch1['short_feedback']) + len(ch2['short_feedback'])} short feedbacks")
