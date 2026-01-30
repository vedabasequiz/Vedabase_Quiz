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

- Deployment trigger


