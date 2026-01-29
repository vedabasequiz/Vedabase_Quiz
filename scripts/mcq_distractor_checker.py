#!/usr/bin/env python3
"""
MCQ Distractor Quality Checker
Tier 3 Gold-Standard Analysis: Distractor Elegance & Plausibility

This tool systematically audits MCQ distractors across all audiences and chapters
to ensure they meet the Tier 3 standard of being plausible misconceptions rather
than absurd or obvious wrong answers.

Tier 3 Requirements:
- Distractors should reflect common misconceptions
- Each distractor should be a partial truth, misplaced emphasis, or common confusion
- No silly, absurd, or non-sequitur answers
- Distractors should make students think, not giggle

Run: python3 scripts/mcq_distractor_checker.py [optional: audience/chapter filter]
Examples:
  python3 scripts/mcq_distractor_checker.py          # Scan all files
  python3 scripts/mcq_distractor_checker.py kids     # Scan only kids audience
  python3 scripts/mcq_distractor_checker.py bg1      # Scan only BG chapter 1
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime

# Distractor quality patterns to flag
RED_FLAGS = {
    "absurd_verbs": ["runs away", "falls asleep", "plays", "hides", "disappears", "explodes"],
    "vague_concepts": ["it doesn't matter", "maybe", "sometimes", "who knows", "unclear"],
    "non_sequitur": ["moves to a new place", "becomes bored", "gets a new job", "travels far"],
    "silly_emotions": ["bored and sleepy", "giggles", "laughs at", "makes a joke"],
    "too_obvious": ["the opposite is true", "everything is wrong", "this is false"],
    "contradiction": ["but still true", "even though it's wrong", "despite being false"],
}

# Quality metrics for each distractor
PLAUSIBILITY_SCALE = {
    5: "EXCELLENT - Plausible misconception requiring careful thought",
    4: "GOOD - Plausible but slightly weaker than others",
    3: "FAIR - Acceptable but could be stronger",
    2: "WEAK - Questionable plausibility, may be too obvious",
    1: "POOR - Absurd or non-sequitur, fails Tier 3 standard",
}

class DistractorAuditor:
    def __init__(self):
        self.results = {}
        self.total_questions = 0
        self.flagged_questions = 0
        self.flagged_distractors = []
        
    def check_distractor_quality(self, distractor_text):
        """Analyze a single distractor for red flags and quality issues."""
        text = distractor_text.lower()
        flags = []
        score = 4  # Start with GOOD assumption
        
        # Check for red flag patterns
        for category, patterns in RED_FLAGS.items():
            for pattern in patterns:
                if pattern in text:
                    flags.append(f"{category}: '{pattern}'")
                    score = min(score, 1 if category in ["absurd_verbs", "non_sequitur", "silly_emotions"] else 2)
        
        # Check for other quality issues
        if len(distractor_text) < 8:
            flags.append("too_short: May be too vague or incomplete")
            score = min(score, 2)
        
        if distractor_text.count("?") > 0:
            flags.append("contains_question: Should be declarative, not interrogative")
            score = min(score, 2)
            
        # Check for extreme length difference
        if len(distractor_text) > 150:
            flags.append("too_long: Distractor significantly longer than typical choice")
            score = min(score, 2)
        
        return score, flags
    
    def audit_question(self, question, file_info):
        """Audit a single question's distractors."""
        question_id = question.get("id", "unknown")
        prompt = question.get("prompt", "")
        choices = question.get("choices", [])
        correct_index = question.get("correctIndex", -1)
        
        if not choices or correct_index < 0:
            return None
        
        correct_answer = choices[correct_index]
        distractors = [choices[i] for i in range(len(choices)) if i != correct_index]
        
        quality_results = []
        has_issues = False
        
        for idx, distractor in enumerate(distractors):
            score, flags = self.check_distractor_quality(distractor)
            quality_results.append({
                "text": distractor,
                "score": score,
                "level": PLAUSIBILITY_SCALE[score],
                "flags": flags
            })
            
            if score <= 2:
                has_issues = True
                self.flagged_distractors.append({
                    "file": f"{file_info['chapter']} {file_info['audience']}",
                    "question_id": question_id,
                    "distractor": distractor,
                    "score": score,
                    "flags": flags
                })
        
        if has_issues:
            self.flagged_questions += 1
            return {
                "id": question_id,
                "prompt": prompt,
                "correct_answer": correct_answer,
                "distractors": quality_results,
                "has_issues": True
            }
        
        return None
    
    def scan_quiz_file(self, filepath):
        """Scan a single quiz file for distractor quality issues."""
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            chapter = data.get("chapter")
            audience = data.get("audience", "unknown")
            scripture = data.get("scripture", "unknown")
            questions = data.get("questions", [])
            
            file_key = f"{scripture.upper()}{chapter}-{audience}"
            file_issues = []
            
            for question in questions:
                self.total_questions += 1
                audit_result = self.audit_question(question, {
                    "chapter": f"{scripture.upper()}{chapter}",
                    "audience": audience
                })
                if audit_result:
                    file_issues.append(audit_result)
            
            if file_issues:
                self.results[file_key] = {
                    "filepath": filepath,
                    "chapter": chapter,
                    "audience": audience,
                    "total_questions": len(questions),
                    "flagged_count": len(file_issues),
                    "issues": file_issues
                }
                return len(file_issues)
            
            return 0
            
        except Exception as e:
            print(f"Error scanning {filepath}: {e}")
            return 0
    
    def scan_all_files(self, base_path="data/quizzes", filter_key=None):
        """Scan all quiz files in the data directory."""
        base = Path(base_path)
        
        if not base.exists():
            print(f"Error: {base_path} not found")
            return
        
        # Find all JSON quiz files
        json_files = list(base.rglob("*.json"))
        
        # Apply filter if provided
        if filter_key:
            json_files = [f for f in json_files if filter_key in str(f)]
        
        print(f"Scanning {len(json_files)} quiz file(s)...\n")
        
        for json_file in sorted(json_files):
            self.scan_quiz_file(str(json_file))
    
    def generate_report(self):
        """Generate comprehensive audit report."""
        print("=" * 80)
        print("MCQ DISTRACTOR QUALITY AUDIT REPORT")
        print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
        print()
        
        print("SUMMARY STATISTICS")
        print("-" * 80)
        print(f"Total questions scanned:        {self.total_questions}")
        print(f"Questions with flagged issues: {self.flagged_questions} ({100*self.flagged_questions/max(1,self.total_questions):.1f}%)")
        print(f"Total weak distractors found:  {len(self.flagged_distractors)}")
        print()
        
        if not self.results:
            print("✓ All files have excellent distractor quality!")
            print()
            return
        
        print("FILES WITH DISTRACTOR ISSUES")
        print("-" * 80)
        for file_key in sorted(self.results.keys()):
            file_info = self.results[file_key]
            print(f"\n📋 {file_key} ({file_info['audience']} audience)")
            print(f"   Path: {file_info['filepath']}")
            print(f"   Flagged questions: {file_info['flagged_count']}/{file_info['total_questions']}")
            
            for issue in file_info['issues']:
                print(f"\n   Q: {issue['prompt'][:70]}...")
                print(f"   ✓ Correct: {issue['correct_answer']}")
                for idx, distractor in enumerate(issue['distractors'], 1):
                    score = distractor['score']
                    emoji = "🔴" if score <= 1 else "🟡" if score == 2 else "🟢"
                    print(f"   {emoji} [{score}/5] {distractor['text']}")
                    if distractor['flags']:
                        for flag in distractor['flags']:
                            print(f"      ⚠️  {flag}")
        
        print()
        print("=" * 80)
        print("RECOMMENDATIONS")
        print("=" * 80)
        
        # Group by severity
        critical = [d for d in self.flagged_distractors if d['score'] <= 1]
        moderate = [d for d in self.flagged_distractors if d['score'] == 2]
        
        if critical:
            print(f"\n🔴 CRITICAL (Score ≤1): {len(critical)} distractor(s)")
            print("These must be replaced to meet Tier 3 standard")
            for item in critical[:5]:
                print(f"  - {item['file']} Q: '{item['distractor']}'")
                print(f"    Flags: {', '.join(item['flags'])}")
            if len(critical) > 5:
                print(f"  ... and {len(critical)-5} more")
        
        if moderate:
            print(f"\n🟡 MODERATE (Score =2): {len(moderate)} distractor(s)")
            print("Consider reviewing and potentially strengthening")
            for item in moderate[:3]:
                print(f"  - {item['file']} Q: '{item['distractor']}'")
                print(f"    Flags: {', '.join(item['flags'])}")
            if len(moderate) > 3:
                print(f"  ... and {len(moderate)-3} more")
        
        print()
        print("TIER 3 STANDARD REFERENCE")
        print("-" * 80)
        print("Excellent distractors should be:")
        print("  • Partial truths or common misconceptions")
        print("  • Misplaced emphasis on a related concept")
        print("  • Plausible wrong interpretations of the text")
        print("  • Distinct from the correct answer but thematically related")
        print()
        print("Avoid:")
        print("  • Silly or absurd responses (e.g., 'falls asleep', 'runs away')")
        print("  • Non-sequiturs unrelated to the question")
        print("  • Vague or too-obvious wrong answers")
        print("  • Answers that contradict the premise")
        print()

def main():
    auditor = DistractorAuditor()
    
    # Check for command-line filter
    filter_key = None
    if len(sys.argv) > 1:
        filter_key = sys.argv[1]
        print(f"Filtering for: {filter_key}\n")
    
    # Change to project root if needed
    if not Path("data/quizzes").exists():
        os.chdir(Path(__file__).parent.parent)
    
    # Scan all files
    auditor.scan_all_files(filter_key=filter_key)
    
    # Generate report
    auditor.generate_report()

if __name__ == "__main__":
    main()
