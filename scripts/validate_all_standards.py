#!/usr/bin/env python3
"""
Comprehensive validator for Vedabase Quiz chapters against ALL standards
(Tier 1: Hard Rules, Tier 2: Strong Constraints, Tier 3: Gold-Standard)
"""

import json
from pathlib import Path

class QuizValidator:
    def __init__(self):
        self.tier1_issues = []
        self.tier2_issues = []
        self.tier3_issues = []
    
    def validate_chapter(self, chapter, filepath):
        """Validate a single chapter file against all tiers."""
        self.tier1_issues = []
        self.tier2_issues = []
        self.tier3_issues = []
        
        # Read file
        try:
            with open(filepath, 'r') as f:
                obj = json.load(f)
        except Exception as e:
            return f"JSON_ERROR: {e}", {}, {}, {}
        
        # TIER 1: HARD RULES
        self._validate_tier1(obj, chapter)
        
        # TIER 2: STRONG CONSTRAINTS
        if not self.tier1_issues:  # Only check Tier 2 if Tier 1 passes
            self._validate_tier2(obj, chapter)
        
        # TIER 3: GOLD-STANDARD (informational, not blocking)
        if not self.tier1_issues:
            self._validate_tier3(obj, chapter)
        
        status = "PASS_ALL" if not self.tier1_issues and not self.tier2_issues else \
                 "PASS_T1_ONLY" if self.tier1_issues else \
                 "ISSUES_T2" if self.tier2_issues else \
                 "ISSUES_T3"
        
        return status, {
            'tier1': self.tier1_issues,
            'tier2': self.tier2_issues,
            'tier3': self.tier3_issues
        }, obj.get('questions', []), obj
    
    def _validate_tier1(self, obj, chapter):
        """1. SOURCE INTEGRITY & STRUCTURAL INTEGRITY"""
        
        # Required fields
        required = ['id', 'scripture', 'chapter', 'audience', 'title', 'difficulty', 'questions']
        for field in required:
            if field not in obj:
                self.tier1_issues.append(f"T1.1: Missing required field '{field}'")
        
        # Question count
        qcount = len(obj.get('questions', []))
        expected = 25 if obj.get('audience') == 'adult' else 15 if obj.get('audience') == 'teens' else 10
        if qcount != expected:
            self.tier1_issues.append(f"T1.2: Question count is {qcount}, expected {expected}")
        
        # Audience validation
        audience = obj.get('audience')
        if audience not in ('adult', 'teens', 'kids'):
            self.tier1_issues.append(f"T1.2: Invalid audience '{audience}'")
        
        # Scripture and chapter
        if obj.get('scripture') != 'bg':
            self.tier1_issues.append(f"T1.2: Invalid scripture '{obj.get('scripture')}'")
        if obj.get('chapter') != chapter:
            self.tier1_issues.append(f"T1.2: Chapter mismatch: file={chapter}, obj={obj.get('chapter')}")
        
        # Per-question validation
        for i, q in enumerate(obj.get('questions', []), start=1):
            if not isinstance(q, dict):
                self.tier1_issues.append(f"T1.3: Q{i} is not a dict")
                continue
            
            # Required fields
            for field in ['id', 'prompt', 'choices', 'correctIndex', 'feedback', 'verseLabel', 'verseUrl', 'verdict']:
                if field not in q:
                    self.tier1_issues.append(f"T1.3: Q{i} missing '{field}'")
            
            # Choices and correctIndex
            choices = q.get('choices', [])
            if not isinstance(choices, list) or len(choices) < 2:
                self.tier1_issues.append(f"T1.3: Q{i} has invalid choices")
            
            ci = q.get('correctIndex')
            if not isinstance(ci, int) or not (0 <= ci < len(choices)):
                self.tier1_issues.append(f"T1.3: Q{i} has invalid correctIndex {ci}")
            
            # ASCII-only
            for field in ['prompt', 'feedback', 'verseLabel']:
                text = q.get(field, '')
                try:
                    text.encode('ascii')
                except UnicodeEncodeError:
                    self.tier1_issues.append(f"T1.4: Q{i} '{field}' contains non-ASCII")
            
            # Vedabase URL
            url = q.get('verseUrl', '')
            if not url.startswith('https://vedabase.io'):
                self.tier1_issues.append(f"T1.4: Q{i} verseUrl not from vedabase.io")
            
            # Verdict values
            verdict = q.get('verdict')
            if verdict not in ('Correct', 'Review'):
                self.tier1_issues.append(f"T1.5: Q{i} verdict '{verdict}' invalid (must be 'Correct' or 'Review')")
    
    def _validate_tier2(self, obj, chapter):
        """2. MCQ QUALITY, TRANSLATION/PURPORT BALANCE, DIFFICULTY, FEEDBACK"""
        
        questions = obj.get('questions', [])
        audience = obj.get('audience', 'adult')
        
        # 6. MCQ Quality
        for i, q in enumerate(questions, start=1):
            choices = q.get('choices', [])
            
            # Check for all/none of the above
            for j, choice in enumerate(choices):
                choice_lower = choice.lower()
                if 'all of the above' in choice_lower or 'none of the above' in choice_lower:
                    self.tier2_issues.append(f"T2.6: Q{i} choice {j+1} uses banned phrase")
            
            # Check distractor plausibility (basic: no all identical, no empty)
            if len(set(choices)) < len(choices):
                self.tier2_issues.append(f"T2.6: Q{i} has duplicate choices")
            
            if any(not c.strip() for c in choices):
                self.tier2_issues.append(f"T2.6: Q{i} has empty choice")
        
        # 8. Difficulty Progression
        # Basic check: first ~60% should be simpler (shorter questions), last ~40% complex
        first_60_idx = int(len(questions) * 0.6)
        first_60 = questions[:first_60_idx]
        last_40 = questions[first_60_idx:]
        
        avg_first = sum(len(q.get('prompt', '')) for q in first_60) / len(first_60) if first_60 else 0
        avg_last = sum(len(q.get('prompt', '')) for q in last_40) / len(last_40) if last_40 else 0
        
        if avg_last < avg_first * 0.8:  # Last section should be longer/more complex
            self.tier2_issues.append(f"T2.8: Difficulty may not progress (first 60% avg {avg_first:.0f} chars, last 40% avg {avg_last:.0f})")
        
        # 9. Feedback Quality
        for i, q in enumerate(questions, start=1):
            feedback = q.get('feedback', '')
            if not feedback or len(feedback.strip()) < 10:
                self.tier2_issues.append(f"T2.9: Q{i} feedback too short or empty")
            
            # For adults: check for contrastive reasoning hint
            if audience == 'adult' and len(feedback) < 50:
                self.tier2_issues.append(f"T2.9: Q{i} feedback may lack depth for adult audience")
    
    def _validate_tier3(self, obj, chapter):
        """3. GOLD-STANDARD: Question craft, Distractor elegance, Feedback depth"""
        
        questions = obj.get('questions', [])
        audience = obj.get('audience', 'adult')
        
        # 11. Question Craft - check for overly long or too short
        for i, q in enumerate(questions, start=1):
            prompt = q.get('prompt', '')
            if len(prompt) > 200:
                self.tier3_issues.append(f"T3.11: Q{i} prompt very long ({len(prompt)} chars)")
            if len(prompt) < 15:
                self.tier3_issues.append(f"T3.11: Q{i} prompt very short ({len(prompt)} chars)")
        
        # 13. Feedback Depth (Adults)
        if audience == 'adult':
            for i, q in enumerate(questions, start=1):
                feedback = q.get('feedback', '')
                # Count sentences
                sentences = feedback.count('.') + feedback.count('!') + feedback.count('?')
                if sentences < 2:
                    self.tier3_issues.append(f"T3.13: Q{i} feedback should be 3-5 sentences (has {sentences})")
        
        # 14. End-of-Chapter Finish - last question shouldn't be purely factual
        if questions:
            last_q = questions[-1]
            last_prompt = last_q.get('prompt', '').lower()
            # Check if it ends on reflection/insight (positive sign)
            insight_words = ['how', 'why', 'meaning', 'teach', 'conclude', 'true', 'nature', 'ultimate']
            has_insight = any(word in last_prompt for word in insight_words)
            if not has_insight:
                self.tier3_issues.append(f"T3.14: Last question may not end on insight/reflection")
        
        # 15. Overall Flow - basic check: no huge prompt length variations
        if questions:
            lengths = [len(q.get('prompt', '')) for q in questions]
            avg_len = sum(lengths) / len(lengths)
            outliers = [i for i, l in enumerate(lengths, start=1) if abs(l - avg_len) > 100]
            if len(outliers) > 3:
                self.tier3_issues.append(f"T3.15: Many questions have very different lengths (outliers: {outliers[:5]})")

