"use client";

import { useState, useEffect } from "react";
import { getWeeklyStreak, getBgProgress, getSbProgress } from "../lib/quizProgress";

function CircularProgress({ percentage, size = 60, strokeWidth = 6 }) {
  const radius = (size - strokeWidth) / 2;
  const circumference = radius * 2 * Math.PI;
  const offset = circumference - (percentage / 100) * circumference;

  return (
    <div style={{ position: "relative", width: size, height: size, flexShrink: 0 }}>
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
      </svg>
      {/* Percentage text overlay */}
      <div style={{
        position: "absolute",
        top: 0,
        left: 0,
        width: size,
        height: size,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        fontSize: 14,
        fontWeight: 600,
        color: "#212529",
      }}>
        {percentage}%
      </div>
    </div>
  );
}

export default function HomePage() {
  const [bgAudience, setBgAudience] = useState("adult");
  const [sbAudience, setSbAudience] = useState("adult");
  const [streak, setStreak] = useState(0);
  const [bgProgress, setBgProgress] = useState({ completed: 0, total: 18, percentage: 0 });
  const [sbProgress, setSbProgress] = useState({ completed: 0, total: 0, percentage: 0 });
  const [aboutExpanded, setAboutExpanded] = useState(false);

  useEffect(() => {
    const currentStreak = getWeeklyStreak();
    setStreak(currentStreak);
  }, []);

  useEffect(() => {
    const bg = getBgProgress(bgAudience);
    setBgProgress(bg);
  }, [bgAudience]);

  useEffect(() => {
    const sb = getSbProgress(sbAudience);
    setSbProgress(sb);
  }, [sbAudience]);

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
          gap: 6px;
          margin-top: 8px;
        }
        .audience-btn {
          padding: 4px 10px;
          border: 1px solid #dee2e6;
          border-radius: 6px;
          background: white;
          cursor: pointer;
          font-size: 12px;
          font-weight: 500;
          transition: all 0.2s ease;
          color: #6c757d;
        }
        .audience-btn:hover {
          border-color: #adb5bd;
          background: #f8f9fa;
        }
        .audience-btn.active {
          background: #4caf50;
          color: white;
          border-color: #4caf50;
        }
        @media (max-width: 600px) {
          .progress-container {
            flex-direction: row !important;
            align-items: center !important;
            gap: 8px !important;
          }
          .progress-label {
            writing-mode: vertical-rl;
            text-orientation: mixed;
            font-size: 9px;
            letter-spacing: 1px;
          }
          .audience-selector {
            flex-direction: column;
            gap: 4px;
            margin-top: 0;
          }
          .audience-btn {
            padding: 4px 8px;
            font-size: 11px;
          }
        }
      `}} />
      
      <h1 style={{ fontSize: 20, marginBottom: 10 }}>Welcome & Hare Krsna!</h1>
      <p style={{ fontSize: 15, color: "#6c757d", marginBottom: 16, lineHeight: 1.5 }}>
        A quiet self-study project to support deeper engagement with the Bhagavad Gita and Srimad Bhagavatam.
      </p>

      {/* Streak Counter or Welcome Message */}
      {streak > 0 ? (
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
      ) : (
        <div style={{
          padding: "12px 16px",
          background: "linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)",
          borderRadius: 10,
          boxShadow: "0 2px 8px rgba(99, 102, 241, 0.25)",
          color: "white",
          marginBottom: 16,
        }}>
          <div style={{ fontWeight: 600, fontSize: 16, marginBottom: 4 }}>
            ✨ Start Your Weekly Streak
          </div>
          <div style={{ fontSize: 13, opacity: 0.95, lineHeight: 1.4 }}>
            Complete at least one quiz each week to build your study streak!
          </div>
        </div>
      )}

      {/* Cards with Progress */}
<div style={{ display: "grid", gap: 12 }}>
  {/* BG Card */}
  <div
    className="scripture-card"
    onClick={() => window.location.href = `/bg/?audience=${bgAudience}`}
    style={{
      padding: 14,
      border: "1px solid #ddd",
      borderRadius: 10,
      display: "grid",
      gridTemplateColumns: "70px 1fr auto",
      gap: 12,
      alignItems: "center",
      minHeight: 100,
      background: "#fff",
      cursor: "pointer",
    }}
  >
    <img
      src="/images/bg-cover.jpg"
      alt="Bhagavad Gita"
      style={{
        width: 70,
        height: 70,
        objectFit: "cover",
        borderRadius: 6,
      }}
    />
    <div>
      <div style={{ fontWeight: 700, marginBottom: 4 }}>Bhagavad Gita</div>
      <div style={{ fontSize: 14, color: "#6c757d" }}>
        {bgProgress.completed}/{bgProgress.total} chapters
      </div>
    </div>
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 8 }} className="progress-container">
      <div className="progress-label" style={{ fontSize: 11, fontWeight: 600, color: "#6c757d", textTransform: "uppercase", letterSpacing: "0.5px" }}>
        Progress
      </div>
      <CircularProgress percentage={bgProgress.percentage} size={55} />
      <div className="audience-selector" onClick={(e) => e.stopPropagation()} style={{ marginTop: 0 }}>
        <button
          className={`audience-btn ${bgAudience === "adult" ? "active" : ""}`}
          onClick={() => setBgAudience("adult")}
        >
          Adults
        </button>
        <button
          className={`audience-btn ${bgAudience === "teens" ? "active" : ""}`}
          onClick={() => setBgAudience("teens")}
        >
          Teens
        </button>
        <button
          className={`audience-btn ${bgAudience === "kids" ? "active" : ""}`}
          onClick={() => setBgAudience("kids")}
        >
          Kids
        </button>
      </div>
    </div>
  </div>

  <div
    className="scripture-card"
    onClick={() => window.location.href = `/sb/?audience=${sbAudience}`}
    style={{
      padding: 14,
      border: "1px solid #ddd",
      borderRadius: 10,
      display: "grid",
      gridTemplateColumns: "70px 1fr auto",
      gap: 12,
      alignItems: "center",
      minHeight: 100,
      background: "#fff",
      cursor: "pointer",
    }}
  >
    <img
      src="/images/sb-cover.jpg"
      alt="Srimad Bhagavatam"
      style={{
        width: 70,
        height: 70,
        objectFit: "cover",
        borderRadius: 6,
      }}
    />
    <div>
      <div style={{ fontWeight: 700, marginBottom: 4 }}>Srimad Bhagavatam</div>
      <div style={{ fontSize: 14, color: "#6c757d" }}>
        {sbProgress.completed}/{sbProgress.total} chapters
      </div>
    </div>
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 8 }} className="progress-container">
      <div className="progress-label" style={{ fontSize: 11, fontWeight: 600, color: "#6c757d", textTransform: "uppercase", letterSpacing: "0.5px" }}>
        Progress
      </div>
      <CircularProgress percentage={sbProgress.percentage} size={55} />
      <div className="audience-selector" onClick={(e) => e.stopPropagation()} style={{ marginTop: 0 }}>
        <button
          className={`audience-btn ${sbAudience === "adult" ? "active" : ""}`}
          onClick={() => setSbAudience("adult")}
        >
          Adults
        </button>
        <button
          className={`audience-btn ${sbAudience === "teens" ? "active" : ""}`}
          onClick={() => setSbAudience("teens")}
        >
          Teens
        </button>
        <button
          className={`audience-btn ${sbAudience === "kids" ? "active" : ""}`}
          onClick={() => setSbAudience("kids")}
        >
          Kids
        </button>
      </div>
    </div>
  </div>

  {/* About Card - Moved to bottom */}
  <div
    className="scripture-card"
    onClick={() => setAboutExpanded(!aboutExpanded)}
    style={{
      padding: 14,
      border: "1px solid #ddd",
      borderRadius: 10,
      background: "#fff",
      cursor: "pointer",
      minHeight: aboutExpanded ? "auto" : 100,
    }}
  >
    <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
      <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
        <span style={{ fontSize: 32 }}>🪷</span>
        <div>
          <div style={{ fontWeight: 700, fontSize: 16 }}>About Vedabase Quiz</div>
          <div style={{ fontSize: 13, color: "#6c757d" }}>
            {aboutExpanded ? "Click to collapse" : "Click to learn more"}
          </div>
        </div>
      </div>
      <span style={{ fontSize: 20, color: "#6c757d" }}>
        {aboutExpanded ? "▲" : "▼"}
      </span>
    </div>

    {aboutExpanded && (
      <div style={{ paddingTop: 20, opacity: 0.92, lineHeight: 1.55, fontSize: 15 }} onClick={(e) => e.stopPropagation()}>
        <p style={{ marginTop: 0, marginBottom: 16 }}>
          Vedabase Quiz is a sacred self-study space to deepen understanding of the Bhagavad Gita and Srimad Bhagavatam.
        </p>

        <p style={{ marginBottom: 16 }}>
          The quizzes encourage careful reflection on verses and purports — slowing down study, clarifying key ideas, and revealing subtle
          insights over time.
        </p>

        <p style={{ marginBottom: 16 }}>
          Not a test or competition, but a support for steady engagement with the scriptures.
        </p>

        <h3 style={{ fontSize: 16, margin: "20px 0 12px", fontWeight: 600 }}>Purpose of the quizzes</h3>
        <p style={{ marginTop: 0, marginBottom: 12 }}>
          Reading sacred texts often happens quickly—especially for familiar chapters or well-known verses. Vedabase Quiz
          exists to gently counter that tendency by encouraging attentive reading and thoughtful reflection.
        </p>

        <ul style={{ marginTop: 8, marginBottom: 16, paddingLeft: 20 }}>
          <li style={{ marginBottom: 8 }}>
            For readers newer to these scriptures, the questions help highlight essential ideas and provide structure
            for careful study.
          </li>
          <li style={{ marginBottom: 8 }}>
            For experienced readers, the quizzes offer an opportunity to revisit familiar passages and notice
            subtleties that are easy to overlook.
          </li>
        </ul>

        <p style={{ marginBottom: 16 }}>
          The goal is not to memorize answers, but to deepen understanding over time.
        </p>

        <h3 style={{ fontSize: 16, margin: "20px 0 12px", fontWeight: 600 }}>Three age groups</h3>
        <p style={{ marginBottom: 16 }}>
          Each quiz is carefully tailored for <strong>kids</strong>, <strong>teens</strong>, and <strong>adults</strong> — ensuring that questions, explanations, and vocabulary are appropriate for each audience. Whether you're introducing children to sacred texts or deepening your own understanding, the quizzes adapt to different learning stages.
        </p>

        <h3 style={{ fontSize: 16, margin: "20px 0 12px", fontWeight: 600 }}>How the quizzes are designed</h3>
        <ul style={{ marginTop: 0, marginBottom: 16, paddingLeft: 20 }}>
          <li style={{ marginBottom: 8 }}>All questions are based <strong>only</strong> on translations and purports from <strong>Vedabase.io</strong></li>
          <li style={{ marginBottom: 8 }}>Each question is verified against the exact verse and purport it references</li>
          <li style={{ marginBottom: 8 }}>Questions follow the natural flow of each chapter, from context to conclusion</li>
          <li style={{ marginBottom: 8 }}>Explanations and direct verse links are provided after submission</li>
        </ul>

        <h3 style={{ fontSize: 16, margin: "20px 0 12px", fontWeight: 600 }}>A self-study space</h3>
        <p style={{ marginTop: 0, marginBottom: 12 }}>
          Vedabase Quiz is meant for individual, self-paced study. There is no pass or fail—only an opportunity to
          engage more thoughtfully with the texts.
        </p>
        <p style={{ marginBottom: 16 }}>
          Readers are encouraged to take their time, revisit verses, and use the quizzes as a companion to regular
          reading rather than a replacement for it.
        </p>

        <h3 style={{ fontSize: 16, margin: "20px 0 12px", fontWeight: 600 }}>Credits and acknowledgement</h3>
        <p style={{ marginTop: 0, marginBottom: 12 }}>
          All scriptural content referenced on this site is sourced from <strong>Vedabase.io</strong>, which makes the
          works of <strong>His Divine Grace A. C. Bhaktivedanta Swami Prabhupada</strong> freely available for study.
        </p>
        <p style={{ marginBottom: 12 }}>
          The original translations and purports are published by the{" "}
          <strong>Bhaktivedanta Book Trust (BBT)</strong>.
        </p>
        <p style={{ marginTop: 8, marginBottom: 0, fontSize: 14, opacity: 0.85 }}>
          Vedabase Quiz is an independent, non-commercial project and is not affiliated with Vedabase.io or the
          Bhaktivedanta Book Trust.
        </p>
      </div>
    )}
  </div>
</div>

    </main>
  );
}
