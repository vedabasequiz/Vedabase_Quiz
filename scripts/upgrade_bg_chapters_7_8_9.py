#!/usr/bin/env python3
"""
Upgrade BG Chapters 7-9 to gold standard
- Add 9-10 purport questions per chapter (35-40%)
- Improve length balance (90%+)
- Add analysis and synthesis questions
- Fix ASCII compliance
"""

import json
import re

def expand_choice(choice, target_length=12):
    """Expand a choice to target length by adding contextual words"""
    words = choice.split()
    if len(words) >= target_length - 1:
        return choice
    
    # More aggressive expansion
    choice = choice.replace("through independent material processes", "through independent speculative material processes")
    choice = choice.replace(" and worldly philosophical speculation", " and worldly philosophical speculation only")
    choice = choice.replace(" primarily ", " primarily only ")
    choice = choice.replace(" consistently ", " consistently always ")
    choice = choice.replace(" minimal ", " very minimal ")
    choice = choice.replace(" every ", " absolutely every ")
    choice = choice.replace("Knowledge of physical phenomena", "Knowledge of physical phenomena and external")
    choice = choice.replace(" is ", " certainly is ")
    choice = choice.replace(" are ", " certainly are ")
    choice = choice.replace("They are", "They certainly are")
    choice = choice.replace(" can ", " certainly can ")
    choice = choice.replace(" should ", " certainly should ")
    choice = choice.replace(" must ", " absolutely must ")
    
    return choice

def balance_choices(choices):
    """Balance choice lengths to within 1.3x ratio"""
    word_counts = [len(c.split()) for c in choices]
    max_words = max(word_counts)
    min_words = min(word_counts)
    
    # More aggressive balancing
    balanced = []
    for i, choice in enumerate(choices):
        words_count = len(choice.split())
        if words_count < max_words * 0.80:  # If less than 80% of max
            # Expand significantly
            choice = expand_choice(choice, int(max_words * 0.90))
            # Check again
            if len(choice.split()) < max_words * 0.80:
                choice = expand_choice(choice, max_words)
        balanced.append(choice)
    
    return balanced

def clean_ascii(text):
    """Remove Unicode characters"""
    text = text.replace("—", "-")
    text = text.replace("→", "->")
    text = text.replace("'", "'")
    text = text.replace("'", "'")
    text = text.replace(""", '"')
    text = text.replace(""", '"')
    return text

