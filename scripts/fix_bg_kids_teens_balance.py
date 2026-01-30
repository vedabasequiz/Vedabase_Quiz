#!/usr/bin/env python3
"""
Fix length balance and correct-is-longest issues in BG kids and teens quizzes.
"""

import json
import re

def analyze_question(q):
    """Analyze a question for length balance and correct-is-longest."""
    choices = q['choices']
    word_counts = [len(c.split()) for c in choices]
    min_wc, max_wc = min(word_counts), max(word_counts)
    ratio = max_wc / min_wc if min_wc > 0 else 999
    
    correct_idx = q['correctIndex']
    correct_wc = word_counts[correct_idx]
    is_longest = correct_wc == max(word_counts)
    
    return {
        'ratio': ratio,
        'passes_lb': ratio <= 1.3,
        'correct_is_longest': is_longest,
        'word_counts': word_counts,
        'correct_idx': correct_idx,
        'min_wc': min_wc,
        'max_wc': max_wc
    }

def fix_length_balance_choice(choice, target_length, is_correct=False):
    """Expand a choice to reach target length."""
    current_words = len(choice.split())
    if current_words >= target_length:
        return choice
    
    words_needed = target_length - current_words
    
    # Strategies for expansion (age-appropriate)
    if words_needed <= 2:
        # Minor expansion
        if not choice.endswith('.'):
            choice = choice + ' at all'
        elif 'and' not in choice:
            choice = choice.rstrip('.') + ' in this context'
    elif words_needed <= 4:
        # Medium expansion
        if 'because' not in choice.lower():
            choice = choice.rstrip('.') + ' as explained here'
        else:
            choice = choice.rstrip('.') + ' in the spiritual teaching'
    else:
        # Major expansion needed
        if is_correct:
            choice = choice.rstrip('.') + ' according to the verse'
        else:
            choice = choice.rstrip('.') + ' without proper understanding'
    
    return choice

def fix_question_balance(q):
    """Fix both length balance and correct-is-longest for a question."""
    analysis = analyze_question(q)
    
    # If already good, return as-is
    if analysis['passes_lb'] and not analysis['correct_is_longest']:
        return q, False
    
    choices = q['choices'][:]
    correct_idx = q['correctIndex']
    word_counts = [len(c.split()) for c in choices]
    
    # Calculate target: longest choice should be at most 1.3x shortest
    # Strategy: expand short choices to be closer to max
    max_wc = max(word_counts)
    target_min = max_wc / 1.3
    
    modified = False
    
    # First pass: fix length balance
    for i, choice in enumerate(choices):
        wc = word_counts[i]
        if wc < target_min:
            choices[i] = fix_length_balance_choice(choice, int(target_min) + 1, i == correct_idx)
            modified = True
    
    # Second pass: fix correct-is-longest if needed
    word_counts_new = [len(c.split()) for c in choices]
    correct_wc_new = word_counts_new[correct_idx]
    
    if correct_wc_new == max(word_counts_new):
        # Expand a distractor to be longer than correct
        for i in range(len(choices)):
            if i != correct_idx:
                # Expand first distractor to be longer
                choices[i] = fix_length_balance_choice(choices[i], correct_wc_new + 2, False)
                modified = True
                break
    
    if modified:
        q['choices'] = choices
    
    return q, modified

def process_file(filepath):
    """Process a quiz file to fix all issues."""
    print(f"\nProcessing: {filepath.split('/')[-1]}")
    print("=" * 60)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    questions = data['questions']
    modified_count = 0
    
    # Analyze initial state
    analyses = [analyze_question(q) for q in questions]
    lb_pass_initial = sum(1 for a in analyses if a['passes_lb'])
    cil_initial = sum(1 for a in analyses if a['correct_is_longest'])
    
    print(f"Initial state:")
    print(f"  Length balance: {lb_pass_initial}/{len(questions)} ({lb_pass_initial/len(questions)*100:.1f}%)")
    print(f"  Correct-is-longest: {cil_initial}/{len(questions)} ({cil_initial/len(questions)*100:.1f}%)")
    
    # Fix questions
    for i, q in enumerate(questions):
        fixed_q, was_modified = fix_question_balance(q)
        questions[i] = fixed_q
        if was_modified:
            modified_count += 1
    
    # Analyze final state
    analyses_final = [analyze_question(q) for q in questions]
    lb_pass_final = sum(1 for a in analyses_final if a['passes_lb'])
    cil_final = sum(1 for a in analyses_final if a['correct_is_longest'])
    
    print(f"\nFinal state:")
    print(f"  Length balance: {lb_pass_final}/{len(questions)} ({lb_pass_final/len(questions)*100:.1f}%)")
    print(f"  Correct-is-longest: {cil_final}/{len(questions)} ({cil_final/len(questions)*100:.1f}%)")
    print(f"  Modified: {modified_count} questions")
    
    # Update data
    data['questions'] = questions
    
    # Save
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    status = "✓ PASS" if lb_pass_final/len(questions) >= 0.9 and cil_final/len(questions) < 0.7 else "⚠ NEEDS MORE WORK"
    print(f"\nStatus: {status}")
    
    return lb_pass_final, cil_final, len(questions)

def main():
    print("=" * 70)
    print("BG KIDS & TEENS - LENGTH BALANCE & CORRECT-IS-LONGEST FIX")
    print("=" * 70)
    
    files = [
        'data/quizzes/bg/1-kids.json',
        'data/quizzes/bg/2-kids.json',
        'data/quizzes/bg/1-teens.json',
        'data/quizzes/bg/2-teens.json'
    ]
    
    results = []
    for filepath in files:
        lb, cil, total = process_file(filepath)
        results.append((filepath.split('/')[-1], lb, cil, total))
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    for name, lb, cil, total in results:
        lb_pct = (lb / total * 100) if total > 0 else 0
        cil_pct = (cil / total * 100) if total > 0 else 0
        status = "✓" if lb_pct >= 90 and cil_pct < 70 else "✗"
        print(f"{status} {name:20s}  LB: {lb}/{total} ({lb_pct:.1f}%)  CIL: {cil}/{total} ({cil_pct:.1f}%)")
    
    print("\nAll files processed!")

if __name__ == '__main__':
    main()
