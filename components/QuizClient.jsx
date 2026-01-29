"use client";

import React, { useMemo, useState } from "react";

function getGrade(score, total) {
  const pct = total > 0 ? score / total : 0;

  if (pct === 1) return { key: "Perfect", emoji: "🌸", title: "Perfect score!", line: "Wonderful focus. Keep going steadily." };
  if (pct >= 0.9) return { key: "Excellent", emoji: "✨", title: "Excellent!", line: "Strong understanding — subtle points are landing." };
  if (pct >= 0.75) return { key: "Strong", emoji: "🙏", title: "Strong effort!", line: "You’re building real clarity. Review a few and continue." };
  if (pct >= 0.6) return { key: "Good", emoji: "📖", title: "Good progress!", line: "Nice work. Revisit the verse links below and try again." };
  return { key: "KeepGoing", emoji: "🌿", title: "Keep going!", line: "This is how learning happens — one careful step at a time." };
}

// Removes misleading leading labels inside feedback text like "Correct." / "Review."
function cleanFeedbackText(text) {
  if (!text) return "";
  return String(text).replace(/^\s*(Correct|Review)\s*[:.\-]\s*/i, "");
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
        idx: i,
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

  const missed = useMemo(() => results.filter((r) => !r.isCorrect), [results]);

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

  const audienceClass =
    quiz.audience === "kids" ? "feedbackKids" : quiz.audience === "teens" ? "feedbackTeens" : "feedbackAdult";

  return (
    <div style={{ maxWidth: 900, margin: "0 auto", padding: "24px 16px" }}>
      <h1 style={{ fontSize: 28, marginBottom: 6 }}>{quiz.title}</h1>

      <div style={{ opacity: 0.8, marginBottom: 18, lineHeight: 1.4 }}>
        {quiz.audience ? <>Audience: {quiz.audience}{" "} |{" "}</> : null}
        {quiz.difficulty ? <>Difficulty: {quiz.difficulty}{" "} |{" "}</> : null}
        Questions: {quiz.questions.length}
        {quiz.publishedOn ? ` | Published: ${quiz.publishedOn}` : ""}
      </div>

      {submitted ? (
        <div className={`scoreBox score${grade.key}`}>
          <div className="scoreTitle">
            {grade.emoji} {grade.title} — {score} / {quiz.questions.length}
          </div>

          <div className="scoreLine">{grade.line}</div>
          <div className="scoreSub">Self-study mode: explanations and verse links are shown below.</div>

          {/* Missed question tags (jump links) */}
          {missed.length > 0 ? (
            <div className="missedWrap">
              <div className="missedLabel">Review missed questions:</div>
              <div className="missedChips">
                {missed.map((r) => (
                  <a key={r.qId} className="missedChip" href={`#q-${r.idx + 1}`}>
                    Q{r.idx + 1}
                  </a>
                ))}
              </div>
            </div>
          ) : (
            <div className="missedWrap">
              <div className="missedLabel">No missed questions. Nice work!</div>
            </div>
          )}

          <button className="btnSecondary" onClick={onReset} style={{ marginTop: 12 }}>
            Retake quiz
          </button>
        </div>
      ) : (
        <div className="scoreBox" style={{ background: "#fff" }}>
          <div style={{ fontSize: 16, fontWeight: 800 }}>Instructions</div>
          <div style={{ marginTop: 8, opacity: 0.9 }}>Answer all questions, then click Submit to see your score and explanations.</div>
        </div>
      )}

      {/* Use a normal <div> list to avoid double numbering */}
      <div>
        {results.map((r, qIdx) => {
          const qNumber = qIdx + 1;

          return (
            <div key={r.qId} id={`q-${qNumber}`} style={{ marginBottom: 22, scrollMarginTop: 90 }}>
              <div style={{ fontWeight: 800, marginBottom: 8, opacity: 0.8 }}>Question {qNumber}</div>

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
                <div
                  className={[
                    "feedbackBox",
                    r.isCorrect ? "feedbackBoxCorrect" : "feedbackBoxReview",
                    audienceClass,
                  ].join(" ")}
                >
                  <div className="feedbackHeaderRow">
                    <div className="feedbackVerdict">{r.isCorrect ? "Correct" : "Review"}</div>
                    <div className="feedbackMeta">
                      {r.isCorrect ? "Nice." : "Re-check the verse/purport."}
                    </div>
                  </div>

                  <div className="feedbackText">{cleanFeedbackText(r.feedback)}</div>

                  <div className="feedbackVerseRow">
                    <span className="feedbackVerseLabel">Verse link:</span>
                    <a className="feedbackVerseLink" href={r.verseUrl} target="_blank" rel="noreferrer">
                      {r.verseLabel}
                    </a>
                  </div>
                </div>
              )}
            </div>
          );
        })}
      </div>

      {!submitted && (
        <button className="btnPrimary" onClick={onSubmit}>
          Submit
        </button>
      )}
    </div>
  );
}
