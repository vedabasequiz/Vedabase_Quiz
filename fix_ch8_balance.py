import json

file_path = 'data/quizzes/bg/8-adult.json'
with open(file_path) as f:
    data = json.load(f)

for q in data['questions']:
    if q['id'] == 'bg8-q1':
        q['choices'][1] = 'What is Brahman, self, action and the material nature?'
        q['choices'][2] = 'These are unimportant questions through speculative material processes'
        print('Fixed q1')
    elif q['id'] == 'bg8-q4':
        q['choices'][0] = 'That sacrifice exists only as external ritual without true significance'
        print('Fixed q4')
    elif q['id'] == 'bg8-q14':
        q['choices'][1] = 'That exclusive devotion without material desires brings Krishna easily attained'
        print('Fixed q14')
    elif q['id'] == 'bg8-q17':
        q['choices'][1] = 'There exists a Supreme Reality beyond material creation eternally'
        print('Fixed q17')
    elif q['id'] == 'bg8-q23':
        q['choices'][1] = 'Return to Krishna eternal abode; the highest goal'
        q['choices'][2] = 'Material pleasure and worldly reasoning philosophical speculation'
        print('Fixed q23')
    elif q['id'] == 'bg8-q24':
        q['choices'][1] = 'Life-long practice shapes consciousness, making Krishna remembrance natural at death'
        q['choices'][3] = 'Only the final moment matters; previous activities insignificant'
        print('Fixed q24')
    elif q['id'] == 'bg8-q25':
        q['choices'][0] = 'Material elevation to higher planets sufficient for complete happiness'
        q['choices'][1] = 'Since all material realms temporary, only return to Krishna absolute'
        q['choices'][2] = 'Cosmic time cycles eventually purify all souls automatically'
        q['choices'][3] = 'The spiritual world merely more refined material planet'
        print('Fixed q25')

with open(file_path, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    
print('All Ch8 fixes complete!')
