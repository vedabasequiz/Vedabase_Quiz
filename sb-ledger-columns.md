# SB Ledger Column Rationale and Usage Guide

## Column Rationale (Why Each Exists)

This is important so the ledger doesn’t rot over time.

### Structural tracking
- **canto, chapter, chapter_title**: Identify the chapter precisely.
- **audience (adult / teens / kids)**: Track which audience the quiz is for.
- **question_count**: Ensure correct number of questions per audience.

### Editorial control
- **archetype**: Prevents philosophical drift by recording the intended editorial approach.
- **notes**: Captures why something is the way it is (critical for future reference and audits).

### Ratio & synthesis control (core SB risks)
- **purport_count**: Number of purport-based questions.
- **purport_ratio**: Ratio of purport questions to total (spot drift without opening quiz file).
- **synthesis_count**: Number of synthesis questions (ensures integration, not just recall).
- **synthesis_in_last_5**: Synthesis questions in the last 5 (ensures consolidation at end).

### Validator health
- **validator_status (pass / fail / not-run)**: Tracks if the quiz passes machine checks.
- **validator_warnings_count**: Number of warnings (helps spot recurring issues or archetype patterns).

### Publishing state
- **published (yes/no)**: Whether the quiz is published.
- **status (planned / mapped / drafted / validated / published)**: Progress stage for each quiz.

This lets you see progress and risks across 335 chapters at a glance.

---

## How This Ledger Is Meant to Be Used

### During mapping
- Fill: archetype, audience, question_count, status=mapped

### After drafting
- Fill: purport_count, synthesis_count, synthesis_in_last_5

### After validation
- Fill: purport_ratio, validator_status, validator_warnings_count

### After publish
- Set: published=yes, status=published

No automation required to be useful.

---

## One Important Rule (Lock This Mentally)
If a chapter is published, never delete its ledger row.
Corrections go in notes, not by rewriting history.

This gives you an audit trail when you reach Cantos 5–7 and wonder “why did we do it this way?”
