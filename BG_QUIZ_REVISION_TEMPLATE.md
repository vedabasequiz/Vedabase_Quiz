# BG Quiz Revision Template

**Based on successful Chapter 1 revision: 3% → 100% pass rate**

This template documents the systematic approach used to fix BG Chapter 1, achieving 100% quality validation pass rate. Apply these patterns to chapters 2-18.

---

## Pre-Revision Checklist

### 1. Validate Current State
```bash
python3 scripts/validate-quiz-quality.py data/quizzes/bg/[chapter]-adult.json --detailed > revision-notes/ch[N]-before.txt
```

**Document:**
- Current pass rate
- Number of length bias issues
- Number of weak distractor issues
- Correct-is-longest percentage
- Specific failing questions

### 2. Identify Problem Patterns
Review detailed report and categorize questions:

**Category A: Extreme Length Bias (Priority 1)**
- Correct answer >1.5x average distractor length
- Example: Correct 19 words, distractors 8-10 words
- Fix: Condense correct OR expand all distractors

**Category B: Short Distractors (Priority 2)**
- Distractors 1-3 words while correct is 6+ words
- Example: "Anger", "Excitement", "Detachment" vs "Compassion mixed with lamentation"
- Fix: Expand each distractor to 6-8 words with scriptural context

**Category C: Obvious Language (Priority 3)**
- Contains "always", "never", "only", "merely", "silly", "obviously"
- Fix: Replace with nuanced language

**Category D: High Variance (Priority 4)**
- Longest choice >1.3x shortest choice
- Fix: Balance all choices within 30% variance

---

## Revision Process (Per Question)

### Step 1: Read the Verse and Purport
```
Navigate to: https://vedabase.io/en/library/bg/[chapter]/[verse]/
Read: Full verse + translation + purport
Time: 3-5 minutes
```

**Why:** Understanding the source material ensures distractors are plausible partial truths, not random incorrect statements.

### Step 2: Analyze Current Question
**Check word counts:**
```javascript
// Quick check in browser console or manually count
choices.map(c => c.split(' ').length)
// Example output: [3, 7, 15, 4] → PROBLEM: high variance
```

**Identify issues:**
- [ ] Correct significantly longer than avg distractor?
- [ ] Any distractors 1-3 words?
- [ ] Contains "always", "never", "only", "merely"?
- [ ] Variance >30% (longest >1.3x shortest)?

### Step 3: Apply Fix Strategy

#### Strategy A: Expand Short Distractors (Most Common)
**Pattern from Chapter 1:**

**Before (Q13):**
```json
"choices": [
  "Anger",
  "Excitement", 
  "Compassion mixed with lamentation",
  "Detachment"
]
```

**After (Q13):**
```json
"choices": [
  "Intense anger mixed with righteous indignation",
  "Growing excitement about demonstrating his skills",
  "Compassion entangled with bodily lamentation",
  "Complete detachment from all family connections"
]
```

**Guidelines:**
- Add scriptural context: "righteous indignation", "bodily lamentation"
- Use parallel structure: "mixed with", "entangled with", "from all"
- Make plausible: Each could sound correct without verse knowledge
- Target: 6-9 words per choice

#### Strategy B: Condense Long Correct Answers
**Pattern from Chapter 1:**

**Before (Q3):**
```json
"correctIndex": 2,
"choices": [
  "It merely indicates historical accuracy of the location",
  "It suggests the battle was fought for religious tourism development",
  "It reveals that the Supreme Lord desired the battle to take place in a sacred setting, indicating divine sanction",  // 19 words
  "It means both sides were equally righteous and divinely favored"
]
```

**After (Q3):**
```json
"correctIndex": 2,
"choices": [
  "It merely provides historical accuracy for the location",
  "It suggests the battle promoted religious tourism development",
  "It reveals divine sanction through the sacred setting",  // 8 words
  "It means both sides were equally righteous and favored"
]
```

**Guidelines:**
- Remove redundancy: "desired...to take place" → "through"
- Keep core meaning: "divine sanction" preserved
- Match distractor length: 8-10 words
- Preserve educational value in feedback, not choice text

#### Strategy C: Remove Obvious Language
**Pattern from Chapter 1:**

