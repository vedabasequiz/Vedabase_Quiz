#!/usr/bin/env python3
"""Analyze length balance issues in quiz files"""

import json
import sys

def analyze_question(q):
    """Analyze a single question's choice length balance"""
    choices = q['choices']
    word_counts = [len(choice.split()) for choice in choices]
    
    min_wc = min(word_counts)
    max_wc = max(word_counts)
    ratio = max_wc / min_wc if min_wc > 0 else 999
    
    correct_idx = q['correctIndex']
    correct_is_longest = word_counts[correct_idx] == max_wc
    
    return {
        'id': q['id'],
        'prompt': q['prompt'],
        'choices': choices,
        'word_counts': word_counts,
        'min': min_wc,
        'max': max_wc,
        'ratio': ratio,
        'passes': ratio <= 1.3,
        'correct_idx': correct_idx,
        'correct_is_longest': correct_is_longest
    }

def main():
    for file_path in sys.argv[1:]:
        with open(file_path) as f:
            data = json.load(f)
        
        chapter = data['chapter']
        results = [analyze_question(q) for q in data['questions']]
        
        failing = [r for r in results if not r['passes']]
        correct_longest_count = sum(1 for r in results if r['correct_is_longest'])
        
        total = len(results)
        pass_rate = ((total - len(failing)) / total) * 100
        correct_longest_pct = (correct_longest_count / total) * 100
        
        print(f"\n{'='*80}")
        print(f"CHAPTER {chapter} Analysis")
        print(f"{'='*80}")
        print(f"Length Balance: {pass_rate:.0f}% ({total - len(failing)}/{total} pass)")
        print(f"Correct-is-Longest: {correct_longest_pct:.0f}% ({correct_longest_count}/{total})")
        print(f"\nFailing Questions: {len(failing)}")
        print()
        
        for r in failing:
            print(f"{r['id']}: {r['prompt'][:70]}...")
            print(f"  Word counts: {r['word_counts']} | Min:{r['min']} Max:{r['max']} Ratio:{r['ratio']:.2f}x")
            for i, (ch, wc) in enumerate(zip(r['choices'], r['word_counts'])):
                marker = " ← CORRECT" if i == r['correct_idx'] else ""
                if wc == r['min']:
                    marker += " [TOO SHORT]"
                elif wc == r['max'] and r['ratio'] > 1.3:
                    marker += " [TOO LONG]"
                print(f"  [{i}] ({wc:2d}w) {ch[:65]}{marker}")
            print()

if __name__ == '__main__':
    main()