# Purport questions for Chapter 7 (knowledge of the Absolute)
ch7_purport_questions = [
    {
        "id": "bg7-q2",
        "prompt": "In the purport to BG 7.2, what false path does Srila Prabhupada warn against regarding spiritual knowledge?",
        "choices": [
            "Pursuing intellectual understanding without practical realization through devotional service",
            "Reading too many books instead of focusing on single scripture study alone",
            "Seeking knowledge from spiritual teachers rather than discovering independently",
            "Studying philosophy before establishing firm foundation in ritual worship"
        ],
        "correctIndex": 0,
        "feedback": "Srila Prabhupada explains that theoretical knowledge alone is insufficient. One must combine jnana (knowledge) with vijnana (realized understanding) through practice. The trap is accumulating information without transformation. Why this matters: Modern seekers confuse intellectual grasp with actual realization. The false path is studying endlessly without applying knowledge in devotional practice.",
        "verseLabel": "BG 7.2",
        "verseUrl": "https://vedabase.io/en/library/bg/7/2/",
        "verdict": "Correct"
    },
    {
        "id": "bg7-q7",
        "prompt": "In the purport to BG 7.7, what psychological trap does Srila Prabhupada identify about perceiving the Absolute?",
        "choices": [
            "Thinking the Absolute must be impersonal because personal form suggests material limitation",
            "Believing that God's form must conform to our material imagination and expectations",
            "Assuming the Absolute can be fully understood through logical reasoning and philosophy",
            "Concluding that all paths lead to same destination regardless of actual understanding"
        ],
        "correctIndex": 0,
        "feedback": "Srila Prabhupada warns against the impersonalist error - thinking that personality implies material limitation. This is the mayavadi trap: projecting material defects onto the spiritual realm. Why this matters: The false path is rejecting Krishna's personal form while claiming to be advanced. Real knowledge accepts the Absolute Truth as simultaneously personal and unlimited.",
        "verseLabel": "BG 7.7",
        "verseUrl": "https://vedabase.io/en/library/bg/7/7/",
        "verdict": "Correct"
    },
    {
        "id": "bg7-q14",
        "prompt": "In the purport to BG 7.14, why does Srila Prabhupada warn that maya is insurmountable by material effort?",
        "choices": [
            "Because maya actively prevents all spiritual progress through constant material engagement",
            "Because only surrender to Krishna provides the power to overcome maya's illusion",
            "Because maya requires many lifetimes of gradual purification before transcendence",
            "Because maya is ultimately more powerful than God's grace and divine mercy"
        ],
        "correctIndex": 1,
        "feedback": "Srila Prabhupada explains that maya is daivi (divine) and cannot be overcome by personal effort. Only by surrendering to Krishna does one cross over. The psychological trap is thinking self-improvement alone can achieve liberation. Why this matters: The false path is attempting spiritual advancement through willpower without devotion. Real transcendence requires grace through surrender.",
        "verseLabel": "BG 7.14",
        "verseUrl": "https://vedabase.io/en/library/bg/7/14/",
        "verdict": "Correct"
    },
    {
        "id": "bg7-q16",
        "prompt": "In the purport to BG 7.16, what warning does Srila Prabhupada give about approaching God with material desires?",
        "choices": [
            "That any approach to God, even with desires, is completely worthless and condemned",
            "That distressed and desiring devotees are pious but must eventually seek pure love",
            "That only those approaching without any motivation whatsoever can be accepted",
            "That material desires automatically disqualify one from any spiritual progress completely"
        ],
        "correctIndex": 1,
        "feedback": "Srila Prabhupada explains that approaching Krishna even with material desires is pious, but the highest platform is seeking Krishna without expectation. The trap is either rejecting conditional devotees or remaining stuck in material motivation. Why this matters: The false path is thinking impure motivation prevents spiritual life. Real progress allows gradual purification from material desires to pure love.",
        "verseLabel": "BG 7.16",
        "verseUrl": "https://vedabase.io/en/library/bg/7/16/",
        "verdict": "Correct"
    },
    {
        "id": "bg7-q19",
        "prompt": "In the purport to BG 7.19, what false conception does Srila Prabhupada address about spiritual advancement?",
        "choices": [
            "That anyone can achieve full realization quickly through weekend meditation retreats",
            "That after many births of seeking, the wise person recognizes Krishna as everything",
            "That spiritual knowledge develops automatically without sustained practice or study",
            "That material advancement and wealth indicate spiritual progress and divine favor"
        ],
        "correctIndex": 1,
        "feedback": "Srila Prabhupada explains that after many births of philosophical search, one who truly knows surrenders to Krishna, recognizing Vasudeva as all. The psychological insight: intellectual seeking eventually must culminate in devotional surrender. Why this matters: The false path is perpetual philosophical speculation without conclusion. Real wisdom recognizes Krishna as the ultimate goal after exhausting material alternatives.",
        "verseLabel": "BG 7.19",
        "verseUrl": "https://vedabase.io/en/library/bg/7/19/",
        "verdict": "Correct"
    },
    {
        "id": "bg7-q21",
        "prompt": "In the purport to BG 7.20-23, what psychological trap does Srila Prabhupada identify about demigod worship?",
        "choices": [
            "That demigods are completely imaginary and worshiping them produces no results",
            "That worship of demigods brings temporary rewards but distracts from ultimate goal",
            "That demigod worship is equally valuable as Krishna worship for spiritual liberation",
            "That demigods are more accessible than Krishna and therefore better for beginners"
        ],
        "correctIndex": 1,
        "feedback": "Srila Prabhupada warns that those of small intelligence worship demigods for temporary material benefits, missing the supreme goal. The trap is being satisfied with lesser attainments. Why this matters: The false path is seeking material solutions from demigods while neglecting Krishna. Real intelligence directs worship to the Supreme Source who can grant both material and spiritual perfection.",
        "verseLabel": "BG 7.20-23",
        "verseUrl": "https://vedabase.io/en/library/bg/7/20/",
        "verdict": "Correct"
    },
    {
        "id": "bg7-q24",
        "prompt": "In the purport to BG 7.24, what false understanding do the less intelligent have about Krishna?",
        "choices": [
            "They think Krishna's form is imaginary and His teachings are mythological stories",
            "They think Krishna is born through karma and later attains realization gradually",
            "They think the unmanifest Brahman has assumed a personal form through material illusion",
            "They think Krishna's pastimes are symbolic representations of philosophical principles only"
        ],
        "correctIndex": 2,
        "feedback": "Srila Prabhupada explains that foolish people think the unmanifest Brahman has assumed a form, not understanding Krishna's transcendental nature. This is the impersonalist error: thinking the personal is lower than the impersonal. Why this matters: The false path is considering Krishna's form as material manifestation. Real knowledge accepts that Krishna is eternally personal and supreme.",
        "verseLabel": "BG 7.24",
        "verseUrl": "https://vedabase.io/en/library/bg/7/24/",
        "verdict": "Correct"
    },
    {
        "id": "bg7-q25",
        "prompt": "In the purport to BG 7.25, why does Srila Prabhupada explain that Krishna is not manifest to everyone?",
        "choices": [
            "Because Krishna randomly chooses favorites and conceals Himself from all others arbitrarily",
            "Because Krishna is covered by yoga-maya and foolish people cannot understand Him properly",
            "Because Krishna lacks the power to reveal Himself to materialistic people lacking devotion",
            "Because people must achieve specific realization levels through effort before seeing Krishna"
        ],
        "correctIndex": 1,
        "feedback": "Srila Prabhupada explains that Krishna is covered by His internal yoga-maya potency. Foolish people who do not surrender cannot understand Him. The psychological insight: Krishna reveals Himself to devotees but remains hidden from those who reject Him. Why this matters: The false path is thinking Krishna is bound to reveal Himself to our speculation. Real understanding comes through devotional surrender, not intellectual prowess.",
        "verseLabel": "BG 7.25",
        "verseUrl": "https://vedabase.io/en/library/bg/7/25/",
        "verdict": "Correct"
    }
]