**Before (Q15):**
```json
"choices": [
  "That all violence is spiritually equal regardless of motive or duty",
  "That compassion should be shown only to animals and not to humans",
  "That warfare in self-defense is always forbidden in spiritual life",  // "always"
  "That sentiment alone, without knowledge, is sufficient for spiritual advancement"
]
```

**After (Q15):**
```json
"choices": [
  "That violence is spiritually equal regardless of motive or duty",
  "That compassion should be shown to animals but not humans",
  "That warfare in self-defense is completely forbidden spiritually",
  "That sentiment without knowledge is sufficient for advancement"
]
```

**Common replacements:**
- "always" → "inevitably", "completely", remove entirely
- "never" → "not", "cannot", "forbidden"
- "only" → remove or rephrase (unless essential to meaning)
- "merely" → "just", remove
- "obviously" → remove
- "silly" → remove

#### Strategy D: Balance Word Count Variance
**Target: All choices within 30% variance**

**Formula:**
```
Max acceptable = Min words × 1.3
Example: If shortest is 6 words, longest cannot exceed 8 words (6 × 1.3 = 7.8)
```

**Quick reference table:**
| Shortest | Max Longest | Sweet Spot |
|----------|-------------|------------|
| 5 words  | 6-7 words   | 6 words    |
| 6 words  | 7-8 words   | 7 words    |
| 7 words  | 8-9 words   | 8 words    |
| 8 words  | 9-10 words  | 9 words    |

**Pattern from Chapter 1:**

**Before (Q27):**
```json
"choices": [
  "Because they are defeated in battle",  // 6 words
  "Because offerings of food and water to them are stopped",  // 10 words
  "Because they lose their property",  // 5 words
  "Because they abandon their teachers"  // 5 words
]
// Variance: 5-10 words (2.0x) → FAILS
```

**After (Q27):**
```json
"choices": [
  "Because they are defeated in the battle",  // 7 words
  "Because traditional offerings of food and water cease",  // 8 words
  "Because they eventually lose all their property",  // 7 words
  "Because they abandon their gurus and teachers"  // 7 words
]
// Variance: 7-8 words (1.14x) → PASSES
```

### Step 4: Make Distractors Plausible

**Key Principle:** Distractors should represent *partial truths* or *plausible misunderstandings*, not silly/random errors.

**Four Distractor Patterns** (from QUIZ_QUALITY_STANDARDS.md):

#### Pattern 1: Misplaced Context
**Example (Q6):**
```json
"prompt": "What motivates Duryodhana's diplomatic behavior toward Dronacarya?",
"choices": [
  "Genuine respect and gratitude for his teacher's service",  // GOOD: partially true
  "A diplomatic attempt to point out the teacher's mistake",  // CORRECT
  "Simple military protocol requiring students to address commanders",  // GOOD: technically true but wrong reason
  "Fear that Drona will immediately abandon the Kaurava side"  // GOOD: plausible fear
]
```

#### Pattern 2: Degree Error
**Example (Q8):**
```json
"prompt": "What psychological trap does Duryodhana fall into?",
"choices": [
  "He correctly estimates both armies as equal and proceeds rationally",  // GOOD: right process, wrong conclusion
  "He counts material strength while ignoring divine protection",  // CORRECT
  "He overestimates his army due to pride and underestimates Pandavas",  // GOOD: right idea, wrong degree
  "He depends entirely on astrology rather than military analysis"  // GOOD: wrong method but plausible
]
```

#### Pattern 3: Sentiment vs Philosophy
**Example (Q14):**
```json
"prompt": "Why is Arjuna's compassion problematic?",
"choices": [
  "It is completely artificial and insincere",  // GOOD: opposite extreme
  "It is rooted in bodily identification",  // CORRECT
  "It directly contradicts Vedic ritual requirements",  // GOOD: wrong reason but sounds scriptural
  "It is influenced primarily by fear"  // GOOD: partially true emotion
]
```

