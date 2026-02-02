# Srimad Bhagavatam Quiz Workflow (Gold Standard, Low Friction)

This workflow is the operational system for producing Srimad Bhagavatam quizzes at scale (335 chapters) while maintaining Gold Standards and minimizing back-and-forth.

This workflow is governed by:
- Editorial standards: sb-standards.md
- Machine rules: sb-validator-rules.md

Legend:
- Tier 1 = hard rules (must pass)
- Tier 2 = strong constraints (must pass)
- Tier 3 = polish heuristics (warn-only unless explicitly promoted)

---

## 1) Chapter Lifecycle

### Step A: Classify Chapter Archetype (Required)
Before any mapping or drafting:
- Assign chapterArchetype (see sb-archetypes.md)
- Record it in the quiz metadata and ledger
- Output: a single line, e.g. `chapterArchetype: "epistemology-heavy"`

### Step B: Map Before Draft (Required)
Create a 25-question map (Adults) before writing questions.
The map must include:
- Verse anchors (planned distribution across the chapter)
- Planned purport budget (see Step C)
- Planned synthesis questions (>=3, with >=1 in last 5)
- Difficulty progression plan (first ~60% grounding, last ~40% harder/integrative)
- No prose drafting yet. Only architecture.

### Step C: Pre-Commit Purport Budgeting (Required)
Before drafting, write the purport plan explicitly:
- Total purport questions: X / 25 (target ~40%, min 35%)
- Spread: early / mid / late (avoid clustering)
- Example: `purport plan: 10/25 (early 3, mid 4, late 3)`
This prevents ratio drift during edits.

### Step D: Draft Questions (Generation)
Write the full quiz file.
Drafting requirements:
- SB-native framing (authority/hearing over ethics-first)
- One unambiguous correct answer
- Parallel choice lengths as feasible
- Feedback includes direct Vedabase verse URL
- No verdict labels in feedback (UI handles Correct/Review)
- ASCII-only
- Metadata expectations (recommended):
  - Top-level: canto, chapterArchetype, publishedOn
  - Per question: source ("translation"|"purport")
  - Synthesis questions: tags: ["synthesis"] or type: "synthesis", per validator rules

### Step E: Validate (Hard Gate)
Run the validator.
- If Tier 1 fails: fix immediately (blocking)
- If Tier 2 fails: fix immediately (blocking)
- If Tier 3 warnings: proceed unless clarity is compromised

### Step F: Editorial Review (Human Gate)
Perform a quick editorial PASS/FAIL using the Acceptance Checklist (below).
This is not a re-litigate-everything step; it is a safety inspection.

### Step G: Publish and Record
Once accepted:
- Mark quiz as publish-ready
- Update availability mapping (if applicable)
- Update the ledger entry

---

## 2) Acceptance Checklist (Definition of Done)
A chapter is publish-ready only if:

### Tier 1 (FAIL if missing)
- Validator passes all Tier 1 rules
- Correct audience + question count (Adult 25 / Teens 15 / Kids 10)
- ASCII-only
- Direct Vedabase verse links in feedback
- Feedback contains no verdict labels

### Tier 2 (FAIL if missing)
- One clear correct answer per question
- Distractors plausible and not silly
- Difficulty progression present (first ~60% easier, last ~40% harder)
- SB focus dominant (authority/hearing/speculation/dharma purpose/Kali-yuga)
- Synthesis rules satisfied (Adults: >=3 synthesis; >=1 in last 5)

### Tier 3 (WARN-only)
- Choice-length balance is reasonable; no chronic short distractors
- Correct-is-longest not systematically biased
- End section feels consolidating and coherent

---

## 3) No-Regeneration Rule (Critical Friction Reducer)
Once Tier 1 and Tier 2 are passing:
- Do NOT regenerate the entire quiz to chase Tier 3 warnings.
- Only make localized edits when:
  - A question is ambiguous
  - A distractor is implausible
  - Feedback is misleading
  - A Tier 3 issue clearly harms clarity
- Default policy:
  - Fix wording and alignment, not architecture.

---

## 4) Change Control Rules (What Is Allowed When)

### Allowed during Mapping
- Verse coverage distribution
- Purport budget distribution
- Placement and count of synthesis questions
- Difficulty curve plan

### Allowed during Drafting
- Wording precision
- Distractor quality
- Feedback clarity
- Minor verse anchor adjustments (without breaking flow)

### Allowed after Tier 2 Pass
- Only localized edits to improve clarity
- No sweeping ratio/structure rewrites

---

## 5) Standard Response to Common Friction
If a quiz "feels off":
- First check: is SB focus drifting into BG ethics framing?
- Second check: is it too abstract (missing narrative grounding)?
- Third check: is purport reasoning clustered or repetitive?
- Fix order:
  - adjust question framing
  - adjust distractors
  - adjust feedback
- Only then consider moving one question in the map (rare).

---

## 6) Recommended Continuous QA Rhythm
Every 10 chapters, do a rolling review:
- ratio drift?
- end-section synthesis quality?
- archetype misuse?
- recurring validator warnings pattern?
- Record findings in the ledger notes and adjust templates accordingly.

---

## 7) Required Artifacts for Each Chapter
Each chapter must have:
- Archetype assigned
- Map created and stored (can be in PR description or notes)
- Purport budget written
- Validator pass record
- Ledger entry updated
