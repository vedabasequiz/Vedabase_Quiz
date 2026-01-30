"use client";

import React, { useMemo, useState, useRef, useEffect } from "react";
import Confetti from "react-confetti";
import { checkMilestone } from "../lib/quizProgress";

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
  const [soundEnabled, setSoundEnabled] = useState(true);
  const confettiRef = useRef(null);

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
  const scorePct = quiz.questions.length > 0 ? score / quiz.questions.length : 0;

  const missed = useMemo(() => results.filter((r) => !r.isCorrect), [results]);

  // Play sound effect based on score
  useEffect(() => {
    if (submitted && soundEnabled) {
      if (scorePct === 1) {
        playSound("celebration"); // Epic celebration for 100%
        speakHariBol(); // Say "Hari Bol" for 100%
      } else if (scorePct >= 0.9) {
        playSound("tada"); // Cheerful tada for 90%+
        speakHariBol(); // Say "Hari Bol" for 90%+
      }
    }
  }, [submitted, soundEnabled, scorePct]);

  function playSound(type) {
    try {
      const audioContext = new (window.AudioContext || window.webkitAudioContext)();
      const now = audioContext.currentTime;

      if (type === "celebration") {
        // Ascending notes: C, E, G, C (happy major chord)
        playTone(audioContext, 262, 0.1, now); // C
        playTone(audioContext, 330, 0.1, now + 0.1); // E
        playTone(audioContext, 392, 0.1, now + 0.2); // G
        playTone(audioContext, 524, 0.2, now + 0.3); // C
      } else if (type === "tada") {
        // Shorter cheerful melody
        playTone(audioContext, 440, 0.08, now); // A
        playTone(audioContext, 554, 0.08, now + 0.08); // C#
        playTone(audioContext, 659, 0.15, now + 0.16); // E
      }
    } catch (e) {
      // Silently fail if audio context not available
    }
  }

  function playTone(audioContext, frequency, duration, startTime) {
    const oscillator = audioContext.createOscillator();
    const envelope = audioContext.createGain();
    
    oscillator.frequency.value = frequency;
    oscillator.connect(envelope);
    envelope.connect(audioContext.destination);
    
    envelope.gain.setValueAtTime(0.3, startTime);
    envelope.gain.exponentialRampToValueAtTime(0.01, startTime + duration);
    
    oscillator.start(startTime);
    oscillator.stop(startTime + duration);
  }

  function speakHariBol() {
    try {
      // Cancel any previous speech
      window.speechSynthesis.cancel();
      
      const voices = window.speechSynthesis.getVoices();
      
      // Try to find an Indian English voice (en-IN)
      let selectedVoice = voices.find(v => v.lang === "en-IN" || v.lang.startsWith("en-IN"));
      
      // If no Indian English, try Hindi
      if (!selectedVoice) {
        selectedVoice = voices.find(v => v.lang === "hi-IN" || v.lang.startsWith("hi-IN"));
      }
      
      // Fallback to any English voice
      if (!selectedVoice) {
        selectedVoice = voices.find(v => v.lang.includes("en")) || voices[0];
      }
      
      // Speak "Hari Bol" once
      const utterance = new SpeechSynthesisUtterance("Hari Bol");
      utterance.rate = 0.85; // Natural speaking pace
      utterance.pitch = 1.0;
      utterance.volume = 1.0;
      utterance.voice = selectedVoice;
      
      window.speechSynthesis.speak(utterance);
    } catch (e) {
      // Silently fail if speech synthesis not available
    }
  }

  // Generate share message based on score
  function generateShareMessage() {
    const pct = Math.round(scorePct * 100);
    const emoji = grade.emoji;
    const achievement = grade.title;
    
    return `${emoji} Just scored ${score}/${quiz.questions.length} (${pct}%) on "${quiz.title}"!\n\nAchievement: ${achievement}\n\nTest yourself and challenge your knowledge!`;
  }

  function shareWhatsApp() {
    const message = encodeURIComponent(generateShareMessage());
    const quizUrl = typeof window !== "undefined" ? window.location.href : "";
    const fullMessage = encodeURIComponent(generateShareMessage() + (quizUrl ? `\n\n${quizUrl}` : ""));
    
    trackShareEvent("whatsapp");
    window.open(`https://wa.me/?text=${fullMessage}`, "_blank");
  }

  function copyToClipboard() {
    const message = generateShareMessage() + (typeof window !== "undefined" ? `\n\n${window.location.href}` : "");
    navigator.clipboard.writeText(message).then(() => {
      alert("Score copied to clipboard! Paste and share with friends.");
      trackShareEvent("clipboard");
    }).catch(() => {
      alert("Failed to copy. Try again or use another sharing method.");
    });
  }

  function shareTwitter() {
    const pct = Math.round(scorePct * 100);
    const text = encodeURIComponent(
      `${grade.emoji} Scored ${score}/${quiz.questions.length} (${pct}%) on "${quiz.title}"! ${grade.title} 📚 #VedabaseQuiz #BhagavadGita`
    );
    const url = typeof window !== "undefined" ? encodeURIComponent(window.location.href) : "";
    
    trackShareEvent("twitter");
    window.open(
      `https://twitter.com/intent/tweet?text=${text}&url=${url}&hashtags=VedabaseQuiz,BhagavadGita,Learning`,
      "_blank"
    );
  }

  function shareFacebook() {
    const quizUrl = typeof window !== "undefined" ? window.location.href : "";
    
    trackShareEvent("facebook");
    window.open(
      `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(quizUrl)}&quote=${encodeURIComponent(generateShareMessage())}`,
      "_blank"
    );
  }

  function shareEmail() {
    const pct = Math.round(scorePct * 100);
    const subject = encodeURIComponent(`Check my ${pct}% score on the Bhagavad Gita Quiz!`);
    const body = encodeURIComponent(
      generateShareMessage() + 
      (typeof window !== "undefined" ? `\n\nQuiz Link: ${window.location.href}` : "")
    );
    
    trackShareEvent("email");
    window.location.href = `mailto:?subject=${subject}&body=${body}`;
  }

  function trackShareEvent(platform) {
    // Analytics tracking - can be connected to Google Analytics, Mixpanel, etc.
    if (typeof window !== "undefined" && window.gtag) {
      window.gtag("event", "quiz_share", {
        platform,
        score,
        total: quiz.questions.length,
        quiz_name: quiz.title,
        score_level: grade.key,
      });
    }
  }

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
    
    // Save quiz result to localStorage
    try {
      const slug = typeof window !== "undefined" ? window.location.pathname.replace("/quiz/", "").replace(/\/$/, "") : null;
      if (slug) {
        const results = JSON.parse(localStorage.getItem("vedabaseQuizResults") || "{}");
        results[slug] = {
          score,
          total: quiz.questions.length,
          percentage: Math.round((score / quiz.questions.length) * 100),
          date: new Date().toISOString(),
        };
        localStorage.setItem("vedabaseQuizResults", JSON.stringify(results));
        
        // Increment completion count
        const completions = JSON.parse(localStorage.getItem("vedabaseQuizCompletions") || "{}");
        completions[slug] = (completions[slug] || 0) + 1;
        localStorage.setItem("vedabaseQuizCompletions", JSON.stringify(completions));
        setCompletionCount(completions[slug]);
        
        // Check for milestone achievements
        const milestone = checkMilestone();
        if (milestone && soundEnabled) {
          // Celebrate milestone with confetti and voice
          setTimeout(() => {
            playSound("celebration");
            speakHariBol();
          }, 100);
        }
      }
    } catch (e) {
      // Silently fail if localStorage not available
    }
    
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  function onReset() {
    setSubmitted(false);
    setAnswers(Array.from({ length: quiz.questions.length }, () => null));
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  const audienceClass =
    quiz.audience === "kids" ? "feedbackKids" : quiz.audience === "teens" ? "feedbackTeens" : "feedbackAdult";

  // Chapter names mapping
  const chapterNames = {
    sb: {
      1: {
        1: "Questions by the Sages",
        2: "Divinity and Divine Service",
      }
    },
    bg: {
      1: "Observing the Armies on the Battlefield of Kurukshetra",
      2: "Contents of the Gita Summarized",
      3: "Karma-yoga",
      4: "Transcendental Knowledge",
      5: "Karma-yoga—Action in Krishna Consciousness",
      6: "Dhyana-yoga",
      7: "Knowledge of the Absolute",
      8: "Attaining the Supreme",
      9: "The Most Confidential Knowledge",
      10: "The Opulence of the Absolute",
      11: "The Universal Form",
      12: "Devotional Service",
      13: "Nature, the Enjoyer, and Consciousness",
      14: "The Three Modes of Material Nature",
      15: "The Yoga of the Supreme Person",
      16: "The Divine and Demoniac Natures",
      17: "The Divisions of Faith",
      18: "Conclusion—The Perfection of Renunciation",
    }
  };

  // Parse quiz ID to extract scripture, canto/chapter info
  function getFormattedTitle() {
    const id = quiz.id || "";
    
    // SB format: sb-1-1-adult -> SB 1.1
    if (id.startsWith("sb-")) {
      const parts = id.split("-");
      const canto = parts[1];
      const chapter = parts[2];
      const cantoUrl = `https://vedabase.io/en/library/sb/${canto}/`;
      const chapterUrl = `https://vedabase.io/en/library/sb/${canto}/${chapter}/`;
      const chapterName = chapterNames.sb?.[canto]?.[chapter] || "";
      
      return (
        <>
          <a href={cantoUrl} target="_blank" rel="noopener noreferrer" style={{ color: "inherit", textDecoration: "none" }}>
            SB {canto}
          </a>
          .
          <a href={chapterUrl} target="_blank" rel="noopener noreferrer" style={{ color: "inherit", textDecoration: "none" }}>
            {chapter}
          </a>
          {chapterName && <span style={{ opacity: 0.8 }}> · {chapterName}</span>}
        </>
      );
    }
    
    // BG format: bg-1-adult -> BG 1
    if (id.startsWith("bg-")) {
      const parts = id.split("-");
      const chapter = parts[1];
      const chapterUrl = `https://vedabase.io/en/library/bg/${chapter}/`;
      const chapterName = chapterNames.bg?.[chapter] || "";
      
      return (
        <>
          <a href={chapterUrl} target="_blank" rel="noopener noreferrer" style={{ color: "inherit", textDecoration: "none" }}>
            BG {chapter}
          </a>
          {chapterName && <span style={{ opacity: 0.8 }}> · {chapterName}</span>}
        </>
      );
    }
    
    // Fallback to original title
    return quiz.title;
  }

  return (
    <div style={{ maxWidth: 900, margin: "0 auto", padding: "24px 16px" }}>
      <h1 
        style={{ 
          fontSize: 24, 
          marginBottom: 6,
          lineHeight: 1.4,
          wordBreak: "break-word"
        }}
        className="quiz-title"
      >
        {getFormattedTitle()}
      </h1>

      <style jsx>{`
        .quiz-title a {
          transition: text-decoration 0.2s;
        }
        .quiz-title a:hover {
          text-decoration: underline;
        }
        @media (max-width: 600px) {
          .quiz-title {
            font-size: 20px !important;
          }
        }
      `}</style>

      <div style={{ opacity: 0.8, marginBottom: 18, lineHeight: 1.4, fontSize: 14 }}>
        {quiz.publishedOn ? `Published: ${quiz.publishedOn}` : ""}
        {completionCount > 0 && (quiz.publishedOn ? " | " : "")}
        {completionCount > 0 && `You've completed this ${completionCount} ${completionCount === 1 ? 'time' : 'times'}`}
      </div>

      {submitted ? (
        <>
          {/* Confetti: Epic for 100%, Moderate for 90%+ */}
          {scorePct === 1 && (
            <Confetti
              ref={confettiRef}
              width={typeof window !== "undefined" ? window.innerWidth : 800}
              height={typeof window !== "undefined" ? window.innerHeight : 600}
              numberOfPieces={80}
              gravity={0.5}
              recycle={false}
              colors={["#2f7d32", "#1e3a8a", "#6b4f1d", "#c41e3a", "#fbbf24"]}
            />
          )}
          {scorePct >= 0.9 && scorePct < 1 && (
            <Confetti
              height={typeof window !== "undefined" ? window.innerHeight : 600}
              numberOfPieces={40}
              gravity={0.8}
              recycle={false}
              colors={["#1e3a8a", "#fbbf24", "#06b6d4"]}
            />
          )}

          <div className={`scoreBox score${grade.key}`}>
            {/* Sound toggle button */}
            <button
              onClick={() => setSoundEnabled(!soundEnabled)}
              style={{
                position: "absolute",
                top: 16,
                right: 16,
                background: "none",
                border: "none",
                fontSize: 20,
                cursor: "pointer",
                opacity: 0.7,
                transition: "opacity 0.2s",
              }}
              onMouseEnter={(e) => (e.target.style.opacity = "1")}
              onMouseLeave={(e) => (e.target.style.opacity = "0.7")}
              title={soundEnabled ? "Mute sound" : "Unmute sound"}
            >
              {soundEnabled ? "🔊" : "🔇"}
            </button>

            {/* Animated Score Ring + Title */}
            <div style={{ display: "flex", alignItems: "center", gap: 20, marginBottom: 16 }}>
              <div className="scoreRing" style={{ "--score": scorePct }}>
                <svg
                  width="80"
                  height="80"
                  viewBox="0 0 80 80"
                  style={{ transform: "rotate(-90deg)", filter: "drop-shadow(0 2px 4px rgba(0,0,0,0.1))" }}
                >
                  <circle cx="40" cy="40" r="35" fill="none" stroke="#f0f0f0" strokeWidth="8" />
                  <circle
                    cx="40"
                    cy="40"
                    r="35"
                    fill="none"
                    stroke={scorePct === 1 ? "#2f7d32" : scorePct >= 0.9 ? "#1e3a8a" : scorePct >= 0.75 ? "#6b4f1d" : "#666"}
                    strokeWidth="8"
                    strokeDasharray={`${2 * Math.PI * 35}`}
                    strokeDashoffset={`${2 * Math.PI * 35 * (1 - scorePct)}`}
                    style={{ transition: "stroke-dashoffset 0.8s ease-out" }}
                  />
                </svg>
                <div className="scoreRingText">{score}/{quiz.questions.length}</div>
              </div>
              <div>
                <div className="scoreTitle" style={{ fontSize: 24 }}>
                  {grade.emoji} {grade.title}
                </div>
              </div>
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

            {/* Share Section */}
            <div className="shareBox">
              <div className="shareLabel">📤 Share Your Achievement:</div>
              <div className="shareBtnGroup">
                <button className="shareBtn shareBtn--whatsapp" onClick={shareWhatsApp} title="Share on WhatsApp">
                  💬 WhatsApp
                </button>
                <button className="shareBtn shareBtn--twitter" onClick={shareTwitter} title="Share on Twitter">
                  𝕏 Twitter
                </button>
                <button className="shareBtn shareBtn--facebook" onClick={shareFacebook} title="Share on Facebook">
                  f Facebook
                </button>
                <button className="shareBtn shareBtn--email" onClick={shareEmail} title="Share via Email">
                  ✉️ Email
                </button>
                <button className="shareBtn shareBtn--copy" onClick={copyToClipboard} title="Copy to clipboard">
                  📋 Copy Link
                </button>
              </div>
            </div>
          </div>
        </>
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
