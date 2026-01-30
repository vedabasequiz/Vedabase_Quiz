# Comprehensive Validation Workflow

## Overview

This document consolidates ALL validation checkpoints to ensure no standard is compromised during quiz creation or revision. Every quiz file must pass these checks before publication.

---

## 🎯 Quick Start

**Before committing any quiz changes:**

```bash
python3 scripts/validate-all-standards.py data/quizzes/bg/[file].json
```

**To validate all BG quizzes:**

```bash
python3 scripts/validate-all-standards.py data/quizzes/bg/*.json
```

**Automated pre-commit hook** is installed and will run automatically on `git commit`.

---

## 📋 Complete Validation Checklist

### TIER 1 - Hard Rules (Must Pass) ✅

These are **non-negotiable**. Any failure blocks publication.

#### 1. ASCII-Only Formatting
- ✅ No Unicode characters (curly quotes, em dashes, special symbols)
- ✅ Use ASCII equivalents: `"` instead of `"`, `--` instead of `—`, `'` instead of `'`
- **Script check:** `validate-all-standards.py` → "ASCII-only"
- **Manual check:** Search for non-ASCII: `grep -P "[^\x00-\x7F]" file.json`

#### 2. JSON Structure Integrity
- ✅ All required top-level fields present:
  - `id`, `scripture`, `chapter`, `audience`, `title`, `difficulty`, `publishedOn`, `questions`
- ✅ All question fields present:
  - `id`, `prompt`, `choices` (array of 4), `correctIndex` (0-3), `feedback`, `verseLabel`, `verseUrl`, `verdict`
- ✅ Valid JSON syntax (no trailing commas, proper escaping)
- **Script check:** `validate-all-standards.py` → "All top-level fields present"
- **Manual check:** `python3 -m json.tool file.json > /dev/null`

#### 3. Source Integrity
- ✅ **All verse URLs point to vedabase.io**
  - Format: `https://vedabase.io/en/library/bg/X/Y/`
  - No external sources allowed
- ✅ **All verse labels correctly formatted**
  - BG format: `BG X.Y` (e.g., "BG 1.1")
  - SB format: `SB X.Y.Z` (e.g., "SB 1.1.1")
- ✅ **All content from Srila Prabhupada's translations and purports only**
  - Feedback cites "Srila Prabhupada explains..."
  - No external commentaries or interpretations
- **Script check:** `validate-all-standards.py` → "All verse URLs point to vedabase.io"
- **Manual spot check:** Open 3-5 random verse URLs, verify they work and point to correct verses

#### 4. Verdict Assignment
- ✅ All questions have valid verdict: `"Correct"` or `"Review"`
- ✅ `"Correct"` = independently verified by review process
- ✅ `"Review"` = needs additional verification
- **Script check:** `validate-all-standards.py` → Validates verdict values

---

### TIER 2 - Strong Constraints ⚠️

These should be met. Violations require justification.

#### 5. MCQ Prompt Quality
- ✅ No ambiguous language:
  - Avoid: "most", "best", "primary", "mainly", "typically"
  - Use specific, verifiable questions
- ✅ Clear, grammatically correct prompts
- ✅ Questions test understanding, not memorization of exact words
- **Script check:** `validate-all-standards.py` → "MCQ prompts checked for ambiguous language"
- **Manual check:** Read 10 random prompts - are they clear and unambiguous?

#### 6. Purport Ratio
- ✅ **BG requirement: 35-40% purport questions**
  - Adult (25Q chapters): 9-10 purport questions
  - Adult (enhanced): 33Q = 11-13 purport questions
  - Teens (20Q): 7-8 purport questions
  - Kids (15Q): 5-6 purport questions
- ✅ **SB requirement: 25-35% purport questions**
- ✅ Label purport questions in `verseLabel` field (e.g., "BG 1.1 (purport)")
- **Script check:** `validate-all-standards.py` → "Purport ratio: X% (Y/Z)"
- **Manual count:** Count questions with "(purport)" in verseLabel, divide by total

