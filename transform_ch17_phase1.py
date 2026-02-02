import json

with open('data/quizzes/bg/17-adult.json') as f:
    data = json.load(f)

# Phase 1: q1-8 feedback enhancement and purport questions
changes = {
    'bg17-q1': {
        'feedback': "Arjuna asks about those who shastra-vidhim utsrijya (disregarding scriptural injunctions) worship with shraddha (faith)-what is their position? The trap: thinking sincere intention alone suffices spiritually. Why this matters: The false path is faith divorced from knowledge. Real understanding recognizes shraddha must be directed by shastra-undirected faith becomes superstition or sentimentalism; scripture channels devotion toward actual truth not imagined spirituality."
    },
    'bg17-q2': {
        'prompt': "In the purport to BG 17.2-3, what misconception does Srila Prabhupada refute about faith?",
        'choices': [
            "That shraddha arises from sattva, rajas, or tamas according to one's guna",
            "That all faiths are equally valid paths leading to the same ultimate destination",
            "That nature of worship reflects consciousness cultivated through material association",
            "That one's shraddha determines what deities or practices one is attracted to"
        ],
        'feedback': "Srila Prabhupada explains shraddha is tri-vidha (threefold) according to gunas-sattva leads to devatas, rajas to yakshas/rakshasas, tamas to pretas/bhutas; destinations differ radically. The trap: sentimental pluralism claiming all worship reaches same goal. Why this matters: The false path is religious relativism denying qualitative distinctions. Real understanding recognizes faith in Krishna consciousness (sattva) liberates; faith in demigods for material gain (rajas) binds; faith in ghosts/spirits (tamas) degrades-choose wisely."
    },
    'bg17-q3': {
        'prompt': "In BG 17.4, what characterizes those in sattvic faith?",
        'choices': [
            "Based on desire through independent material processes",
            "They worship the demigods; those in rajas worship demons; in tamas worship ghosts",
            "Impure desire and worldly philosophical speculation",
            "Lust-driven and worldly philosophical speculation"
        ],
        'feedback': "Sattvika purusha (those in goodness) worship devatas (demigods), rajasas worship yakshas-rakshasas (demons), tamasas worship pretas-bhutas (ghosts/spirits). The trap: thinking object of worship doesn't matter if faith is sincere. Why this matters: The false path is devotional indifference. Real understanding recognizes worship directs consciousness-sattvic worship elevates toward brahman; rajasic binds in sense gratification; tamasic degrades into darkness. What you worship determines where you go."
    },
    'bg17-q4': {
        'prompt': "In the purport to BG 17.5-6, what false asceticism does Srila Prabhupada critique?",
        'choices': [
            "That regulated tapasya according to shastra purifies consciousness systematically",
            "That extreme self-torture and unauthorized austerities demonstrate spiritual advancement",
            "That disciplined body-mind-speech control constitutes genuine tapas",
            "That austerity performed without ego-display leads to actual purification"
        ],
        'feedback': "Srila Prabhupada warns against ashastra-vihitam (not enjoined in scripture) tapas performed with dambha (pride), ahamkara (ego), showing off-torturing sharira-stham bhuta-gramam (bodily elements) and Paramatma within. The trap: equating suffering with spirituality. Why this matters: The false path is ascetic exhibitionism-fasting contests, extreme deprivation for recognition. Real tapas follows shastra, purifies consciousness without harming body; self-torture is tamasic delusion not spiritual progress."
    },
    'bg17-q5': {
        'prompt': "According to BG 17.4, what characterizes tamasic faith?",
        'choices': [
            "Leading to truth through independent material processes",
            "Worship of pretas and bhutas - ghosts and spirits in ignorance",
            "Enlightening and worldly philosophical speculation",
            "Beneficial and worldly philosophical speculation"
        ],
        'feedback': "Those in tamo-guna worship pretas (ghosts) and bhuta-gana (spirits)-seeking material harm or petty powers through dark forces. The trap: dismissing this as harmless folk practice or cultural tradition. Why this matters: The false path is occultism-séances, spirit channeling, black magic-treating tamas as neutral spirituality. Real understanding recognizes engaging ghosts/spirits degrades consciousness toward hellish realms; sattvic worship of Supreme elevates-direction matters absolutely."
    },
    'bg17-q6': {
        'prompt': "In the purport to BG 17.7-10, what modern misconception does Srila Prabhupada address about food?",
        'choices': [
            "That sattvic food increases ayuh (life), sattva (purity), bala (strength), arogya (health)",
            "That diet is merely physical nutrition with no effect on consciousness or spiritual progress",
            "That rajasic food creates katu (bitter), amla (sour), lavana (salty) disturbance",
            "That tamasic food includes yata-yamam (stale), gata-rasam (tasteless), puti (putrid) items"
        ],
        'feedback': "Srila Prabhupada explains ahara (food) directly affects consciousness-sattvic ahara supports sattva-guna enabling spiritual practice; rajasic creates rajas (agitation); tamasic produces tamas (lethargy/delusion). The trap: thinking diet is purely physiological. Why this matters: The false path is nutritional reductionism. Real understanding recognizes food nourishes subtle body-eating meat, stale, intoxicated foods literally absorbs those qualities into consciousness; prasadam elevates. You are what you eat, spiritually."
    },
    'bg17-q7': {
        'prompt': "In the purport to BG 17.11-13, what false understanding of yajna does Srila Prabhupada critique?",
        'choices': [
            "That sattvic yajna performed as duty (kartavya) without phala-desire liberates",
            "That sacrifice performed for material gains or recognition constitutes genuine spirituality",
            "That deshakala-patrabhih (proper place, time, person) determines yajna's effectiveness",
            "That yajna without shraddha, without proper mantra or offering is tamasic"
        ],
        'feedback': "Srila Prabhupada explains sattvic yajna is nishkama (desireless)-performed as kartavya (duty) per vidhi-dishtah (scriptural ordinance) without phala-prepsuna (fruit desire). Rajasic yajna seeks dambhartham (ostentation) or phala (reward). The trap: thinking ritual with selfish motive equals spirituality. Why this matters: The false path is transactional religion-sacrificing for profit, fame, or favor is business not bhakti. Real yajna purifies ego through selfless offering; rajasic yajna strengthens ego through religious exhibitionism."
    },
    'bg17-q8': {
        'prompt': "According to BG 17.11, what defines sattvic sacrifice?",
        'choices': [
            "For personal gain through independent material processes",
            "Performed as duty according to scripture without desire for result; that is sattvic",
            "For show and worldly philosophical speculation",
            "Selfish and worldly philosophical speculation"
        ],
        'feedback': "Sattvic yajna done vidhi-dishtah (according to injunction), kartavyam (as duty), without phala-prepsuna (desiring fruit)-pure offering without expectation. The trap: seeking spiritual merit or heavenly reward from sacrifice. Why this matters: The false path is conditional devotion-'I'll worship if You give me...' Real sattvic yajna is unconditional-performed because it's dharma regardless of outcome; this nishkama-karma purifies consciousness of selfish motivation, enabling actual spiritual progress beyond transaction."
    }
}

for q in data['questions']:
    if q['id'] in changes:
        for key, value in changes[q['id']].items():
            q[key] = value
        print(f"Updated {q['id']}")

with open('data/quizzes/bg/17-adult.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\nPhase 1 complete: q1-8 transformed")