def main():
    validator = QuizValidator()
    data_dir = Path('data/quizzes/bg')
    
    results = {}
    chapters_pass_all = 0
    chapters_pass_t1 = 0
    chapters_with_t2_issues = 0
    chapters_with_t3_issues = 0
    
    print("=" * 80)
    print("COMPREHENSIVE VALIDATION: All Tiers (T1, T2, T3)")
    print("=" * 80)
    
    for chapter in range(1, 19):
        filepath = data_dir / f'{chapter}-adult.json'
        
        if not filepath.exists():
            print(f"BG {chapter:2d}: FILE NOT FOUND")
            results[chapter] = 'NOT_FOUND'
            continue
        
        status, issues, questions, obj = validator.validate_chapter(chapter, filepath)
        results[chapter] = status
        
        # Summarize
        t1_cnt = len(issues['tier1'])
        t2_cnt = len(issues['tier2'])
        t3_cnt = len(issues['tier3'])
        
        if status == 'JSON_ERROR':
            print(f"BG {chapter:2d}: {status} - {issues}")
        elif status == 'PASS_ALL':
            chapters_pass_all += 1
            print(f"BG {chapter:2d}: ✓ PASS (All Tiers)")
        else:
            print(f"BG {chapter:2d}: {status}")
            if t1_cnt > 0:
                chapters_pass_t1 += 1
                print(f"           Tier 1 Issues ({t1_cnt}):")
                for issue in issues['tier1'][:3]:
                    print(f"             • {issue}")
                if t1_cnt > 3:
                    print(f"             ... and {t1_cnt - 3} more")
            if t2_cnt > 0:
                chapters_with_t2_issues += 1
                print(f"           Tier 2 Issues ({t2_cnt}):")
                for issue in issues['tier2'][:2]:
                    print(f"             • {issue}")
                if t2_cnt > 2:
                    print(f"             ... and {t2_cnt - 2} more")
            if t3_cnt > 0:
                chapters_with_t3_issues += 1
                print(f"           Tier 3 Notes ({t3_cnt}):")
                for issue in issues['tier3'][:2]:
                    print(f"             • {issue}")
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"✓ Chapters PASS All Tiers:     {chapters_pass_all}/18")
    print(f"✓ Chapters PASS Tier 1 only:   {chapters_pass_t1}/18")
    print(f"⚠ Chapters with Tier 2 issues: {chapters_with_t2_issues}/18")
    print(f"💡 Chapters with Tier 3 notes: {chapters_with_t3_issues}/18")
    print("=" * 80)
    
    return 0 if chapters_pass_all == 18 else 1

if __name__ == '__main__':
    import sys
    sys.exit(main())