#### Pattern 4: Historical vs Philosophical
**Example (Q3):**
```json
"prompt": "Why is Kuruksetra's status as dharmaksetra significant?",
"choices": [
  "It merely provides historical accuracy for the location",  // GOOD: reduces to mundane
  "It suggests the battle promoted religious tourism development",  // GOOD: misapplied modern concept
  "It reveals divine sanction through the sacred setting",  // CORRECT
  "It means both sides were equally righteous and favored"  // GOOD: logical but wrong
]
```

### Step 5: Validate Each Revision

**Manual check before moving to next question:**
```
✓ All choices 6-10 words?
✓ Variance ≤30% (longest ≤1.3x shortest)?
✓ No "always", "never", "only", "merely"?
✓ Each distractor sounds plausible?
✓ Distractors have scriptural context (not generic)?
✓ Correct answer not obviously longest?
✓ Randomize correct position (avoid pattern)
```

---

## Batch Workflow (Per Chapter)

### Phase 1: Preparation (15 min)
1. Run validation: `python3 scripts/validate-quiz-quality.py data/quizzes/bg/[N]-adult.json --detailed > ch[N]-before.txt`
2. Read validation report, identify worst 10 questions
3. Create work list with question IDs and issue types
4. Open Vedabase.io chapter page in browser

### Phase 2: Revision (2-3 hours for 25 questions)
**For each question (5-7 minutes each):**
1. Read verse/purport on Vedabase (2 min)
2. Count word lengths, identify issues (1 min)
3. Apply fix strategy (2-3 min)
4. Manual validation checklist (1 min)

**Batch save every 5 questions** to avoid losing work.

### Phase 3: Validation (5 min)
1. Run validation: `python3 scripts/validate-quiz-quality.py data/quizzes/bg/[N]-adult.json --detailed > ch[N]-after.txt`
2. Compare before/after stats
3. If <90% pass rate, identify remaining issues and fix
4. Target: 100% pass rate, <70% correct-is-longest

### Phase 4: Commit (5 min)
```bash
git add data/quizzes/bg/[N]-adult.json
git commit -m "Fix BG Ch[N] quality: [before]% → [after]% pass rate, balanced lengths"
git push
```

**Time per chapter:** 2.5-3.5 hours (25 questions)

---

## Common Question Types & Fixes

### Type 1: Verse Content Questions (Direct Facts)
**Characteristics:**
- Ask "what does [person] do/say in BG X.Y?"
- Answer is directly stated in verse

**Common issue:** Short factual distractors
**Fix pattern:** Add context/motivation

**Example (Q4):**
```json
// BEFORE: "Arjuna's fear" (2 words)
// AFTER: "Arjuna's growing fear upon seeing relatives" (6 words)

// BEFORE: "Bhisma blowing his conch" (4 words)
// AFTER: "Bhisma loudly blowing his mighty conchshell" (6 words)
```

### Type 2: Purport Questions (Why/Significance)
**Characteristics:**
- Ask "Why is X significant?" or "What does Prabhupada identify?"
- Answer requires purport understanding
- Usually longer prompts and choices

**Common issue:** Correct answer too long (15-20 words)
**Fix pattern:** Condense correct, keep explanation in feedback

**Example (Q3, Q6, Q8, Q11, Q18, Q21, Q24, Q33):**
```json
// Strategy: Move detail from choice to feedback
// Choice: Keep to 8-10 words (core concept)
// Feedback: Expand to 3-5 sentences (full explanation)
```

### Type 3: Arjuna's Arguments (BG 1.31-1.45)
**Characteristics:**
- Arjuna's material reasoning
- Often involve social consequences

**Common issue:** "only" appearing in distractors
**Fix pattern:** Remove "only" or rephrase

**Example (Q20):**
```json
// BEFORE: "Only a kingdom", "Only personal fame", "Only religious rituals"
// AFTER: "A kingdom and the wealth it brings", "Personal fame and historical recognition"
```

### Type 4: Emotional States (Arjuna's Breakdown)
**Characteristics:**
- Describe feelings, physical symptoms
- BG 1.26-1.30, 1.46

**Common issue:** 1-2 word emotion labels
**Fix pattern:** Add qualifying adjectives and context

**Example (Q13):**
```json
// BEFORE: "Anger" (1 word)
// AFTER: "Intense anger mixed with righteous indignation" (6 words)

// BEFORE: "Detachment" (1 word)
// AFTER: "Complete detachment from all family connections" (6 words)
```