---

### QUALITY STANDARDS 🌟

These ensure excellent user experience. Focus of quality revision process.

#### 7. Length Balance (30% Variance Rule)
- ✅ **Max word count ≤ 1.3x min word count per question**
- ✅ Example: If shortest choice = 6 words, longest ≤ 7.8 words (8 words rounded)
- ✅ Correct answer position randomized (not always longest or shortest)
- **Script check:** `validate-all-standards.py` → "Length balance: All X questions within 30% variance"
- **How to fix:**
  - **Expand short distractors:** Add context, qualifiers (6+ words minimum)
  - **Condense long correct answers:** Remove redundant words, tighten phrasing
  - See [BG_QUIZ_REVISION_TEMPLATE.md](BG_QUIZ_REVISION_TEMPLATE.md) Strategy A & B

#### 8. Distractor Plausibility
- ✅ **No obvious language:**
  - Avoid: "always", "never", "only", "all", "none", "completely", "totally"
  - These make distractors obviously wrong
- ✅ **No 1-3 word distractors** (too easy to eliminate)
- ✅ **Use partial truths** (scriptural facts from wrong context)
- ✅ **Maintain scriptural tone** (not absurd or joke answers)
- **Script check:** `validate-all-standards.py` → "Distractors: X% with minor issues"
- **Target:** ≤10% distractors with issues
- **Gold Standard Reference:** See [BG_DISTRACTOR_STYLE_GUIDE.md](BG_DISTRACTOR_STYLE_GUIDE.md) for comprehensive creation guidelines
- **How to fix:**
  - **Remove obvious language:** Replace with nuanced phrasing
  - **Expand short distractors:** Add scriptural context, qualifiers
  - See [BG_QUIZ_REVISION_TEMPLATE.md](BG_QUIZ_REVISION_TEMPLATE.md) Strategy A & C

#### 9. Correct-Is-Longest Pattern
- ✅ **Target: ≤70% correct-is-longest** (acceptable)
- ✅ **Ideal: ~25%** (random distribution)
- ✅ Prevents "pick longest answer" strategy
- **Script check:** `validate-all-standards.py` → "Correct-is-longest: X% (Y/Z)"
- **Red flag:** >80% indicates systematic bias
- **How to fix:** Apply Strategy B (condense correct answers) from template

#### 10. Cognitive Depth Distribution (NEW - Tier 3)
- ✅ **Recall Questions (40-50% target):** "What," "Who," "Which," "According to"
- ✅ **Analysis Questions (30-40% target):** "Why," "How," "What distinguishes," "What does Prabhupada warn"
- ✅ **Synthesis Questions (15-25% target):** "Compare," "How would this apply," "What connects," "Relate X to Y"
- **Script check:** `validate-all-standards.py` → "Cognitive distribution: X% recall, Y% analysis, Z% synthesis"
- **Status:** Tier 3 (excellence metric, not blocking)
- **Purpose:** Ensures questions provoke reflection, not just memorization
- **How to enhance:**
  - Convert simple "what" questions to "why" or "how" where possible
  - Add 2-3 synthesis questions per chapter (last 40%)
  - Ensure purport questions require reasoning, not just recall

#### 11. Difficulty Progression (NEW - Tier 3)
- ✅ **First 15 questions (60%):** Accessible, grounding (mostly recall/comprehension)
- ✅ **Last 10 questions (40%):** Moderately harder, integrative (analysis/synthesis)
- ✅ **Final 3-5 questions:** Emphasis on warnings, integration, philosophical contrasts
- **Script check:** Analyze question complexity by position
- **Status:** Tier 3 (quality indicator)
- **Purpose:** Aligns with Tier 2 requirement (Section 8: Difficulty Progression)
- **How to improve:**
  - Move complex questions to later positions
  - Ensure last questions require multi-step reasoning
  - End with insight, caution, or integration (not trivial facts)

