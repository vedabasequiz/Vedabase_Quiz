import json

file_path = 'data/quizzes/bg/1-adult.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data['questions']:
    if q['id'] == 'bg1-q22':
        # Current: [12, 9, 7, 7] - reduce longest from 12 to 10, expand shortest from 7 to 9
        q['choices'][0] = 'Both reveal bodymind identifying with relationships not soul'
        q['choices'][2] = 'They are unrelated physical and mental phenomena entirely'
        q['choices'][3] = 'Physical weakness causes mental confusion through material exhaustion'
        print('Fixed q22')
    elif q['id'] == 'bg1-q24':
        # Current: [8, 8, 8, 6] - expand shortest from 6 to 8
        q['choices'][3] = 'Both are merely unfortunate disabilities without deeper meaning entirely'
        print('Fixed q24')

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    
print('Ch1 final fixes complete!')
