# Teen Bhagavad Gita Quiz Standards (2026)

## Tier 1: Hard Rules (Blocking)
These are non-negotiable. Any failure here blocks publishing.
- Audience field: "teens" in JSON
- Question count: 15 questions per chapter
- Sources: All verseUrl fields must point directly to Vedabase.io (no summaries, no third-party sites)
- Verdict handling: No "verdict" fields in JSON (UI-only)
- JSON validity: Valid JSON syntax, no trailing commas
- IDs: All question IDs must be unique

## Tier 2: Strong Constraints (Editorial)
These define quality and appropriateness for teens.
- Language & Tone: Clear, concrete, age-appropriate; no dense metaphysics, no adult lecture or sermon tone, avoid institutional/abstract phrasing
- Content Mix (Guideline): ~60% translation-based, ~40% purport-guided; up to ~45% purport-guided allowed only when chapter content supports it; >45% purport-guided requires explicit justification
- Chapter Flow: Questions should generally follow the order of the chapter; minor reordering is acceptable
- MCQ Quality: One clear correct answer, plausible distractors, no joke/trick/fake choices
- Feedback: 1–2 short sentences, guided reasoning, explain why the answer fits, no preaching/adult-centric commentary
- IDs: Sequential (bg1-q1, bg1-q2, … bg1-q15)

## Tier 3: Gold Standard Refinement (Polish)
These do not usually block publishing but define excellence.
- Technical & Formatting: ASCII-only, use - (hyphen) not – (Unicode dash), consistent verse label format (e.g., BG 1.7-1.8), verse labels should align with linked verse
- MCQ Craft: Balanced choice lengths, avoid “correct-is-longest” bias, no duplicate/near-duplicate questions
- Overall Quality: Reads naturally for teens, pedagogically strong, clearly distinct from Adult quizzes

## Editorial Intent
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

---

**For all quiz editors, validators, and reviewers:**
- Use this document as the definitive reference for Teen BG quiz creation and review.
- All scripts and editorial processes should align with these standards.
- Communicate any updates or clarifications to the team.
