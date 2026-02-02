import json

with open('data/quizzes/bg/2-adult.json') as f:
    data = json.load(f)
    
trap = sum(1 for q in data['questions'] if 'trap' in q.get('feedback', '').lower())
fp = sum(1 for q in data['questions'] if 'false path' in q.get('feedback', '').lower())
depth = sum(1 for q in data['questions'] if len([s for s in q.get('feedback', '').split('.') if s.strip()]) >= 2)
total = len(data['questions'])

print(f'Ch2: trap={trap}/{total} ({(trap/total)*100:.0f}%), fp={fp}/{total} ({(fp/total)*100:.0f}%), depth={depth}/{total} ({(depth/total)*100:.0f}%)')
print(f'Quality: {((trap/total + fp/total + depth/total)/3)*100:.0f}%')