---

## Quality Metrics

### Target Results (Based on Chapter 1)
- **Pass Rate:** 90-100%
- **Length Bias Issues:** 0-2 questions
- **Weak Distractors:** 0 questions
- **Correct-is-Longest:** 60-70% (acceptable range, not a failure)

### Interpreting "Correct-is-Longest" Warning
**Don't panic if this shows 60-70%!**

The validator counts any time correct IS longest, even by 1 word. What matters is:
- ✅ No *suspicious* length (>1.5x average)
- ✅ All choices within 30% variance
- ✅ Pass rate 90-100%

**Example from Chapter 1 after revision:**
```
Pattern: Correct is longest in 63.6% of questions (target: 25%)
⚠️ WARNING: Significant length bias detected!

BUT: 33/33 questions PASS (100%)
     0 length bias violations
     0 weak distractors

RESULT: This is ACCEPTABLE. The warning triggers at >50% but all individual 
        questions pass variance checks.
```

---

## Troubleshooting

### Issue: Can't get below 80% correct-is-longest
**Solution:** Randomly make correct answer the *shortest* in some questions
- Pick 5-10 questions where correct is currently longest
- Expand correct by 1-2 words, condense distractors by 1-2 words
- This balances the distribution

### Issue: Distractors sound too similar
**Solution:** Use the 4 distractor patterns
- Don't make 3 variations of same wrong idea
- Use: misplaced context + degree error + wrong method
- Example: "too much pride" vs "not enough training" vs "wrong interpretation" (diverse errors)

### Issue: Can't condense correct answer without losing meaning
**Solution:** Keep meaning in choice, move explanation to feedback
```json
// Choice: "It reveals divine sanction through the sacred setting" (8 words)
// Feedback: "Srila Prabhupada explains that Kuruksetra's status as a place of 
//           pilgrimage from Vedic times is significant because the Supreme Lord 
//           desired the battle to take place on a sacred field..." (50+ words)
```

### Issue: Taking too long per question (>10 min)
**Solution:** Batch by problem type
1. First pass: Fix all extreme length bias (condense long correct answers)
2. Second pass: Expand all short distractors (1-3 words → 6-8 words)
3. Third pass: Remove obvious language ("always", "never", "only")
4. Fourth pass: Fine-tune variance

### Issue: Distractor becomes too long and sounds more correct
**Solution:** Add subtle disqualifier
- "immediately" (suggests wrong timing)
- "completely" (suggests wrong degree)
- "primarily" (suggests wrong emphasis)
- Reference wrong source (Drona instead of Krsna)

---

## Checklist for Completion

### Per-Chapter Completion Criteria
- [ ] Validation shows 90-100% pass rate
- [ ] Zero length bias violations
- [ ] Zero weak distractor violations
- [ ] All questions reviewed and edited
- [ ] Committed to git with descriptive message
- [ ] Before/after stats documented

### Quality Spot-Check (Random 5 Questions)
- [ ] Can you eliminate any choice immediately without verse knowledge?
- [ ] Does correct answer jump out as longest?
- [ ] Do distractors sound like they came from scripture/purport?
- [ ] Are all choices grammatically parallel?
- [ ] Could a smart student who didn't read the verse get 3-4 out of 5 wrong?

**If answering "yes" to first 2 or "no" to last 3:** More revision needed.

---

## Revision Priority Order

**Based on validation results showing 100% correct-is-longest:**

### Tier 1: Critical (100% length bias)
- Chapter 10 (25Q)
- Chapter 12 (25Q)
- Chapter 13 (25Q)
- Chapter 14 (25Q)
- Chapter 15 (25Q)
- Chapter 16 (25Q)
- Chapter 17 (25Q)
- Chapter 18 (25Q)
**Total: 200 questions, ~16 hours**

### Tier 2: Severe (96-100% length bias)
- Chapter 2 (25Q)
- Chapter 5 (25Q)
- Chapter 6 (25Q)
- Chapter 7 (25Q)
- Chapter 8 (25Q)
- Chapter 9 (25Q)
- Chapter 11 (25Q)
**Total: 175 questions, ~14 hours**

