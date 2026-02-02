#!/usr/bin/env python3
"""
Analyze BG teens quiz files for gold standard compliance.
Checks: purport ratio, length balance, feedback depth, and ID format
"""

import json
import re
from collections import defaultdict

def count_words(text):
    """Count words in text"""
    return len(text.split())

def analyze_quiz(filepath):
    """Analyze a single quiz file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    questions = data['questions']
    total_q = len(questions)
    
    # Count purport questions
    purport_count = sum(1 for q in questions if 'purport' in q.get('verseLabel', '').lower())
    purport_pct = (purport_count / total_q * 100) if total_q > 0 else 0
    
    # Check length balance (1.5x threshold)
    length_issues = []
    for q in questions:
        choices = q['choices']
        if len(choices) >= 2:
            correct_idx = q['correctIndex']
            correct_len = len(choices[correct_idx])
            
            for i, choice in enumerate(choices):
                if i != correct_idx:
                    if len(choice) > correct_len * 1.5:
                        length_issues.append({
                            'id': q['id'],
                            'correct_len': correct_len,
                            'distractor_len': len(choice),
                            'ratio': len(choice) / correct_len if correct_len > 0 else 0
                        })
    
    length_balance_pct = ((total_q - len(length_issues)) / total_q * 100) if total_q > 0 else 0
    
    # Check feedback depth
    feedback_lengths = []
    short_feedback = []
    for q in questions:
        fb_len = count_words(q.get('feedback', ''))
        feedback_lengths.append(fb_len)
        if fb_len < 30:  # Minimum threshold
            short_feedback.append({'id': q['id'], 'words': fb_len})
    
    avg_feedback = sum(feedback_lengths) / len(feedback_lengths) if feedback_lengths else 0
    
    # Check ID format
    id_issues = []
    for i, q in enumerate(questions):
        qid = q['id']
        # Check if ID matches expected sequential format
        expected_num = i + 1
        chapter = data['chapter']
        expected_id = f"bg{chapter}-q{expected_num}"
        
        if qid != expected_id:
            id_issues.append({
                'current': qid,
                'expected': expected_id,
                'index': i
            })
    
    return {
        'filepath': filepath,
        'chapter': data['chapter'],
        'total_questions': total_q,
        'purport_count': purport_count,
        'purport_pct': purport_pct,
        'length_balance_pct': length_balance_pct,
        'length_issues': length_issues,
        'avg_feedback': avg_feedback,
        'short_feedback': short_feedback,
        'id_issues': id_issues
    }

def print_report(analysis):
    """Print analysis report"""
    print(f"\n{'='*70}")
    print(f"CHAPTER {analysis['chapter']} TEENS QUIZ ANALYSIS")
    print(f"{'='*70}")
    
    print(f"\n📊 OVERVIEW:")
    print(f"   Total Questions: {analysis['total_questions']}")
    print(f"   Purport Questions: {analysis['purport_count']} ({analysis['purport_pct']:.1f}%)")
    print(f"   Target: 35-40% (5-6 questions)")
    
    if analysis['purport_pct'] < 35:
        print(f"   ❌ BELOW TARGET - Need {int(analysis['total_questions'] * 0.35) - analysis['purport_count']} more purport questions")
    elif analysis['purport_pct'] > 40:
        print(f"   ⚠️  ABOVE TARGET - {analysis['purport_count'] - int(analysis['total_questions'] * 0.40)} too many purport questions")
    else:
        print(f"   ✅ WITHIN TARGET RANGE")
    
    print(f"\n📏 LENGTH BALANCE:")
    print(f"   Questions passing 1.5x threshold: {analysis['length_balance_pct']:.1f}%")
    
    if analysis['length_issues']:
        print(f"   ❌ {len(analysis['length_issues'])} questions with length issues:")
        for issue in analysis['length_issues'][:5]:  # Show first 5
            print(f"      - {issue['id']}: distractor {issue['distractor_len']} chars vs correct {issue['correct_len']} chars ({issue['ratio']:.2f}x)")
        if len(analysis['length_issues']) > 5:
            print(f"      ... and {len(analysis['length_issues']) - 5} more")
    else:
        print(f"   ✅ All questions pass length balance check")
    
    print(f"\n💬 FEEDBACK DEPTH:")
    print(f"   Average feedback length: {analysis['avg_feedback']:.1f} words")
    print(f"   Target: 30-60 words (2-3 sentences)")
    
    if analysis['short_feedback']:
        print(f"   ⚠️  {len(analysis['short_feedback'])} questions with short feedback (<30 words):")
        for fb in analysis['short_feedback']:
            print(f"      - {fb['id']}: {fb['words']} words")
    else:
        print(f"   ✅ All questions have adequate feedback depth")
    
    print(f"\n🔢 ID FORMAT:")
    if analysis['id_issues']:
        print(f"   ❌ {len(analysis['id_issues'])} questions with non-sequential IDs:")
        for issue in analysis['id_issues'][:10]:  # Show first 10
            print(f"      - Current: {issue['current']} → Should be: {issue['expected']}")
        if len(analysis['id_issues']) > 10:
            print(f"      ... and {len(analysis['id_issues']) - 10} more")
    else:
        print(f"   ✅ All IDs are sequential")

if __name__ == '__main__':
    files = [
        'data/quizzes/bg/1-teens.json',
        'data/quizzes/bg/2-teens.json'
    ]
    
    print("\n" + "="*70)
    print("BG TEENS QUIZ QUALITY ANALYSIS - GOLD STANDARD CHECK")
    print("="*70)
    
    for filepath in files:
        analysis = analyze_quiz(filepath)
        print_report(analysis)
    
    print("\n" + "="*70)
    print("ANALYSIS COMPLETE")
    print("="*70 + "\n")