#### 12. Distractor Philosophy Depth (NEW - Tier 3)
- ✅ **Philosophical misunderstandings:** Mayavadi, impersonalist, karma-mimamsa positions
- ✅ **Partial truths:** Correct in isolation but wrong in context
- ✅ **Misplaced emphasis:** True fact but irrelevant to question focus
- **Script check:** Flag generic errors vs philosophical position errors
- **Target:** 50%+ distractors referencing specific philosophical errors
- **Status:** Tier 3 (excellence metric)
- **Gold Standard Reference:** See [BG_DISTRACTOR_STYLE_GUIDE.md](BG_DISTRACTOR_STYLE_GUIDE.md) for:
  - 6 approved distractor categories (partial truth, bodily identification, false renunciation, material calculation, moralism, misapplied scripture)
  - 4 forbidden types (academic labels, silly options, absolutist strawmen, vague statements)
  - Chapter-specific emphasis patterns (BG 1-18)
- **Purpose:** Makes wrong answers instructive about common deviations
- **How to enhance:**
  - Replace generic wrong answers with specific philosophical errors
  - Reference Mayavadi oneness, impersonalist void, karma-kanda rituals
  - Use Prabhupada's purport warnings as distractor sources

---

## 🔄 Validation Workflow

### During Quiz Creation

1. **Draft questions** using scriptural content
2. **Apply quality standards** from start:
   - Balance word counts as you write
   - Use plausible distractors (partial truths)
   - Avoid obvious language
3. **Run validation:**
   ```bash
   python3 scripts/validate-all-standards.py data/quizzes/bg/[chapter]-adult.json
   ```
4. **Fix any issues** before proceeding
5. **Commit when passes:**
   ```bash
   git add data/quizzes/bg/[chapter]-adult.json
   git commit -m "Add BG Chapter X adult quiz - all standards met"
   ```

### During Quiz Revision

1. **Run validation to identify issues:**
   ```bash
   python3 scripts/validate-quiz-quality.py data/quizzes/bg/[chapter]-adult.json --detailed
   ```
2. **Follow [BG_QUIZ_REVISION_TEMPLATE.md](BG_QUIZ_REVISION_TEMPLATE.md):**
   - Pre-revision checklist
   - Categorize problems by fix strategy
   - Revise systematically (6-7 min per question)
3. **Re-validate after revision:**
   ```bash
   python3 scripts/validate-all-standards.py data/quizzes/bg/[chapter]-adult.json
   ```
4. **Must show:**
   - ✅ All Tier 1 checks pass (hard rules)
   - ✅ All Tier 2 checks pass or acceptable warnings
   - ✅ Quality metrics improved (target: 100% pass rate)
5. **Commit only when validated:**
   ```bash
   git add data/quizzes/bg/[chapter]-adult.json
   git commit -m "Revise BG Chapter X - quality standards met (100% pass rate)"
   ```

### Before Publication

1. **Run comprehensive validation on all files:**
   ```bash
   python3 scripts/validate-all-standards.py data/quizzes/bg/*.json
   ```
2. **Family testing** (see [FAMILY_TESTING_GUIDE.md](FAMILY_TESTING_GUIDE.md)):
   - Test 1: Length pattern elimination (wife picks longest)
   - Test 2: Distractor plausibility (daughter identifies obvious wrongs)
   - Test 3: Normal experience (both take after reading chapter)
3. **Manual spot checks:**
   - Open 5 random verse URLs → verify they work
   - Read 10 random questions → check clarity and tone
   - Check publishedOn dates → ensure accurate
4. **Document results** in commit message

---

## 🚨 Pre-Commit Hook (Automated)

A pre-commit hook is installed at `.git/hooks/pre-commit` that automatically runs validation on quiz files.

### How It Works

1. You make changes to quiz files
2. Stage changes: `git add data/quizzes/bg/1-adult.json`
3. Attempt commit: `git commit -m "Update BG Chapter 1"`
4. **Hook automatically runs** `validate-all-standards.py` on staged quiz files
5. **If validation passes:** Commit succeeds ✅
6. **If validation fails:** Commit blocked ❌ with error details

