#!/usr/bin/env python3
"""
Balanced shuffling of MCQ choices for all BG and SB quizzes (all audiences).
Ensures each answer position (0-3) is used ~equally as correctIndex per quiz file.
"""
import json
import random
from pathlib import Path
from collections import Counter
import sys

def balanced_shuffle_indices(n_questions, n_choices):
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
    target_positions = balanced_shuffle_indices(n, n_choices)
    new_questions = []
    for i, q in enumerate(questions):
        choices = q['choices'][:]
        correct = q['correctIndex']
        correct_choice = choices[correct]
        distractors = choices[:correct] + choices[correct+1:]
        random.shuffle(distractors)
        pos = target_positions[i]
        new_choices = distractors[:]
        new_choices.insert(pos, correct_choice)
        new_q = q.copy()
        new_q['choices'] = new_choices
        new_q['correctIndex'] = pos
        new_questions.append(new_q)
    obj['questions'] = new_questions
    with open(filepath, 'w') as f:
        json.dump(obj, f, indent=2, ensure_ascii=True)
    return [q['correctIndex'] for q in new_questions]

def find_quiz_files():
    quiz_files = []
    for base in ['data/quizzes/bg', 'data/quizzes/sb']:
        for path in Path(base).rglob('*.json'):
            quiz_files.append(path)
    return quiz_files

def main():
    quiz_files = find_quiz_files()
    for path in quiz_files:
        print(f"Shuffling {path} ...", end=' ')
        try:
            indices = shuffle_quiz_file(path)
            c = Counter(indices)
            print(f"[CorrectIndex counts: {dict(c)}]")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()
