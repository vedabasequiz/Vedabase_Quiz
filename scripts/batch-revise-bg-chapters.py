#!/usr/bin/env python3
"""
Batch BG Chapter Quality Revision Script

Automates the systematic revision of BG chapters 2-18 for MCQ quality standards.
Applies the 4 fix strategies from BG_QUIZ_REVISION_TEMPLATE.md:
- Strategy A: Expand short distractors (1-4 words → 6-9 words)
- Strategy B: Condense long correct answers
- Strategy C: Remove obvious language
- Strategy D: Balance word count variance (≤30%)

Usage:
    python3 scripts/batch-revise-bg-chapters.py 11
    python3 scripts/batch-revise-bg-chapters.py 11-15
    python3 scripts/batch-revise-bg-chapters.py --all

Generates revised files with .revised.json extension for review before replacing originals.
"""

import json
import sys
import re
from pathlib import Path
from typing import List, Dict, Tuple

# Expansion templates for common short distractor patterns
EXPANSION_PATTERNS = {
    # Negative/dismissive (2-3 words)
    r'^(He|I) (is|am) (weak|powerless|limited|absent|dependent|inferior|ordinary|temporary|unimportant|cruel|indifferent)\.{3}$': [
        'He possesses diminished power in material affairs',
        'He lacks the ability to manifest power',
        'He remains absent from worldly phenomena',
        'He depends on material energy for support',
        'He ranks below the most powerful entities'
    ],
    r'^(Magic|Worldly|Political|Technical|Material|Ordinary) (tricks|secrets|strategy|knowledge|wealth|perception)\.{3}$': [
        'Mystical powers through material manipulation and discipline',
        'Knowledge of worldly success and political influence',
        'Military strategies for winning battles',
        'Mastery of technical skills and knowledge',
        'Accumulation of material wealth and possessions',
        'Sensory experience and philosophical speculation combined'
    ],
    r'^(Only|Nothing|Very little|Confused|Doubt|Fear|Worldly|Temporary) ': [
        'Knowledge of physical phenomena and external forms',
        'Minimal support to manifested reality',
        'Philosophical uncertainty about the ultimate goal',
        'Hesitation between material and spiritual paths',
        'Attachment to family duties and worldly obligations',
        'Momentary peace from material anxieties'
    ],
    # "They are" patterns
    r'^They are (all equal|unrelated|unconnected|independent)\.{3}$': [
        'All manifestations possess equivalent power and position',
        'Great personalities exist without any mutual connection',
        'Divine manifestations function independently of each other',
        'These entities operate completely independently'
    ],
    # Hierarchy/existence negation
    r'^(Hierarchy|Matter|Creation) (does not exist|operates independently|is independent)\.{3}$': [
        'No hierarchy exists among divine beings',
        'Matter operates entirely through independent laws',
        'Creation operates entirely through independent material laws'
    ]
}

# Words to remove (obvious language - Strategy C)
OBVIOUS_WORDS = ['always', 'never', 'only', 'all', 'none', 'completely', 'totally', 'nothing', 'everything']

def load_quiz(filepath: str) -> Dict:
    """Load quiz JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_quiz(data: Dict, filepath: str) -> None:
    """Save quiz JSON file with proper formatting."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')

def count_words(text: str) -> int:
    """Count words in a string."""
    return len(text.split())

def calculate_variance(word_counts: List[int]) -> float:
    """Calculate variance ratio (max/min)."""
    if min(word_counts) == 0:
        return float('inf')
    return max(word_counts) / min(word_counts)

def has_obvious_language(text: str) -> List[str]:
    """Check if text contains obvious language."""
    found = []
    text_lower = text.lower()
    for word in OBVIOUS_WORDS:
        # Check for word boundaries
        pattern = r'\b' + word + r'\b'
        if re.search(pattern, text_lower):
            found.append(word)
    return found