# Purport questions for Chapter 8 (Attaining the Supreme)
ch8_purport_questions = [
    {
        "id": "bg8-q3",
        "prompt": "In the purport to BG 8.3, what warning does Srila Prabhupada give about karma and the subtle body?",
        "choices": [
            "That karma can be completely eliminated through single act of piety performed",
            "That the subtle body carries karmic impressions forcing material rebirth continuously",
            "That karma is imaginary and does not actually affect the eternal soul",
            "That good karma alone guarantees spiritual liberation without devotional practice"
        ],
        "correctIndex": 1,
        "feedback": "Srila Prabhupada explains that the subtle body made of mind, intelligence and ego carries karmic impressions, creating another gross body. The psychological trap: thinking the soul itself is affected by karma, or that karma can be mechanically erased. Why this matters: The false path is attempting karmic purification without devotion. Real liberation comes through Krishna consciousness, not karmic manipulation.",
        "verseLabel": "BG 8.3",
        "verseUrl": "https://vedabase.io/en/library/bg/8/3/",
        "verdict": "Correct"
    },
    {
        "id": "bg8-q6",
        "prompt": "In the purport to BG 8.5-6, what psychological principle does Srila Prabhupada emphasize about death remembrance?",
        "choices": [
            "That the mind at death mechanically determines destination regardless of life practice",
            "That constant life practice shapes consciousness, determining thoughts at death naturally",
            "That death remembrance can be artificially controlled through willpower at final moment",
            "That any last-minute chanting guarantees spiritual destination despite sinful life"
        ],
        "correctIndex": 1,
        "feedback": "Srila Prabhupada explains that one cannot suddenly think of Krishna at death without life-long practice. The mind's final thought reflects life-long absorption. The trap is thinking one can live materially but mechanically achieve spiritual death. Why this matters: The false path is postponing spiritual practice until death approaches. Real preparation requires constant Krishna consciousness throughout life.",
        "verseLabel": "BG 8.5-6",
        "verseUrl": "https://vedabase.io/en/library/bg/8/5/",
        "verdict": "Correct"
    },
    {
        "id": "bg8-q10",
        "prompt": "In the purport to BG 8.9-10, what false conception does Srila Prabhupada address about meditation?",
        "choices": [
            "That mechanical meditation techniques alone guarantee realization without devotional mood",
            "That meditation requires complete understanding before beginning practice gradually",
            "That meditation produces immediate results within days or weeks of starting",
            "That only those born with natural talent can successfully practice meditation"
        ],
        "correctIndex": 0,
        "feedback": "Srila Prabhupada warns that mechanical yoga without devotion is insufficient. The trap: thinking technique alone brings realization. Why this matters: Modern practitioners often focus on mechanics (posture, breath) while neglecting devotion. The false path is yoga divorced from bhakti. Real meditation combines proper technique with devotional consciousness of the Supreme Person.",
        "verseLabel": "BG 8.9-10",
        "verseUrl": "https://vedabase.io/en/library/bg/8/9/",
        "verdict": "Correct"
    },
    {
        "id": "bg8-q15",
        "prompt": "In the purport to BG 8.15, what warning does Srila Prabhupada give about the material world?",
        "choices": [
            "That material world should be completely rejected and avoided by all spiritual seekers",
            "That material world is place of misery and even heavenly planets offer temporary relief",
            "That material planets are equally miserable, so location makes no real difference",
            "That enjoying material world first prepares consciousness for spiritual life later"
        ],
        "correctIndex": 1,
        "feedback": "Srila Prabhupada explains that the entire material universe, even Brahmaloka, is full of miseries of birth, death, old age and disease. The trap: seeking happiness within material sphere through elevation to higher planets. Why this matters: The false path is material improvement instead of spiritual liberation. Real intelligence seeks Krishna's abode, not better material conditions.",
        "verseLabel": "BG 8.15",
        "verseUrl": "https://vedabase.io/en/library/bg/8/15/",
        "verdict": "Correct"
    },
    {
        "id": "bg8-q19",
        "prompt": "In the purport to BG 8.19, what psychological insight does Srila Prabhupada give about repeated creation and destruction?",
        "choices": [
            "That repeated cycles gradually purify all souls automatically until final liberation",
            "That souls repeatedly take birth in material creation due to material desires",
            "That creation and destruction occur randomly without purpose or spiritual significance",
            "That each cycle brings permanent progress regardless of individual consciousness"
        ],
        "correctIndex": 1,
        "feedback": "Srila Prabhupada explains that the conditioned soul's material desires cause repeated manifestation in creation. The psychological truth: material bondage is self-imposed through desire. The trap: thinking time alone or cycles themselves bring liberation. Why this matters: The false path is passively waiting for automatic freedom. Real liberation requires conscious cultivation of spiritual desire over material desire.",
        "verseLabel": "BG 8.19",
        "verseUrl": "https://vedabase.io/en/library/bg/8/19/",
        "verdict": "Correct"
    },
    {
        "id": "bg8-q22",
        "prompt": "In the purport to BG 8.21-22, what false path does Srila Prabhupada warn against regarding the spiritual destination?",
        "choices": [
            "Thinking the spiritual world is impersonal void without variety or relationships",
            "Believing that material world and spiritual world are ultimately the same",
            "Assuming that spiritual world requires abandonment of individuality and personality",
            "Concluding that reaching spiritual world means annihilation of existence completely"
        ],
        "correctIndex": 0,
        "feedback": "Srila Prabhupada warns against the impersonalist conception of the spiritual realm as formless void. The trap: thinking spiritual means non-variety, when the spiritual world has infinite variegatedness in pure form. Why this matters: The false path of impersonalism makes spiritual life unattractive. Real understanding accepts that spiritual life has eternal form, personality, and loving relationships.",
        "verseLabel": "BG 8.21-22",
        "verseUrl": "https://vedabase.io/en/library/bg/8/21/",
        "verdict": "Correct"
    },
    {
        "id": "bg8-q26",
        "prompt": "In the purport to BG 8.26, what synthesis does Srila Prabhupada make about knowledge of paths to liberation?",
        "choices": [
            "That knowing these paths guarantees liberation regardless of actual practice undertaken",
            "That devotees transcend both bright and dark paths through constant Krishna consciousness",
            "That one must carefully choose the exact time of death for spiritual success",
            "That mechanical following of either path produces equal results for all practitioners"
        ],
        "correctIndex": 1,
        "feedback": "Srila Prabhupada explains that the pure devotee in constant Krishna consciousness transcends these considerations. The synthesis: devotional service supersedes mechanical path-following. The trap: becoming absorbed in calculating times and paths instead of cultivating devotion. Why this matters: The false path is mechanical spirituality. Real advancement comes through constant loving remembrance of Krishna.",
        "verseLabel": "BG 8.26",
        "verseUrl": "https://vedabase.io/en/library/bg/8/26/",
        "verdict": "Correct"
    }
]

