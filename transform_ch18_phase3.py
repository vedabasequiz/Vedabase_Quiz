import json

with open('data/quizzes/bg/18-adult.json') as f:
    data = json.load(f)

# Phase 3: Transform q17-25 with purport questions + synthesis + Adult feedback
# Ch18 themes: threefold happiness/intelligence/determination, varnashrama-dharma, brahma-bhuta state, sarva-dharman parityajya (ultimate surrender)
# False paths: happiness through sense gratification, liberation through impersonal merging, transcendence without devotion

changes = {
    'bg18-q17': {
        'feedback': "Threefold karta (doer): sattvic is mukta-sanga-anahankara (free from attachment-ego), dhryutsaha-samanvita (endued with determination-enthusiasm), performing duty steadily regardless of success-failure; rajasic is sakta (attached to fruits), labdhakankshi (desiring gain), full of greed-pride-impurity; tamasic is ayukta (undisciplined), prakrita (vulgar), stabdha (stubborn), performing action through fraud-laziness. The trap: identifying with rajasic/tamasic patterns while claiming spirituality. Why this matters: The false path is unconscious doership-acting from impure motivation while rationalizing as duty. Real sadhana: Examine who is acting-is doer attached, greedy, stubborn? Must cultivate sattvic karta through deliberate purification-this transforms actor not just action."
    },
    'bg18-q18': {
        'prompt': 'In the purport to BG 18.36-39, what misconception about happiness does Srila Prabhupada refute?',
        'choices': [
            'That sattvic happiness begins bitter (discipline) but ends nectarean (self-realization)',
            'That all happiness is equally valid since subjective experience determines value',
            'That rajasic happiness from sense contact gives temporary pleasure but ends in distress',
            'That tamasic happiness from sleep-laziness-intoxication deludes consciousness from beginning to end'
        ],
        'correctIndex': 1,
        'feedback': "Srila Prabhupada distinguishes: sattvic sukha is vishad-iva (poison-like initially-requires tapas) but amrita-upamam (nectar-like ultimately-atma-buddhi-prasada from self-knowledge); rajasic is vishaya-indriya-samyogat (sense-contact) giving immediate pleasure but pariname visham-iva (poison-like in consequence-creates bondage); tamasic is nidralasya-pramadottham (sleep-laziness-intoxication) deluding from adyantam (beginning to end). The trap: happiness relativism-claiming all pleasure equally valid. Why this matters: The false path is hedonic equivalence-treating sattvic discipline and tamasic intoxication as preference differences. Real discrimination: Happiness has hierarchy determined by consequence-sattvic leads to liberation, rajasic to bondage, tamasic to degradation. Must accept initial difficulty of sattvic cultivation for ultimate freedom, not pursue immediate rajasic/tamasic pleasure perpetuating suffering."
    },
    'bg18-q19': {
        'feedback': "Threefold buddhi (intelligence): sattvic distinguishes pravritti-nivritti (engagement-withdrawal), kartavya-akartavya (duty-non-duty), bhaya-abhaya (fear-fearlessness), bandha-moksha (bondage-liberation) properly through shastra-yukti; rajasic confuses dharma-adharma through desires-rationalizations; tamasic considers adharma as dharma being covered by tamas. The trap: trusting rajasic/tamasic buddhi making spiritual decisions. Why this matters: The false path is deluded certainty-confidently choosing adharma thinking it's dharma because buddhi is clouded. Real sadhana: Don't trust personal intelligence alone-consult shastra-guru-sadhu for dharma-discrimination. Rajasic buddhi rationalizes desire as duty; tamasic buddhi inverts values completely. Must cultivate sattvic intelligence through association-study-reflection, not rely on conditioned mind pretending to be discrimination."
    },
    'bg18-q20': {
        'feedback': "Varnashrama-dharma assigns duties according to guna-karma (qualities-activities)-not birth alone but psychological-occupational nature. Brahmanas (intellectual-priestly), kshatriyas (administrative-martial), vaishyas (economic-productive), shudras (service-labor)-each has prescribed duties suited to svabhava (inherent nature). The trap: thinking one path fits all or duties are arbitrary social constructs. Why this matters: The false path is dharma-relativism-rejecting varnashrama as cultural accident rather than psychological-spiritual necessity. Real understanding: Different natures require different sadhanas-intellectual types need jnana-emphasis, active types need karma-emphasis. Cannot impose uniform path ignoring svabhava. Therefore find one's actual guna-determined nature, perform corresponding dharma with bhakti-this is personalized spirituality respecting psycho-physical reality, not forcing artificial uniformity."
    },
    'bg18-q21': {
        'feedback': "Path to siddhi (perfection): perform sva-dharma (own duty) according to svabhava-ja-karma (nature-born-work) without attachment-offering all to Krishna. Better imperfect own-dharma than perfect para-dharma (another's duty). The trap: spiritual vocation-envy-desiring someone else's path thinking it superior. Why this matters: The false path is imitative spirituality-abandoning actual dharma to artificially adopt prestigious roles. Real sadhana: Accept current position as Krishna's arrangement-purify consciousness within that context through bhakti. Brahmana shouldn't envy kshatriya action; kshatriya shouldn't falsely adopt sannyasa. Must work through actual svabhava toward transcendence, not pretend to be something else. Therefore embrace reality, serve Krishna there-transformation comes through authentic service not artificial role-playing."
    },
    'bg18-q22': {
        'prompt': 'In the purport to BG 18.54, what does Srila Prabhupada explain about brahma-bhuta (self-realized) state?',
        'choices': [
            'That brahma-bhuta means established in Brahman experiencing sama-darshana (equal vision)',
            'That brahma-bhuta automatically grants prema-bhakti without further cultivation or surrender',
            'That brahma-bhuta is prasannatma (joyful self) beyond material duality and lamentation',
            'That brahma-bhuta develops into para-bhakti through hearing-chanting about Krishna'
        ],
        'correctIndex': 1,
        'feedback': "Srila Prabhupada explains brahma-bhuta (established in Brahman-transcending bodily identification) is NOT final goal but preliminary qualification-prasannatma (joyful self), na shochati na kankshati (neither laments nor desires material), sama-sarvesu (equal to all beings). The trap: mistaking brahma-bhuta for perfection. Why this matters: The false path is impersonal finality-achieving brahma-nirvana (liberation from material identification) then stopping, considering devotion sentimental. Real understanding: Brahma-bhuta is platform FROM WHICH bhakti begins-18.54 continues 'mad-bhaktim labhate param' (attains supreme devotion to Me). Impersonal liberation clears ground; bhakti is actual cultivation. Cannot bypass devotion claiming Brahman-realization suffices-that's incomplete understanding stopping at nirvishesha (formless) missing supreme personal aspect. Must proceed from brahma-bhuta to Krishna-bhakti for complete perfection."
    },
    'bg18-q23': {
        'feedback': "BG 18.55 declares bhaktya mam abhijanati (through devotion alone one truly knows Me)-yavan yash chasmi tattvatah (who I am in truth). Only bhakti enables yato mam tattvato jnatva (knowing Me in reality) then visate tad-anantaram (enters into Me immediately). The trap: thinking jnana or karma alone sufficient for Krishna-realization. Why this matters: The false path is non-devotional spirituality-pursuing liberation through knowledge or action without bhakti. Real understanding: Jnana reveals Brahman (impersonal aspect); karma purifies consciousness; but only bhakti reveals Krishna's personal svarupa (form-qualities-pastimes) and grants entrance into transcendental seva. Cannot know Supreme Person through impersonal means-requires personal relationship. Therefore bhakti isn't one path among many but THE path to highest realization-Krishna Himself accessible only through devotion."
    },
    'bg18-q24': {
        'feedback': "BG 18.62-63 instructs tam eva sharanam gaccha sarva-bhavena (take shelter of Him alone with all your being)-this complete surrender grants tat-prasadat param-shantim (supreme peace from His grace) and sthanam-avapsyasi (eternal abode). The trap: partial surrender maintaining independence in some life areas. Why this matters: The false path is compartmentalized spirituality-'Krishna for spiritual matters, I decide everything else.' Real sharanagati (surrender): sarva-bhavena means total-every thought-word-action oriented to Krishna. Not partial delegation but complete dependence. This isn't loss of selfhood but finding true self in relationship with Supreme-individual personality perfected through love not annihilated through merging. Therefore hold nothing back-surrender all plans-attachments-identifications; this total offering paradoxically grants perfect fulfillment, not diminishment."
    },
    'bg18-q25': {
        'prompt': 'How does Chapter 18 synthesize the entire Bhagavad-gita teaching into complete realization?',
        'choices': [
            'Presents isolated techniques for meditation-renunciation-action without unified framework',
            'Complete arc from sannyasa-tyaga analysis through threefold guna-mapping culminating in sarva-dharman parityajya-total surrender transcending all preliminary paths',
            'Recommends choosing either karma-yoga or jnana-yoga or bhakti-yoga based on preference',
            'Focuses purely on philosophical analysis without practical application to spiritual life'
        ],
        'correctIndex': 1,
        'feedback': "Chapter 18 is Gita's crescendo synthesizing everything: (1) FOUNDATION: Distinguishes sannyasa-tyaga-proper renunciation isn't abandoning action but relinquishing selfish desire within action (18.1-12). (2) ANALYSIS: Presents comprehensive threefold framework-knowledge (20-22), action (23-25), doer (26-28), intelligence (29-32), determination (33-35), happiness (36-39) all analyzed through sattva-rajas-tamas showing systematic guna-purification path. (3) INTEGRATION: Varnashrama-dharma (41-48) provides personalized sadhana respecting svabhava-each person's duty suited to nature. (4) TRANSCENDENCE: Brahma-bhuta state (54) transcends gunas but isn't final-leads to para-bhakti (supreme devotion). (5) CULMINATION: Sarva-dharman parityajya mam ekam sharanam vraja (18.66)-abandon all varieties of dharma, surrender to Me alone-Krishna guarantees mokshayishyami (I shall liberate) from all papa (sin). Arc: Threefold analysis elevates through sattva; brahma-bhuta transcends gunas; but perfection comes through complete surrender to Krishna-bhakti subsumes and completes all yoga paths. Final teaching: Not impersonal merging or renunciation but personal devotional surrender to Supreme Person-this is Gita's conclusion integrating karma-jnana-bhakti into unified sadhana culminating in Krishna-prapti (attaining Krishna) in eternal Goloka-dhama.",
        'verseLabel': 'BG 18.1-78',
        'verseUrl': 'https://vedabase.io/en/library/bg/18/',
        'correctIndex': 1,
        'choices': [
            'Presents isolated techniques for meditation-renunciation-action without unified framework',
            'Complete arc from sannyasa-tyaga analysis through threefold guna-mapping culminating in sarva-dharman parityajya-total surrender transcending all preliminary paths',
            'Recommends choosing either karma-yoga or jnana-yoga or bhakti-yoga based on preference',
            'Focuses purely on philosophical analysis without practical application to spiritual life'
        ]
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
                print(f"Updated {qid} to PURPORT/SYNTHESIS question")
            elif key == 'choices':
                print(f"Updated {qid} choices")
            elif key == 'correctIndex':
                print(f"Updated {qid} correctIndex")

with open('data/quizzes/bg/18-adult.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\n=== Phase 3 Complete ===")
print("Transformed bg18-q17 through bg18-q25:")
print("- Added 3 purport questions (bg18-q18, bg18-q22, bg18-q25 SYNTHESIS)")
print("- Enhanced all 9 feedback entries to Adult depth")
print("- Created comprehensive synthesis q25 integrating entire Gita arc")
print("- Themes: threefold happiness/intelligence, varnashrama, brahma-bhuta, sarva-dharman parityajya")
