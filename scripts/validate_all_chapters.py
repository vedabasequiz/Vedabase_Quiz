#!/usr/bin/env python3
"""Validate all BG chapter quizzes (1-18) against Tier 1 checklist."""
import json
from pathlib import Path

def validate_file(filepath):
    """Validate single quiz file."""
    try:
        with open(filepath, 'r') as f:
            obj = json.load(f)
    except Exception as e:
        return f"PARSE_ERROR: {e}"
    
    issues = []
    
    # Check required fields
    for field in ['id', 'scripture', 'chapter', 'audience', 'title', 'difficulty', 'questions']:
        if field not in obj:
            issues.append(f"Missing top-level: {field}")
    
    # Check question count
    qcount = len(obj.get('questions', []))
    if qcount != 25:
        issues.append(f"Question count {qcount} != 25")
    
    # Check each question
    for i, q in enumerate(obj.get('questions', []), 1):
        if not isinstance(q, dict):
            issues.append(f"Q{i}: not dict")
            continue
        
        # Required fields
        for field in ['id', 'prompt', 'choices', 'correctIndex', 'feedback', 'verseLabel', 'verseUrl', 'verdict']:
            if field not in q:
                issues.append(f"Q{i}: missing {field}")
        
        # Validate choices
        choices = q.get('choices', [])
        if not isinstance(choices, list) or len(choices) < 2:
            issues.append(f"Q{i}: bad choices (< 2 options)")
        
        # Validate correctIndex
        ci = q.get('correctIndex')
        if not isinstance(ci, int) or not (0 <= ci < len(choices)):
            issues.append(f"Q{i}: correctIndex {ci} out of range [0, {len(choices)-1}]")
        
        # Check ASCII
        for field in ['prompt', 'feedback', 'verseLabel']:
            text = q.get(field, '')
            try:
                text.encode('ascii')
            except UnicodeEncodeError:
                issues.append(f"Q{i}: non-ASCII in {field}")
        
        # Check verseUrl
        vu = q.get('verseUrl', '')
        if not vu.startswith('https://vedabase.io'):
            issues.append(f"Q{i}: bad verseUrl (not vedabase.io)")
        
        # Check verdict
        if q.get('verdict') not in ('Correct', 'Review'):
            issues.append(f"Q{i}: verdict '{q.get('verdict')}' not in (Correct, Review)")
    
    return issues if issues else None

def main():
    quiz_dir = Path('data/quizzes/bg')
    results = {}
    ok_count = 0
    
    for chapter in range(1, 19):
        filepath = quiz_dir / f'{chapter}-adult.json'
        if not filepath.exists():
            results[chapter] = 'SKIP (file not found)'
            continue
        
        issues = validate_file(filepath)
        if issues is None:
            results[chapter] = 'PASS'
            ok_count += 1
        else:
            results[chapter] = f'FAIL ({len(issues)} issues)'
            for issue in issues[:3]:  # Show first 3 issues
                print(f"  BG {chapter}: {issue}")
            if len(issues) > 3:
                print(f"  BG {chapter}: ... and {len(issues)-3} more")
    
    print("\n" + "="*60)
    print(f"TIER 1 VALIDATION RESULTS")
    print("="*60)
    for ch in sorted(results.keys()):
        status = results[ch]
        marker = "✓" if status == "PASS" else "✗" if "FAIL" in status else "○"
        print(f"{marker} BG {ch:2d}: {status}")
    
    print(f"\n✓ PASSED: {ok_count}/18")
    print(f"✗ FAILED: {18-ok_count}/18")
    
    return 0 if ok_count == 18 else 1

if __name__ == '__main__':
    import sys
    sys.exit(main())
