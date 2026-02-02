import json

with open('data/quizzes/bg/18-adult.json') as f:
    data = json.load(f)

# Phase 2: Transform q9-16 with purport questions + Adult feedback
# Ch18 themes: threefold analysis of action/knowledge/worker/happiness, five factors in action, daivi-sampat culmination
# False paths: thinking all action equal, ignoring guna-influence, believing will alone determines results

changes = {
    'bg18-q9': {
        'feedback': "Even imperfect karma-yoga purifies when performed for Krishna. The trap: perfectionism paralysis-refusing to act until perfectly detached. Why this matters: The false path is spiritual procrastination-waiting for complete qualification before beginning devotional service. Real sadhana: Begin with current capacity-sincere offering of imperfect action purifies consciousness gradually. Krishna accepts bhava (devotional intent) over mechanical perfection. Process itself transforms practitioner-through repeated offering, attachment naturally diminishes. Therefore start bhakti-yoga now despite imperfections, not after achieving some impossible standard of flawless renunciation."
    },
    'bg18-q10': {
        'prompt': 'In the purport to BG 18.12, what does Srila Prabhupada explain about the threefold fruits of action?',
        'choices': [
            'That sattvic work gives svarga, rajasic gives human birth, tamasic gives hell',
            'That work without Krishna consciousness gives desirable/undesirable/mixed results perpetuating samsara',
            'That all work inevitably produces good fruit if performed sincerely with effort',
            'That fruits depend purely on external circumstances like time and place'
        ],
        'correctIndex': 1,
        'feedback': "Srila Prabhupada explains anishta (undesirable)-ishta (desirable)-mishrita (mixed) fruits perpetuate material bondage-even good results bind through enjoyment/attachment. The trap: seeking sattvic fruit as spiritual goal. Why this matters: The false path is upgraded materialism-pursuing piety/heaven/happiness within samsara calling it spirituality. Real tyaga: Offer ALL action to Krishna without desiring any result-this transcends threefold fruits entirely. Only bhakti-yoga liberates-karma-yoga without Krishna consciousness may elevate to higher planets but cannot grant moksha. Must transcend fruit-desire itself, not just pursue better fruits."
    },
    'bg18-q11': {
        'feedback': "Five factors-adhishthana (body-locus), karta (doer-ego), karana (instruments-senses), cheshta (efforts-pranas), daivam (providence-Supersoul)-combine producing action. The trap: false independence-believing 'I alone determine results.' Why this matters: The false path is egotistic agency-ignoring divine sanction, material conditions, and instrumental causes. Real understanding: Success requires harmony of all five-proper body, purified doership-sense, focused effort, Krishna's sanction. Cannot control all factors; must depend on daivam (divine will). Therefore offer action to Krishna recognizing He orchestrates total field-this humility enables grace. Arrogance produces frustration; surrender produces cooperation with Supreme arrangement."
    },
    'bg18-q12': {
        'feedback': "Guna determines action's nature-sattva produces sattvic action (duty-based, detached), rajas produces rajasic action (fruit-driven, agitated), tamas produces tamasic action (deluded, harmful). The trap: thinking mode-transcendence happens through willpower alone. Why this matters: The false path is naive voluntarism-believing one can instantly perform sattvic action while consciousness remains rajasic/tamasic. Real sadhana: Systematically cultivate sattva through prescribed means-sattvic association, food, activities-this gradually transforms consciousness enabling natural sattvic action. Cannot bypass guna-purification; must elevate from tamas to rajas to sattva to transcendence. Process requires patience-sudden jumps create artificial spirituality, not genuine transformation."
    },
    'bg18-q13': {
        'prompt': 'In the purport to BG 18.20-22, what false understanding about knowledge does Srila Prabhupada refute?',
        'choices': [
            'That sattvic knowledge sees unity in diversity through Paramatma vision',
            'That all knowledge systems are equally valid paths to truth regardless of epistemological foundation',
            'That rajasic knowledge focuses on diversity while tamasic knowledge is confused delusion',
            'That knowledge develops through threefold stages from tamas to rajas to sattva'
        ],
        'correctIndex': 1,
        'feedback': "Srila Prabhupada distinguishes: sattvic jnana sees eka-bhava (oneness-in-Brahman) pervading all bodies; rajasic sees prithak-prithak (separateness-multiple independent entities); tamasic sees tuccha (insignificant-bodily identification only). The trap: epistemological relativism-claiming all viewpoints equally valid. Why this matters: The false path is knowledge pluralism-treating sattvic Vedantic vision and tamasic materialism as cultural preferences. Real discrimination: Knowledge has hierarchy-sattvic knowledge reveals reality (Paramatma connecting all beings); rajasic knowledge fragments reality; tamasic knowledge obscures reality. Must cultivate sattvic jnana through shastra-guru-sadhu pramana, not validate ignorance as 'alternative perspective.'"
    },
    'bg18-q14': {
        'feedback': "Sattvic karma: niyata (prescribed duty), nirmama (without ego), nirdvandva (beyond duality-attraction/aversion), performed steadily without fruit-attachment. The trap: confusing sattvic action with mechanical ritual. Why this matters: The false path is pharisaical dharma-externally correct action with internal pride/attachment. Real sattvic action requires both external correctness AND internal purity-doing right thing with right consciousness. Must examine motivation not just behavior-pride in one's renunciation is rajasic not sattvic. Therefore cultivate genuine detachment through bhakti-offering action to Krishna naturally purifies ego-sense creating authentic sattvic karma, not artificial performance."
    },
    'bg18-q15': {
        'feedback': "Rajasic karma: performed with ahankara (ego-'I am doer'), bahulayasa (excessive effort-strain), iccha (desire for fruit). Creates disturbance-within self (anxiety/attachment) and externally (others affected by selfish pursuit). The trap: glorifying struggle as spirituality. Why this matters: The false path is achievement spirituality-measuring advancement by effort-intensity or results-accumulation. Real understanding: Rajasic striving strengthens false ego even in religious context-'I am great renunciate/devotee/scholar.' Must transition from rajasic effortfulness to sattvic equilibrium-acting from duty not desire, offering to Krishna not building ego. Peaceful action indicates progress; agitated action indicates passion-mode dominance requiring purification."
    },
    'bg18-q16': {
        'feedback': "Tamasic karma: moha (delusion)-performed without understanding purpose/consequence; apeksha (disregard)-ignoring dharma-adharma; anavasthita (careless)-without proper knowledge; creates vinasha (destruction)-harms self/others. The trap: rationalizing harmful action through spiritual language. Why this matters: The false path is antinomian spirituality-claiming transcendence of ethics justifies violating dharma. Real understanding: Liberation requires following dharma in sattva, not abandoning dharma in tamas. Cannot justify harmful action as 'beyond duality'-that's tamasic delusion not transcendence. Must perform prescribed duties carefully considering consequences, following shastra-vidhi, avoiding harm-this sattvic care protects from tamasic degradation pretending to be freedom."
    },
}

for q in data['questions']:
    if q['id'] in changes:
        for key, value in changes[q['id']].items():
            q[key] = value
            qid = q['id']
            if key == 'feedback':
                print(f"Updated {qid} feedback to Adult depth")
            elif key == 'prompt':
                print(f"Updated {qid} to PURPORT question")
            elif key == 'choices':
                print(f"Updated {qid} choices for purport")
            elif key == 'correctIndex':
                print(f"Updated {qid} correctIndex")

with open('data/quizzes/bg/18-adult.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\n=== Phase 2 Complete ===")
print("Transformed bg18-q9 through bg18-q16:")
print("- Added 2 purport questions (bg18-q10, bg18-q13)")
print("- Enhanced all 8 feedback entries to Adult depth")
print("- Themes: threefold fruits, five action-factors, threefold knowledge, threefold action by guna")
