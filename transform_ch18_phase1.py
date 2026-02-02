import json

with open('data/quizzes/bg/18-adult.json') as f:
    data = json.load(f)

# Phase 1: Transform q1-8 with purport questions + Adult feedback
# Ch18 themes: sannyasa vs tyaga, false path of complete inaction, threefold analysis culmination, ultimate surrender
# False paths to expose: sannyasa as inaction, tyaga as mere mental renunciation, karma-yoga as inferior preliminary path, renunciation without Krishna consciousness

changes = {
    'bg18-q1': {
        'feedback': "Arjuna's question is strategic-after 17 chapters, he seeks final clarity distinguishing sannyasa (renunciation order) from tyaga (relinquishment of fruit-desire). The trap: treating these as synonyms or unrelated paths. Why this matters: The false path is confusion about renunciation-some think sannyasa means abandoning all action; others think tyaga is mere mental detachment. Real understanding: Krishna will explain sannyasa means renouncing actions born of desire; tyaga means performing duty without attachment to results-both culminate in bhakti."
    },
    'bg18-q2': {
        'prompt': 'In the purport to BG 18.2, what misconception about renunciation does Srila Prabhupada refute?',
        'choices': [
            'That sannyasa means formally taking renounced order through institutional initiation',
            'That sannyasa means giving up only karma-kanda rituals while continuing dharmic duties',
            'That renunciation means complete cessation of all activities including devotional service',
            'That tyaga means offering fruits to Krishna while sannyasa means mental detachment'
        ],
        'correctIndex': 2,
        'feedback': "Srila Prabhupada explains sannyasa means renouncing kamya-karma (activities with fruit-desire) NOT renouncing devotional duties; tyaga means relinquishing attachment/fruit-expectation. The trap: impersonalist sannyasa advocating complete inaction as liberation. Why this matters: The false path is mayavadi renunciation-claiming all activity is maya, one should cease action entirely. Real sadhana: Krishna consciousness isn't inaction but action without selfish desire-bhakti-yoga purifies through engaged devotion, not withdrawal into vacancy. Gita advocates nishkama-karma (desireless action) culminating in bhakti, not cessation of service."
    },
    'bg18-q3': {
        'feedback': "Some Sankhya philosophers argue all karma is dosha-yukta (faulty)-even sattvic action binds through subtle ego-identification with doership. The trap: taking this analysis as prescription for total inaction. Why this matters: The false path is philosophical nihilism-using Sankhya's analysis of action's imperfection to justify renouncing prescribed duties. Real discrimination: While all material action has some defect, abandoning dharma creates greater bondage; performing duty without attachment (nishkama-karma) purifies consciousness enabling transcendence. Krishna refutes complete withdrawal-proper tyaga means acting without fruit-desire, not abandoning action itself."
    },
    'bg18-q4': {
        'feedback': "Krishna establishes ontological necessity of action-maintaining sharira (body) requires activities: breathing, eating, walking, thinking. Even sannyasis act constantly-difference is motivation not cessation. The trap: believing spiritual advancement requires physical immobility or mental vacancy. Why this matters: The false path is artificial renunciation-forcibly suppressing natural activities thinking stillness equals spirituality. Real understanding: Action is inevitable (prakrti compels through gunas); question is quality-selfish or selfless, binding or liberating. Cannot stop acting; can transform action's orientation from kama (desire) to seva (service). Therefore path isn't inaction but right action."
    },
    'bg18-q5': {
        'feedback': "Krishna establishes hierarchy: yajna-dana-tapas (sacrifice-charity-austerity) purify even great souls-never abandon these. The trap: thinking advanced renunciation means stopping all ritual/charitable activities. Why this matters: The false path is premature renunciation-abandoning external dharma before internal purification. Real progression: Perform yajna-dana-tapas without fruit-desire; these systematically purify consciousness. Path isn't renouncing duties but renouncing selfish motivation within duties. Therefore karma-yoga isn't preliminary stage to abandon but foundation supporting bhakti-devotional service includes prescribed duties performed for Krishna, not cessation of all activity."
    },
    'bg18-q6': {
        'feedback': "True tyaga means performing niyata-karma (prescribed duty) without raga-dvesha (attachment-aversion) or phala-kamana (fruit-desire). The trap: thinking renunciation means choosing which duties to perform based on preference. Why this matters: The false path is selective dharma-doing only pleasant duties while avoiding difficult ones under guise of detachment. Real sadhana: Perform all prescribed duties regardless of personal inclination-neither attracted to pleasant results nor averse to unpleasant-offering everything to Krishna. This transforms karma (binding action) into karma-yoga (liberating devotion). Renunciation isn't choosing inaction but transcending motivation within action."
    },
    'bg18-q7': {
        'feedback': "Those who abandon prescribed duties thinking they're troublesome commit tamasic tyaga-renunciation in ignorance creating greater bondage. The trap: rationalizing dharma-abandonment as spiritual advancement. Why this matters: The false path is convenient renunciation-avoiding responsibilities under spiritual pretexts. Real understanding: Dharma is purification system-avoiding prescribed duties doesn't liberate but degrades consciousness through tamas. Cannot bypass duty through philosophical shortcuts. Must perform duties detached from results-this detachment is tyaga, not abandoning action itself. Therefore path to perfection requires fulfilling responsibilities without selfish attachment, not escaping into artificial renunciation."
    },
    'bg18-q8': {
        'feedback': "Summarizing 18.7-8: rajasic tyaga avoids unpleasant duties from bodily concern/aversion; tamasic tyaga abandons prescribed duties from delusion/laziness. Neither attains tyaga-phala (fruit of renunciation). The trap: thinking avoiding difficult duties equals detachment. Why this matters: The false path is rationalized avoidance-abandoning challenging responsibilities claiming spiritual renunciation while actually driven by comfort-seeking or delusion. Real tyaga: Performing ALL prescribed duties (pleasant/unpleasant) without attachment to results-this sattvic tyaga purifies toward liberation. Cannot cherry-pick dharma; must fulfill responsibilities transcending preference, offering all to Krishna as seva not strategic self-interest."
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

print("\n=== Phase 1 Complete ===")
print("Transformed bg18-q1 through bg18-q8:")
print("- Added 1 purport question (bg18-q2)")
print("- Enhanced all 8 feedback entries to Adult depth")
print("- Themes: sannyasa vs tyaga distinction, false inaction, karma-yoga necessity, proper renunciation")
