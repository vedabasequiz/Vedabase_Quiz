# Quiz Quality Standards: MCQ Design Rules
**Critical Issues Identified: Length Bias & Obvious Distractors**

---

## Problem Statement

### Issue 1: Length Bias
**Observation**: Correct answers tend to be significantly longer than distractors, creating a pattern that allows test-takers to guess without knowledge.

**Example of BAD design:**
```
Correct answer: "Arjuna is bewildered by illusion on account of material affection for his family members, causing him to see inauspicious omens where none objectively exist"
Distractor: "He is exhausted"
Distractor: "He has been cursed"
Distractor: "He is physically ill"
```

### Issue 2: Obvious Distractors
**Observation**: Wrong answers are implausible or clearly incorrect, making them too easy to eliminate without actual understanding.

**Example of BAD design:**
```
Question: "What does Arjuna ask Krsna in BG 2.7?"
A) To bring him lunch
B) To instruct him on his duty clearly
C) To leave the battlefield
D) To summon Duryodhana
```

---

## SOLUTION 1: Length Balance Rules

### Mandatory Requirements

#### Rule 1.1: Balanced Length (Hard Rule)
- **All 4 choices must be within 30% length variance**
- Measure by word count, not character count
- If correct answer is 12 words, distractors should be 8-15 words

#### Rule 1.2: Randomize Length Position (Hard Rule)
- **Correct answer length distribution:**
  - Shortest answer: 25% of questions
  - Second shortest: 25% of questions
  - Second longest: 25% of questions
  - Longest answer: 25% of questions

#### Rule 1.3: Detail Parity (Strong Constraint)
- If correct answer includes a "because" clause, at least 2 distractors should also
- If correct answer references a verse number, distractors should reference verses too
- Match the grammatical complexity across all choices

### Implementation Guide

**BEFORE (Length Bias):**
```json
{
  "choices": [
    "Physical blindness only",
    "Lack of military strategy",
    "Both physical blindness and spiritual ignorance reflecting his attachment to his sons which prevents clear moral and spiritual vision",
    "Dependence on Sanjaya"
  ],
  "correctIndex": 2
}
```
**Word counts**: 3, 4, 18, 3 → FAILS (correct is 6x longer)

**AFTER (Length Balanced):**
```json
{
  "choices": [
    "Only his physical condition without spiritual significance",
    "His lack of military knowledge and strategic weakness",
    "Both physical blindness and spiritual ignorance due to attachment",
    "His dependence on Sanjaya for battlefield intelligence"
  ],
  "correctIndex": 2
}
```
**Word counts**: 7, 8, 9, 8 → PASSES (within 30% variance)

---

## SOLUTION 2: Plausible Distractor Rules

### Mandatory Requirements

#### Rule 2.1: Partial Truth Distractors (Tier 2)
Every distractor must contain at least one of:
- **Partial truth**: Correct in isolation but wrong in context
- **Misplaced emphasis**: True fact but irrelevant to the question
- **Common misunderstanding**: Something a sincere student might believe
- **Opposite extreme**: Logically opposite error

**BAD Distractors (too obvious):**
```
Question: "Why is Kuruksetra significant?"
A) It's where Krsna ate lunch
B) It's a dharmaksetra desired by the Supreme Lord for the battle
C) It has good weather
D) It's near Delhi
```

**GOOD Distractors (plausible):**
```
Question: "Why is Kuruksetra significant?"
A) It merely indicates historical accuracy of the location
B) It reveals divine sanction for the battle on sacred ground
C) It suggests the battle was fought for religious tourism
D) It means both sides were equally divinely favored
```

#### Rule 2.2: Scriptural Language (Tier 2)
- Distractors should use vocabulary from the same text
- Reference actual concepts from the chapter (misapplied)
- Avoid modern slang or anachronistic language

**BAD (anachronistic):**
```
A) Krsna wanted to boost tourism
B) Arjuna was having a panic attack
C) The battlefield had good Wi-Fi
```

**GOOD (contextual):**
```
A) Arjuna was overcome by false renunciation
B) Arjuna properly understood his ksatriya duty
C) Arjuna was demonstrating genuine compassion
```

#### Rule 2.3: Conceptual Proximity (Tier 3)
The best distractors are **almost correct**:
- Off by one verse reference
- Correct teaching but wrong context
- Right concept but inverted application
- True in a different chapter

**Example:**
```
Question: "In BG 2.13, what analogy does Krsna use?"
A) The changing of bodies is like changing clothes (BG 2.22 - wrong verse!)
B) Childhood, youth, old age, then another body (Correct - BG 2.13)
C) The soul is unbreakable like the sky (BG 2.24 - wrong verse!)
D) Weapons cannot cut the soul (BG 2.23 - wrong verse!)
```
→ All distractors are TRUE but from WRONG verses

