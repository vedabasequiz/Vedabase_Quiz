"use client";

import { useState, useEffect } from "react";
import { getWeeklyStreak, getBgProgress, getSbProgress } from "../lib/quizProgress";

function CircularProgress({ percentage, size = 60, strokeWidth = 6 }) {
  const radius = (size - strokeWidth) / 2;
  const circumference = radius * 2 * Math.PI;
  const offset = circumference - (percentage / 100) * circumference;

  return (
    <svg width={size} height={size} style={{ transform: "rotate(-90deg)" }}>
      {/* Background circle */}
      <circle
        cx={size / 2}
        cy={size / 2}
        r={radius}
        fill="none"
        stroke="#e9ecef"
        strokeWidth={strokeWidth}
      />
      {/* Progress circle */}
      <circle
        cx={size / 2}
        cy={size / 2}
        r={radius}
        fill="none"
        stroke="#4caf50"
        strokeWidth={strokeWidth}
        strokeDasharray={circumference}
        strokeDashoffset={offset}
        strokeLinecap="round"
        style={{ transition: "stroke-dashoffset 0.5s ease" }}
      />
      {/* Percentage text */}
      <text
        x="50%"
        y="50%"
        textAnchor="middle"
        dy="0.3em"
        fontSize="16"
        fontWeight="600"
        fill="#212529"
        style={{ transform: "rotate(90deg)", transformOrigin: "center" }}
      >
        {percentage}%
      </text>
    </svg>
  );
}

export default function HomePage() {
  const [audience, setAudience] = useState("adult");
  const [streak, setStreak] = useState(0);
  const [bgProgress, setBgProgress] = useState({ completed: 0, total: 18, percentage: 0 });
  const [sbProgress, setSbProgress] = useState({ completed: 0, total: 0, percentage: 0 });

  useEffect(() => {
    const currentStreak = getWeeklyStreak();
    const bg = getBgProgress(audience);
    const sb = getSbProgress(audience);

    setStreak(currentStreak);
    setBgProgress(bg);
    setSbProgress(sb);
  }, [audience]);

  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: "24px 16px" }}>
      <style dangerouslySetInnerHTML={{__html: `
        .scripture-card {
          transition: all 0.2s ease;
        }
        .scripture-card:hover {
          transform: scale(1.02);
          box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
          border-color: #bbb !important;
        }
        .about-card {
          transition: all 0.2s ease;
        }
        .about-card:hover {
          box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
          border-color: #bbb !important;
        }
        .about-card summary {
          cursor: pointer;
          user-select: none;
          font-size: 16px;
        }
        .about-card summary::marker {
          font-size: 20px;
        }
        .audience-selector {
          display: flex;
          gap: 8px;
          margin-bottom: 16px;
        }
        .audience-btn {
          padding: 8px 16px;
          border: 2px solid #dee2e6;
          border-radius: 8px;
          background: white;
          cursor: pointer;
          font-size: 14px;
          font-weight: 500;
          transition: all 0.2s ease;
        }
        .audience-btn:hover {
          border-color: #adb5bd;
        }
        .audience-btn.active {
          background: #4caf50;
          color: white;
          border-color: #4caf50;
        }
      `}} />
      
      <h1 style={{ fontSize: 20, marginBottom: 10 }}>Welcome & Hare Krsna!</h1>

      {/* Streak Counter */}
      {streak > 0 && (
        <div style={{
          display: "flex",
          alignItems: "center",
          gap: 8,
          padding: "12px 16px",
          background: "linear-gradient(135deg, #ff6b35 0%, #ff8c42 100%)",
          borderRadius: 10,
          boxShadow: "0 2px 8px rgba(255, 107, 53, 0.25)",
          color: "white",
          fontWeight: 600,
          fontSize: 16,
          marginBottom: 16,
        }}>
          <span style={{ fontSize: 24 }}>🔥</span>
          <span>{streak}-week streak!</span>
        </div>
      )}

      {/* Audience Selector */}
      <div className="audience-selector">
        <button
          className={`audience-btn ${audience === "adult" ? "active" : ""}`}
          onClick={() => setAudience("adult")}
        >
          Adults
        </button>
        <button
          className={`audience-btn ${audience === "teens" ? "active" : ""}`}
          onClick={() => setAudience("teens")}
        >
          Teens
        </button>
        <button
          className={`audience-btn ${audience === "kids" ? "active" : ""}`}
          onClick={() => setAudience("kids")}
        >
          Kids
        </button>
      </div>

      {/* NEW intro text (mobile-tight) */}
      <div style={{ opacity: 0.9, marginTop: 0, lineHeight: 1.5 }}>
        <p style={{ marginTop: 0, marginBottom: 10 }}>
          Vedabase Quiz is a sacred self-study space to deepen understanding of the Bhagavad Gita and Srimad Bhagavatam.
        </p>

        <p style={{ marginTop: 0, marginBottom: 10 }}>
          The quizzes encourage careful reflection on verses and purports — slowing down study, clarifying key ideas, and revealing subtle
          insights over time.
        </p>

        <p style={{ marginTop: 0, marginBottom: 20 }}>
          Not a test or competition, but a support for steady engagement with the scriptures.{" "}
          <span style={{ opacity: 0.9 }}>
            New here? Read below about the intention and design of the quizzes.
          </span>
        </p>
      </div>

      {/* Cards with Progress */}
