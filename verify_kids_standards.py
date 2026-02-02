"""
Verify BG Kids Ch1-2 against locked kids standards
"""
import json

def analyze_kids_quiz(filename, chapter):
    with open(filename) as f:
        data = json.load(f)
    
    total = len(data['questions'])
    purport_qs = [q for q in data['questions'] if 'purport' in q.get('prompt', '').lower()]
    verse_qs = [q for q in data['questions'] if 'purport' not in q.get('prompt', '').lower()]
    
    purport_pct = (len(purport_qs) / total * 100) if total else 0
    verse_pct = (len(verse_qs) / total * 100) if total else 0
    
    print(f"\n{'='*70}")
    print(f"CHAPTER {chapter} KIDS - STANDARDS VERIFICATION")
    print(f"{'='*70}")
    
    # 1. Question Count
    print(f"\n1. QUESTION COUNT:")
    print(f"   Expected: 10 questions")
    print(f"   Actual: {total} questions {'✅' if total == 10 else '❌'}")
    
    # 2. Difficulty
    print(f"\n2. DIFFICULTY LEVEL:")
    print(f"   Expected: 'easy'")
    print(f"   Actual: '{data.get('difficulty', 'N/A')}' {'✅' if data.get('difficulty') in ['easy', 'easy-medium'] else '❌'}")
    
    # 3. Content Mix - USER'S LOCKED STANDARD: ~80% verse, ~20% purport
    print(f"\n3. CONTENT MIX:")
    print(f"   USER'S LOCKED STANDARD:")
    print(f"     ~80% translation/narrative-based (verse)")
    print(f"     ~20% simple purport points")
    print(f"   ACTUAL:")
    print(f"     Verse: {len(verse_qs)}/{total} ({verse_pct:.0f}%) {'✅' if 75 <= verse_pct <= 85 else '⚠️'}")
    print(f"     Purport: {len(purport_qs)}/{total} ({purport_pct:.0f}%) {'✅' if 15 <= purport_pct <= 25 else '⚠️'}")
    
    # 4. Cognitive Style - check for forbidden topics
    print(f"\n4. COGNITIVE STYLE (No abstractions):")
    forbidden = ['non-doership', 'modes of nature', 'mayavada', 'renunciation', 
                 'epistemology', 'psychological', 'philosophy', 'abstract']
    issues = []
    for i, q in enumerate(data['questions'], 1):
        content = (q.get('prompt', '') + ' ' + q.get('feedback', '')).lower()
        for term in forbidden:
            if term in content:
                issues.append(f"q{i} uses '{term}'")
    
    if issues:
        print(f"   ⚠️ Found forbidden abstractions: {', '.join(issues[:5])}")
    else:
        print(f"   ✅ No forbidden abstractions found")
    
    # 5. Bhakti Framing - must be direct and positive, no comparisons
    print(f"\n5. BHAKTI FRAMING:")
    bhakti_issues = []
    for i, q in enumerate(data['questions'], 1):
        content = (q.get('prompt', '') + ' ' + q.get('feedback', '')).lower()
        if any(term in content for term in ['superior', 'better than', 'other paths', 
                                             'comparing', 'critiquing', 'refutes']):
            bhakti_issues.append(f"q{i}")
    
    if bhakti_issues:
        print(f"   ⚠️ Comparative bhakti found in: {', '.join(bhakti_issues)}")
        print(f"   RULE VIOLATION: Kids introduced to devotion, not asked to analyze it")
    else:
        print(f"   ✅ Bhakti is direct, positive, concrete")
    
    # 6. Language - check for Sanskrit terms (should be minimal)
    print(f"\n6. LANGUAGE RULES:")
    sanskrit_terms = ['dharma', 'karma', 'yoga', 'atma', 'brahman', 'moksha', 
                      'samsara', 'maya', 'prakriti', 'purusha']
    sanskrit_found = []
    for i, q in enumerate(data['questions'], 1):
        content = (q.get('prompt', '') + ' ' + q.get('feedback', '')).lower()
        for term in sanskrit_terms:
            if term in content:
                sanskrit_found.append(f"q{i}:{term}")
    
    if len(sanskrit_found) > 3:
        print(f"   ⚠️ Too many Sanskrit terms: {', '.join(sanskrit_found[:5])}")
        print(f"   RULE: Only Krishna/Arjuna allowed unless unavoidable")
    else:
        print(f"   ✅ Minimal Sanskrit terms ({len(sanskrit_found)} found)")
    
    # 7. Feedback Length - should be 1-2 SHORT sentences
    print(f"\n7. FEEDBACK RULES:")
    feedback_lens = [(i+1, len(q['feedback'].split())) for i, q in enumerate(data['questions'])]
    avg_words = sum(w for _, w in feedback_lens) / len(feedback_lens)
    long_fb = [(q, w) for q, w in feedback_lens if w > 25]
    
    print(f"   Target: 1-2 short sentences (~10-20 words)")
    print(f"   Average: {avg_words:.1f} words")
    
    if long_fb:
        long_list = [f"q{q}({w}w)" for q, w in long_fb]
        print(f"   ⚠️ Too long (>25w): {long_list}")
        print(f"   RULE: Keep it simple for kids")
    else:
        print(f"   ✅ All feedback appropriate length")
    
    # 8. Check feedback tone - should be positive, no "why wrong"
    print(f"\n8. FEEDBACK TONE:")
    negative_patterns = []
    for i, q in enumerate(data['questions'], 1):
        feedback = q.get('feedback', '').lower()
        if any(phrase in feedback for phrase in ['wrong because', 'incorrect because', 
                                                   'not this because', 'the false']):
            negative_patterns.append(f"q{i}")
    
    if negative_patterns:
        print(f"   ⚠️ Negative/corrective tone in: {', '.join(negative_patterns)}")
        print(f"   RULE: Positive tone, no comparison of options")
    else:
        print(f"   ✅ Positive tone throughout")
    
    return {
        'total': total,
        'verse_pct': verse_pct,
        'purport_pct': purport_pct,
        'has_abstractions': len(issues) > 0,
        'has_comparative_bhakti': len(bhakti_issues) > 0,
        'has_too_much_sanskrit': len(sanskrit_found) > 3,
        'avg_feedback_words': avg_words,
        'has_long_feedback': len(long_fb) > 0,
        'has_negative_tone': len(negative_patterns) > 0
    }

