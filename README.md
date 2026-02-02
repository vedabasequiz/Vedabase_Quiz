# Vedabase Quiz (JS-only)

This is a JavaScript-only Next.js (App Router) project for hosting self-study quizzes.

## Deploy on Vercel (recommended)

1. Create a new GitHub repository (e.g., `VedabaseQuiz`).
2. Upload **all files/folders in this project** to the repo root (so `package.json` is in the root).
3. In Vercel: **Add New Project** -> Import your GitHub repo -> **Deploy**.

### Important Vercel settings
- **Framework preset**: Next.js (auto-detected)
- **Root Directory**: leave blank (repo root)

## Run locally (optional)

```bash
npm install
npm run dev
```

## Where quizzes live

Quiz JSON files are in:
- `data/quizzes/bg/...`
- `data/quizzes/sb/...`

Each quiz page is served at:
- `/quiz/<slug>/`


## ✅ Quiz Quality Standards

## Kids Bhagavad Gita Quiz Standards (2026)

See: [KIDS_BG_QUIZ_STANDARDS_2026.md](KIDS_BG_QUIZ_STANDARDS_2026.md) for the full checklist, requirements, and examples for Kids quizzes (ages 8–12).

Key points:
- Audience field: "kids" in JSON
- Question count: 10 questions per chapter
- Source field: "translation" or "purport" only
- Simple, concrete language; positive tone; no abstract philosophy
- 1–2 purport questions max; rest translation/narrative
- ASCII-only, no smart quotes or Unicode dashes
- Feedback: 1–2 short, positive sentences

All validator scripts and editorial processes should align with these standards.

## Teen Bhagavad Gita Quiz Standards (2026)

### Tier 1: Hard Rules (Blocking)
These are non-negotiable. Any failure here blocks publishing.
- Audience field: "teens" in JSON
- Question count: 15 questions per chapter
- Sources: All verseUrl fields must point directly to Vedabase.io (no summaries, no third-party sites)
- Verdict handling: No "verdict" fields in JSON (UI-only)
- JSON validity: Valid JSON syntax, no trailing commas
- IDs: All question IDs must be unique

### Tier 2: Strong Constraints (Editorial)
These define quality and appropriateness for teens.
- Language & Tone: Clear, concrete, age-appropriate; no dense metaphysics, no adult lecture or sermon tone, avoid institutional/abstract phrasing
- Content Mix (Guideline): ~60% translation-based, ~40% purport-guided; up to ~45% purport-guided allowed only when chapter content supports it; >45% purport-guided requires explicit justification
- Chapter Flow: Questions should generally follow the order of the chapter; minor reordering is acceptable
- MCQ Quality: One clear correct answer, plausible distractors, no joke/trick/fake choices
- Feedback: 1–2 short sentences, guided reasoning, explain why the answer fits, no preaching/adult-centric commentary
- IDs: Sequential (bg1-q1, bg1-q2, … bg1-q15)

### Tier 3: Gold Standard Refinement (Polish)
These do not usually block publishing but define excellence.
- Technical & Formatting: ASCII-only, use - (hyphen) not – (Unicode dash), consistent verse label format (e.g., BG 1.7-1.8), verse labels should align with linked verse
- MCQ Craft: Balanced choice lengths, avoid “correct-is-longest” bias, no duplicate/near-duplicate questions
- Overall Quality: Reads naturally for teens, pedagogically strong, clearly distinct from Adult quizzes

### Editorial Intent
Teen quizzes are meant to:
- Build scriptural literacy
- Develop basic moral and psychological reasoning
- Help teens recognize emotional confusion, attachment vs duty, false renunciation (gently, without abstraction)
Teen quizzes are not meant to:
- Preach
- Overwhelm
- Function as simplified Adult philosophy quizzes

**One-line summary (locked):**
Teens = clarity before commentary, understanding before philosophy, guidance without preaching.

**Before committing any quiz changes, run comprehensive validation:**

```bash
python3 scripts/validate-all-standards.py data/quizzes/bg/[file].json
```

**To validate all BG quizzes:**

```bash
python3 scripts/validate-all-standards.py data/quizzes/bg/*.json
```

**Automated pre-commit hook** is installed at `.git/hooks/pre-commit` and will automatically validate quiz files on every commit.

### Documentation

- **[BG_COMPREHENSIVE_VALIDATION_WORKFLOW.md](BG_COMPREHENSIVE_VALIDATION_WORKFLOW.md)** - Complete validation checklist and workflow (START HERE)
- **[VEDABASE_BG_PUBLISH_CHECKLIST.md](VEDABASE_BG_PUBLISH_CHECKLIST.md)** - 3-tier governance standards (Tier 1/2/3)
- **[QUIZ_QUALITY_STANDARDS.md](QUIZ_QUALITY_STANDARDS.md)** - MCQ design guidelines (length balance, plausible distractors)
- **[BG_QUIZ_REVISION_TEMPLATE.md](BG_QUIZ_REVISION_TEMPLATE.md)** - Step-by-step revision process with fix strategies
- **[FAMILY_TESTING_GUIDE.md](FAMILY_TESTING_GUIDE.md)** - User testing protocol (3 tests)

### Validation Scripts

1. **`validate-all-standards.py`** - Comprehensive check (Tier 1/2/3 + quality)
2. **`validate-quiz-quality.py`** - Detailed per-question quality analysis
3. **`fix-unicode-bg.py`** - Automated Unicode → ASCII conversion


