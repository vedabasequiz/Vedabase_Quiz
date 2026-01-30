#!/usr/bin/env python3
import json
import os
import glob

bg_dir = 'data/quizzes/bg'
files = sorted(glob.glob(f'{bg_dir}/*.json'))

chapter_names = {
    1: "Observing the Armies on the Battlefield of Kurukshetra",
    2: "Contents of the Gita Summarized",
    3: "Karma-yoga",
    4: "Transcendental Knowledge",
    5: "Karma-yoga—Action in Krishna Consciousness",
    6: "Dhyana-yoga",
    7: "Knowledge of the Absolute",
    8: "Attaining the Supreme",
    9: "The Most Confidential Knowledge",
    10: "The Opulence of the Absolute",
    11: "The Universal Form",
    12: "Devotional Service",
    13: "Nature, the Enjoyer, and Consciousness",
    14: "The Three Modes of Material Nature",
    15: "The Yoga of the Supreme Person",
    16: "The Divine and Demoniac Natures",
    17: "The Divisions of Faith",
    18: "Conclusion—The Perfection of Renunciation",
}

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        quiz = json.load(f)
    
    # Extract chapter number from id
    quiz_id = quiz.get('id', '')
    parts = quiz_id.split('-')
    if len(parts) < 2:
        print(f"Skipping {file_path} - could not parse chapter number")
        continue
    
    try:
        chapter_num = int(parts[1])
    except ValueError:
        print(f"Skipping {file_path} - invalid chapter number")
        continue
    
    # Determine audience suffix
    audience = quiz.get('audience', 'adult')
    if audience == 'kids':
        audience_suffix = ' (Kids)'
    elif audience == 'teens':
        audience_suffix = ' (Teens)'
    else:
        audience_suffix = ' (Adult)'
    
    question_count = len(quiz.get('questions', []))
    
    # Update title to match SB format
    quiz['title'] = f"Bhagavad Gita - Chapter {chapter_num}{audience_suffix} | {question_count}Q"
    
    # Add publishedOn field
    quiz['publishedOn'] = "2026-01-28"
    
    # Reorder keys to match SB format
    ordered_quiz = {
        'id': quiz['id'],
        'scripture': quiz.get('scripture'),
        'chapter': quiz.get('chapter'),
        'audience': quiz.get('audience'),
        'title': quiz['title'],
        'difficulty': quiz.get('difficulty'),
        'publishedOn': quiz['publishedOn'],
        'questions': quiz['questions']
    }
    
    # Remove None values
    ordered_quiz = {k: v for k, v in ordered_quiz.items() if v is not None}
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(ordered_quiz, f, indent=2, ensure_ascii=False)
        f.write('\n')
    
    print(f"✓ Updated {os.path.basename(file_path)}: \"{quiz['title']}\"")

print(f"\n✅ Updated {len(files)} BG quiz files")