def expand_short_distractor(text: str, target_words: int = 7) -> str:
    """
    Strategy A: Expand short distractors to target word count.
    Uses contextual expansion patterns.
    """
    current_words = count_words(text)
    
    if current_words >= 6:
        return text
    
    # Try pattern matching for expansion templates
    for pattern, expansions in EXPANSION_PATTERNS.items():
        if re.match(pattern, text):
            # Return first expansion that fits target
            for expansion in expansions:
                if 6 <= count_words(expansion) <= 9:
                    return expansion
    
    # Generic expansion strategies
    if current_words <= 2:
        # Very short - add scriptural context
        base = text.rstrip('.')
        if '...' in text:
            base = text.rstrip('.')
            return f"{base} through material methods and personal effort"
        return f"{base} and worldly philosophical speculation"
    
    elif current_words <= 4:
        # Short - add qualifier
        if text.endswith('...'):
            base = text[:-3].strip()
            return f"{base} with limited understanding of truth"
        return f"{text.rstrip('.')} through independent material processes"
    
    return text

def condense_correct_answer(text: str, target_words: int = 7) -> str:
    """
    Strategy B: Condense long correct answers to target word count.
    Removes redundancy while preserving meaning.
    """
    current_words = count_words(text)
    
    if current_words <= 8:
        return text
    
    # Remove common redundant phrases
    condensed = text
    
    # Remove redundant clauses
    condensed = re.sub(r'; (I am|all is|everything|all)|; (I|He).*(?:resting|emanates|flows)', '', condensed)
    condensed = re.sub(r', (and|the|all|in all)', '', condensed)
    
    # Shorten common verbose patterns
    replacements = {
        'Among all': 'Among',
        'Among the': 'Among',
        'I am the source of all creation; everything': 'I am the source of all creation',
        'in the heart of all beings': 'in all hearts',
        'all emanates from me; all rests': 'all emanates from Me',
        'from me; meditate on': 'from Me;'
    }
    
    for old, new in replacements.items():
        condensed = condensed.replace(old, new)
    
    # If still too long, try more aggressive condensing
    if count_words(condensed) > target_words + 2:
        # Remove final clauses after semicolon
        if ';' in condensed:
            condensed = condensed.split(';')[0]
    
    return condensed.strip()

def remove_obvious_language_from_choices(choices: List[str]) -> List[str]:
    """
    Strategy C: Remove obvious language from all choices.
    Replaces with more nuanced phrasing.
    """
    revised = []
    
    replacements = {
        r'\balways\b': 'consistently',
        r'\bnever\b': 'not',
        r'\bonly\b': 'primarily',
        r'\ball\b(?! beings| creation)': 'every',  # Keep "all beings", "all creation"
        r'\bnone\b': 'no',
        r'\bcompletely\b': 'entirely',
        r'\btotally\b': 'fully',
        r'\bnothing\b': 'minimal',
        r'\beverything\b': 'all things'
    }
    
    for choice in choices:
        text = choice
        for pattern, replacement in replacements.items():
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        revised.append(text)
    
    return revised

