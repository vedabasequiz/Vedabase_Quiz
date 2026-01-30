#!/usr/bin/env python3
"""
Quiz Quality Validator
Checks for length bias and obvious distractors in BG quiz files.
"""

import json
import os
import sys
from typing import List, Tuple

def check_length_bias(choices: List[str], correct_index: int) -> Tuple[bool, str, dict]:
    """Check if correct answer has suspicious length patterns."""
    lengths = [len(choice.split()) for choice in choices]
    correct_length = lengths[correct_index]
    distractor_lengths = [l for i, l in enumerate(lengths) if i != correct_index]
    avg_distractor_length = sum(distractor_lengths) / len(distractor_lengths)
    max_length = max(lengths)
    min_length = min(lengths)
    
    issues = []
    
    # Check if correct is significantly longer than average
    if correct_length > avg_distractor_length * 1.5:
        issues.append(f"Correct answer is {correct_length} words vs {avg_distractor_length:.1f} avg distractor")
    
    # Check if variance is too high (longest > 1.3x shortest)
    if max_length > min_length * 1.3:
        variance_ratio = max_length / min_length
        issues.append(f"High variance: {min_length}-{max_length} words ({variance_ratio:.1f}x)")
    
    # Check if correct is consistently in longest position
    longest_index = lengths.index(max_length)
    if longest_index == correct_index and max_length > min_length * 1.2:
        issues.append(f"Correct is longest ({max_length} vs {min_length} words)")
    
    stats = {
        "lengths": lengths,
        "correct_length": correct_length,
        "avg_distractor": round(avg_distractor_length, 1),
        "min": min_length,
        "max": max_length,
        "variance_ratio": round(max_length / min_length, 2)
    }
    
    return len(issues) == 0, "; ".join(issues) if issues else "Pass", stats

def check_distractor_plausibility(choices: List[str], correct_index: int) -> Tuple[bool, str]:
    """Check if distractors are too obviously wrong."""
    distractors = [c for i, c in enumerate(choices) if i != correct_index]
    
    issues = []
    
    # Check for obvious language
    obvious_words = ['obviously', 'never', 'always', 'impossible', 'silly', 'absurd', 
                     'lunch', 'dinner', 'breakfast', 'random', 'nothing']
    for idx, d in enumerate(distractors, 1):
        d_lower = d.lower()
        for word in obvious_words:
            if word in d_lower:
                issues.append(f"D{idx} contains obvious word '{word}'")
    
    # Check for very short distractors
    for idx, d in enumerate(distractors, 1):
        if len(d.split()) < 4:
            issues.append(f"D{idx} too short ({len(d.split())} words): '{d[:40]}...'")
    
    # Check for lack of specificity
    generic_patterns = ['only', 'just', 'simply', 'merely']
    generic_count = sum(1 for d in distractors if any(p in d.lower() for p in generic_patterns))
    if generic_count >= 2:
        issues.append(f"{generic_count} distractors use generic/dismissive language")
    
    return len(issues) == 0, "; ".join(issues) if issues else "Pass"

def analyze_question(question: dict, qnum: int) -> dict:
    """Analyze a single question for quality issues."""
    choices = question.get('choices', [])
    correct_index = question.get('correctIndex', -1)
    
    if len(choices) != 4 or correct_index < 0:
        return {
            "number": qnum,
            "id": question.get('id', '?'),
            "length_pass": False,
            "length_msg": "Invalid structure",
            "distractor_pass": False,
            "distractor_msg": "Invalid structure",
            "overall": "FAIL"
        }
    
    length_pass, length_msg, stats = check_length_bias(choices, correct_index)
    distractor_pass, distractor_msg = check_distractor_plausibility(choices, correct_index)
    
    return {
        "number": qnum,
        "id": question.get('id', '?'),
        "length_pass": length_pass,
        "length_msg": length_msg,
        "length_stats": stats,
        "distractor_pass": distractor_pass,
        "distractor_msg": distractor_msg,
        "overall": "PASS" if (length_pass and distractor_pass) else "FAIL"
    }