### Example Output

```bash
$ git commit -m "Update BG Chapter 1"

🔍 Running comprehensive validation on quiz files...
Found quiz files to validate:
  - data/quizzes/bg/1-adult.json

======================================================================
                       Validating: 1-adult.json                       
======================================================================

TIER 1 - Hard Rules (Must Pass)
✅ ASCII-only (no Unicode characters)
✅ All top-level fields present
✅ Question count: 33 (enhanced)
✅ All verse URLs point to vedabase.io
✅ All verse labels correctly formatted

TIER 2 - Strong Constraints
✅ MCQ prompts checked for ambiguous language
⚠️  Purport ratio: 33.3% (11/33) - Below target 35-40%

Quality Standards
✅ Length balance: All 33 questions within 30% variance
✅ Distractors: 3.0% with minor issues (3/99)
✅ Correct-is-longest: 63.6% (21/33) - Acceptable

⚠️  QUIZ PASSES with warnings - Review recommended

✅ All quiz files passed validation
✅ Commit allowed
[main abc123] Update BG Chapter 1
```

### If Validation Fails

```bash
$ git commit -m "Update BG Chapter 2"

🔍 Running comprehensive validation on quiz files...
Found quiz files to validate:
  - data/quizzes/bg/2-adult.json

❌ ERROR: Found 12 Unicode characters in file
❌ ERROR: Purport ratio: 8.0% (2/25) - Below target 35-40%
❌ ERROR: Correct-is-longest: 96.0% (24/25) - Above threshold 70%

❌ QUIZ FAILS validation

❌ Validation failed - commit blocked

To fix:
  1. Review errors above
  2. Fix issues in quiz files
  3. Re-stage files: git add data/quizzes/bg/2-adult.json
  4. Try commit again

To bypass (NOT RECOMMENDED):
  git commit --no-verify
```

### Bypassing the Hook (Emergency Only)

```bash
git commit --no-verify -m "WIP: incomplete work"
```

**⚠️ WARNING:** Only bypass for work-in-progress commits. Never bypass for production/main branch commits.

---

## 📊 Validation Scripts Reference

### 1. `validate-all-standards.py` (Comprehensive)

**Purpose:** Single script checking ALL Tier 1, 2, 3, and quality standards.

**Usage:**

```bash
# Single file
python3 scripts/validate-all-standards.py data/quizzes/bg/1-adult.json

# Multiple files
python3 scripts/validate-all-standards.py data/quizzes/bg/1-adult.json data/quizzes/bg/2-adult.json

# All BG quizzes
python3 scripts/validate-all-standards.py data/quizzes/bg/*.json

# Strict mode (treat warnings as errors)
python3 scripts/validate-all-standards.py data/quizzes/bg/1-adult.json --strict
```

**Checks:**
- ✅ Tier 1: ASCII-only, JSON structure, source integrity
- ✅ Tier 2: MCQ quality, purport ratio
- ✅ Quality: Length balance, distractor plausibility, correct-is-longest

**Output:** Color-coded (RED=error, YELLOW=warning, GREEN=pass)

**Exit codes:** 0 (pass), 1 (fail) - CI/CD friendly

### 2. `validate-quiz-quality.py` (Detailed Quality Analysis)

**Purpose:** Deep dive into specific quality issues with per-question details.

**Usage:**

```bash
# Detailed per-question analysis
python3 scripts/validate-quiz-quality.py data/quizzes/bg/1-adult.json --detailed

# Directory (all files)
python3 scripts/validate-quiz-quality.py data/quizzes/bg/ --detailed
```

**Output:**
- Per-question length analysis (variance, word counts)
- Per-question distractor issues (obvious language, short distractors)
- Correct-is-longest pattern tracking
- Overall statistics