# Analyze both chapters
ch1 = analyze_kids_quiz('data/quizzes/bg/1-kids.json', 1)
ch2 = analyze_kids_quiz('data/quizzes/bg/2-kids.json', 2)

print(f"\n{'='*70}")
print("OVERALL COMPLIANCE SUMMARY")
print(f"{'='*70}")

violations = []

# Check question count
if ch1['total'] != 10:
    violations.append(f"Ch1 has {ch1['total']} questions (should be 10)")
if ch2['total'] != 10:
    violations.append(f"Ch2 has {ch2['total']} questions (should be 10)")

# Check content mix - USER'S STANDARD is ~80% verse, ~20% purport
if not (75 <= ch1['verse_pct'] <= 85):
    violations.append(f"Ch1 verse ratio {ch1['verse_pct']:.0f}% (should be ~80%)")
if not (75 <= ch2['verse_pct'] <= 85):
    violations.append(f"Ch2 verse ratio {ch2['verse_pct']:.0f}% (should be ~80%)")

if ch1['has_abstractions'] or ch2['has_abstractions']:
    violations.append("Abstract/philosophical terms found (forbidden for kids)")

if ch1['has_comparative_bhakti'] or ch2['has_comparative_bhakti']:
    violations.append("Comparative bhakti (should be direct and positive only)")

if ch1['has_too_much_sanskrit'] or ch2['has_too_much_sanskrit']:
    violations.append("Too many Sanskrit terms (only Krishna/Arjuna allowed)")

if ch1['has_long_feedback'] or ch2['has_long_feedback']:
    violations.append("Feedback too long (should be 1-2 short sentences, ~10-20w)")

if ch1['has_negative_tone'] or ch2['has_negative_tone']:
    violations.append("Negative/corrective tone (should be positive only)")

if violations:
    print(f"\n❌ STANDARDS VIOLATIONS FOUND:")
    for v in violations:
        print(f"   • {v}")
    print(f"\n⚠️ THESE CHAPTERS DO NOT FULLY MEET USER'S LOCKED KIDS STANDARDS")
else:
    print(f"\n✅ ALL LOCKED KIDS STANDARDS MET")
    print(f"\nKids meet the Bhagavad Gita as a friendly guide, not a test of intelligence.")
