"""
Verify BG Teens Ch1-2 against locked teen standards
"""
import json

def analyze_teen_quiz(filename, chapter):
    with open(filename) as f:
        data = json.load(f)
    
    total = len(data['questions'])
    purport_qs = [q for q in data['questions'] if 'purport' in q.get('prompt', '').lower()]
    verse_qs = [q for q in data['questions'] if 'purport' not in q.get('prompt', '').lower()]
    
    purport_pct = (len(purport_qs) / total * 100) if total else 0
    verse_pct = (len(verse_qs) / total * 100) if total else 0
    
    print(f"\n{'='*70}")
    print(f"CHAPTER {chapter} TEENS - STANDARDS VERIFICATION")
    print(f"{'='*70}")
    
    # 1. Question Count
    print(f"\n1. QUESTION COUNT:")
    print(f"   Expected: 15 questions")
    print(f"   Actual: {total} questions {'✅' if total == 15 else '❌'}")
    
    # 2. Difficulty
    print(f"\n2. DIFFICULTY LEVEL:")
    print(f"   Expected: 'medium'")
    print(f"   Actual: '{data.get('difficulty', 'N/A')}' {'✅' if data.get('difficulty') == 'medium' else '❌'}")
    
    # 3. Content Mix - USER'S LOCKED STANDARD: ~55% verse, ~45% purport
    print(f"\n3. CONTENT MIX:")
    print(f"   USER'S LOCKED STANDARD:")
    print(f"     ~55% translation-based (verse)")
    print(f"     ~45% purport-guided reasoning")
    print(f"   ACTUAL:")
    print(f"     Verse: {len(verse_qs)}/{total} ({verse_pct:.0f}%) {'✅' if 50 <= verse_pct <= 60 else '⚠️'}")
    print(f"     Purport: {len(purport_qs)}/{total} ({purport_pct:.0f}%) {'✅' if 40 <= purport_pct <= 50 else '⚠️'}")
    
    # 4. Cognitive Style - check for adult-level abstractions
    print(f"\n4. COGNITIVE STYLE:")
    abstract_terms = ['mayavada', 'ontology', 'ontological', 'epistemology', 'metaphysics']
    issues = []
    for i, q in enumerate(data['questions'], 1):
        feedback = q.get('feedback', '').lower()
        for term in abstract_terms:
            if term in feedback:
                issues.append(f"q{i} uses '{term}'")
    
    if issues:
        print(f"   ⚠️ Found adult abstractions: {', '.join(issues)}")
    else:
        print(f"   ✅ No abstract metaphysics found")
    
    # 5. Bhakti Framing
    print(f"\n5. BHAKTI FRAMING:")
    philosophical_bhakti = []
    for i, q in enumerate(data['questions'], 1):
        feedback = q.get('feedback', '').lower()
        if any(term in feedback for term in ['refutes', 'refuting', 'false philosophy', 'mayavadi']):
            philosophical_bhakti.append(f"q{i}")
    
    if philosophical_bhakti:
        print(f"   ⚠️ Philosophical defense of bhakti found in: {', '.join(philosophical_bhakti)}")
        print(f"   RULE VIOLATION: Teens shown bhakti, not asked to defend it")
    else:
        print(f"   ✅ No philosophical defenses - bhakti shown concretely")
    
    # 6. Feedback Length - should be 2-3 sentences
    print(f"\n6. FEEDBACK RULES:")
    feedback_lens = [(i+1, len(q['feedback'].split())) for i, q in enumerate(data['questions'])]
    avg_words = sum(w for _, w in feedback_lens) / len(feedback_lens)
    long_fb = [(q, w) for q, w in feedback_lens if w > 60]
    
    print(f"   Target: 2-3 sentences (~30-50 words)")
    print(f"   Average: {avg_words:.1f} words")
    
    if long_fb:
        long_list = [f"q{q}({w}w)" for q, w in long_fb]
        print(f"   ⚠️ Too long (>60w): {long_list}")
        print(f"   RULE: No metaphysical density")
    else:
        print(f"   ✅ All feedback appropriate length")
    
    # 7. Check for "Why this matters" - adult pattern
    print(f"\n7. ADULT PATTERNS:")
    adult_patterns = []
    for i, q in enumerate(data['questions'], 1):
        feedback = q.get('feedback', '')
        if 'why this matters' in feedback.lower():
            adult_patterns.append(f"q{i} has 'Why this matters'")
        if 'the trap:' in feedback.lower():
            adult_patterns.append(f"q{i} has 'The trap:'")
        if 'false path' in feedback.lower():
            adult_patterns.append(f"q{i} has 'false path'")
    
    if adult_patterns:
        print(f"   ⚠️ ADULT PATTERNS FOUND:")
        for p in adult_patterns[:5]:
            print(f"     - {p}")
        print(f"   RULE VIOLATION: These are adult reflection patterns")
    else:
        print(f"   ✅ No adult reflection patterns")
    
    return {
        'total': total,
        'verse_pct': verse_pct,
        'purport_pct': purport_pct,
        'has_abstractions': len(issues) > 0,
        'has_philosophical_bhakti': len(philosophical_bhakti) > 0,
        'has_adult_patterns': len(adult_patterns) > 0,
        'avg_feedback_words': avg_words
    }

# Analyze both chapters
ch1 = analyze_teen_quiz('data/quizzes/bg/1-teens.json', 1)
ch2 = analyze_teen_quiz('data/quizzes/bg/2-teens.json', 2)

print(f"\n{'='*70}")
print("OVERALL COMPLIANCE SUMMARY")
print(f"{'='*70}")

violations = []

# Check content mix - USER'S STANDARD is ~55% verse, ~45% purport
if not (50 <= ch1['verse_pct'] <= 60):
    violations.append(f"Ch1 verse ratio {ch1['verse_pct']:.0f}% (should be ~55%)")
if not (50 <= ch2['verse_pct'] <= 60):
    violations.append(f"Ch2 verse ratio {ch2['verse_pct']:.0f}% (should be ~55%)")

if ch1['has_abstractions'] or ch2['has_abstractions']:
    violations.append("Abstract metaphysical terms found")

if ch1['has_philosophical_bhakti'] or ch2['has_philosophical_bhakti']:
    violations.append("Philosophical defense of bhakti (should be shown, not defended)")

if ch1['has_adult_patterns'] or ch2['has_adult_patterns']:
    violations.append("Adult reflection patterns ('Why this matters', 'The trap:', 'false path')")

if violations:
    print(f"\n❌ STANDARDS VIOLATIONS FOUND:")
    for v in violations:
        print(f"   • {v}")
    print(f"\n⚠️ THESE CHAPTERS DO NOT FULLY MEET USER'S LOCKED TEEN STANDARDS")
    print(f"\nKey issue: Content mix should be ~55% verse / ~45% purport")
    print(f"           Current: Ch1={ch1['verse_pct']:.0f}%/{ch1['purport_pct']:.0f}%, Ch2={ch2['verse_pct']:.0f}%/{ch2['purport_pct']:.0f}%")
else:
    print(f"\n✅ ALL LOCKED TEEN STANDARDS MET")