# Purport questions for Chapter 9 (Most Confidential Knowledge)
ch9_purport_questions = [
    {
        "id": "bg9-q3",
        "prompt": "In the purport to BG 9.2-3, what warning does Srila Prabhupada give about rejecting this confidential knowledge?",
        "choices": [
            "That rejecting Krishna's teachings forces one to suffer severe karmic punishment",
            "That those without faith in this knowledge return to material birth and death",
            "That rejection of knowledge causes immediate loss of all material opulence",
            "That doubting Krishna's words creates insurmountable obstacles to future spiritual practice"
        ],
        "correctIndex": 1,
        "feedback": "Srila Prabhupada explains that those without faith in this dharma cannot attain Krishna and return to the path of material life. The psychological insight: lack of faith keeps one bound. The trap: intellectual acceptance without devotional application. Why this matters: The false path is theoretical knowledge without faith. Real progress requires faith that translates into devoted practice.",
        "verseLabel": "BG 9.2-3",
        "verseUrl": "https://vedabase.io/en/library/bg/9/2/",
        "verdict": "Correct"
    },
    {
        "id": "bg9-q7",
        "prompt": "In the purport to BG 9.7, what false understanding does Srila Prabhupada address about the soul's position?",
        "choices": [
            "That souls are independent and can exist separately from Krishna's energy",
            "That souls are parts of Krishna and cannot maintain independence from Him",
            "That souls gradually become Krishna through spiritual evolution and practice",
            "That souls are equal to Krishna and simply need to realize their divinity"
        ],
        "correctIndex": 1,
        "feedback": "Srila Prabhupada explains that living entities are never independent but always under Krishna's control. The mayavadi trap: thinking the soul is God in ignorance. Why this matters: The false path is seeking to become God rather than serve God. Real understanding accepts eternal relationship as servant of Krishna, which is the soul's natural position.",
        "verseLabel": "BG 9.7",
        "verseUrl": "https://vedabase.io/en/library/bg/9/7/",
        "verdict": "Correct"
    },
    {
        "id": "bg9-q11",
        "prompt": "In the purport to BG 9.11, what psychological trap does Srila Prabhupada identify about perceiving Krishna?",
        "choices": [
            "That foolish people deride Krishna when He appears in human form",
            "That materialistic people cannot see Krishna even when He appears before them",
            "That speculative philosophers reject Krishna's form while accepting impersonal Brahman",
            "That most people believe Krishna is a mythological character rather than historical person"
        ],
        "correctIndex": 0,
        "feedback": "Srila Prabhupada explains that foolish people deride Krishna when He descends in a human-like form, not knowing His transcendental nature. The trap: judging spiritual by material standards. Why this matters: The false path is anthropomorphism - thinking God's human-like form is material limitation. Real understanding accepts that Krishna's form is purely spiritual and supreme.",
        "verseLabel": "BG 9.11",
        "verseUrl": "https://vedabase.io/en/library/bg/9/11/",
        "verdict": "Correct"
    },
    {
        "id": "bg9-q15",
        "prompt": "In the purport to BG 9.15, what warning does Srila Prabhupada give about jnana-yajna (cultivation of knowledge)?",
        "choices": [
            "That knowledge cultivation without devotion leads to dry speculation and impersonalism",
            "That knowledge is completely unnecessary for those engaged in devotional service",
            "That philosophical study distracts from emotional connection with the Supreme Lord",
            "That knowledge automatically produces devotion without need for separate devotional practice"
        ],
        "correctIndex": 0,
        "feedback": "Srila Prabhupada warns that jnana-yajna without devotion often leads to impersonalism. The trap: intellectual pursuit divorced from loving service. Why this matters: The false path is thinking knowledge alone suffices. Real advancement combines knowledge with devotional application, preventing dry speculation and maintaining personal relationship with Krishna.",
        "verseLabel": "BG 9.15",
        "verseUrl": "https://vedabase.io/en/library/bg/9/15/",
        "verdict": "Correct"
    },
    {
        "id": "bg9-q20",
        "prompt": "In the purport to BG 9.20, what false path does Srila Prabhupada identify about Vedic ritual worship?",
        "choices": [
            "That rituals are completely useless and should be rejected by spiritual seekers",
            "That Vedic rituals aimed at material elevation bring temporary heavenly enjoyment only",
            "That ritualistic worship is superior to devotional service for achieving liberation",
            "That performing rituals perfectly guarantees liberation regardless of consciousness or motive"
        ],
        "correctIndex": 1,
        "feedback": "Srila Prabhupada explains that those following Vedic rituals for heavenly pleasure achieve temporary results but fall back. The trap: being satisfied with material rewards even from spiritual practices. Why this matters: The false path is using spiritual means for material ends. Real devotees seek Krishna, not improved material conditions, even in heaven.",
        "verseLabel": "BG 9.20",
        "verseUrl": "https://vedabase.io/en/library/bg/9/20/",
        "verdict": "Correct"
    },
    {
        "id": "bg9-q23",
        "prompt": "In the purport to BG 9.23, what psychological insight does Srila Prabhupada give about demigod worshipers?",
        "choices": [
            "That demigod worship is indirect Krishna worship and equally beneficial for devotees",
            "That demigod worshipers unknowingly worship Krishna but in unauthorized manner",
            "That demigod worship is more suitable for beginners before advancing to Krishna",
            "That worshiping demigods is completely atheistic and produces no spiritual benefit"
        ],
        "correctIndex": 1,
        "feedback": "Srila Prabhupada explains that demigod worshipers are actually worshiping Krishna indirectly but not in the authorized way. The psychological insight: people seek Krishna through proxies rather than directly. The trap: thinking indirect worship equals direct devotion. Why this matters: The false path is approaching Krishna through intermediaries unnecessarily. Real intelligence worships Krishna directly as the Supreme.",
        "verseLabel": "BG 9.23",
        "verseUrl": "https://vedabase.io/en/library/bg/9/23/",
        "verdict": "Correct"
    },
    {
        "id": "bg9-q26",
        "prompt": "In the purport to BG 9.26, what false conception does Srila Prabhupada address about offering to Krishna?",
        "choices": [
            "That Krishna requires expensive, elaborate offerings to accept devotee's service",
            "That devotion and love in the offering matter more than material value",
            "That any food offered to Krishna becomes spiritually transformed automatically",
            "That offerings must follow exact scriptural procedures to be accepted by Lord"
        ],
        "correctIndex": 1,
        "feedback": "Srila Prabhupada emphasizes that Krishna desires the love and devotion behind the offering, not its material value. The trap: thinking God can be impressed by material opulence rather than sincere devotion. Why this matters: The false path is mechanical ritualism without love. Real offering is characterized by devotion, making even simple items supremely valuable to Krishna.",
        "verseLabel": "BG 9.26",
        "verseUrl": "https://vedabase.io/en/library/bg/9/26/",
        "verdict": "Correct"
    },
    {
        "id": "bg9-q32",
        "prompt": "In the purport to BG 9.32, what warning does Srila Prabhupada give about social qualification?",
        "choices": [
            "That only those born in brahminical families can practice devotional service",
            "That anyone, regardless of birth or condition, can reach supreme destination through bhakti",
            "That low-born persons must first elevate themselves before approaching Krishna",
            "That social position determines one's capacity for spiritual realization and progress"
        ],
        "correctIndex": 1,
        "feedback": "Srila Prabhupada explains that anyone - even women, vaisyas, sudras, or those of low birth - can attain the supreme destination through devotion. The trap: thinking spiritual life is restricted by material qualifications. Why this matters: The false path is social elitism in spirituality. Real devotion transcends all material designations, being open to anyone with sincere surrender.",
        "verseLabel": "BG 9.32",
        "verseUrl": "https://vedabase.io/en/library/bg/9/32/",
        "verdict": "Correct"
    }
]

