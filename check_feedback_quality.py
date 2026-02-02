import json
import os

# Check feedback quality across all chapters
chapters_checked = 0
total_questions = 0
feedback_with_trap = 0
feedback_with_false_path = 0
feedback_adult_depth = 0

issues = []

for i in range(1, 19):
    filepath = f'data/quizzes/bg/{i}-adult.json'
    if not os.path.exists(filepath):
        continue
    
    with open(filepath) as f:
        data = json.load(f)
    
    chapters_checked += 1
    
    for q in data['questions']:
        total_questions += 1
        feedback = q.get('feedback', '')
        
        # Check for expert critique patterns
        has_trap = 'trap:' in feedback.lower() or 'the trap' in feedback.lower()
        has_false_path = 'false path' in feedback.lower()
        has_real = ('real understanding' in feedback.lower() or 
                   'real sadhana' in feedback.lower() or 
                   'real discrimination' in feedback.lower() or 
                   'real progression' in feedback.lower() or
                   'real bhakti' in feedback.lower() or
                   'real path' in feedback.lower())
        
        # Check depth (2+ sentences)
        sentence_count = feedback.count('. ') + 1
        is_adult_depth = sentence_count >= 2
        
        if has_trap:
            feedback_with_trap += 1
        if has_false_path:
            feedback_with_false_path += 1
        if is_adult_depth:
            feedback_adult_depth += 1
        
        # Flag issues - only if BOTH conditions fail
        if not is_adult_depth:
            issues.append(f'{q["id"]}: Only 1 sentence (need 2-5)')
        if not (has_trap or has_false_path or has_real):
            issues.append(f'{q["id"]}: Missing expert critique pattern')

print(f'=== FEEDBACK QUALITY CHECK: ALL 18 BG CHAPTERS ===\n')
print(f'Chapters checked: {chapters_checked}/18')
print(f'Total questions: {total_questions}\n')

print(f'Expert Critique Patterns:')
print(f'  - "The trap:" usage: {feedback_with_trap}/{total_questions} ({feedback_with_trap/total_questions*100:.0f}%)')
print(f'  - "False path" usage: {feedback_with_false_path}/{total_questions} ({feedback_with_false_path/total_questions*100:.0f}%)')
print(f'  - Adult depth (2+ sentences): {feedback_adult_depth}/{total_questions} ({feedback_adult_depth/total_questions*100:.0f}%)\n')

if issues:
    print(f'⚠️  Issues found: {len(issues)}\n')
    
    # Group by chapter
    by_chapter = {}
    for issue in issues:
        ch = issue.split('-')[0]
        if ch not in by_chapter:
            by_chapter[ch] = []
        by_chapter[ch].append(issue)
    
    print('Issues by chapter:')
    for ch in sorted(by_chapter.keys(), key=lambda x: int(x.replace('bg', ''))):
        print(f'\n{ch}: {len(by_chapter[ch])} issues')
        for issue in by_chapter[ch][:5]:
            print(f'  - {issue}')
        if len(by_chapter[ch]) > 5:
            print(f'  ... and {len(by_chapter[ch])-5} more')
else:
    print('✅ All feedback meets expert critique standards!')

# Calculate overall quality score
trap_score = (feedback_with_trap / total_questions) * 100
false_path_score = (feedback_with_false_path / total_questions) * 100
depth_score = (feedback_adult_depth / total_questions) * 100

overall = (trap_score + false_path_score + depth_score) / 3

print(f'\n=== OVERALL QUALITY SCORE ===')
print(f'Trap usage: {trap_score:.0f}%')
print(f'False path: {false_path_score:.0f}%')
print(f'Adult depth: {depth_score:.0f}%')
print(f'Overall: {overall:.0f}%')

if overall >= 90:
    print('✅ EXCELLENT - Feedback meets expert critique standards')
elif overall >= 75:
    print('⚠️  GOOD - Minor improvements needed')
else:
    print('❌ NEEDS WORK - Significant improvements required')
