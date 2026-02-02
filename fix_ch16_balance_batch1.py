import json

with open('data/quizzes/bg/16-adult.json') as f:
    data = json.load(f)

fixes = {
    # q1: [7,5,7,7] -> expand 5 to 6
    'bg16-q1': {
        'The divine nature is virtuous': 'The divine nature is essentially virtuous'
    },
    
    # q5: [6,10,6,7] -> reduce 10 to 8
    'bg16-q5': {
        'The demoniac know neither proper conduct nor renunciation nor cleanliness': 'Demoniac lack proper conduct renunciation and cleanliness'
    },
    
    # q8: [7,11,7,7] -> reduce 11 to 9
    'bg16-q8': {
        'Bound by hundreds of desires they accumulate wealth through unrighteous means': 'Bound by desires accumulating wealth through unrighteous means'
    },
    
    # q9: [5,14,6,7] -> reduce 14 to 10, expand 5 to 7
    'bg16-q9': {
        'Liberation and worldly philosophical speculation': 'Liberation and worldly philosophical idle speculation',
        'I have slain my enemy and shall slay others; I am lord and enjoyer': 'I slew my enemy shall slay others I am enjoyer'
    },
    
    # q10: [11,10,11,8] -> reduce 11s to 10, expand 8 to 9
    'bg16-q10': {
        'That compassion for all beings reflects spiritual advancement and divine nature': 'Compassion for all beings reflects spiritual advancement and divine nature',
        'That cooperation and service lead to genuine prosperity for all participants': 'Cooperation and service lead to genuine prosperity for all participants',
        'That considering others\' welfare creates sustainable harmonious civilization': 'Considering others\' welfare creates sustainable harmonious civilization always'
    },
    
    # q11: [5,10,6,5] -> reduce 10 to 7, expand 5s to 6
    'bg16-q11': {
        'Liberation and worldly philosophical speculation': 'Liberation and worldly philosophical idle speculation',
        'Repeatedly He casts them into demoniac wombs birth after birth': 'He casts them into demoniac wombs repeatedly',
        'Heaven and worldly philosophical speculation': 'Heaven and worldly philosophical idle speculation'
    },
    
    # q12: [8,8,5,5] -> expand 5s to 7
    'bg16-q12': {
        'Virtues and worldly philosophical speculation': 'Virtues and worldly philosophical idle speculation',
        'Knowledge and worldly philosophical speculation': 'Knowledge and worldly philosophical idle speculation'
    },
    
    # q13: [11,11,8,10] -> reduce 11s to 10, expand 8 to 9
    'bg16-q13': {
        'That liberation requires abandoning three gates (lust, anger, greed) through discipline': 'Liberation requires abandoning three gates (lust, anger, greed) through discipline',
        'That spiritual realization comes from inner guidance rejecting external scriptural authority': 'Spiritual realization comes from inner guidance rejecting external scriptural authority',
        'That progress demands following shastra-vidhana (scriptural injunctions) systematically': 'That progress demands following shastra-vidhana (scriptural injunctions) systematically always'
    },
    
    # q14: [6,12,6,5] -> reduce 12 to 8, expand 5 to 7
    'bg16-q14': {
        'Therefore the scriptures are your authority in determining what should be done': 'Scriptures determine authority for proper actions',
        'Passion and worldly philosophical speculation': 'Passion and worldly philosophical idle speculation'
    },
    
    # q15: [13,10,8,11] -> reduce 13 to 11
    'bg16-q15': {
        'That scriptural injunctions lead to sukha (happiness), siddhi (perfection), param gatim (supreme goal)': 'Scriptural injunctions lead to sukha (happiness), siddhi (perfection), param gatim (goal)'
    },
    
    # q16: [7,11,7,7] -> reduce 11 to 9
    'bg16-q16': {
        'Alignment with cosmic dharma vs selfish indulgence; fear lessness vs arrogance': 'Cosmic dharma alignment vs selfish indulgence and arrogance'
    },
    
    # q17: [7,10,7,8] -> reduce 10 to 8
    'bg16-q17': {
        'By identifying qualities to cultivate and reject; providing self-assessment framework': 'Identifying qualities to cultivate and reject with assessment'
    },
    
    # q19: [5,11,5,5] -> reduce 11 to 6, expand 5s to 6
    'bg16-q19': {
        'Confusion and worldly philosophical speculation': 'Confusion and worldly philosophical idle speculation',
        'Liberation and eternal happiness in Krishna\'s abode; freedom from material bondage': 'Liberation in Krishna\'s abode and freedom',
        'Bondage and worldly philosophical speculation': 'Bondage and worldly philosophical idle speculation',
        'Suffering and worldly philosophical speculation': 'Suffering and worldly philosophical idle speculation'
    },
    
    # q20: [6,12,5,6] -> reduce 12 to 8, expand 5 to 6
    'bg16-q20': {
        'Ego delusion and ignorance; stubborn refusal to follow dharma or scriptural guidance': 'Ego delusion ignorance and stubborn dharma refusal',
        'Fate and worldly philosophical speculation': 'Fate and worldly philosophical idle speculation'
    },
    
    # q23: [9,12,11,10] -> reduce 12 to 10
    'bg16-q23': {
        'Abandoning kama, krodha, lobha creates space for abhaya, dama, dana to develop': 'Abandoning kama krodha lobha enables abhaya dama dana development'
    }
}

for q in data['questions']:
    if q['id'] in fixes:
        for i, choice in enumerate(q['choices']):
            if choice in fixes[q['id']]:
                old_len = len(choice.split())
                q['choices'][i] = fixes[q['id']][choice]
                new_len = len(q['choices'][i].split())
                print(f"Fixed {q['id']}: {old_len} -> {new_len} words")

with open('data/quizzes/bg/16-adult.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\nValidating new ratios:")
for qid in sorted(fixes.keys()):
    q = [x for x in data['questions'] if x['id'] == qid][0]
    lens = [len(c.split()) for c in q['choices']]
    ratio = max(lens) / min(lens)
    status = "✓" if ratio <= 1.3 else "✗"
    print(f"{status} {qid}: {lens} = {ratio:.2f}x")