---

## Automated Validation Rules

### Create Validation Script: `validate-quiz-quality.py`

```python
def check_length_bias(choices, correct_index):
    """Check if correct answer is suspiciously longer."""
    lengths = [len(choice.split()) for choice in choices]
    correct_length = lengths[correct_index]
    avg_distractor_length = sum(l for i, l in enumerate(lengths) if i != correct_index) / 3
    
    # Fail if correct is more than 50% longer than average distractor
    if correct_length > avg_distractor_length * 1.5:
        return False, f"Length bias: correct is {correct_length} words vs {avg_distractor_length:.1f} avg"
    
    # Fail if variance is too high
    max_length = max(lengths)
    min_length = min(lengths)
    if max_length > min_length * 1.3:
        return False, f"Variance too high: {min_length}-{max_length} words"
    
    return True, "Pass"

def check_distractor_plausibility(choices, correct_index, chapter_keywords):
    """Check if distractors use chapter-relevant vocabulary."""
    distractors = [c for i, c in enumerate(choices) if i != correct_index]
    
    obvious_words = ['obviously', 'never', 'always', 'impossible', 'silly', 'absurd']
    for d in distractors:
        if any(word in d.lower() for word in obvious_words):
            return False, f"Obvious distractor contains absolute language"
    
    # Check if distractors reference scriptural concepts
    for d in distractors:
        if len(d.split()) < 5:
            return False, f"Distractor too short: '{d}'"
    
    return True, "Pass"
```

---

## Distractor Design Patterns (Examples from BG)

### Pattern 1: Misplaced Context
```
Question: "What does BG 2.47 teach about action?"
Correct: "You have right to work but not to the fruits"
Distractor: "You should renounce all action entirely" (BG 5.2 misapplied)
Distractor: "Work should be done for material gain" (material consciousness)
Distractor: "Action is bondage and should be avoided" (sannyasa misunderstood)
```

### Pattern 2: Degree Error
```
Question: "How does Krsna describe the soul in BG 2.20?"
Correct: "Never born, eternal, primeval, not slain when body is slain"
Distractor: "Born at the beginning of creation and dies at the end" (partial creation)
Distractor: "Temporarily manifested during embodiment only" (material view)
Distractor: "Born from Brahman and merges back into oneness" (impersonalism)
```

### Pattern 3: Sentiment vs Philosophy
```
Question: "Why does Prabhupada say Arjuna's compassion is problematic (BG 1.28)?"
Correct: "Based on bodily identification without spiritual knowledge"
Distractor: "Compassion is never appropriate for a warrior" (too extreme)
Distractor: "True compassion requires considering the soul's eternal welfare" (actually correct - wrong context)
Distractor: "Arjuna should show no feeling at all" (stoicism, not Gita)
```

### Pattern 4: Historical vs Philosophical
```
Question: "What is the significance of Kuruksetra being a dharmaksetra?"
Correct: "Reveals divine sanction for battle on sacred ground"
Distractor: "Simply provides geographical accuracy" (reduces to history)
Distractor: "Indicates equal religious merit for both armies" (false equivalence)
Distractor: "Suggests peaceful resolution was geographically impossible" (material logic)
```

---

## Revision Process for Existing Quizzes

### Phase 1: Automated Detection
```bash
python3 scripts/validate-quiz-quality.py data/quizzes/bg/*.json
```

**Output example:**
```
Chapter 1 Adult:
  Q3: ⚠️ Length bias - correct is 18 words vs 5.3 avg
  Q7: ⚠️ Obvious distractor: "He wanted to eat lunch"
  Q12: ✓ Pass
  Q18: ⚠️ Length bias - correct is 22 words vs 7.0 avg
  
Summary: 22/33 questions PASS, 11 need revision
```

### Phase 2: Manual Revision (per question)

**Step 1: Identify problem**
- Length bias? → Expand distractors or compress correct answer
- Obvious distractor? → Replace with plausible alternative

**Step 2: Research alternatives**
- Read the verse and purport again
- Note related verses that could be confused
- Identify common misunderstandings Prabhupada addresses

**Step 3: Rewrite distractors**
- Match word count (±2 words)
- Use scriptural vocabulary
- Make it sound like something a student might think

**Step 4: Test with family**
- Ask: "Can you eliminate any without knowing the answer?"
- Ask: "Is the longest answer most likely correct?"
- Revise until both answers are "No"

