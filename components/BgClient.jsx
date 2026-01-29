"use client";
import { useState, useEffect } from "react";
import Link from "next/link";
import { formatTimeAgo } from "../lib/quizProgress";

export default function BgClient({ chapters, availability, titles, initialAudience }) {
  const [quizResults, setQuizResults] = useState({});
  
  const audience = initialAudience;
  const audienceLabel = audience.charAt(0).toUpperCase() + audience.slice(1);

  useEffect(() => {
    try {
      const stored = localStorage.getItem("vedabaseQuizResults");
      if (stored) setQuizResults(JSON.parse(stored));
    } catch (e) {
      // Ignore localStorage errors
    }
  }, []);

  function linkFor(chapter, aud) {
    const key = `${chapter}-${aud}`;
    const meta = availability[key];
    return meta ? `/quiz/${meta.slug}/` : null;
  }

  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: "24px 16px" }}>
      {/* Breadcrumb */}
      <div style={{ fontSize: 14, opacity: 0.8, marginBottom: 10 }}>
        <Link href="/">Home</Link>
        <span style={{ opacity: 0.6 }}> / </span>
        <span>Bhagavad Gita</span>
        <span style={{ opacity: 0.6 }}> / </span>
        <span>{audienceLabel}</span>
      </div>

      <h1 style={{ fontSize: 28, margin: "0 0 10px" }}>Bhagavad Gita</h1>

      {/* Tabs */}
      <div className="filterBar" style={{ marginTop: 10, marginBottom: 18 }}>
        <Link href="/bg/?audience=adult">
          <button className={`filterBtn ${audience === "adult" ? "filterBtnActive" : ""}`}>Adult</button>
        </Link>
        <Link href="/bg/?audience=teens">
          <button className={`filterBtn ${audience === "teens" ? "filterBtnActive" : ""}`}>Teens</button>
        </Link>
        <Link href="/bg/?audience=kids">
          <button className={`filterBtn ${audience === "kids" ? "filterBtnActive" : ""}`}>Kids</button>
        </Link>
      </div>

      {/* Cards */}
      <div className="chapterGrid">
        {chapters.map((ch) => {
          const selectedUrl = linkFor(ch, audience);
          const isAvailable = !!selectedUrl;
          const title = titles[ch] || "";
          
          // Get quiz result for this chapter
          const slug = selectedUrl ? selectedUrl.replace(/^\/quiz\//, "").replace(/\/$/, "") : null;
          const result = slug ? quizResults[slug] : null;

          const cardInner = (
            <div className={`chapterCard ${isAvailable ? "" : "chapterCardDisabled"} ${result ? "chapterCardCompleted" : ""}`}>
              <div>
                <div style={{ fontWeight: 800, marginBottom: 8 }}>Chapter {ch}</div>
                {title ? <div className="chapterTitle">{title}</div> : null}
                
                {/* Progress badge */}
                {result && (
                  <div style={{ marginTop: 8, fontSize: 13 }}>
                    <div className="completionBadge">
                      ✓ {result.score}/{result.total} ({result.percentage}%)
                    </div>
                    <div className="lastPlayed">{formatTimeAgo(result.date)}</div>
                  </div>
                )}
              </div>

              {!isAvailable ? (
                <div className="comingSoonBadge">{audienceLabel}: coming soon</div>
              ) : (
                <div />
              )}
            </div>
          );

          return isAvailable ? (
            <Link key={ch} href={selectedUrl} className="cardLink">
              {cardInner}
            </Link>
          ) : (
            <div key={ch} className="cardLink cardLinkDisabled">
              {cardInner}
            </div>
          );
        })}
      </div>

      <div style={{ marginTop: 18 }}>
        <Link href="/">Back to home</Link>
      </div>
    </main>
  );
}
