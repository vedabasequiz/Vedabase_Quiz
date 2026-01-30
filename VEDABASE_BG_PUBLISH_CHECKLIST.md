Vedabase Quiz – Final Pre-Publish Checklist

(3-Tier Governance Model)

🔒 TIER 1 — HARD RULES

Non-negotiable. Any violation = automatic rejection.

These protect truth, trust, and scriptural integrity.

1. Source Integrity (Absolute)

☐ All content sourced only from Vedabase.io

☐ Translations and purports by Srila Prabhupada only

☐ No speculative interpretation, paraphrasing, or external commentary

☐ Questions and correct answers verified against exact verse and/or purport

☐ Verse numbers and links are accurate and clickable

2. Structural Integrity

☐ Correct question count:

Adults: 25

Teens: 15

Kids: 10

☐ Correct scripture and chapter (BG / SB, chapter/canto correct)

☐ Correct audience tag (adult / teens / kids)

☐ Quiz follows chapter flow (no random ordering)

3. Platform & Delivery

☐ Website-ready JSON only (Vedabase Quiz website)

☐ No Google Forms, PDFs, or external platforms

☐ Compatible with existing QuizClient structure

☐ Slug, routing, and availability keys correct

4. Formatting & Encoding

☐ ASCII-only text (no Unicode, no smart quotes)

☐ Plain, readable English

☐ No Sanskrit diacritics unless already present in Vedabase translation

5. Feedback & Scoring Logic

☐ Every question has feedback

☐ Feedback verdict uses only:

“Correct”

“Review”

☐ Feedback verdict matches user’s answer (no mismatches)

☐ Verse link present in feedback

⚖️ TIER 2 — STRONG CONSTRAINTS

Must be fixed before publish. No release until resolved.

These protect learning quality and user clarity.

6. MCQ Quality

☐ Exactly one unambiguously correct answer

☐ Distractors are:

Plausible

Conceptually distinct

Based on common misunderstandings (not silly or irrelevant)

☐ No trick questions

☐ No “all of the above / none of the above”
**Reference:** See audience-specific distractor guides:
- Adults: [BG_DISTRACTOR_STYLE_GUIDE.md](BG_DISTRACTOR_STYLE_GUIDE.md)
- Teens: [BG_DISTRACTOR_STYLE_GUIDE_TEENS.md](BG_DISTRACTOR_STYLE_GUIDE_TEENS.md)
- Kids: [BG_DISTRACTOR_STYLE_GUIDE_KIDS.md](BG_DISTRACTOR_STYLE_GUIDE_KIDS.md)
7. Translation vs Purport Balance

☐ Overall mix respects locked ratio:

~60–65% translation-anchored

~35–40% purport-critical

☐ Purport-based questions emphasize:

False paths

Psychological traps

Misinterpretations warned against by Srila Prabhupada

8. Difficulty Progression

☐ First ~60%: accessible, grounding questions

☐ Last ~40%: moderately harder, integrative

☐ Final section includes synthesis / warning / reflection questions (Adults & Teens)

9. Feedback Quality

✅ Global Feedback Rules (ALL quizzes, ALL ages)

Every question's feedback must include all three elements, in this order:

1. Verdict label

☐ Use only: "Correct" or "Review"

❌ Never use "Wrong", "Incorrect", or similar

2. Reasoned explanation

☐ Must align with the intent of the verse and/or purport

☐ Explanation quality scales by age group (see below)

3. Mandatory verse link

☐ A direct clickable link to the exact verse page on vedabase.io

❌ No generic chapter links, no homepage links

🎓 Adult Feedback Requirements

☐ Length: 2-5 sentences per question

☐ Contrastive and purport-driven

☐ Explicitly warn against false paths, such as:

Doership illusion

False renunciation

Mundane or speculative interpretation

Attachment disguised as duty

☐ Explain why wrong options fail, not just why the correct one works

☐ Emphasize psychological and philosophical consequences of misunderstanding

☐ Optional: In 2-5 questions per quiz, include "Why this matters" (practical/philosophical consequence)

☐ **Adult quizzes must not frame bhakti as sentimental or isolated devotion; bhakti must be grounded in philosophical reasoning, contrastive analysis, and purport-supported epistemology**

🧑‍🎓 Teen Feedback Requirements

☐ Length: 2-3 sentences

☐ Guided reasoning, one-step logic

☐ May briefly explain why one distractor fails

❌ No dense metaphysics

❌ No abstract Sanskrit philosophy

🧒 Kids Feedback Requirements

☐ Length: 1-2 short, positive sentences

☐ Concrete, cause-effect explanation only

❌ No option comparison

❌ No abstract or philosophical terms

☐ References mainly appear in feedback, not the prompt

🚫 Explicitly Forbidden Across ALL Feedback

❌ Using "Wrong" instead of "Review"

❌ Vague affirmations ("This is correct because Krishna says so")

❌ Feedback that merely restates the question

❌ Missing vedabase.io verse links

❌ Neutral explanations that fail to warn about misinterpretation risks (Adults)

10. UX & Labeling

☐ Question numbering correct (no duplicates)

☐ Breadcrumbs correct

☐ Audience label consistent across page

☐ Score summary matches question count

🎨 TIER 3 — GOLD-STANDARD REFINEMENT

Aspirational. Used for polishing, not rejection.

These protect excellence, depth, and long-term quality.

11. Question Craft

☐ Language is precise and uncluttered

☐ No safe, purely definitional overuse

☐ Questions provoke reflection, not memorization

☐ Psychological contrasts sharpened where applicable

12. Distractor Elegance

☐ Wrong options reflect:

Partial truths

Misplaced emphasis

Common devotional misunderstandings

☐ Distractors do not accidentally become correct under loose reading

**Gold Standard:** See audience-specific distractor guides:
- **Adults** [BG_DISTRACTOR_STYLE_GUIDE.md](BG_DISTRACTOR_STYLE_GUIDE.md): Philosophical contrast, partial truths, false paths
- **Teens** [BG_DISTRACTOR_STYLE_GUIDE_TEENS.md](BG_DISTRACTOR_STYLE_GUIDE_TEENS.md): Emotional reasoning, peer logic, oversimplified ideas
- **Kids** [BG_DISTRACTOR_STYLE_GUIDE_KIDS.md](BG_DISTRACTOR_STYLE_GUIDE_KIDS.md): Story confusion, cause-effect mix-ups, simple emotions

Each guide includes approved categories, forbidden types, structural rules, and chapter-specific emphasis

13. Feedback Depth (Adults)

☐ 3–5 sentences where needed

☐ Optional “Why this matters” included for key questions

☐ Consequences of misunderstanding briefly highlighted

14. End-of-Chapter Finish

☐ Quiz ends on:

Insight

Caution

Integration

☐ Avoid ending on trivial or purely factual questions

15. Overall Flow

☐ Questions feel coherent as a sequence

☐ No abrupt tonal shifts

☐ The quiz feels like a guided study session, not a test

🔐 Exception Clause (Important)

Mechanical or labeling errors (e.g., verdict text, missing tags, minor formatting) may be corrected without regenerating questions, provided source integrity, logic, and structure remain unchanged.

This prevents unnecessary regeneration while preserving rigor.
