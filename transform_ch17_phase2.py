import json

with open('data/quizzes/bg/17-adult.json') as f:
    data = json.load(f)

# Phase 2: q9-16 feedback enhancement and purport questions
changes = {
    'bg17-q9': {
        'feedback': "Rajasic yajna performed abhisandhayadambhartham (with aim for reward or ostentation)-seeking puja (worship), pratishtha (fame), material benefit. The trap: thinking religious display equals spiritual advancement. Why this matters: The false path is performative piety-grand rituals for social credit, charity for recognition. Real spirituality transforms ego; rajasic spirituality inflates it. Sattvic yajna purifies through humility; rajasic yajna pollutes through pride-same external act, opposite internal effect based on motivation."
    },
    'bg17-q10': {
        'prompt': "In the purport to BG 17.13, what false sacrifice does Srila Prabhupada identify?",
        'choices': [
            "Yajna performed vidhi-dishtah (according to ordinance) with proper shraddha",
            "Sacrifice without shraddha, without mantra, without offerings, violating dharma",
            "Yajna given to qualified brahmanas at proper time and place systematically",
            "Sacrifice performed as kartavya (duty) without seeking reward or recognition"
        ],
        'feedback': "Srila Prabhupada identifies tamasic yajna-avidhi-purvakam (without proper process), shraddha-virahitam (devoid of faith), no mantras, no dakshina (offerings), no annam (food distribution). The trap: thinking ritual form suffices without proper execution. Why this matters: The false path is spiritual negligence-haphazard rituals, no mantras, prohibited items, expecting results. Real yajna follows shastra precisely; tamasic yajna ignores procedure expecting magic-worse than not performing because creates offense not merit."
    },
    'bg17-q11': {
        'feedback': "Sattvic tapas includes sharira (body), vak (speech), manas (mind) discipline-worship of devatas-brahmanas-gurus, shauca (cleanliness), arjava (straightforwardness), brahmacharya-ahimsa-performed without phala-prepsuna (fruit desire). The trap: thinking austerity must be dramatic display. Why this matters: The false path is ascetic theater. Real tapas is daily discipline-regulated eating/sleeping, truthful speech, pure thought-performed steadily without fanfare; this builds spiritual strength. Rajasic tapas performs extreme acts for attention; sattvic tapas cultivates steady virtue privately."
    },
    'bg17-q12': {
        'feedback': "Rajasic tapas performed satkara-mana-pujartham (for honor, prestige, worship), dambhena (with hypocrisy)-chala (temporary), asthiram (unstable). The trap: spiritual practices for social status. Why this matters: The false path is religious careerism-austerity as resume builder, charity for publicity, meditation for celebrity. Real tapas transforms consciousness; rajasic tapas cultivates image. When motivation is recognition not realization, practice becomes obstacle-strengthening ego rather than dissolving it."
    },
    'bg17-q13': {
        'prompt': "In the purport to BG 17.19, what extreme practice does Srila Prabhupada warn against?",
        'choices': [
            "Regulated tapasya following shastra under guru guidance with proper balance",
            "Self-torture, extreme fasting, body mutilation performed from delusion to harm others",
            "Disciplined austerity of body, speech, mind cultivating divine qualities steadily",
            "Measured asceticism that purifies without damaging physical or mental health"
        ],
        'feedback': "Srila Prabhupada warns against mudha-grahenatmanah (foolish conception of self) tapas-self-torture, extreme starvation, body-mutilation to control others or cause harm. The trap: equating pain with piety. Why this matters: The false path is masochistic asceticism. Real tapas follows shastra-measured discipline purifying consciousness; tamasic tapas tortures body from moha (delusion), often with black magic intent. Paramatma resides in body-harming it is himsa (violence) against Supreme within."
    },
    'bg17-q14': {
        'prompt': "According to BG 17.20-22, what are the three types of charity?",
        'choices': [
            "No difference exists through independent material processes",
            "Sattvic given to worthy at proper time-place without expectation; rajasic for return; tamasic to unworthy",
            "Equally valuable and worldly philosophical speculation",
            "One standard primarily through independent material processes"
        ],
        'feedback': "Sattvic danam given desha-kale cha patre (proper place, time, person), anapekshya (without expectation), kartavya (as duty). Rajasic given pratyupakarartha (for return) or phalam (fruit). Tamasic given adesha-kale (wrong place-time), apatrebhyah (unworthy), avajnaya (disrespectfully). The trap: thinking all charity equally meritorious. Why this matters: The false path is indiscriminate giving. Real dana requires discrimination-supporting worthy causes advances dharma; funding vice enables degradation; giving for return is transaction not charity."
    },
    'bg17-q15': {
        'prompt': "In the purport to BG 17.23-27, what is the significance of Om Tat Sat?",
        'choices': [
            "Arbitrary sounds and worldly philosophical speculation",
            "Om designates Supreme; Tat signifies transcendence; Sat denotes eternal existence",
            "Meaningless syllables through independent material processes",
            "Cultural tradition and worldly philosophical speculation"
        ],
        'feedback': "Srila Prabhupada explains Om is Brahman's designation, Tat indicates 'that' (transcendent), Sat means 'eternal existence'-together indicating param brahma (Supreme Absolute Truth). The trap: treating sacred syllables as superstition. Why this matters: The false path is spiritual materialism ignoring transcendent content. Real understanding recognizes Om Tat Sat invokes Supreme Reality-chanting these sabdas (sounds) connects consciousness to tattva (truth) they represent; not magic formula but conscious alignment with Absolute."
    },
    'bg17-q16': {
        'feedback': "Krishna teaches tri-vidha (threefold) division based on gunas-sattvic shraddha-ahara-yajna-tapas-dana leads to sattva-guna elevation; rajasic creates rajas; tamasic produces tamas. Each category (faith, food, sacrifice, austerity, charity) reflects and reinforces one's consciousness. The trap: thinking externals don't affect internals. Why this matters: The false path is spiritual carelessness. Real practice requires discrimination-choosing sattvic food, sattvic charity, sattvic tapas systematically cultivates sattva-guna; mixed practice produces mixed results. What you worship, eat, sacrifice, practice, give-determines who you become."
    }
}

for q in data['questions']:
    if q['id'] in changes:
        for key, value in changes[q['id']].items():
            q[key] = value
        print(f"Updated {q['id']}")

with open('data/quizzes/bg/17-adult.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\nPhase 2 complete: q9-16 transformed")