**Use when:** Identifying specific questions needing revision during quality improvement process.

### 3. `fix-unicode-bg.py` (Automated Tier 1 Fix)

**Purpose:** Automatically converts Unicode to ASCII.

**Usage:**

```bash
# Single file
python3 scripts/fix-unicode-bg.py data/quizzes/bg/1-adult.json

# All BG quizzes
python3 scripts/fix-unicode-bg.py data/quizzes/bg/*.json
```

**Creates:** `.backup` files before modifying

**Conversions:**
- `"` → `"`
- `'` → `'`
- `—` → `--`
- And all other Unicode → ASCII equivalents

---

## 🎓 Integration with Existing Documents

This workflow consolidates and integrates:

1. **[VEDABASE_BG_PUBLISH_CHECKLIST.md](VEDABASE_BG_PUBLISH_CHECKLIST.md)**
   - Tier 1, 2, 3 governance structure
   - Publication requirements
   - → Script checks: `validate-all-standards.py`

2. **[QUIZ_QUALITY_STANDARDS.md](QUIZ_QUALITY_STANDARDS.md)**
   - Length balance rules (30% variance)
   - Plausible distractor guidelines
   - Design patterns and examples
   - → Script checks: `validate-all-standards.py` + `validate-quiz-quality.py`

3. **[BG_QUIZ_REVISION_TEMPLATE.md](BG_QUIZ_REVISION_TEMPLATE.md)**
   - Step-by-step revision process
   - 4 fix strategies (A/B/C/D)
   - Batch workflow for chapters 2-18
   - → Manual process guided by script output

4. **[FAMILY_TESTING_GUIDE.md](FAMILY_TESTING_GUIDE.md)**
   - Human validation of quality improvements
   - 3 test protocol (length pattern, distractor plausibility, normal experience)
   - → Complements automated validation

5. **[BG_PURPORT_ENHANCEMENT_PLAN.md](BG_PURPORT_ENHANCEMENT_PLAN.md)**
   - Systematic purport question addition
   - Target ratios per audience
   - → Tier 2 requirement checked by script

---

## 📈 Success Metrics

### Per Quiz File

✅ **PASS** requires:
- Tier 1: 100% compliance (all checks pass)
- Tier 2: 100% compliance or justified exceptions
- Quality: ≥90% questions pass length + distractor checks
- Correct-is-longest: ≤70%

🌟 **EXCELLENT** achieves:
- All PASS requirements +
- Quality: 100% questions pass all checks
- Correct-is-longest: ≤60% (approaching random 25%)
- Purport ratio: Within 35-40% target (BG)
- Family testing: All 3 tests pass

### Across All BG Quizzes

Current status (after Chapter 1 revision):
- ✅ Tier 1: 22/22 files pass (100%)
- 🔄 Quality: 1/22 files pass (Chapter 1 only)
- 🎯 Target: 22/22 files pass all standards

Progress tracking:
```bash
# Run on all files, count passes
python3 scripts/validate-all-standards.py data/quizzes/bg/*.json 2>&1 | grep "PASSES"
```

---

## 🔧 Troubleshooting

### "Pre-commit hook not running"

```bash
# Check if hook is executable
ls -l .git/hooks/pre-commit

# If not executable:
chmod +x .git/hooks/pre-commit
```

### "Validation script not found"

```bash
# Ensure you're in workspace root
pwd
# Should show: /Users/prakashchincholikar/Vedabase_Quiz

# Check script exists
ls -l scripts/validate-all-standards.py

# Make executable if needed
chmod +x scripts/validate-all-standards.py
```

### "Unicode errors after using fix-unicode-bg.py"

```bash
# Check if actually fixed
grep -P "[^\x00-\x7F]" data/quizzes/bg/1-adult.json

# If still has Unicode, may need manual fix
# Common culprits: apostrophes in names, quotes in feedback
```

### "Purport ratio slightly below target"