<div style={{ display: "grid", gap: 12 }}>
  <a
    href={`/bg/?audience=${audience}`}
    className="scripture-card"
    style={{
      padding: 14,
      border: "1px solid #ddd",
      borderRadius: 10,
      textDecoration: "none",
      color: "inherit",
      display: "grid",
      gridTemplateColumns: "88px 1fr auto",
      gap: 12,
      alignItems: "center",
      minHeight: 100,
      background: "#fff",
    }}
  >
    <img
      src="/images/bg-cover.jpg"
      alt="Bhagavad Gita"
      style={{
        width: 88,
        height: 88,
        objectFit: "cover",
        borderRadius: 10,
        border: "1px solid #eee",
      }}
    />
    <div>
      <div style={{ fontWeight: 700, marginBottom: 4 }}>Bhagavad Gita</div>
      <div style={{ fontSize: 14, color: "#6c757d" }}>
        {bgProgress.completed}/{bgProgress.total} chapters
      </div>
    </div>
    <CircularProgress percentage={bgProgress.percentage} />
  </a>

  <a
    href={`/sb/?audience=${audience}`}
    className="scripture-card"
    style={{
      padding: 14,
      border: "1px solid #ddd",
      borderRadius: 10,
      textDecoration: "none",
      color: "inherit",
      display: "grid",
      gridTemplateColumns: "88px 1fr auto",
      gap: 12,
      alignItems: "center",
      minHeight: 100,
      background: "#fff",
    }}
  >
    <img
      src="/images/sb-cover.jpg"
      alt="Srimad Bhagavatam"
      style={{
        width: 88,
        height: 88,
        objectFit: "cover",
        borderRadius: 10,
        border: "1px solid #eee",
      }}
    />
    <div>
      <div style={{ fontWeight: 700, marginBottom: 4 }}>Srimad Bhagavatam</div>
      <div style={{ fontSize: 14, color: "#6c757d" }}>
        {sbProgress.completed}/{sbProgress.total} chapters
      </div>
    </div>
    <CircularProgress percentage={sbProgress.percentage} />
  </a>
</div>

       {/* About section as card */}
      <details 
        className="about-card"
        style={{ 
          marginTop: 14, 
          marginBottom: 18,
          padding: 14,
          border: "1px solid #ddd",
          borderRadius: 10,
          background: "#fff"
        }}
      >
  <summary
    style={{
      fontWeight: 700,
      fontSize: 16,
    }}
  >
    🪷 About Vedabase Quiz
  </summary>

  <div style={{ paddingTop: 16, opacity: 0.92, lineHeight: 1.55 }}>
    <p style={{ marginTop: 0 }}>
      <strong>Vedabase Quiz</strong> is a quiet self-study project created to support deeper engagement with the{" "}
      <em>Bhagavad Gita</em> and <em>Srimad Bhagavatam</em>.
    </p>

    <p>
      The quizzes on this site are not tests, competitions, or assessments of knowledge. They are designed to help
      readers slow down, reflect carefully on verses, and consider the intended meaning of the teachings as presented
      in Srila Prabhupada’s translations and purports.
    </p>
    <p>
      Each quiz is carefully tailored for three age groups — <strong>kids</strong>, <strong>teens</strong>, and <strong>adults</strong> — ensuring that questions, explanations, and vocabulary are appropriate for each audience. Whether you're introducing children to sacred texts or deepening your own understanding, the quizzes adapt to different learning stages.
    </p>
    <h3 style={{ fontSize: 16, margin: "16px 0 8px" }}>Purpose of the quizzes</h3>
    <p style={{ marginTop: 0 }}>
      Reading sacred texts often happens quickly—especially for familiar chapters or well-known verses. Vedabase Quiz
      exists to gently counter that tendency by encouraging attentive reading and thoughtful reflection.
    </p>

    <ul style={{ marginTop: 8 }}>
      <li>
        For readers newer to these scriptures, the questions help highlight essential ideas and provide structure
        for careful study.
      </li>
      <li>
        For experienced readers, the quizzes offer an opportunity to revisit familiar passages and notice
        subtleties that are easy to overlook.
      </li>
    </ul>

    <p style={{ marginTop: 10 }}>
      The goal is not to memorize answers, but to deepen understanding over time.
    </p>

    <h3 style={{ fontSize: 16, margin: "16px 0 8px" }}>How the quizzes are designed</h3>
    <ul style={{ marginTop: 0 }}>
      <li>All questions are based <strong>only</strong> on translations and purports from <strong>Vedabase.io</strong></li>
      <li>Each question is verified against the exact verse and purport it references</li>
      <li>Questions follow the natural flow of each chapter, from context to conclusion</li>
      <li>Explanations and direct verse links are provided after submission</li>
    </ul>

    <h3 style={{ fontSize: 16, margin: "16px 0 8px" }}>A self-study space</h3>
    <p style={{ marginTop: 0 }}>
      Vedabase Quiz is meant for individual, self-paced study. There is no pass or fail—only an opportunity to
      engage more thoughtfully with the texts.
    </p>
    <p>
      Readers are encouraged to take their time, revisit verses, and use the quizzes as a companion to regular
      reading rather than a replacement for it.
    </p>

    <h3 style={{ fontSize: 16, margin: "16px 0 8px" }}>Credits and acknowledgement</h3>
    <p style={{ marginTop: 0 }}>
      All scriptural content referenced on this site is sourced from <strong>Vedabase.io</strong>, which makes the
      works of <strong>His Divine Grace A. C. Bhaktivedanta Swami Prabhupada</strong> freely available for study.
    </p>
    <p style={{ marginBottom: 0 }}>
      The original translations and purports are published by the{" "}
      <strong>Bhaktivedanta Book Trust (BBT)</strong>.
    </p>
    <p style={{ marginTop: 8, fontSize: 14, opacity: 0.85 }}>
      Vedabase Quiz is an independent, non-commercial project and is not affiliated with Vedabase.io or the
      Bhaktivedanta Book Trust.
    </p>
  </div>
</details>

    </main>
  );
}
