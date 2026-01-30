# BG Quiz Purport Enhancement Plan
**Phase 2: Chapters 2-18 Adult Quizzes**

## Objective
Add 8 purport-critical questions to each of the remaining 17 BG Adult chapters to achieve the required 35-40% purport ratio per VEDABASE_BG_PUBLISH_CHECKLIST.md Tier 2 standards.

---

## Current Status

### ✅ Completed
- **Chapter 1 Adult**: 33 questions (8 purport-focused added) ✅

### 🔄 Remaining Work
- **Chapters 2-18 Adult**: 17 chapters × 8 purport questions = **136 new questions**

---

## Three-Tier Priority Structure

### 🔴 TIER 1 - Critical Foundation (Complete First)
**Chapters 2-4** - Core philosophical framework

| Chapter | Theme | Why Critical | Target Questions |
|---------|-------|--------------|------------------|
| **Ch 2** | Analytical Study of Material/Spiritual Nature | Most quoted chapter, sankhya-yoga foundation | 33 total (25→33) |
| **Ch 3** | Karma-yoga | Practical philosophy of action | 33 total (25→33) |
| **Ch 4** | Transcendental Knowledge | Guru succession, sacrifice | 33 total (25→33) |

**Time Estimate**: 12-18 hours (3 chapters × 4-6 hours each)  
**Completion Deadline**: Week 1

---

### 🟡 TIER 2 - Major Teaching Chapters (Second Priority)
**Chapters 6, 7, 9, 12, 18** - Key devotional and philosophical content

| Chapter | Theme | Why Important | Target Questions |
|---------|-------|---------------|------------------|
| **Ch 6** | Dhyana-yoga | Meditation, mind control | 33 total (25→33) |
| **Ch 7** | Knowledge of the Absolute | Krsna's energies, worship | 33 total (25→33) |
| **Ch 9** | Most Confidential Knowledge | Pure devotion, raja-vidya | 33 total (25→33) |
| **Ch 12** | Devotional Service | Bhakti vs other paths | 33 total (25→33) |
| **Ch 18** | Conclusion/Liberation | Final instructions, surrender | 33 total (25→33) |

**Time Estimate**: 20-30 hours (5 chapters × 4-6 hours each)  
**Completion Deadline**: Week 2-3

---

### 🟢 TIER 3 - Supporting Chapters (Third Priority)
**Chapters 5, 8, 10, 11, 13, 14, 15, 16, 17** - Important but less foundational

| Chapter | Theme | Complexity | Target Questions |
|---------|-------|------------|------------------|
| **Ch 5** | Karma-yoga (Action in Krsna Consciousness) | Medium | 33 total |
| **Ch 8** | Attaining the Supreme | Medium | 33 total |
| **Ch 10** | Opulence of the Absolute | Medium | 33 total |
| **Ch 11** | Universal Form | High (visual/descriptive) | 33 total |
| **Ch 13** | Nature, Enjoyer, Consciousness | High (philosophical) | 33 total |
| **Ch 14** | Three Modes of Material Nature | Medium | 33 total |
| **Ch 15** | Supreme Person | Medium | 33 total |
| **Ch 16** | Divine/Demoniac Natures | Medium | 33 total |
| **Ch 17** | Divisions of Faith | Medium | 33 total |

**Time Estimate**: 36-54 hours (9 chapters × 4-6 hours each)  
**Completion Deadline**: Week 4-6

---

## Standard Workflow Per Chapter

### Step 1: Preparation (30 min)
1. Read existing 25-question quiz for the chapter
2. Note which verses already have questions
3. Review chapter on Vedabase.io focusing on purports
4. Identify 8-10 verses with rich purport content on:
   - False paths/warnings
   - Psychological traps
   - Misinterpretations Prabhupada addresses
   - Contrastive reasoning (material vs spiritual)

### Step 2: Question Generation (2-3 hours)
For each of the 8 new questions:

**Content Requirements:**
- Prompt explicitly references "purport" or "Srila Prabhupada explains"
- Focus on purport-only content (not verse translation)
- Target warnings, false paths, or deeper insights
- Include 4 plausible choices with contrastive reasoning

**Example Template:**
```json
{
  "id": "bg[chapter]-q[number]",
  "prompt": "In the purport to BG [chapter].[verse], Srila Prabhupada warns against [false path]. What does he explain?",
  "choices": [
    "[Partial truth/common misunderstanding]",
    "[Material/sentimental interpretation]",
    "[Correct transcendental understanding]",
    "[Opposite extreme]"
  ],
  "correctIndex": 2,
  "feedback": "[3-5 sentences explaining why correct answer is right, why others fail, includes 'Why this matters' for key questions]",
  "verseLabel": "BG [chapter].[verse]",
  "verseUrl": "https://vedabase.io/en/library/bg/[chapter]/[verse]/",
  "verdict": "Correct"
}
```

### Step 3: Integration (30-60 min)
1. Insert new questions strategically (not just at end)
2. Maintain difficulty progression: 60% accessible → 40% harder
3. Update question count in title: "| 33Q"
4. Verify JSON structure
5. Test one question for accuracy against Vedabase

### Step 4: Quality Check (15 min)
- [ ] All 8 questions reference purport explicitly
- [ ] Feedback is 3-5 sentences for adults
- [ ] Distractors are plausible (not silly)
- [ ] ASCII-only (no Unicode)
- [ ] Verse URLs correct and clickable
- [ ] Total question count: 33
- [ ] Purport ratio: ~24% (8/33) minimum achieved

---

## Automation Opportunities

