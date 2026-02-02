Srimad Bhagavatam Quiz Standards
(Editorial, Philosophical, and Operational — LOCKED)

This document defines the authoritative editorial and operational standards for all Srimad Bhagavatam quizzes.
It governs what “good” means.
The validator may enforce only what is explicitly listed in sb-validator-rules.md.

1. Scope and Source Integrity

Source: Vedabase.io only

Authority: Srila Prabhupada translations and purports only

No external commentaries, no paraphrased sourcing, no alternate translations

2. Platform and Format

Website-first delivery (JSON for the Next.js quiz system)

ASCII-only content (no Unicode anywhere)

No Google Forms or PDFs unless explicitly requested (default: never)

3. Audience and Question Counts

Adults: 25 questions

Teens: 15 questions (audience: "teens")

Kids: 10 questions

4. Srimad Bhagavatam Focus (Core Difference vs Bhagavad Gita)

SB quizzes emphasize how knowledge is received, not merely what actions are correct.

Primary emphases:

Epistemology and authority: hearing (sravana), disciplic succession, qualification of speaker/hearer, pramana

Anti-speculation: rejection of mental invention and speculative religion

Purpose of dharma: dharma as bhakti-awakening; rejection of kaitava-dharma

Kali-yuga realism: degradation patterns and the prescribed remedy

Narrative-as-teaching: narratives are philosophical vehicles, not trivia

Avoid:

BG-style decision-tree ethics as the dominant mode

Trivia without philosophical consequence

Abstract metaphysics detached from purport intent

5. Difficulty Progression

First ~60%: grounding, narrative orientation, foundational clarity

Last ~40%: moderately harder, contrastive, integrative

Final 20–25% must consolidate, not introduce confusion

6. Translation vs Purport Balance (Adults — LOCKED)

Target: ~40% purport-guided

Acceptable range: 35–45%

Hard minimum: 35%

Editorial intent:

Purport questions should be distributed (not clustered)

Translation questions must still test meaning, not recall

7. Chapter Archetypes (Editorial Metadata — REQUIRED)

Each SB chapter must be assigned a chapter archetype before mapping.

Archetypes (defined in sb-archetypes.md):

epistemology-heavy

narrative-heavy

mixed

genealogy

theological-core

Archetypes:

guide mapping and review expectations

do not change locked ratios

are not validator-enforced

8. Mapping-Before-Generation (REQUIRED)

No SB chapter may be generated without a completed question map.

A valid map includes:

Verse coverage plan

Purport budget (count + early/mid/late spread)

Planned synthesis questions (>=3; >=1 in last 5)

Difficulty progression outline

9. Pre-Commit Purport Budgeting (REQUIRED)

Before drafting, explicitly state:

“This chapter will contain X purport questions, distributed early / mid / late.”

This prevents ratio drift during editing.

10. Question Taxonomy (Editorial Review)

Each SB Adult chapter must demonstrate coverage of:

Epistemology / authority

Purport-based false-path detection

Narrative-as-teaching

Synthesis / integration

These categories may overlap and are editorially reviewed, not machine-enforced (except synthesis count).

11. MCQ Design Principles

One unambiguous correct answer

Plausible, philosophy-aligned distractors

No trick phrasing; no all/none-of-the-above

Proper nouns must be contextualized

12. Feedback Standards

Verse- and purport-aligned explanation

No verdict labels in feedback (UI handles Correct/Review)

Mandatory direct Vedabase verse URL

Feedback depth:

Adults: 3–5 sentences; contrastive; warn against false paths

Teens: 2–3 sentences; guided reasoning

Kids: 1–2 short, concrete, cause-effect sentences

13. Tags and Metadata (Discipline, Not Burden)
Adults

source: "translation" | "purport" (required)

Tags recommended; used for synthesis detection

Use tags: ["synthesis"] on synthesis questions

Teens

source required

Tags optional, informational only

Kids

Tags optional and minimal (narrative / lesson)

Validator ignores Kids tags entirely

14. Operational Quality Rules (LOCKED)
Tier-2 Stop Rule (Critical)

Once a chapter passes Tier 1 and Tier 2:

Do not regenerate to chase Tier-3 warnings

Fix wording and clarity only, not structure

No-Regeneration Principle

Fix philosophy with framing, not architecture.

15. Ledger Requirement

All SB chapters must be tracked in sb-ledger.csv:

archetype

purport ratio

synthesis count

validator status

publish status

Ledger entries are never deleted; corrections go in notes.

16. Pre-Publish Editorial Acceptance (Human Gate)

A chapter is publish-ready only if:

SB focus is dominant

Archetype intent is respected

Purport reasoning is present throughout

Ending synthesizes rather than confuses

No BG-style drift appears
