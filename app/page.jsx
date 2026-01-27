export default function HomePage() {
  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: "24px 16px" }}>
      <h1 style={{ fontSize: 32, marginBottom: 10 }}>Vedabase Quiz</h1>

      <p style={{ opacity: 0.85, marginTop: 0, lineHeight: 1.5 }}>
        Vedabase Quiz is a self-study space to understand the Bhagavad Gita and Srimad Bhagavatam more deeply.
        These are not tests or competitions - they are meant to slow down reading, clarify key ideas, and support thoughtful study.
      </p>

      {/* Collapsible section */}
      <details style={{ marginTop: 14, marginBottom: 18 }}>
        <summary
          style={{
            cursor: "pointer",
            fontWeight: 700,
            fontSize: 16,
          }}
        >
          How the quizzes are designed
        </summary>

        <div style={{ paddingTop: 10, paddingLeft: 12, opacity: 0.9, lineHeight: 1.5 }}>
          <ul style={{ marginTop: 0 }}>
            <li>Based only on Vedabase.io (Srila Prabhupada translations and purports)</li>
            <li>Each question is checked against the exact verse/purport</li>
            <li>Focus on understanding (not memorization)</li>
            <li>Questions follow the flow of the chapter</li>
            <li>Instant explanations with direct verse links</li>
          </ul>

          <p style={{ marginTop: 10, marginBottom: 0 }}>
            Self-study pace: submit, review explanations, revisit verses, and learn steadily.
          </p>
        </div>
      </details>

      {/* Cards */}
      <div style={{ display: "grid", gap: 12 }}>
        <a
          href="/bg/"
          style={{
            padding: 14,
            border: "1px solid #ddd",
            borderRadius: 10,
            textDecoration: "none",
            color: "inherit",
          }}
        >
          <div style={{ fontWeight: 700 }}>Bhagavad Gita</div>
          <div style={{ opacity: 0.8 }}>Chapters 1-18</div>
        </a>

        <a
          href="/sb/"
          style={{
            padding: 14,
            border: "1px solid #ddd",
            borderRadius: 10,
            textDecoration: "none",
            color: "inherit",
          }}
        >
          <div style={{ fontWeight: 700 }}>Srimad Bhagavatam</div>
          <div style={{ opacity: 0.8 }}>Cantos 1-12</div>
        </a>
      </div>
    </main>
  );
}
