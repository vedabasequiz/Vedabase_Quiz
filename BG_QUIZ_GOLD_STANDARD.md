# Gold-Standard Quiz Creation & Validation Standards (Bhagavad Gita)

## 1. Content Quality (Gold-Standard Rubric)
- **Purport Integration:** At least 35–40% of questions must be purport-based (not just literal verse recall). Synthesis, application, and deep understanding are required.
- **MCQ Plausibility:** All distractors (wrong choices) must be plausible, non-trivial, and free from obvious giveaways or joke answers.
- **Feedback Depth:** Each question must have feedback that:
  - Explains why the correct answer is right (with purport insight if possible)
  - Explains why the wrong answers are wrong (exposing common misconceptions)
  - Offers a practical takeaway or application ("Practice" line)
- **Synthesis:** At least one question per quiz must synthesize across multiple verses or themes (not just single-verse recall).
- **No Verdict Logic:** No questions or feedback should contain verdicts ("You are right/wrong", "Correct/Incorrect", etc.).
- **No Unicode:** All content must be ASCII-only (no Unicode dashes, smart quotes, etc.).
- **No Copy-Paste from Source:** All prompts, choices, and feedback must be original, not verbatim from Vedabase or other sources.

## 2. Technical & Formatting Standards
- **JSON Structure:**
  - Each question: `id`, `prompt`, `choices`, `correctIndex`, `feedback`, `verseLabel`, `verseUrl`.
  - No extra fields or missing required fields.
- **Validator Compliance:**
  - Must pass all checks in `scripts/validate-all-standards.py` and `scripts/mcq_distractor_checker.py`.
  - If validator flags a false negative (e.g., purport ratio), manual audit and documentation are required.
- **ASCII Only:**
  - No Unicode characters (em dashes, curly quotes, etc.).
  - Use plain hyphens, straight quotes, etc.
- **Length & Difficulty:**
  - 25 questions per chapter (unless otherwise specified).
  - Mix of easy, medium, and hard questions; avoid clustering all hard or all easy.
- **No Redundancy:**
  - No duplicate questions, prompts, or feedback.

## 3. Review & Audit Process
- **Manual Rubric Check:**
  - Each quiz must be manually checked against this rubric before finalization.
- **Validator Run:**
  - Run all validator scripts and address all errors/warnings (except known false negatives, which must be documented).
- **Git Commit:**
  - Only gold-standard, validator-passing files are committed and pushed.
- **Documentation:**
  - Any exceptions (e.g., validator false negatives) must be noted in the commit message or a separate audit file.

## 4. Example (Question Structure)
```json
{
  "id": "bg9-q1",
  "prompt": "In BG 9.1, why does Krishna say He will reveal the most confidential knowledge to Arjuna?",
  "choices": [
    "Because Arjuna is learned in ritual and deserves heavenly rewards",
    "Because Arjuna is non-envious and receptive, so he can understand and be freed from miseries",
    "Because Arjuna has mastered impersonal meditation and is ready to merge into Brahman",
    "Because Arjuna asked for secret mantras to defeat his enemies"
  ],
  "correctIndex": 1,
  "feedback": "Krishna highlights Arjuna's non-envious disposition as the qualification to receive confidential knowledge. The false path is thinking spiritual truth is earned mainly by status, technique, or secret formulas. Real understanding: receptivity and sincere submission open the heart to realized knowledge that frees one from misery. Practice: guard against envy and cultivate a teachable, devotional mood.",
  "verseLabel": "BG 9.1",
  "verseUrl": "https://vedabase.io/en/library/bg/9/1/"
}
```

---

**This file must be updated if standards evolve or new validator requirements are added.**
