#!/usr/bin/env python3
"""
Comprehensive BG Quiz Audit against VEDABASE_BG_PUBLISH_CHECKLIST.md
"""

import json
import os
import re
from pathlib import Path

# Quiz directory
QUIZ_DIR = Path("/Users/prakashchincholikar/Vedabase_Quiz/data/quizzes/bg")

# Expected question counts
EXPECTED_COUNTS = {
    "adult": 25,
    "teens": 15,
    "kids": 10
}

def check_unicode_chars(text):
    """Check for Unicode smart quotes and special chars"""
    unicode_chars = []
    # Smart quotes and dashes
    problematic = ['', '', '', '', '–', '—', '…']
    for char in problematic:
        if char in text:
            unicode_chars.append(char)
    return unicode_chars

def analyze_quiz_file(filepath):
    """Analyze a single quiz file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    filename = filepath.name
    issues = {
        'tier1': [],
        'tier2': [],
        'tier3': []
    }
    
    # Basic metadata
    scripture = data.get('scripture', '')
    chapter = data.get('chapter', '')
    audience = data.get('audience', '')
    questions = data.get('questions', [])
    
    # TIER 1 CHECKS
    # 1. Scripture/chapter/audience tags
    if scripture != 'bg':
        issues['tier1'].append(f"❌ Scripture tag is '{scripture}', expected 'bg'")
    
    # 2. Structural integrity - question count
    expected_count = EXPECTED_COUNTS.get(audience, 0)
    actual_count = len(questions)
    if actual_count != expected_count:
        issues['tier1'].append(f"❌ Question count: {actual_count}, expected {expected_count}")
    
    # Check each question
    translation_count = 0
    purport_count = 0
    
    for i, q in enumerate(questions, 1):
        qid = q.get('id', f'q{i}')
        
        # TIER 1: Feedback presence
        feedback = q.get('feedback', '')
        if not feedback:
            issues['tier1'].append(f"❌ Q{i} ({qid}): Missing feedback")
        
        # TIER 1: Verdict check
        verdict = q.get('verdict', '')
        if verdict not in ['Correct', 'Review']:
            issues['tier1'].append(f"❌ Q{i} ({qid}): Invalid verdict '{verdict}'")
        
        # TIER 1: Verse URL presence
        verse_url = q.get('verseUrl', '')
        if not verse_url:
            issues['tier1'].append(f"❌ Q{i} ({qid}): Missing verseUrl")
        elif not verse_url.startswith('https://vedabase.io/'):
            issues['tier1'].append(f"❌ Q{i} ({qid}): Invalid verseUrl (not vedabase.io)")
        
        # TIER 1: ASCII-only check
        prompt = q.get('prompt', '')
        choices = q.get('choices', [])
        
        unicode_in_prompt = check_unicode_chars(prompt)
        if unicode_in_prompt:
            issues['tier1'].append(f"❌ Q{i} ({qid}): Unicode chars in prompt: {unicode_in_prompt}")
        
        for ci, choice in enumerate(choices):
            unicode_in_choice = check_unicode_chars(str(choice))
            if unicode_in_choice:
                issues['tier1'].append(f"❌ Q{i} ({qid}): Unicode chars in choice {ci+1}: {unicode_in_choice}")
        
        unicode_in_feedback = check_unicode_chars(feedback)
        if unicode_in_feedback:
            issues['tier1'].append(f"❌ Q{i} ({qid}): Unicode chars in feedback: {unicode_in_feedback}")
        
        # TIER 2: MCQ Quality - exactly 4 choices
        if len(choices) != 4:
            issues['tier2'].append(f"⚠️ Q{i} ({qid}): {len(choices)} choices (expected 4)")
        
        # TIER 2: Correct index validation
        correct_idx = q.get('correctIndex')
        if correct_idx is None or correct_idx < 0 or correct_idx >= len(choices):
            issues['tier2'].append(f"⚠️ Q{i} ({qid}): Invalid correctIndex {correct_idx}")
        
        # TIER 2: Check for "all of the above" or "none of the above"
        for choice in choices:
            choice_lower = str(choice).lower()
            if 'all of the above' in choice_lower or 'none of the above' in choice_lower:
                issues['tier2'].append(f"⚠️ Q{i} ({qid}): Contains 'all/none of the above'")
                break
        
        # Count translation vs purport based questions
        verse_label = q.get('verseLabel', '').lower()
        if 'purport' in feedback.lower() or 'prabhupada' in feedback.lower():
            purport_count += 1
        else:
            translation_count += 1
    
    # TIER 2: Translation vs Purport balance
    if len(questions) > 0:
        purport_ratio = purport_count / len(questions) * 100
        translation_ratio = translation_count / len(questions) * 100
        
        # Expected: ~60-65% translation, ~35-40% purport
        if purport_ratio < 30 or purport_ratio > 45:
            issues['tier2'].append(f"⚠️ Purport ratio: {purport_ratio:.1f}% (expected ~35-40%)")
        if translation_ratio < 55 or translation_ratio > 70:
            issues['tier2'].append(f"⚠️ Translation ratio: {translation_ratio:.1f}% (expected ~60-65%)")
    
    # TIER 3: Feedback depth for adults
    if audience == 'adult':
        short_feedback_count = 0
        for i, q in enumerate(questions, 1):
            feedback = q.get('feedback', '')
            sentences = len([s for s in feedback.split('.') if s.strip()])
            if sentences < 2:
                short_feedback_count += 1
        
        if short_feedback_count > len(questions) * 0.3:
            issues['tier3'].append(f"ℹ️ {short_feedback_count} questions have brief feedback (adults should have 3-5 sentences for depth)")
    
    return {
        'filename': filename,
        'chapter': chapter,
        'audience': audience,
        'question_count': len(questions),
        'expected_count': expected_count,
        'translation_count': translation_count,
        'purport_count': purport_count,
        'issues': issues
    }

def main():
    """Main audit function"""
    print("="*80)
    print("VEDABASE BG QUIZ AUDIT REPORT")
    print("="*80)
    print()
    
    # Get all quiz files
    quiz_files = sorted(QUIZ_DIR.glob("*.json"))
    
    all_results = []
    
    for filepath in quiz_files:
        result = analyze_quiz_file(filepath)
        all_results.append(result)
    
    # Organize by chapter
    chapters = {}
    for result in all_results:
        ch = result['chapter']
        if ch not in chapters:
            chapters[ch] = {'adult': None, 'teens': None, 'kids': None}
        chapters[ch][result['audience']] = result
    
    # Print report
    for ch in sorted(chapters.keys()):
        print(f"\n{'='*80}")
        print(f"CHAPTER {ch}")
        print(f"{'='*80}")
        
        for audience in ['adult', 'teens', 'kids']:
            result = chapters[ch].get(audience)
            if not result:
                print(f"\n  [{audience.upper()}] - FILE MISSING")
                continue
            
            print(f"\n  [{audience.upper()}] - {result['filename']}")
            print(f"  Questions: {result['question_count']} / {result['expected_count']} expected")
            
            if result['translation_count'] + result['purport_count'] > 0:
                trans_pct = result['translation_count'] / result['question_count'] * 100
                purp_pct = result['purport_count'] / result['question_count'] * 100
                print(f"  Translation: ~{trans_pct:.0f}% | Purport: ~{purp_pct:.0f}%")
            
            # TIER 1 issues
            if result['issues']['tier1']:
                print(f"\n  🔴 TIER 1 VIOLATIONS (CRITICAL):")
                for issue in result['issues']['tier1'][:10]:  # Limit display
                    print(f"    {issue}")
                if len(result['issues']['tier1']) > 10:
                    print(f"    ... and {len(result['issues']['tier1']) - 10} more")
            
            # TIER 2 issues
            if result['issues']['tier2']:
                print(f"\n  🟡 TIER 2 ISSUES (MUST FIX):")
                for issue in result['issues']['tier2'][:10]:
                    print(f"    {issue}")
                if len(result['issues']['tier2']) > 10:
                    print(f"    ... and {len(result['issues']['tier2']) - 10} more")
            
            # TIER 3 observations
            if result['issues']['tier3']:
                print(f"\n  🔵 TIER 3 OBSERVATIONS (POLISH):")
                for issue in result['issues']['tier3']:
                    print(f"    {issue}")
            
            # Overall verdict
            if not result['issues']['tier1'] and not result['issues']['tier2']:
                print(f"\n  ✅ VERDICT: READY TO PUBLISH")
            elif result['issues']['tier1']:
                print(f"\n  ❌ VERDICT: BLOCKED - Fix Tier 1 violations before publish")
            else:
                print(f"\n  ⚠️  VERDICT: NEEDS IMPROVEMENT - Address Tier 2 issues")
    
    # Summary
    print(f"\n\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    
    total_files = len(all_results)
    tier1_blocked = sum(1 for r in all_results if r['issues']['tier1'])
    tier2_issues = sum(1 for r in all_results if r['issues']['tier2'])
    ready = sum(1 for r in all_results if not r['issues']['tier1'] and not r['issues']['tier2'])
    
    print(f"Total quiz files: {total_files}")
    print(f"✅ Ready to publish: {ready}")
    print(f"⚠️  Tier 2 issues only: {tier2_issues - tier1_blocked}")
    print(f"❌ Tier 1 blocked: {tier1_blocked}")
    
    print("\n" + "="*80)

if __name__ == "__main__":
    main()
