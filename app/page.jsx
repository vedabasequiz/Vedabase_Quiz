export default function HomePage() {
  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: "24px 16px" }}>
      <h1 style={{ fontSize: 20, marginBottom: 10 }}>Welcome & Hare Krsna!</h1>

      {/* NEW intro text (mobile-tight) */}
      <div style={{ opacity: 0.9, marginTop: 0, lineHeight: 1.5 }}>
        <p style={{ marginTop: 0, marginBottom: 10 }}>
          Vedabase Quiz is a quiet self-study space to deepen understanding of the Bhagavad Gita and Srimad Bhagavatam.
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
      display: "grid",
      gridTemplateColumns: "88px 1fr",
      gap: 12,
      alignItems: "center",
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
      <div style={{ fontWeight: 700 }}>Bhagavad Gita</div>
    </div>
  </a>

  <a
    href="/sb/"
    style={{
      padding: 14,
      border: "1px solid #ddd",
      borderRadius: 10,
      textDecoration: "none",
      color: "inherit",
      display: "grid",
      gridTemplateColumns: "88px 1fr",
      gap: 12,
      alignItems: "center",
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
      <div style={{ fontWeight: 700 }}>Srimad Bhagavatam</div>
    </div>
  </a>
</div>

       {/* Collapsible section */}
      <details style={{ marginTop: 14, marginBottom: 18 }}>
        <summary
          style={{
            cursor: "pointer",
            fontWeight: 700,
            fontSize: 16,
            padding: "8px 0",
          }}
        >
          How the quizzes are designed
        </summary>

        <div style={{ paddingTop: 8, paddingLeft: 12, opacity: 0.9, lineHeight: 1.5 }}>
          <ul style={{ marginTop: 0, marginBottom: 10 }}>
            <li>Based only on Vedabase.io (Srila Prabhupada’s translations and purports)</li>
            <li>Every question is verified against the exact verse/purport</li>
            <li>Focus on understanding (not memorization)</li>
            <li>Follows the chapter’s natural flow</li>
            <li>Instant explanations with direct verse links</li>
          </ul>

          <p style={{ marginTop: 0, marginBottom: 0 }}>
            Take your time: submit, review, revisit verses, and continue.
          </p>
        </div>
      </details>

    </main>
  );
}
