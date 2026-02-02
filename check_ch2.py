import json

with open('data/quizzes/bg/2-adult.json') as f:
    data = json.load(f)
    
trap_count = 0
false_path_count = 0
depth_count = 0
total = len(data['questions'])

needs_work = []
for i, q in enumerate(data['questions'], 1):
    fb = q.get('feedback', '')
    has_trap = 'trap' in fb.lower()
    has_fp = 'false path' in fb.lower()
    sentences = len([s for s in fb.split('.') if s.strip()])
    has_depth = sentences >= 2
    
    if not (has_trap and has_fp):
        needs_work.append(i)
    
    if has_trap: trap_count += 1
    if has_fp: false_path_count += 1
    if has_depth: depth_count += 1

print(f'Ch2 Total: {total}')
print(f'Trap: {trap_count}/{total} ({(trap_count/total)*100:.0f}%)')
print(f'False path: {false_path_count}/{total} ({(false_path_count/total)*100:.0f}%)')
print(f'Depth: {depth_count}/{total} ({(depth_count/total)*100:.0f}%)')
print(f'Quality: {((trap_count/total + false_path_count/total + depth_count/total)/3)*100:.0f}%')
print(f'\nQuestions needing enhancement (missing trap or false path): {len(needs_work)}')
print(f'List: {needs_work}')