This may be acceptable if:
- Chapter 1 enhanced: 33.3% (11/33) is only 1.7% below 35%
- Standard chapters: 36% (9/25) is within 35-40% range
- Can add 1 more purport question to reach target if needed

### "Correct-is-longest above 70%"

This is the main focus of quality revision:
1. Run detailed analysis:
   ```bash
   python3 scripts/validate-quiz-quality.py file.json --detailed
   ```
2. Identify questions where correct is longest
3. Apply Strategy B from [BG_QUIZ_REVISION_TEMPLATE.md](BG_QUIZ_REVISION_TEMPLATE.md):
   - Condense correct answer
   - Remove redundant words
   - Tighten phrasing
4. Re-validate

---

## 📅 Workflow Timeline

### For New Quiz Creation (e.g., BG Chapter 19)

1. **Research & Draft** (2-3 hours)
   - Read chapter, purport
   - Draft 25 questions (9-10 purport)
2. **Apply quality standards** (30 min)
   - Balance word counts
   - Use plausible distractors
3. **Validate** (5 min)
   - Run `validate-all-standards.py`
4. **Fix & re-validate** (15-30 min)
5. **Commit** (5 min)
6. **Total: 3-4 hours**

### For Quiz Revision (e.g., BG Chapter 2)

1. **Pre-revision validation** (5 min)
   - Identify problem questions
2. **Systematic revision** (2-3 hours)
   - Follow [BG_QUIZ_REVISION_TEMPLATE.md](BG_QUIZ_REVISION_TEMPLATE.md)
   - 6-7 min per question × 25 questions
3. **Post-revision validation** (5 min)
4. **Commit** (5 min)
5. **Total: 3-4 hours per chapter**

### For Batch Revision (Chapters 2-18)

- 17 chapters × 3-4 hours = **51-68 hours**
- At 2 chapters/week = **8-9 weeks**
- At 1 chapter/day (sprints) = **3-4 weeks**

---

## ✅ Final Checklist Before Publication

- [ ] All quiz files pass `validate-all-standards.py`
- [ ] Tier 1 compliance: 100% (no exceptions)
- [ ] Tier 2 compliance: 100% or documented exceptions
- [ ] Quality metrics meet targets (length, distractors, patterns)
- [ ] Family testing completed and passed (all 3 tests)
- [ ] Manual spot checks completed (URLs, tone, clarity)
- [ ] publishedOn dates accurate
- [ ] Committed to git with descriptive messages
- [ ] Deployed to production
- [ ] Post-deployment spot check (sample quiz URLs work)

---

## 📞 Support

**For validation issues:**
1. Read error messages carefully (script provides specific guidance)
2. Consult relevant standards document:
   - Tier 1 issues → [VEDABASE_BG_PUBLISH_CHECKLIST.md](VEDABASE_BG_PUBLISH_CHECKLIST.md)
   - Quality issues → [QUIZ_QUALITY_STANDARDS.md](QUIZ_QUALITY_STANDARDS.md)
   - Revision help → [BG_QUIZ_REVISION_TEMPLATE.md](BG_QUIZ_REVISION_TEMPLATE.md)
3. Check "Troubleshooting" section above
4. Run detailed analysis: `validate-quiz-quality.py --detailed`

**For urgent exceptions:**
- Document in commit message why standard cannot be met
- Get approval before bypassing pre-commit hook
- Add TODO to revisit issue later

---

## 🎯 Summary

**One command to rule them all:**

```bash
python3 scripts/validate-all-standards.py data/quizzes/bg/*.json
```

**Automated protection:**
- Pre-commit hook blocks bad commits
- No manual checklist needed
- All standards checked every time

**Clear feedback:**
- Color-coded output
- Specific error messages
- Actionable fix guidance

**Comprehensive coverage:**
- Tier 1: Hard rules (ASCII, structure, source)
- Tier 2: Strong constraints (MCQ, purport)
- Quality: User experience (length, distractors, patterns)

**Result:** High-quality quizzes that meet all standards, every time. 🎉
