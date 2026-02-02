Srimad Bhagavatam Validator Rules
(Machine-Enforced Only)

This document defines binary, machine-checkable rules only.
Anything not listed here must not block builds.

Legend:

FAIL = build blocked

WARN = allowed but flagged

1. Structural Rules (FAIL)

Correct question count:
- Adults: 25
- Teens: 15
- Kids: 10

Required schema fields present

JSON parses successfully

2. ASCII-Only Rule (FAIL)

Entire file must be ASCII-only

Any Unicode character anywhere FAILS

3. Verse Link Rules (FAIL)

Each question must include at least one direct Vedabase.io verse URL

Non-Vedabase domains FAIL

4. Feedback Rules (FAIL)

Feedback must be non-empty

Feedback must not include verdict labels:
Disallowed: “Correct”, “Review”, “Wrong”

5. Source Field Rules (FAIL)

Adults and Teens:
Each question must include
source: "translation" or source: "purport"

Kids:
source optional

6. Purport Ratio Rules (Adults)

Compute purport ratio using source

FAIL if < 0.35

WARN if > 0.45

Target (~0.40) is informational only

7. Synthesis Rules (Adults — FAIL)

Synthesis detection must be explicit.
A question counts as synthesis if:
- tags includes "synthesis", OR
- type === "synthesis"

Rules:
- FAIL if synthesis count < 3
- FAIL if synthesis in last 5 < 1

8. Teens Rules (FAIL)

Every Teen question must include source

Tags optional; validator must not fail or warn based on Teen tags

9. Kids Rules

Tags optional

Validator must ignore Kids tags entirely

10. Heuristic Quality Checks (WARN-ONLY)

These must never block builds:
- High variance in choice lengths
- Very short distractors (<3 words)
- Correct-is-longest rate > ~70%
- Length-balance pass rate < ~65%

11. Explicit Non-Goals (Validator MUST NOT Enforce)

The validator must not:
- Enforce chapter archetypes
- Enforce epistemology/Kali-yuga coverage
- Judge narrative quality
- Enforce question templates
- Enforce workflow or ledger rules

Those belong to sb-standards.md.