### Semi-Automated Approach (Recommended)
1. **AI-assisted generation**: Use Claude/GPT to draft questions based on purport analysis
2. **Human verification**: Check each question against actual Vedabase content
3. **Batch processing**: Generate 3 chapters at a time, review, commit
4. **Template reuse**: Use Chapter 1 questions as quality examples

### Tools Needed
- Python script to insert questions into JSON at specific positions
- Verification script to check purport ratio per chapter
- Automated verse URL validation

---

## Quality Benchmarks (Based on Chapter 1)

### Excellent Purport Question Characteristics
1. **Contrastive reasoning**: "Why this matters" section explaining false paths
2. **Psychological depth**: Addresses inner motivations, not just external actions
3. **Authority citation**: "Srila Prabhupada explains/warns/reveals"
4. **Practical application**: Shows how misunderstanding affects spiritual life

### Example from Chapter 1 (bg1-q8):
```
Prompt: "In the purport to BG 1.10, Srila Prabhupada explains Duryodhana's 
assessment of military strength. What psychological trap does Duryodhana fall into?"

Feedback: "Srila Prabhupada explains that Duryodhana focused on measurable 
military assets while remaining blind to the crucial factor: Krsna's presence 
with the Pandavas... This is the materialist's trap - calculating only what 
can be counted while dismissing divine intervention. Why this matters: Modern 
people similarly rely on quantifiable resources... while neglecting spiritual 
strength."
```

---

## Progress Tracking

### Completion Checklist

**Tier 1 (Critical):**
- [ ] Chapter 2 Adult (33Q) - Priority 1
- [ ] Chapter 3 Adult (33Q) - Priority 2  
- [ ] Chapter 4 Adult (33Q) - Priority 3

**Tier 2 (Major):**
- [ ] Chapter 6 Adult (33Q)
- [ ] Chapter 7 Adult (33Q)
- [ ] Chapter 9 Adult (33Q)
- [ ] Chapter 12 Adult (33Q)
- [ ] Chapter 18 Adult (33Q)

**Tier 3 (Supporting):**
- [ ] Chapter 5 Adult (33Q)
- [ ] Chapter 8 Adult (33Q)
- [ ] Chapter 10 Adult (33Q)
- [ ] Chapter 11 Adult (33Q)
- [ ] Chapter 13 Adult (33Q)
- [ ] Chapter 14 Adult (33Q)
- [ ] Chapter 15 Adult (33Q)
- [ ] Chapter 16 Adult (33Q)
- [ ] Chapter 17 Adult (33Q)

---

## Git Workflow

### Commit Strategy
**After each chapter completion:**
```bash
git add data/quizzes/bg/[chapter]-adult.json
git commit -m "Add purport questions to BG Ch[X] Adult (25→33Q)

- Added 8 purport-critical questions focusing on [theme]
- Questions target false paths: [specific warnings]
- Achieves 35%+ purport ratio per Tier 2 standards
- Maintains difficulty progression and pedagogical flow"
git push
```

**After each tier completion:**
```bash
git commit -m "Complete Tier [1/2/3] BG purport enhancement

Chapters [X-Y] Adult quizzes now meet Tier 2 standards:
- [N] chapters × 8 purport questions = [N×8] new questions
- All chapters achieve 35-40% purport ratio
- Focus areas: [list key themes/warnings addressed]"
```

---

## Risk Mitigation

### Common Pitfalls to Avoid
1. **Mechanical question generation**: Each question must genuinely reflect purport content
2. **Speculation**: Only use what Prabhupada explicitly states
3. **Repetition**: Avoid duplicate themes across chapters
4. **End-loading**: Distribute purport questions throughout, not just at end
5. **ASCII violations**: Double-check for smart quotes after generation

### Quality Assurance
- Verify every question against actual Vedabase.io purport text
- Test distractors for plausibility (would a sincere student pick them?)
- Check that feedback explains contrastively (why wrong answers fail)
- Ensure "Why this matters" appears in 40% of purport questions

---

## Resource Requirements

### Time Investment
- **Total**: 68-102 hours for 17 chapters
- **Per chapter**: 4-6 hours (prep, generation, integration, QA)
- **Recommended pace**: 2-3 chapters per week to maintain quality

### Human Review Essential
- AI can draft questions, but human verification against Vedabase is mandatory
- Every feedback statement must be traceable to specific purport text
- No substitution for careful reading of Prabhupada's words

---

## Success Metrics

### Tier 2 Compliance Achieved When:
- [ ] All 17 chapters have 33 questions (25 original + 8 purport)
- [ ] Each chapter shows 35-40% purport ratio (8-10 questions minimum)
- [ ] All purport questions cite purport explicitly in prompt or feedback
- [ ] Feedback quality matches Chapter 1 benchmark (3-5 sentences, contrastive)
- [ ] No Tier 1 violations remain (ASCII-only, correct structure)

### Tier 3 Gold Standard Achieved When:
- [ ] Questions provoke reflection, not just memorization
- [ ] Distractors reflect partial truths and common devotional misunderstandings
- [ ] Each chapter ends on insight/integration (not trivial fact)
- [ ] Overall quiz flow feels like guided study session

---

## Next Immediate Action

**Start with Chapter 2** (most critical):
1. Read BG Chapter 2 purports on Vedabase.io
2. Identify 8 verses with warnings about false paths (likely: 2.11-13 [body vs soul], 2.29 [amazement at soul], 2.42-43 [flowery language of Vedas], 2.62-63 [sense gratification downfall])
3. Generate 8 questions using Chapter 1 as template
4. Integrate into existing 25-question structure
5. Commit: "Add purport questions to BG Ch2 Adult (25→33Q)"

**Estimated completion of Tier 1 (Ch 2-4)**: 1-2 weeks at 2-3 hours per day
