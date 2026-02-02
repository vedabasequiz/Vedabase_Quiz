# Srimad Bhagavatam Quiz Standards (Editorial - Locked)

This document defines the editorial, philosophical, and pedagogical standards for Srimad Bhagavatam quizzes. It is authoritative for content quality. The validator should enforce only what is explicitly listed in sb-validator-rules.md.

## 1) Scope and Source Integrity
- Source: Vedabase.io only.
- Authority: Srila Prabhupada translations and purports only.
- No external commentaries, no paraphrase-based sourcing, no alternate translations.

## 2) Platform and Format
- Website-first delivery (JSON for the Next.js quiz system).
- ASCII-only content (no Unicode anywhere in prompt/choices/feedback).
- No Google Forms or PDFs unless explicitly requested (default: never).

## 3) Audience and Question Counts
- Adults: 25 questions
- Teens: 15 questions (audience: "teens")
- Kids: 10 questions

## 4) Srimad Bhagavatam Focus (Core Difference vs BG)
SB quizzes must emphasize how knowledge is received (authority, hearing, disciplic succession), not merely what actions are correct.

Primary emphases:
- Epistemology and authority: hearing (sravana), disciplic succession, qualification of speaker, pramana.
- Anti-speculation: reject mental invention and speculative religion.
- Purpose of dharma: dharma as bhakti-awakening; rejection of kaitava-dharma.
- Kali-yuga realism: degradation patterns and the remedy (hearing/chanting/bhakti).
- Narrative-as-teaching: narratives are philosophical vehicles; avoid trivia.

Avoid:
- Trivia-heavy recall (names/events without philosophical purpose).
- BG-style decision-tree ethics as the dominant mode.
- Abstract metaphysics detached from purport intent.

## 5) Difficulty Progression
- First ~60%: grounding, narrative orientation, foundational concepts.
- Last ~40%: moderately harder, more contrastive, more integrative.
- Final 20-25% should consolidate (synthesis) rather than introduce confusing novelty.

## 6) Adults Translation vs Purport Balance (Locked)
- Purport-guided target: ~40%
- Acceptable range: 35-45%
- Hard minimum: 35% (below this should fail validation)
- Editorial notes:
  - Purport questions should be distributed across the quiz (not clustered).
  - Translation questions should still test meaning, not just plot recall.

## 7) Taxonomy Expectations (Editorial Review Only)
Each SB Adult chapter should demonstrate coverage of:
- Epistemology/authority
- Purport-based false-path detection
- Narrative-as-teaching
- Synthesis/integration

These categories may overlap and are evaluated during human pre-publish review, not via validator hard rules (except synthesis requirements where configured in validator).

## 8) MCQ Design Principles
- One unambiguous correct answer per question.
- Plausible distractors aligned with verse/purport intent.
- Avoid "all of the above", "none of the above", and trick wording.
- Proper nouns must be contextualized when used as options.

## 9) Feedback Standards
- Verse- and purport-aligned explanation.
- Do NOT include verdict labels ("Correct", "Review", "Wrong") in feedback (UI handles verdict display).
- Mandatory direct Vedabase verse URL.
- Feedback length and style:
  - Adults: 3-5 sentences; contrastive; warn against false paths when relevant.
  - Teens: 2-3 sentences; guided reasoning (one-step); minimal option-comparison.
  - Kids: 1-2 short, concrete, positive sentences (cause-effect only).

## 10) Tags and Metadata (Recommended Discipline)
Tags are optional metadata to support editorial audits and analytics. They must not create maintenance burden or validator churn.

### Adults
- Tags are recommended and may be used for synthesis detection.
- Suggested tags: ["synthesis","epistemology","false-path","kali-yuga","narrative"]
- source field is recommended for SB Adults (helps ratio checks), but may remain optional if the repo already infers it differently.

### Teens
- source field is required on every question (locked).
- Tags are optional, informational only (not enforced).
- Recommended small tag set:
  - narrative, reasoning, reflection (avoid heavy adult tags)

### Kids
- Tags are optional and should remain minimal.
- If used, keep to: narrative or lesson
- Validator must ignore Kids tags entirely.

## 11) Pre-Publish Editorial Review (Human)
Before publish, confirm:
- SB focus is present (authority/hearing/speculation/dharma purpose/Kali-yuga realism).
- Purport reasoning appears throughout (not just at the end).
- Ending questions synthesize rather than confuse.
- No BG-style drift in framing.
