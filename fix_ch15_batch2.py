import json

file_path = 'data/quizzes/bg/15-adult.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# More targeted fixes based on actual lengths
fixes = {
    'bg15-q1': {
        1: 'The material world with roots above branches below'  # 9w -> 8w
    },
    'bg15-q4': {
        0: 'That material attachment is natural and detachment creates psychological harm definitely',  # 11w -> 12w
        1: 'Must cut down tree with detachment weapon seeking source Krishna',  # 15w -> 11w
        2: 'That attachment to material relationships demonstrates evolved emotional intelligence naturally'  # 9w -> 11w
    },
    'bg15-q5': {
        2: 'Desires grow continuously and worldly philosophical speculation increases'  # 7w -> 9w
    },
    'bg15-q6': {
        1: 'That Krishna abode is illuminated by His effulgence not sun moon'  # 12w -> 12w (keep)
    },
    'bg15-q7': {
        1: 'That living beings are eternal fragmental parts of Krishna struggling with senses'  # 14w -> 13w
    },
    'bg15-q10': {
        1: 'One obtains body according to mode of nature at death time',  # 16w -> 12w
        3: 'That social conditions rather than consciousness determine birth destination entirely'  # 8w -> 11w
    },
    'bg15-q11': {
        0: 'It is completely impossible through any independent material processes whatsoever',  # 9w -> 11w
        2: 'Everyone perceives Him automatically without any effort whatsoever naturally'  # 9w -> 10w
    },
    'bg15-q13': {
        0: 'That digestion is purely mechanical chemical process requiring no conscious controller',  # 11w -> 12w (expand by 1)
        1: 'That Krishna as Vaisvanara fire digests all kinds of foods',  # 11w -> keep
        2: 'That stomach operates autonomously through evolved biological mechanisms alone definitely',  # 10w -> 11w
        3: 'That diet alone determines health without any transcendental factor involved'  # 10w -> keep
    },
    'bg15-q14': {
        2: 'He is distant entirely separated through independent material processes'  # 8w -> 9w
    },
    'bg15-q15': {
        1: 'That perishable and imperishable have distinct natures not confused',  # 10w -> 10w (keep)
        2: 'That material and spiritual realities are equivalent manifestations of same substance',  # 11w -> 12w
        3: 'That dualism is outdated and enlightenment means transcending all distinctions'  # 10w -> 11w
    },
    'bg15-q17': {
        0: 'The strong representing worldly philosophical speculation entirely',  # 6w -> 7w
        1: 'One who knows me as Supreme Self is my devotee',  # 12w -> 11w
        2: 'The powerful representing worldly philosophical speculation entirely',  # 6w -> 7w
        3: 'The wealthy representing worldly philosophical speculation entirely'  # 6w -> 7w
    },
    'bg15-q19': {
        0: 'Matter is supreme entirely through independent material processes',  # 8w -> 9w
        2: 'The universe is eternal through independent material processes',  # 8w -> 9w
        3: 'minimal is real through independent material processes entirely'  # 7w -> 9w
    },
    'bg15-q20': {
        0: 'Just nature operating through independent material processes entirely',  # 7w -> 9w
        1: 'It represents material universe and path to transcend it',  # 11w -> 10w
        2: 'It is permanent eternally through independent material processes'  # 7w -> 9w
    },
    'bg15-q21': {
        0: 'By studying alone and worldly philosophical speculation entirely',  # 7w -> 9w
        2: 'By ignoring everything through independent material processes entirely',  # 7w -> 9w
        3: 'It is impossible entirely through independent material processes'  # 7w -> 9w
    },
    'bg15-q22': {
        0: 'That improving material conditions can solve fundamental problem of birth death',  # 11w -> 12w
        2: 'That gradual material progress eventually leads to spiritual realization automatically',  # 11w -> 12w
        3: 'That reforming material society eliminates suffering without transcendental solution entirely'  # 10w -> 12w
    },
    'bg15-q23': {
        0: 'minimal special and worldly philosophical speculation entirely now',  # 7w -> 9w
        2: 'Confusion increases steadily and worldly philosophical speculation entirely',  # 8w -> 10w
        3: 'They suffer more continuously through independent material processes'  # 7w -> 9w
    },
    'bg15-q24': {
        0: 'If Krishna sustains everything then material engagement spiritualized requires no detachment',  # 12w -> 13w
        2: 'They are contradictory if Krishna is in matter then attachment unavoidable',  # 12w -> 13w
        3: 'Material sustenance proves matter importance deserving our full absorption entirely'  # 10w -> 12w
    },
    'bg15-q25': {
        1: 'Understanding material world as inverted tree enables detachment; recognizing souls as parts reveals relationship; knowing Purushottama produces devotion',  # 24w -> 20w
        3: 'The tree represents material science; soul fragments justify individualism; Supreme Person symbolizes collective'  # 14w -> 16w
    }
}

for q in data['questions']:
    if q['id'] in fixes:
        for idx, text in fixes[q['id']].items():
            q['choices'][idx] = text
        print(f"Fixed {q['id']}")

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print('\nCh15 balance fixes Batch 2 complete!')
