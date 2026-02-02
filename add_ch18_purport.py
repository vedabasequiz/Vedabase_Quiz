import json

with open('data/quizzes/bg/18-adult.json') as f:
    data = json.load(f)

# Add 4 more purport questions to reach 9/25 = 36%
# Target: q4, q7, q14, q21 - strategic positions covering key themes

changes = {
    'bg18-q4': {
        'prompt': 'In the purport to BG 18.5, what does Srila Prabhupada explain about yajna-dana-tapas (sacrifice-charity-austerity)?',
        'choices': [
            'That these purify consciousness and should never be renounced even by sannyasis',
            'That advanced souls transcend these preliminary practices entering pure spontaneous devotion',
            'That yajna-dana-tapas are karma-kanda rituals for materialistic people seeking heavenly rewards',
            'That renunciation means abandoning external rituals to focus purely on internal meditation'
        ],
        'correctIndex': 0,
        'feedback': "Srila Prabhupada explains yajna-dana-tapas are pavitrani (purifying) for mahatmanam api (even great souls)-must never be abandoned. The trap: premature transcendence-thinking advanced devotion means stopping prescribed practices. Why this matters: The false path is sahajiya spirituality-claiming spontaneous bhava makes discipline unnecessary. Real understanding: Yajna-dana-tapas systematically purify subtle conditioning-even elevated consciousness benefits from structured sadhana. Cannot bypass discipline claiming advanced realization-that's projection not actual transcendence. Must continue prescribed practices throughout life as purification and example-perfection includes discipline not abandonment. Therefore maintain yajna-dana-tapas with bhakti-bhava transforming obligation into devotional offering, not discarding as 'preliminary.'"
    },
    'bg18-q7': {
        'prompt': 'In the purport to BG 18.9, what does Srila Prabhupada explain distinguishes tyaga (proper relinquishment) from false renunciation?',
        'choices': [
            'That tyaga means performing niyata-karma (prescribed duty) without phala-asha (fruit-expectation)',
            'That all renunciation is ultimately illusion since action is inevitable in material existence',
            'That tyaga means minimizing duties to bare necessities while maximizing meditation time',
            'That proper renunciation requires formal sannyasa initiation from qualified spiritual master'
        ],
        'correctIndex': 0,
        'feedback': "Srila Prabhupada distinguishes sattvic tyaga: performing niyata-karma (duty according to shastra) without phala-asha (desire for results)-this is real relinquishment. The trap: confusing renunciation with inaction or minimal action. Why this matters: The false path is escapist renunciation-reducing duties thinking less activity equals more spirituality. Real tyaga: Fully engage in prescribed duties WITH detachment from fruits-action level remains robust, desire level drops to zero. It's psychological transformation not behavioral reduction. Cannot achieve tyaga through doing less but through desiring less WHILE acting fully. Therefore authentic renunciation means maximum engagement (duty) with minimum attachment (fruit-desire)-reversed formula of rajasic action (maximum desire with convenient duty-avoidance)."
    },
    'bg18-q14': {
        'prompt': 'In the purport to BG 18.26-28, what does Srila Prabhupada explain about the three types of workers (karta)?',
        'choices': [
            'That sattvic worker is mukta-sanga (free from attachment) and anahankara (without false ego)',
            'That all workers are equally bound by material nature regardless of consciousness quality',
            'That only formal sannyasis can be sattvic workers while householders remain rajasic',
            'That threefold worker classification is theoretical analysis without practical application'
        ],
        'correctIndex': 0,
        'feedback': "Srila Prabhupada explains sattvic karta is mukta-sanga (free from material association-attachment to results), anahankara (without false ego-'I am doer'), dhryutsaha-samanvita (endued with determination-enthusiasm), performing duty siddhi-asiddhyor nirvikara (unaffected by success-failure). The trap: thinking guna-transformation happens automatically with time. Why this matters: The false path is passive spirituality-waiting for purification without examining actual doership-quality. Real sadhana: Consciously cultivate sattvic karta through self-observation-am I attached to results? Do I claim credit? Am I disturbed by outcomes? Must deliberately transcend rajasic agency (fruit-driven) and tamasic agency (deluded-lazy) toward sattvic (duty-focused-steady). This requires active self-transformation not drift. Therefore study these characteristics, apply to actual work, progressively embody sattvic doership through bhakti-infused karma-this purifies agent enabling eventual transcendence to Krishna-dasa identity."
    },
    'bg18-q21': {
        'prompt': 'In the purport to BG 18.49-51, what does Srila Prabhupada explain about achieving siddhi (perfection) through sva-dharma?',
        'choices': [
            'That perfection comes by performing own prescribed duty without attachment offering to Krishna',
            'That sva-dharma is temporary stage to transcend eventually abandoning all material duties',
            'That perfection requires renouncing householder duties to adopt formal sannyasa order',
            'That sva-dharma varies by personal preference so one should follow internal inclinations'
        ],
        'correctIndex': 0,
        'feedback': "Srila Prabhupada explains sva-dharma-nishtha (being fixed in one's prescribed duty) leads to siddhi (perfection) by offering all to Krishna-yajna-arthat-karmano'nyatra (work for yajna purpose else bondage). The trap: spiritual restlessness-constantly seeking different paths thinking current position inadequate. Why this matters: The false path is dharma-shopping-abandoning actual duties pursuing exotic practices. Real sadhana: Accept current position as Krishna's arrangement-purify consciousness THERE through bhakti. Brahmana shouldn't envy kshatriya action; grhastha shouldn't artificially adopt sannyasa. Better sva-dharma imperfectly performed than para-dharma (another's duty) perfectly imitated-authenticity matters more than prestige. Therefore work through actual nature-position toward transcendence, not abandon reality for fantasy. Perfection comes through transformed consciousness in one's actual dharma, not through adopted roles."
    },
}

for q in data['questions']:
    if q['id'] in changes:
        for key, value in changes[q['id']].items():
            q[key] = value
            qid = q['id']
            if key == 'feedback':
                print(f"Updated {qid} feedback")
            elif key == 'prompt':
                print(f"Updated {qid} to PURPORT question")
            elif key == 'choices':
                print(f"Updated {qid} choices")
            elif key == 'correctIndex':
                print(f"Updated {qid} correctIndex")

with open('data/quizzes/bg/18-adult.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\n=== Additional Purport Questions Added ===")
print("Added 4 purport questions: bg18-q4, q7, q14, q21")
print("Total purport should now be 9/25 = 36%")
print("Themes: yajna-dana-tapas necessity, proper tyaga definition, sattvic worker cultivation, sva-dharma perfection")