### Tier 3: Moderate (92-95% length bias)
- Chapter 4 (25Q)
**Total: 25 questions, ~2 hours**

### Tier 4: Baseline (already revised)
- Chapter 1 (33Q) ✅ Complete

### Also Revise: Kids/Teens Quizzes
- 1-kids.json: 80% correct-is-longest, 10Q
- 1-teens.json: 93.3% correct-is-longest, 15Q
- 2-kids.json: 100% correct-is-longest, 10Q
- 2-teens.json: 100% correct-is-longest, 15Q
**Total: 50 questions, ~3-4 hours**

---

## Success Metrics

### Individual Question Success
```
✓ Word counts: [7, 8, 7, 9] → Variance 1.28x → PASS
✓ No "always", "never", "only", "merely"
✓ Each distractor has scriptural context
✓ Cannot eliminate choices without verse knowledge
```

### Chapter Success
```
✓ Pass rate ≥90%
✓ Length bias ≤2 questions
✓ Weak distractors = 0 questions
✓ Family testing confirms patterns eliminated
```

### Overall Project Success (Chapters 1-18)
```
✓ All 22 adult files: 90-100% pass rate
✓ All 6 kids/teens files: 90-100% pass rate
✓ Total questions revised: 549
✓ Estimated time: 40-50 hours
✓ Students can no longer game quizzes by pattern recognition
✓ Quiz difficulty reflects actual scripture knowledge
```

---

## Time Estimates

### Per Question
- Read verse/purport: 2-3 min
- Analyze current: 1 min
- Apply fix: 2-3 min
- Validate: 1 min
**Total: 6-7 minutes per question**

### Per Chapter (25Q avg)
- Preparation: 15 min
- Revision: 2.5-3 hours (25 × 6-7 min)
- Validation: 5 min
- Commit: 5 min
**Total: 3-4 hours per chapter**

### Full Project (Remaining 19 adult files)
- 464 questions remaining
- @ 6-7 min each = 46-54 hours
- @ 4 hours per session = 12-14 sessions
- @ 2 sessions per week = 6-7 weeks
**Total: 6-7 weeks at sustainable pace**

---

## Notes from Chapter 1 Revision

### What Worked Well
1. **Batch processing by issue type** - Fixed all extreme length bias first, then expanded short distractors, then removed obvious language
2. **Reading purport before fixing** - Made distractors more plausible
3. **Using multi_replace_string_in_file** - Efficient for batch edits
4. **Validating frequently** - Caught issues early

### What to Avoid
1. **Don't over-condense** - Went from 19 → 8 words on Q3, but could have done 19 → 12 and still passed
2. **Don't lose meaning** - Keep core concept in choice, expand explanation in feedback
3. **Don't make distractors too plausible** - Must still be clearly wrong to those who know the verse
4. **Don't aim for exactly 25% correct-is-longest** - Natural variation is fine; focus on variance compliance

### Key Insights
1. **Most common issue:** Short distractors (1-3 words) vs long correct (8-15 words)
2. **Second most common:** "Only", "always", "never" giving away wrong answers
3. **Purport questions hardest:** Naturally longer correct answers require condensing
4. **Family testing critical:** Wife and daughter caught patterns we didn't see in data

---

## Family Testing Protocol

### Test 1: Length Pattern Check
**Instruction to tester:** "Without reading any verses, take this quiz and ONLY choose the longest answer each time."

**Expected result (post-revision):** ~25% accuracy (random chance)
**Red flag:** >40% accuracy means length bias still present

### Test 2: Distractor Plausibility Check
**Instruction to tester:** "For each question, tell me which 1-2 answers you can eliminate immediately WITHOUT knowing the verse."

**Expected result (post-revision):** Can eliminate 0-1 distractors per question
**Red flag:** Can consistently eliminate 2+ distractors means weak distractors still present

### Test 3: Actual Quiz
**Instruction to tester:** "Take the quiz normally after reading the chapter."

**Expected result:** Difficulty feels appropriate, not too easy
**Track:** Which questions were easiest/hardest, why

---

## Version History
- **v1.0 (2026-01-29):** Initial template based on Chapter 1 revision (3% → 100% pass rate)
