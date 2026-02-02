import json

with open('data/quizzes/bg/17-adult.json') as f:
    data = json.load(f)

# Phase 3: q17-25 - enhance feedback, fix duplicates, add purport questions, create synthesis
changes = {
    'bg17-q17': {
        'feedback': "Sattvic action done niyatam (regulated), sangam tyaktva (abandoning attachment), phalam (fruit) not desired-this elevates to shuddha-sattva (pure goodness) toward mukti (liberation). The trap: thinking action itself causes bondage. Why this matters: The false path is escapism-avoiding duty seeking liberation through inaction. Real freedom comes through nishkama-karma-performing duty with detachment transforms karma-bandhana (bondage of action) into karma-yoga (yoga of action); same act, different consciousness, opposite result."
    },
    'bg17-q18': {
        'prompt': "In the purport to BG 17.23-24, what misconception about Om Tat Sat does Srila Prabhupada address?",
        'choices': [
            "That yajna-dana-tapas performed with Om Tat Sat dedication reaches Supreme Brahman",
            "That sacred syllables are mechanical formulas working automatically without bhava (devotion)",
            "That three terms indicate param brahma (Supreme Absolute Truth) beyond material existence",
            "That activities sanctified by Om Tat Sat transcend guna-influence toward transcendence"
        ],
        'feedback': "Srila Prabhupada clarifies Om Tat Sat isn't magic spell-requires shraddha-bhakti (faithful devotion) toward param brahma (Supreme). Chanting sounds without consciousness of tattva (reality) they represent is mechanical ritual. The trap: treating mantras as vending machines. Why this matters: The false path is mantra materialism. Real practice engages consciousness-Om invokes Absolute, Tat indicates transcendence, Sat affirms eternal existence; together directing awareness to Krishna beyond gunas. Sound with consciousness transforms; sound without consciousness remains noise."
    },
    'bg17-q19': {
        'feedback': "Chapter 17 provides practical diagnostic-assess shraddha, ahara, yajna, tapas, dana by guna-quality. Sattvic practices systematically cultivate sattva; rajasic strengthen rajas; tamasic degrade into tamas. The trap: thinking self-assessment is judgmental. Why this matters: The false path is spiritual blindness. Real progress requires honest evaluation-is my worship sattvic (Supreme), rajasic (demigods for gain), tamasic (ghosts/spirits)? Is diet sattvic, rajasic, tamasic? Daily choices determine trajectory. This knowledge empowers conscious cultivation of sattva toward transcendence."
    },
    'bg17-q20': {
        'feedback': "Krishna's prescription is clear: choose sattvic shraddha-ahara-yajna-tapas-dana deliberately. These systematically elevate guna from tamas → rajas → sattva → nirguna (transcendence). The trap: drifting with conditioning. Why this matters: The false path is spiritual passivity-accepting inherited patterns unexamined. Real sadhana requires agency-consciously adopting sattvic food, sattvic worship, sattvic charity despite conditioning. This volitional cultivation of sattva-guna is preliminary purification enabling eventual transcendence beyond all gunas to shuddha-bhakti."
    },
    'bg17-q21': {
        'prompt': "How does Chapter 17's threefold analysis of faith relate to Krishna's earlier teachings on gunas?",
        'choices': [
            "It contradicts guna teachings through independent material processes entirely",
            "It shows shraddha operates within guna-framework reflecting consciousness level",
            "Faith is independent from gunas through independent material processes",
            "Gunas are irrelevant to faith through independent material processes"
        ],
        'feedback': "Chapter 17 applies guna-theory (Ch14) to shraddha specifically-faith isn't beyond gunas but expresses through them. Sattvika shraddha worships devatas/Supreme, rajasika seeks material rewards, tamasika engages darkness. Understanding this prevents romanticizing blind faith; all shraddha isn't equal. Real advancement requires cultivating sattvic faith through knowledge-association, elevating consciousness from rajas/tamas. Faith within gunas is material; transcendent bhakti goes beyond all three."
    },
    'bg17-q22': {
        'prompt': "In the purport to BG 17.28, what does Srila Prabhupada teach about activities without faith?",
        'choices': [
            "That shraddha-less sacrifice-charity-austerity still accumulates some spiritual merit gradually",
            "That actions without faith in Krishna are asat (temporary) bringing no eternal benefit",
            "That mechanical performance of duty generates karma-phala in svarga (heaven) eventually",
            "That faithless yajna-dana-tapas purify consciousness through habitual repetition automatically"
        ],
        'feedback': "Srila Prabhupada emphasizes shraddha-virahitam (without faith) action is asat (not eternal), naiveha (not here), na pretya (not hereafter)-bears no lasting fruit. The trap: thinking religious actions accumulate merit automatically. Why this matters: The false path is faithless ritual. Real benefit requires shraddha directed toward param brahma-ritualistic performance without devotional consciousness is asat (temporary), produces no transcendent result. Faith connects action to eternal; faithlessness keeps action material."
    },
    'bg17-q23': {
        'prompt': "How does Chapter 17 provide practical guidance for spiritual discrimination in daily life?",
        'choices': [
            "It teaches abstract philosophy without practical application to daily choices",
            "It maps guna-quality across faith, food, sacrifice, austerity, charity for self-assessment",
            "It focuses only on ritualistic rules without consciousness transformation",
            "Theory dominates without connection to actual spiritual practice or progress"
        ],
        'feedback': "Chapter 17 is operational manual-provides guna-mapping for assessing every aspect of spiritual life. Before eating: sattvic, rajasic, tamasic? Before charity: proper recipient, time, place? Before worship: sattvic deity or rajasic demigod? This framework enables moment-by-moment discrimination. Real spiritual life is conscious choice based on knowledge; unconscious drift follows conditioning. This teaching empowers deliberate cultivation of sattva-guna systematically through informed daily decisions."
    },
    'bg17-q24': {
        'prompt': "How does Om Tat Sat (17.23) function as integrating principle for Chapter 17's teachings?",
        'choices': [
            "As arbitrary formula unrelated to chapter's guna-analysis framework",
            "As transcendent reference point ensuring actions transcend guna-limitations toward Absolute",
            "Merely cultural mantra without philosophical significance for spiritual practice",
            "Mechanical sound automatically purifying actions regardless of consciousness or motivation"
        ],
        'feedback': "Om Tat Sat provides vertical axis-while guna-analysis (sattva-rajas-tamas) shows horizontal differentiation, Om Tat Sat points upward toward param brahma beyond all gunas. Without this transcendent reference, sattvic practices remain within material nature. Om Tat Sat dedication transforms sattvic action into bhakti-directing worship, austerity, charity toward Absolute not just elevated material platform. Integration: know gunas (horizontal), transcend through Om Tat Sat (vertical) toward Krishna."
    },
    'bg17-q25': {
        'prompt': "How do Chapter 17's teachings on threefold faith (17.2-4), threefold food (17.7-10), threefold sacrifice (17.11-13), threefold austerity (17.14-19), and threefold charity (17.20-22) work together to guide spiritual practice?",
        'choices': [
            "Five unrelated teachings requiring choosing which category to emphasize",
            "Comprehensive guna-mapping showing faith determines food, food affects capacity for sacrifice, sacrifice enables austerity, austerity qualifies charity-integrated cultivation",
            "Theoretical philosophy without practical implications for daily spiritual life or sadhana",
            "Contradictory approaches to spirituality requiring personal interpretation or selective application"
        ],
        'feedback': "Chapter 17 presents integrated system: (1) Shraddha (faith) establishes consciousness-level determining what you worship. (2) Ahara (food) reinforces that guna-sattvic food supports sattvic consciousness. (3) Yajna (sacrifice) channels energy-sattvic yajna purifies accumulated karma. (4) Tapas (austerity) disciplines body-mind-speech-sattvic tapas builds spiritual strength. (5) Dana (charity) distributes resources-sattvic dana advances dharma. These aren't isolated but synergistic: sattvic faith → sattvic food → capacity for sattvic yajna → strength for sattvic tapas → discrimination for sattvic dana. Result: systematic cultivation of sattva-guna. Final step: Om Tat Sat dedication transcends sattva toward nirguna-bhakti-pure devotion beyond material nature.",
        'verseLabel': "BG 17.28",
        'verseUrl': "https://vedabase.io/en/library/bg/17/28/"
    }
}

for q in data['questions']:
    if q['id'] in changes:
        for key, value in changes[q['id']].items():
            q[key] = value
        print(f"Updated {q['id']}")

with open('data/quizzes/bg/17-adult.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\nPhase 3 complete: q17-25 transformed with synthesis")
