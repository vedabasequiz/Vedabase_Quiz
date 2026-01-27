import Link from "next/link";

export default function HomePage() {
  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: "24px 16px" }}>
      <h1 style={{ fontSize: 32, marginBottom: 10 }}>Vedabase Quiz</h1>
      <p style={{ opacity: 0.85, marginTop: 0 }}>
      <b>Vedabase Quiz</b> is a self-study space for readers who want to understand the Bhagavad Gita and Srimad Bhagavatam more deeply.

These quizzes are not tests or competitions. They are meant to slow down reading, clarify important ideas, and support thoughtful study.
      </p>

      <div style={{ display: "grid", gap: 12, marginTop: 18 }}>
        <a
          href="/bg/"
          style={{
            padding: 14,
            border: "1px solid #ddd",
            borderRadius: 10,
            textDecoration: "none",
          }}
        >
          <details style={{ marginTop: 16 }}>
  <summary
    style={{
      cursor: "pointer",
      fontWeight: 600,
      fontSize: 16,
      marginBottom: 8,
    }}
  >
    How the quizzes are made
  </summary>

  <div style={{ paddingLeft: 12, opacity: 0.9 }}>
    <ul style={{ marginTop: 8 }}>
      <li>Based only on Vedabase.io (Srila Prabhupada’s translations and purports)</li>
      <li>Each question is checked against the exact verse and purport</li>
      <li>Focus on understanding meaning, not memorization</li>
      <li>Questions follow the natural flow of each chapter</li>
      <li>Instant explanations with direct verse links</li>
    </ul>

    <p style={{ marginTop: 10 }}>
      These quizzes are meant for quiet self-study. Take your time. Revisit verses.
      There is no pass or fail — only learning.
    </p>
  </div>
</details>
        </div>

          <div style={{ fontWeight: 700 }}>Bhagavad Gita</div>
          <div style={{ opacity: 0.8 }}>Chapters 1–18</div>
        </a>

        <a
          href="/sb/"
          style={{
            padding: 14,
            border: "1px solid #ddd",
            borderRadius: 10,
            textDecoration: "none",
          }}
        >
          <div style={{ fontWeight: 700 }}>Srimad Bhagavatam</div>
          <div style={{ opacity: 0.8 }}>Cantos 1-12</div>
        </a>
      </div>
    </main>
  );
}