def revise_question(question: Dict) -> Tuple[Dict, List[str]]:
    """
    Revise a single question applying all 4 strategies.
    Returns: (revised_question, list_of_changes)
    """
    changes = []
    choices = question['choices']
    correct_idx = question['correctIndex']
    
    # Calculate initial metrics
    word_counts = [count_words(c) for c in choices]
    initial_variance = calculate_variance(word_counts)
    initial_correct_longest = word_counts[correct_idx] == max(word_counts)
    
    # Strategy C: Remove obvious language first
    obvious_found = []
    for i, choice in enumerate(choices):
        obvious = has_obvious_language(choice)
        if obvious:
            obvious_found.extend([(i, w) for w in obvious])
    
    if obvious_found:
        choices = remove_obvious_language_from_choices(choices)
        changes.append(f"Removed obvious language: {', '.join([w for _, w in obvious_found])}")
    
    # Strategy A: Expand short distractors (non-correct answers)
    for i in range(len(choices)):
        if i == correct_idx:
            continue
        
        wc = count_words(choices[i])
        if wc < 6:
            original = choices[i]
            choices[i] = expand_short_distractor(choices[i])
            if choices[i] != original:
                changes.append(f"D{i}: Expanded from {wc} to {count_words(choices[i])} words")
    
    # Strategy B: Condense long correct answer
    correct_wc = count_words(choices[correct_idx])
    if correct_wc > 10:
        original = choices[correct_idx]
        choices[correct_idx] = condense_correct_answer(choices[correct_idx])
        if choices[correct_idx] != original:
            changes.append(f"Correct: Condensed from {correct_wc} to {count_words(choices[correct_idx])} words")
    
    # Strategy D: Check final variance
    final_word_counts = [count_words(c) for c in choices]
    final_variance = calculate_variance(final_word_counts)
    
    if final_variance <= 1.3:
        changes.append(f"✓ Variance: {initial_variance:.1f}x → {final_variance:.1f}x (PASS)")
    elif final_variance < initial_variance:
        changes.append(f"⚠ Variance: {initial_variance:.1f}x → {final_variance:.1f}x (improved)")
    
    # Update question
    revised_question = question.copy()
    revised_question['choices'] = choices
    
    return revised_question, changes

def revise_chapter(chapter_num: int, dry_run: bool = False) -> bool:
    """
    Revise a single chapter.
    Returns True if successful.
    """
    filepath = Path(f"data/quizzes/bg/{chapter_num}-adult.json")
    
    if not filepath.exists():
        print(f"❌ File not found: {filepath}")
        return False
    
    print(f"\n{'='*70}")
    print(f"Revising BG Chapter {chapter_num}")
    print(f"{'='*70}\n")
    
    # Load quiz
    data = load_quiz(filepath)
    questions = data['questions']
    
    # Revise each question
    revised_questions = []
    total_changes = 0
    
    for i, q in enumerate(questions, 1):
        print(f"Q{i} ({q['id']})")
        revised_q, changes = revise_question(q)
        
        if changes:
            for change in changes:
                print(f"  • {change}")
            total_changes += len(changes)
        else:
            print(f"  • No changes needed")
        
        revised_questions.append(revised_q)
        print()
    
    # Update data
    data['questions'] = revised_questions
    
    # Save revised file
    if not dry_run:
        revised_path = filepath.with_suffix('.revised.json')
        save_quiz(data, str(revised_path))
        print(f"✅ Saved to: {revised_path}")
        print(f"📊 Total changes: {total_changes} across {len(questions)} questions")
        print(f"\n⚠️  Review the .revised.json file, then:")
        print(f"   mv {revised_path} {filepath}")
    else:
        print(f"🔍 Dry run complete - no files modified")
        print(f"📊 Would make {total_changes} changes across {len(questions)} questions")
    
    return True

def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    arg = sys.argv[1]
    dry_run = '--dry-run' in sys.argv
    
    if arg == '--all':
        # Revise all chapters 2-18
        chapters = list(range(2, 19))
    elif '-' in arg:
        # Range: 11-15
        start, end = map(int, arg.split('-'))
        chapters = list(range(start, end + 1))
    else:
        # Single chapter
        chapters = [int(arg)]
    
    print(f"🎯 Target chapters: {chapters}")
    if dry_run:
        print(f"🔍 DRY RUN MODE - No files will be modified\n")
    
    success_count = 0
    for chapter in chapters:
        if revise_chapter(chapter, dry_run):
            success_count += 1
    
    print(f"\n{'='*70}")
    print(f"✅ Successfully processed {success_count}/{len(chapters)} chapters")
    print(f"{'='*70}\n")
    
    if not dry_run and success_count > 0:
        print("Next steps:")
        print("1. Review .revised.json files")
        print("2. Validate: python3 scripts/validate-quiz-quality.py data/quizzes/bg/[chapter]-adult.revised.json")
        print("3. If good: mv [chapter]-adult.revised.json [chapter]-adult.json")
        print("4. Commit: git add data/quizzes/bg/[chapter]-adult.json && git commit")

if __name__ == '__main__':
    main()
