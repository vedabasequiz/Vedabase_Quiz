# Kids Bhagavad Gita Quiz Standards Checklist (2026)

Audience: Kids (ages 8–12)
Purpose: Build understanding, confidence, and love for the Gita through clear stories and simple truths — not testing philosophical reasoning.

---

## Tier 1: Hard Rules (Blocking)
If any item fails, the quiz is not publishable.

### Structure & Metadata
- audience is exactly "kids"
- Total questions = 10
- JSON is valid (no trailing commas, correct syntax)
- Question IDs are unique and sequential
  - Format: bgX-q1 … bgX-q10

### Content Integrity
- Every question includes:
  - prompt
  - choices
  - correctIndex
  - feedback
  - verseUrl
  - source
- All verseUrl links point directly to vedabase.io
- No UI-only fields (no verdict, no scoring metadata)

### ASCII-Only Requirement
- ASCII characters only
- No smart quotes (’ “ ”)
- No Unicode dashes (–, —)
- Use standard ASCII (', ", -)

### Source Tagging (Required)
- Every question includes a source field
- Allowed values only: "translation", "purport"

---

## Tier 2: Editorial & Pedagogical Rules (Strict)
These rules protect child comprehension and tone. Violations require revision before publish.

### Language & Tone
- Simple, concrete language
- Short sentences
- Positive, encouraging tone
- No abstract philosophy
- No adult lecture style
- No negative or trick phrasing


### Content Mix
- Target mix: ~80% translation / narrative, ~20% purport-based
- Maximum 1–2 purport questions per quiz
- **Purport ratio is advisory for kids quizzes. It is not a Tier 1 (blocking) requirement. Quizzes with 0–2 purport questions may still be published if all other standards are met.**

### Purport Question Rules (Kids-Specific)
Purport questions must be:
- Explicit and surface-level
- Simple cause–effect only
- Directly stated in the purport

❌ Not allowed for Kids:
- Hidden reasoning
- Psychological analysis
- “What does this show about…”
- “Why is this dangerous…”
- Multi-step inference

### Chapter Flow
- Questions broadly follow chapter order
- Story progression is clear
- Quiz ends on clarity or reassurance (not confusion or tension)

---

## Tier 3: Light Technical & MCQ Quality (Advisory)
These are human-reviewed sanity checks, not heavy validator enforcement.

### MCQ Quality
- One clearly correct answer per question
- Distractors are reasonable, not silly or joke options
- No intentionally misleading choices

### Option Length (Light Guidance)
- Avoid 1-word distractors when possible
- Avoid one option being dramatically longer than others
- Parallel phrasing preferred, but clarity always wins
- ⚠️ No length-balance percentages
- ⚠️ No correct-is-longest thresholds
- ⚠️ No variance math for Kids

### Feedback Rules (Very Important)
- 1–2 short sentences only
- Positive and reassuring
- Explains the answer simply
- No comparison of wrong options
- No moral pressure or fear-based framing

Example (good):
“Arjuna feels sad because he sees his family on both sides. This shows he has a kind heart.”

Example (not allowed):
“This reflects bodily identification and confusion about dharma.”

---

## Final Sanity Check (Before Publish)
- Re-scan text for Unicode characters
- Read aloud 2 random questions — does a 9-year-old understand them?
- Confirm purport questions are explicit, not disguised reasoning
- Confirm quiz ends on a calm, clear note

---

## Definition of “Publish-Ready” (Kids)
A Kids BG quiz is publish-ready only if:
- Tier 1 is 100% PASS
- Tier 2 is fully compliant
- Tier 3 has no issues that reduce clarity or confidence

---

## Guiding Principle (Lock This)
Kids quizzes teach understanding, not evaluation.
If a child feels confused or tested, the quiz has failed — even if it is technically correct.
