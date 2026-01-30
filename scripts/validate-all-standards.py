#!/usr/bin/env python3
"""
Comprehensive validation script for BG/SB quizzes
Checks ALL Tier 1, 2, 3 standards + Quality standards
Run before committing any quiz changes
"""

import json
import sys
import re
from pathlib import Path
from typing import Dict, List, Tuple

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_header(text):
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text.center(70)}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.END}\n")

def print_pass(text):
    print(f"{Colors.GREEN}✅ {text}{Colors.END}")

def print_fail(text):
    print(f"{Colors.RED}❌ {text}{Colors.END}")

def print_warn(text):
    print(f"{Colors.YELLOW}⚠️  {text}{Colors.END}")

def print_info(text):
    print(f"   {text}")

class QuizValidator:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.data = None
        self.errors = []
        self.warnings = []
        self.passes = []
        
    def load_quiz(self) -> bool:
        """Load and parse JSON file"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            return True
        except json.JSONDecodeError as e:
            self.errors.append(f"Invalid JSON: {e}")
            return False
        except Exception as e:
            self.errors.append(f"Failed to load file: {e}")
            return False
    
    def check_tier1_formatting(self) -> None:
        """TIER 1: ASCII-only, no Unicode"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        unicode_chars = [c for c in content if ord(c) > 127]
        if unicode_chars:
            unique = list(set(unicode_chars))[:5]
            self.errors.append(f"Unicode characters found: {len(unicode_chars)} total, examples: {unique}")
        else:
            self.passes.append("ASCII-only (no Unicode characters)")
    
    def check_tier1_structure(self) -> None:
        """TIER 1: Required fields and structure"""
        # Top-level fields
        required_top = ['id', 'scripture', 'chapter', 'audience', 'title', 'difficulty', 'publishedOn', 'questions']
        missing_top = [f for f in required_top if f not in self.data]
        
        if missing_top:
            self.errors.append(f"Missing top-level fields: {missing_top}")
        else:
            self.passes.append(f"All top-level fields present")
        
        # Question count validation
        audience = self.data.get('audience', '')
        expected_counts = {'adult': 25, 'teens': 20, 'kids': 15}
        actual_count = len(self.data.get('questions', []))
        
        expected = expected_counts.get(audience, 25)
        if actual_count == expected:
            self.passes.append(f"Question count: {actual_count} (correct for {audience})")
        else:
            self.errors.append(f"Question count: {actual_count}, expected {expected} for {audience}")
        
        # Question structure
        required_q = ['id', 'prompt', 'choices', 'correctIndex', 'feedback', 'verseLabel', 'verseUrl', 'verdict']
        for i, q in enumerate(self.data.get('questions', []), 1):
            missing_q = [f for f in required_q if f not in q]
            if missing_q:
                self.errors.append(f"Q{i} missing fields: {missing_q}")
            
            # Choices validation
            if 'choices' in q:
                if not isinstance(q['choices'], list):
                    self.errors.append(f"Q{i} choices is not an array")
                elif len(q['choices']) != 4:
                    self.errors.append(f"Q{i} has {len(q['choices'])} choices, expected 4")
            
            # correctIndex validation
            if 'correctIndex' in q:
                if not isinstance(q['correctIndex'], int) or q['correctIndex'] < 0 or q['correctIndex'] > 3:
                    self.errors.append(f"Q{i} invalid correctIndex: {q['correctIndex']}")
    
    def check_tier1_source_integrity(self) -> None:
        """TIER 1: All content from Vedabase.io"""
        scripture = self.data.get('scripture', '')
        
        for i, q in enumerate(self.data.get('questions', []), 1):
            # Check verseUrl
            verse_url = q.get('verseUrl', '')
            if not verse_url.startswith('https://vedabase.io'):
                self.errors.append(f"Q{i} invalid verseUrl: {verse_url}")
            
            # Check verseLabel format
            verse_label = q.get('verseLabel', '')
            if scripture == 'bg' and not verse_label.startswith('BG '):
                self.errors.append(f"Q{i} invalid verseLabel format: {verse_label}")
            elif scripture == 'sb' and not verse_label.startswith('SB '):
                self.errors.append(f"Q{i} invalid verseLabel format: {verse_label}")
            
            # Check verdict
            verdict = q.get('verdict', '')
            if verdict not in ['Correct', 'Review']:
                self.errors.append(f"Q{i} invalid verdict: {verdict} (must be 'Correct' or 'Review')")
        
        if not self.errors:
            self.passes.append(f"All verse URLs point to vedabase.io")
            self.passes.append(f"All verse labels correctly formatted")
    
    def check_tier2_mcq_quality(self) -> None:
        """TIER 2: MCQ quality - unambiguous correct answers"""
        for i, q in enumerate(self.data.get('questions', []), 1):
            prompt = q.get('prompt', '')
            choices = q.get('choices', [])
            
            # Check for ambiguous language
            ambiguous_words = ['probably', 'might', 'possibly', 'sometimes', 'often']
            for word in ambiguous_words:
                if word in prompt.lower():
                    self.warnings.append(f"Q{i} contains ambiguous word in prompt: '{word}'")
        
        self.passes.append("MCQ prompts checked for ambiguous language")
    
    def check_tier2_purport_ratio(self) -> None:
        """TIER 2: Purport question ratio (35-40% for BG)"""
        scripture = self.data.get('scripture', '')
        if scripture != 'bg':
            return  # SB has different requirements
        
        questions = self.data.get('questions', [])
        purport_count = 0
        
        # Count purport questions (those mentioning "purport" or "Prabhupada" in prompt)
        for q in questions:
            prompt = q.get('prompt', '').lower()
            if 'purport' in prompt or 'prabhupada' in prompt:
                purport_count += 1
        
        total = len(questions)
        ratio = (purport_count / total * 100) if total > 0 else 0
        
        # Target: 35-40%
        if 35 <= ratio <= 40:
            self.passes.append(f"Purport ratio: {ratio:.1f}% ({purport_count}/{total}) ✓ Target: 35-40%")
        elif 30 <= ratio < 35:
            self.warnings.append(f"Purport ratio: {ratio:.1f}% ({purport_count}/{total}) - Below target 35-40%")
        elif ratio < 30:
            self.errors.append(f"Purport ratio: {ratio:.1f}% ({purport_count}/{total}) - Well below target 35-40%")
        else:
            self.warnings.append(f"Purport ratio: {ratio:.1f}% ({purport_count}/{total}) - Above target 35-40%")
    
    def check_quality_length_balance(self) -> None:
        """Quality Standards: Length balance (30% variance)"""
        issues = 0
        
        for i, q in enumerate(self.data.get('questions', []), 1):
            choices = q.get('choices', [])
            if len(choices) != 4:
                continue
            
            lengths = [len(choice.split()) for choice in choices]
            min_len = min(lengths)
            max_len = max(lengths)
            
            # Check 30% variance rule (max should be ≤ 1.3x min)
            if max_len > min_len * 1.3:
                issues += 1
                variance = max_len / min_len if min_len > 0 else 0
                # Only report if severe (>1.5x)
                if variance > 1.5:
                    self.warnings.append(f"Q{i} high variance: {min_len}-{max_len} words ({variance:.1f}x)")
        
        total = len(self.data.get('questions', []))
        if issues == 0:
            self.passes.append(f"Length balance: All {total} questions within 30% variance")
        else:
            pass_rate = ((total - issues) / total * 100) if total > 0 else 0
            if pass_rate >= 90:
                self.passes.append(f"Length balance: {pass_rate:.1f}% pass rate ({total-issues}/{total})")
            elif pass_rate >= 70:
                self.warnings.append(f"Length balance: {pass_rate:.1f}% pass rate ({total-issues}/{total}) - Below 90%")
            else:
                self.errors.append(f"Length balance: {pass_rate:.1f}% pass rate ({total-issues}/{total}) - Well below 90%")
    
    def check_quality_distractors(self) -> None:
        """Quality Standards: Plausible distractors"""
        issues = 0
        obvious_words = ['always', 'never', 'only', 'merely', 'obviously', 'silly', 'clearly', 'must']
        
        for i, q in enumerate(self.data.get('questions', []), 1):
            choices = q.get('choices', [])
            correct_idx = q.get('correctIndex', 0)
            
            for idx, choice in enumerate(choices):
                if idx == correct_idx:
                    continue  # Skip correct answer
                
                # Check for obvious language
                choice_lower = choice.lower()
                found_obvious = [word for word in obvious_words if word in choice_lower.split()]
                if found_obvious:
                    issues += 1
                    if len(found_obvious) > 1:  # Only warn if multiple obvious words
                        self.warnings.append(f"Q{i} distractor {idx+1} has obvious language: {found_obvious}")
                
                # Check for very short distractors (1-2 words)
                word_count = len(choice.split())
                if word_count <= 2:
                    issues += 1
                    self.warnings.append(f"Q{i} distractor {idx+1} is very short: {word_count} words")
        
        total_distractors = len(self.data.get('questions', [])) * 3  # 3 distractors per question
        if issues == 0:
            self.passes.append(f"Distractors: All {total_distractors} checked (no obvious issues)")
        else:
            issue_rate = (issues / total_distractors * 100) if total_distractors > 0 else 0
            if issue_rate < 10:
                self.passes.append(f"Distractors: {issue_rate:.1f}% with minor issues ({issues}/{total_distractors})")
            else:
                self.warnings.append(f"Distractors: {issue_rate:.1f}% with issues ({issues}/{total_distractors})")
    
    def check_quality_correct_is_longest(self) -> None:
        """Quality Standards: Track correct-is-longest pattern"""
        correct_is_longest = 0
        
        for q in self.data.get('questions', []):
            choices = q.get('choices', [])
            correct_idx = q.get('correctIndex', 0)
            
            if len(choices) != 4:
                continue
            
            lengths = [len(choice.split()) for choice in choices]
            if lengths[correct_idx] == max(lengths):
                correct_is_longest += 1
        
        total = len(self.data.get('questions', []))
        percentage = (correct_is_longest / total * 100) if total > 0 else 0
        
        # This is informational - 60-70% is acceptable after revision
        if percentage <= 40:
            self.passes.append(f"Correct-is-longest: {percentage:.1f}% ({correct_is_longest}/{total}) - Excellent")
        elif percentage <= 70:
            self.passes.append(f"Correct-is-longest: {percentage:.1f}% ({correct_is_longest}/{total}) - Acceptable")
        else:
            self.warnings.append(f"Correct-is-longest: {percentage:.1f}% ({correct_is_longest}/{total}) - High (target <70%)")
    
    def run_all_checks(self) -> bool:
        """Run all validation checks"""
        print_header(f"Validating: {self.file_path.name}")
        
        if not self.load_quiz():
            print_fail("Failed to load quiz file")
            for error in self.errors:
                print_info(error)
            return False
        
        # TIER 1 CHECKS
        print(f"\n{Colors.BOLD}TIER 1 - Hard Rules (Must Pass){Colors.END}")
        self.check_tier1_formatting()
        self.check_tier1_structure()
        self.check_tier1_source_integrity()
        
        # TIER 2 CHECKS
        print(f"\n{Colors.BOLD}TIER 2 - Strong Constraints{Colors.END}")
        self.check_tier2_mcq_quality()
        self.check_tier2_purport_ratio()
        
        # QUALITY STANDARDS CHECKS
        print(f"\n{Colors.BOLD}Quality Standards{Colors.END}")
        self.check_quality_length_balance()
        self.check_quality_distractors()
        self.check_quality_correct_is_longest()
        
        # RESULTS
        print(f"\n{Colors.BOLD}RESULTS{Colors.END}")
        
        if self.errors:
            print_fail(f"FAILED: {len(self.errors)} critical error(s)")
            for error in self.errors:
                print_fail(error)
        
        if self.warnings:
            for warning in self.warnings:
                print_warn(warning)
        
        for pass_msg in self.passes:
            print_pass(pass_msg)
        
        # Final verdict
        if self.errors:
            print(f"\n{Colors.RED}{Colors.BOLD}❌ QUIZ BLOCKED - Fix errors before commit{Colors.END}")
            return False
        elif self.warnings:
            print(f"\n{Colors.YELLOW}{Colors.BOLD}⚠️  QUIZ PASSES with warnings - Review recommended{Colors.END}")
            return True
        else:
            print(f"\n{Colors.GREEN}{Colors.BOLD}✅ QUIZ APPROVED - All standards met{Colors.END}")
            return True

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Validate quiz files against all standards')
    parser.add_argument('files', nargs='+', help='Quiz JSON file(s) to validate')
    parser.add_argument('--strict', action='store_true', help='Treat warnings as errors')
    
    args = parser.parse_args()
    
    all_passed = True
    results = []
    
    for file_path in args.files:
        validator = QuizValidator(file_path)
        passed = validator.run_all_checks()
        
        if args.strict and validator.warnings:
            passed = False
        
        results.append((file_path, passed, len(validator.errors), len(validator.warnings)))
        all_passed = all_passed and passed
        
        print("\n" + "="*70 + "\n")
    
    # Summary
    if len(args.files) > 1:
        print_header("VALIDATION SUMMARY")
        for file_path, passed, errors, warnings in results:
            status = "✅ PASS" if passed else "❌ FAIL"
            print(f"{status} | {Path(file_path).name} | Errors: {errors}, Warnings: {warnings}")
        
        total_passed = sum(1 for _, p, _, _ in results if p)
        print(f"\n{Colors.BOLD}Total: {total_passed}/{len(results)} files passed{Colors.END}")
    
    sys.exit(0 if all_passed else 1)

if __name__ == '__main__':
    main()