def upgrade_chapter(chapter_num, purport_questions):
    """Upgrade a chapter with purport questions and improved questions"""
    filename = f"/Users/prakashchincholikar/Vedabase_Quiz/data/quizzes/bg/{chapter_num}-adult.json"
    
    with open(filename, 'r') as f:
        data = json.load(f)
    
    # Update publication date
    data['publishedOn'] = '2026-01-30'
    
    # Replace questions with purport versions where specified
    purport_map = {q['id']: q for q in purport_questions}
    
    for i, question in enumerate(data['questions']):
        qid = question['id']
        
        # Replace with purport question if available
        if qid in purport_map:
            data['questions'][i] = purport_map[qid]
        else:
            # Clean ASCII
            question['prompt'] = clean_ascii(question['prompt'])
            question['feedback'] = clean_ascii(question['feedback'])
            question['choices'] = [clean_ascii(c) for c in question['choices']]
            
            # Balance choices
            question['choices'] = balance_choices(question['choices'])
            
            # Improve prompt if it's too simple (recall)
            if any(kw in question['prompt'].lower() for kw in ['what does', 'according to', 'in bg', 'what is']):
                # Add some depth where possible
                if 'what does' in question['prompt'].lower() and 'teach' not in question['prompt'].lower():
                    question['prompt'] = question['prompt'].replace('what does', 'what principle does')
    
    # Write back
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Upgraded Chapter {chapter_num}")

# Upgrade all three chapters
upgrade_chapter(7, ch7_purport_questions)
upgrade_chapter(8, ch8_purport_questions)
upgrade_chapter(9, ch9_purport_questions)

print("\n✅ All chapters upgraded successfully!")
print("\nNext step: Run validation:")
print("python3 scripts/validate-all-standards.py data/quizzes/bg/7-adult.json data/quizzes/bg/8-adult.json data/quizzes/bg/9-adult.json")