def analyze_quiz_file(filepath: str) -> dict:
    """Analyze entire quiz file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            quiz = json.load(f)
        
        questions = quiz.get('questions', [])
        results = [analyze_question(q, i+1) for i, q in enumerate(questions)]
        
        pass_count = sum(1 for r in results if r['overall'] == 'PASS')
        fail_count = len(results) - pass_count
        
        length_issues = sum(1 for r in results if not r['length_pass'])
        distractor_issues = sum(1 for r in results if not r['distractor_pass'])
        
        # Calculate length bias pattern
        correct_is_longest = 0
        for q in questions:
            if len(q.get('choices', [])) == 4:
                lengths = [len(c.split()) for c in q['choices']]
                correct_idx = q.get('correctIndex', -1)
                if correct_idx >= 0 and lengths[correct_idx] == max(lengths):
                    correct_is_longest += 1
        
        return {
            "file": os.path.basename(filepath),
            "title": quiz.get('title', '?'),
            "total_questions": len(results),
            "pass": pass_count,
            "fail": fail_count,
            "length_issues": length_issues,
            "distractor_issues": distractor_issues,
            "correct_is_longest_pct": round(100 * correct_is_longest / len(questions), 1),
            "results": results
        }
    except Exception as e:
        return {
            "file": os.path.basename(filepath),
            "error": str(e)
        }

def print_summary(analysis: dict):
    """Print summary for one quiz file."""
    if 'error' in analysis:
        print(f"\n❌ {analysis['file']}: ERROR - {analysis['error']}")
        return
    
    emoji = "✅" if analysis['fail'] == 0 else "⚠️"
    print(f"\n{emoji} {analysis['file']} - {analysis['title']}")
    print(f"   {analysis['pass']}/{analysis['total_questions']} questions PASS")
    
    if analysis['fail'] > 0:
        print(f"   Issues: {analysis['length_issues']} length bias, {analysis['distractor_issues']} weak distractors")
        print(f"   Pattern: Correct is longest in {analysis['correct_is_longest_pct']}% of questions (target: 25%)")

def print_detailed_issues(analysis: dict, show_all: bool = False):
    """Print detailed issues for failed questions."""
    if 'error' in analysis:
        return
    
    print(f"\n{'='*70}")
    print(f"{analysis['file']} - Detailed Report")
    print(f"{'='*70}")
    
    for result in analysis['results']:
        if result['overall'] == 'FAIL' or show_all:
            status = "✓" if result['overall'] == 'PASS' else "✗"
            print(f"\n  {status} Q{result['number']} ({result['id']})")
            
            if not result['length_pass']:
                print(f"     LENGTH: {result['length_msg']}")
                stats = result.get('length_stats', {})
                print(f"     Word counts: {stats.get('lengths', [])}")
            
            if not result['distractor_pass']:
                print(f"     DISTRACTORS: {result['distractor_msg']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 validate-quiz-quality.py <quiz_file_or_directory>")
        print("\nOptions:")
        print("  --detailed     Show detailed issues for each failed question")
        print("  --all          Show all questions, not just failures")
        sys.exit(1)
    
    path = sys.argv[1]
    detailed = '--detailed' in sys.argv
    show_all = '--all' in sys.argv
    
    files = []
    if os.path.isdir(path):
        files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.json')]
    elif os.path.isfile(path):
        files = [path]
    else:
        print(f"Error: {path} not found")
        sys.exit(1)
    
    files.sort()
    
    print(f"\n{'='*70}")
    print(f"Quiz Quality Validation Report")
    print(f"{'='*70}")
    print(f"Analyzing {len(files)} quiz file(s)...\n")
    
    all_analyses = []
    for filepath in files:
        analysis = analyze_quiz_file(filepath)
        all_analyses.append(analysis)
        print_summary(analysis)
    
    if detailed or show_all:
        for analysis in all_analyses:
            if analysis.get('fail', 0) > 0 or show_all:
                print_detailed_issues(analysis, show_all)
    
    # Overall summary
    total_questions = sum(a.get('total_questions', 0) for a in all_analyses)
    total_pass = sum(a.get('pass', 0) for a in all_analyses)
    total_fail = sum(a.get('fail', 0) for a in all_analyses)
    total_length_issues = sum(a.get('length_issues', 0) for a in all_analyses)
    total_distractor_issues = sum(a.get('distractor_issues', 0) for a in all_analyses)
    
    avg_longest_pct = sum(a.get('correct_is_longest_pct', 0) for a in all_analyses if 'error' not in a) / len([a for a in all_analyses if 'error' not in a])
    
    print(f"\n{'='*70}")
    print(f"OVERALL SUMMARY")
    print(f"{'='*70}")
    print(f"Total questions analyzed: {total_questions}")
    print(f"Pass: {total_pass} ({100*total_pass/total_questions:.1f}%)")
    print(f"Fail: {total_fail} ({100*total_fail/total_questions:.1f}%)")
    print(f"\nIssue breakdown:")
    print(f"  Length bias: {total_length_issues} questions")
    print(f"  Weak distractors: {total_distractor_issues} questions")
    print(f"\nPattern analysis:")
    print(f"  Correct is longest: {avg_longest_pct:.1f}% (target: 25%)")
    
    if avg_longest_pct > 40:
        print(f"\n⚠️  WARNING: Significant length bias detected!")
        print(f"   Students can guess correct answers by choosing longest option.")
    
    print()

if __name__ == '__main__':
    main()
