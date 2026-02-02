import json

# Ch1: Fix 4 questions (q3, q11, q22, q24)
ch1_fixes = {
    'bg1-q3': {
        0: 'It merely provides historical accuracy for the battlefield location',
        1: 'It demonstrates equal divine favor for both opposing armies'
    },
    'bg1-q11': {
        0: 'They are arbitrary poetic embellishments without deeper meaning',
        3: 'They indicate virtues but are merely conventional'
    },
    'bg1-q22': {
        1: 'Both reveal bodymind identifying with relationships not eternal soul',
        2: 'They are unrelated physical and mental phenomena'
    },
    'bg1-q24': {
        0: 'Blindness prevents clear judgment causing attachment to outcomes',
        2: 'Both are merely unfortunate disabilities without deeper significance'
    }
}

# Ch2: Fix 3 questions (q7, q8, q18) + need to check purport
ch2_fixes = {
    'bg2-q7': {
        0: 'Like a river flowing continuously through different changing landscapes',
        1: 'As embodied soul passes from boyhood to youth to age'
    },
    'bg2-q8': {
        1: 'Temporary sensations come and go like seasons; endure them',
        2: 'Happiness and distress alternate predictably like seasonal weather cycles'
    },
    'bg2-q18': {
        0: 'Both reveal duty transcends personal comfort; act despite difficulty',
        2: 'They contradict each other revealing inconsistency in teaching'
    }
}

# Ch4: Fix 5 questions (q8, q11, q13, q18, q24)
ch4_fixes = {
    'bg4-q8': {
        1: 'Natural abilities determine suitable service; arrangement prevents exploitation'
    },
    'bg4-q11': {
        1: 'Because action appears as inaction and inaction appears action',
        3: 'Because material existence obscures spiritual reality causing confusion'
    },
    'bg4-q13': {
        0: 'Detachment allows full action without generating karmic bondage',
        3: 'They are contradictory creating tension between duty and liberation'
    },
    'bg4-q18': {
        1: 'Both show misappropriation of spiritual authority enables exploitation',
        2: 'They are unrelated historical observations without common theme'
    },
    'bg4-q24': {
        1: 'Both require humble submission rejecting pride in intelligence',
        3: 'They are contradictory suggesting both surrender and independence'
    }
}

# Ch5: Fix 3 questions (q1, q15, q21)
ch5_fixes = {
    'bg5-q1': {
        0: 'The dualistic error seeing renunciation and action contradictory',
        1: 'Krishna deliberately confuses Arjuna with contradictory spiritual teachings'
    },
    'bg5-q15': {
        0: 'Both paths reach same goal revealing surface difference only',
        2: 'They are incompatible requiring choice between action or renunciation'
    },
    'bg5-q21': {
        0: 'Both recognize false proprietorship causes conflict and anxiety',
        2: 'They are unrelated political and spiritual observations'
    }
}

def fix_chapter(file_path, fixes, chapter_name):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    count = 0
    for q in data['questions']:
        if q['id'] in fixes:
            for idx, text in fixes[q['id']].items():
                q['choices'][idx] = text
            print(f"Fixed {q['id']}")
            count += 1
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"{chapter_name}: Fixed {count} questions\n")

# Fix all chapters
fix_chapter('data/quizzes/bg/1-adult.json', ch1_fixes, 'Ch1')
fix_chapter('data/quizzes/bg/2-adult.json', ch2_fixes, 'Ch2')
fix_chapter('data/quizzes/bg/4-adult.json', ch4_fixes, 'Ch4')
fix_chapter('data/quizzes/bg/5-adult.json', ch5_fixes, 'Ch5')

print('All fixes complete!')
