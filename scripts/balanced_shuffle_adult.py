#!/usr/bin/env python3
"""
Balanced shuffling of MCQ choices for BG adult quizzes (chapters 1-18).
Ensures each answer position (0-3) is used ~equally as correctIndex per chapter.
"""
import json
import random
from pathlib import Path
from collections import Counter

def balanced_shuffle_indices(n_questions, n_choices):
    # Distribute positions as evenly as possible
    base = n_questions // n_choices
    extra = n_questions % n_choices
    positions = [i for i in range(n_choices) for _ in range(base)]
    for i in range(extra):
        positions.append(i)
    random.shuffle(positions)
    return positions

def shuffle_quiz_file(filepath):
    with open(filepath, 'r') as f:
        obj = json.load(f)
    questions = obj['questions']
    n = len(questions)
    n_choices = len(questions[0]['choices'])
    # Get balanced target positions for correct answer
    target_positions = balanced_shuffle_indices(n, n_choices)
    new_questions = []
    for i, q in enumerate(questions):
        choices = q['choices'][:]
        correct = q['correctIndex']
        correct_choice = choices[correct]
        # Remove correct choice
        distractors = choices[:correct] + choices[correct+1:]
        # Shuffle distractors
        random.shuffle(distractors)
        # Insert correct_choice at target position
        pos = target_positions[i]
        new_choices = distractors[:]
        new_choices.insert(pos, correct_choice)
        new_q = q.copy()
        new_q['choices'] = new_choices
        new_q['correctIndex'] = pos
        new_questions.append(new_q)
    obj['questions'] = new_questions
    # Save to file (overwrite)
    with open(filepath, 'w') as f:
        json.dump(obj, f, indent=2, ensure_ascii=True)
    # For validation: return new correctIndex distribution
    return [q['correctIndex'] for q in new_questions]

def main():
    data_dir = Path('data/quizzes/bg')
    for ch in range(1, 19):
        path = data_dir / f'{ch}-adult.json'
        if not path.exists():
            print(f"Skip {path}")
            continue
        print(f"Shuffling {path} ...", end=' ')
        indices = shuffle_quiz_file(path)
        c = Counter(indices)
        print(f"[CorrectIndex counts: {dict(c)}]")

if __name__ == '__main__':
    main()
