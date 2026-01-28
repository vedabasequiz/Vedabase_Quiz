"use client";

import React, { useMemo, useState } from "react";

function getGrade(score, total) {
  const pct = total > 0 ? score / total : 0;

  if (pct === 1)
    return { label: "Perfect", emoji: "🌸", title: "Perfect score!", line: "Wonderful focus. Keep going steadily." };
  if (pct >= 0.9)
    return { label: "Excellent", emoji: "✨", title: "Excellent!", line: "Strong understanding — subtle points are landing." };
  if (pct >= 0.75)
    return { label: "Strong", emoji: "🙏", title: "Strong effort!", line: "You’re building real clarity. Review a few and continue." };
  if (pct >= 0.6)
    return { label: "Good", emoji: "📖", title: "Good progress!", line: "Nice work. Revisit the verses linked below and try again." };
  return { label: "Keep going", emoji: "🌿", title: "Keep going!", line: "This is how learning happens — one careful step at a time." };
}

function scrollToId(id) {
  const el = document.getElementById(id);
  if (!el) return;
  el.scrollIntoView({ behavior: "smooth", block: "start" });
}

export default function QuizClient({ quiz }) {
  const [answers, setAnswers] = useState(Array.from({ length: quiz.questions.length }, () => null));
  const [submitted, setSubmitted] = useState(false);

  const results = useMemo(() => {
    return quiz.questions.map((q, i) => {
      const selectedIndex = answers[i];
      const isCorrect = selectedIndex === q.correctIndex;

      return {
        qId: q.id ?? String(i),
        prompt: q.prompt,
        choices: q.choices,
        selectedIndex,
        correctIndex: q.correctIndex,
        isCorrect,
        feedback: q.feedback,
        verseLabel: q.verseLabel,
        verseUrl: q.verseUrl,
      };
    });
  }, [answers, quiz.questions]);

  const score = useMemo(() => results.reduce((acc, r) => acc + (r.isCorrect ? 1 : 0), 0), [results]);

  const grade = useMemo(() => getGrade(score, quiz.questions.length), [score, quiz.questions.length]);

  const missed = useMemo(() => {
    return results.map((r, idx) => ({ ...r, qIdx: idx })).filter((x) => !x.isCorrect);
  }, [results]);

  function onSelect(qIdx, choiceIdx) {
    if (submitted) return;
    setAnswers((prev) => {
      const next = [...prev];
      next[qIdx] = choiceIdx;
      return next;
    });
  }

  function onSubmit() {
    const anyBlank = answers.some((a) => a === null);
    if (anyBlank) {
      alert("Please answer all questions before submitting.");
      return;
    }
    setSubmitted(true);
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  function onReset() {
    setSubmitted(false);
    setAnswers(Array.from({ length: quiz.questions.length }, () => null));
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  return (
    <div style={{ maxWidth: 900, margin: "0 auto", padding: "24px 16px" }}>
      <h1 style={{ fontSize: 28, marginBottom: 6 }}>{quiz.title}</h1>

      <div style={{ opacity: 0.8, marginBottom: 18, lineHeight: 1.4 }}>
        {quiz.audience ? (
          <>
            Audience: {quiz.audience}{" "}
            <span style={{ opacity: 0.6 }}>|</span>{" "}
          </>
        ) : null}
        {quiz.difficulty ? (
          <>
            Difficulty: {quiz.difficulty}{" "}
            <span style={{ opacity: 0.6 }}>|</span>{" "}
          </>
        ) : null}
        Questions: {quiz.questions.length}
        {quiz.publishedOn ? ` | Published: ${quiz.publishedOn}` : ""}
      </div>

      {submitted ? (
        <div
          style={{
            border: "1px solid #ddd",
            borderRadius: 12,
            padding: 16,
            marginBottom: 18,
            background: "#fafafa",
          }}
        >
          <div style={{ fontSize: 18, fontWeight: 800 }}>
            {grade.emoji} {grade.title} — {score} / {quiz.questions.length}
          </div>
          <div style={{ marginTop: 8, opacity: 0.9 }}>{grade.line}</div>
          <div style={{ marginTop: 10, opacity: 0.85 }}>
            Self-study mode: correct answers and explanations are shown below.
          </div>

          {/* Review missed questions jump links */}
          {missed.length > 0 ? (
            <div style={{ marginTop: 14 }}>
              <div style={{ fontWeight: 800, marginBottom: 8 }}>Review missed questions</div>

              <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
                {missed.map((m) => (
                  <button
                    key={m.qId}
                    onClick={() => scrollToId(`q-${m.qIdx + 1}`)}
                    style={{
                      padding: "6px 10px",
                      borderRadius: 999,
                      border: "1px solid #ddd",
                      background: "#fff",
                      cursor: "pointer",
                      fontWeight: 800,
                      fontSize: 13,
                    }}
                    aria-label={`Jump to question ${m.qIdx + 1}`}
                  >
                    Q{m.qIdx + 1}
                  </button>
                ))}
              </div>

              <div style={{ marginTop: 8, opacity: 0.85, fontSize: 13 }}>
                Tip: open the verse links on missed questions and re-read the translation/purport once.
              </div>
            </div>
          ) : (
            <div style={{ marginTop: 14, fontWeight: 800, opacity: 0.95 }}>
              You got everything correct — wonderful! 🌸
            </div>
          )}

          <button
            onClick={onReset}
            style={{
              marginTop: 14,
              padding: "10px 14px",
              borderRadius: 12,
              border: "1px solid #ccc",
              cursor: "pointer",
              fontWeight: 800,
              background: "#fff",
            }}
          >
            Retake quiz
          </button>
        </div>
      ) : (
        <div style={{ border: "1px solid #ddd", borderRadius: 12, padding: 16, marginBottom: 18 }}>
          <div style={{ fontSize: 16, fontWeight: 800 }}>Instructions</div>
          <div style={{ marginTop: 8, opacity: 0.9 }}>
            Answer all questions, then click Submit to see your score and explanations.
          </div>
        </div>
      )}

      {/* Using a normal <div> list (not <ol>) to avoid double numbering */}
      <div>
        {results.map((r, qIdx) => (
          <div
            key={r.qId}
            id={`q-${qIdx + 1}`}
            style={{ marginBottom: 22, scrollMarginTop: 90 }}
          >
            <div style={{ fontWeight: 800, marginBottom: 8, opacity: 0.8 }}>
              Question {qIdx + 1}
            </div>

            <div style={{ fontWeight: 700, marginBottom: 10 }}>{r.prompt}</div>

            <div style={{ display: "grid", gap: 8 }}>
              {r.choices.map((choice, cIdx) => {
                const checked = answers[qIdx] === cIdx;
                const isCorrectChoice = submitted && cIdx === r.correctIndex;
                const isWrongChosen = submitted && checked && cIdx !== r.correctIndex;

                return (
                  <label
                    key={cIdx}
                    style={{
                      display: "flex",
                      gap: 10,
                      alignItems: "flex-start",
                      padding: "10px 12px",
                      borderRadius: 12,
                      border: "1px solid #ddd",
                      cursor: submitted ? "default" : "pointer",
                      background: isCorrectChoice ? "#eef8ee" : isWrongChosen ? "#fdeeee" : "#fff",
                    }}
                  >
                    <input
                      type="radio"
                      name={`q-${qIdx}`}
                      checked={checked}
                      onChange={() => onSelect(qIdx, cIdx)}
                      disabled={submitted}
                      style={{ marginTop: 2 }}
                    />
                    <span>{choice}</span>
                  </label>
                );
              })}
            </div>

            {submitted && (
              <div style={{ marginTop: 10, padding: "10px 12px", borderLeft: "4px solid #ccc" }}>
                <div style={{ fontWeight: 800 }}>{r.isCorrect ? "Correct" : "Review"}</div>
                <div style={{ marginTop: 6 }}>{r.feedback}</div>
                <div style={{ marginTop: 6 }}>
                  Verse link:{" "}
                  <a href={r.verseUrl} target="_blank" rel="noreferrer">
                    {r.verseLabel}
                  </a>
                </div>
              </div>
            )}
          </div>
        ))}
      </div>

      {!submitted && (
        <button
          onClick={onSubmit}
          style={{
            padding: "12px 16px",
            borderRadius: 12,
            border: "1px solid #111",
            cursor: "pointer",
            fontWeight: 800,
            background: "#111",
            color: "#fff",
          }}
        >
          Submit
        </button>
      )}
    </div>
  );
}