### Phase 3: Documentation
Update quiz with comment:
```json
{
  "id": "bg2-q5-revised",
  "prompt": "...",
  "choices": [...],
  "correctIndex": 2,
  "feedback": "...",
  "revision_notes": "Fixed length bias and improved distractor plausibility (2026-01-29)"
}
```

---

## Quality Checklist (per question)

### Length Balance Check
- [ ] Count words in each choice (not characters)
- [ ] Longest choice is ≤1.3x shortest choice
- [ ] Correct answer is NOT consistently longest in the quiz
- [ ] If correct has subordinate clause, so do 2+ distractors

### Distractor Plausibility Check
- [ ] Each distractor represents a believable error
- [ ] No distractor uses "obviously", "never", "always", "silly"
- [ ] Distractors reference actual scriptural concepts (not random)
- [ ] At least one distractor is a "partial truth"
- [ ] At least one distractor is a "common misunderstanding"

### Advanced Check (Tier 3)
- [ ] Could a smart student eliminate options without verse knowledge?
- [ ] Do distractors test conceptual understanding (not just memory)?
- [ ] Would Prabhupada's purport explicitly address why each distractor fails?

---

## Priority Action Items

### Immediate (This Week)
1. **Create validation script**: Scan all BG quizzes for length bias
2. **Audit Chapter 1**: Manually review all 33 questions with family
3. **Document worst offenders**: List questions that need urgent revision

### Short-term (Next 2 Weeks)
4. **Revise flagged questions**: Fix length bias and obvious distractors in Chapters 1-4
5. **Establish baseline**: Ensure Tier 1 chapters meet quality standards before proceeding

### Medium-term (Ongoing)
6. **Apply to new questions**: When adding purport questions to Chapters 2-18, apply these rules from the start
7. **Periodic review**: Re-test with family members quarterly

---

## Success Metrics

### Before Fix (Current State)
- Correct answer is longest: ~60-70% of questions
- Obvious distractors: ~30-40% of questions
- Can eliminate 2+ choices without knowledge: ~50% of questions

### After Fix (Target State)
- Correct answer is longest: ~25% of questions (random)
- Obvious distractors: <5% of questions
- Can eliminate 2+ choices without knowledge: <10% of questions

### Family Test Protocol
Have wife/daughter take quiz:
1. Mark which questions they could answer by length pattern alone
2. Mark which questions had "silly" distractors
3. Track accuracy when guessing vs knowing

**Target**: Guessing success rate should be ~25% (random chance), not 60-70%

---

## Integration with BG Enhancement Plan

### When Adding New Purport Questions (Chapters 2-18)
**Mandatory checklist before inserting each question:**

1. **Length check**: 
   ```
   Correct: ___ words
   Distractor 1: ___ words (within 30%?)
   Distractor 2: ___ words (within 30%?)
   Distractor 3: ___ words (within 30%?)
   ```

2. **Plausibility check**:
   - [ ] Each distractor represents a real philosophical error
   - [ ] At least 2 distractors contain specific scriptural references
   - [ ] No distractor is "silly" or "absurd"

3. **Family test**: Show to wife/daughter - can they eliminate choices too easily?

### Revised Time Estimates
- Original: 4-6 hours per chapter
- With quality control: **5-7 hours per chapter**
  - +30 min for length balancing
  - +30 min for distractor improvement
  - +15 min for family testing

---

## Tools Needed

### 1. Validation Script
`scripts/validate-quiz-quality.py` - automated length and pattern checks

### 2. Distractor Bank
Maintain a list of common philosophical errors for each chapter:
- Material compassion (BG 1)
- Body-soul confusion (BG 2)
- False renunciation (BG 3)
- Impersonalism (throughout)
- Karma-mimamsa (BG 3-4)

### 3. Review Template
```markdown
## Question Review: bg[chapter]-q[number]

**Original choices word count**: [3, 4, 18, 3]
**Issue**: Length bias (correct 6x longer)

**Revised choices word count**: [7, 8, 9, 8]
**Status**: ✓ FIXED

**Distractor quality**:
- D1: Partial truth (material understanding)
- D2: Opposite extreme (absolute renunciation)
- D3: Misplaced emphasis (different context)

**Family test**: Daughter unable to eliminate without verse knowledge ✓
```

---

## Next Steps

1. **Create validation script** (1 hour)
2. **Run on all BG quizzes** (15 min)
3. **Review results with family** (30 min)
4. **Prioritize worst 20 questions** for immediate revision (1 week)
5. **Apply standards to all new questions** going forward

This ensures quiz quality improves systematically rather than question-by-question as issues are noticed.
