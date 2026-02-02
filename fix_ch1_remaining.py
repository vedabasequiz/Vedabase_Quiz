import json

file_path = 'data/quizzes/bg/1-adult.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data['questions']:
    if q['id'] == 'bg1-q3':
        q['choices'][2] = 'It reveals divine sanction through the sacred battlefield setting'
        q['choices'][3] = 'It implies sacred setting alone prevents sinful reactions'
        print('Fixed q3')
    elif q['id'] == 'bg1-q22':
        # Need to see current state first
        print(f"q22 current: {[len(c.split()) for c in q['choices']]}")
    elif q['id'] == 'bg1-q24':
        # Need to see current state first
        print(f"q24 current: {[len(c.split()) for c in q['choices']]}")

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    
print('Ch1 additional fixes applied!')
