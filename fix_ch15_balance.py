import json
import statistics

file_path = 'data/quizzes/bg/15-adult.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

fixes = {
    'bg15-q1': {
        0: 'A forest representing worldly philosophical speculation',
        2: 'A flower representing worldly philosophical speculation',
        3: 'A mountain representing worldly philosophical speculation'
    },
    'bg15-q3': {
        0: 'Ignorance alone and worldly philosophical speculation entirely'
    },
    'bg15-q4': {
        1: 'That one must cut down tree with detachment weapon seeking source',
        2: 'That attachment to material relationships demonstrates emotional intelligence'
    },
    'bg15-q5': {
        0: 'Knowledge of physical phenomena and external material forms',
        3: 'Confusion increases steadily and worldly philosophical speculation'
    },
    'bg15-q6': {
        2: 'That spiritual realm needs artificial lighting like material universe',
        3: 'That enlightenment means intellectual understanding without devotional realization'
    },
    'bg15-q7': {
        0: 'That individual souls are completely independent entities requiring no God',
        2: 'That soul gradually evolves into God through spiritual advancement',
        3: 'That consciousness emerges from material combinations rather than individual'
    },
    'bg15-q8': {
        0: 'minimal controls them through independent material processes only',
        2: 'Senses are master controlling through independent material processes',
        3: 'Mind is independent operating through independent material processes'
    },
    'bg15-q9': {
        0: 'minimal happens entirely and worldly philosophical speculation only',
        2: 'primarily body changes through independent material processes only',
        3: 'Consciousness remains static through independent material processes entirely'
    },
    'bg15-q10': {
        0: 'That birth circumstances are random chance unrelated to consciousness',
        2: 'That genetic inheritance alone determines physical and mental characteristics',
        3: 'That social conditions rather than consciousness determine birth'
    },
    'bg15-q12': {
        0: 'I am limited entirely through independent material processes',
        2: 'I am distant entirely through independent material processes',
        3: 'I depend on others through independent material processes'
    },
    'bg15-q13': {
        0: 'That digestion is purely mechanical chemical process requiring no controller',
        2: 'That stomach operates autonomously through evolved biological mechanisms',
        3: 'That diet alone determines health without any transcendental factor'
    },
    'bg15-q14': {
        0: 'He is absent entirely through independent material processes',
        2: 'He is distant entirely through independent material processes',
        3: 'He does not interfere through independent material processes'
    },
    'bg15-q15': {
        0: 'That matter and spirit are equally important and balanced',
        2: 'That material and spiritual realities are equivalent manifestations',
        3: 'That dualism is outdated and enlightenment transcends distinctions'
    },
    'bg15-q16': {
        0: 'He is mortal entirely through independent material processes',
        2: 'He is material entirely through independent material processes',
        3: 'He is temporary entirely through independent material processes'
    },
    'bg15-q17': {
        1: 'One who knows me as Supreme Self is devotee and worships rightly',
        2: 'The powerful representing worldly philosophical speculation',
        3: 'The wealthy representing worldly philosophical speculation'
    },
    'bg15-q20': {
        0: 'Just nature operating through independent material processes',
        2: 'It is permanent through independent material processes',
        3: 'It has no meaning through independent material processes'
    }
}

for q in data['questions']:
    if q['id'] in fixes:
        for idx, text in fixes[q['id']].items():
            q['choices'][idx] = text
        print(f"Fixed {q['id']}")

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print('\nAll Ch15 length balance fixes complete!')
