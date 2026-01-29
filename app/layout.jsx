import "./globals.css";

export const metadata = {
  title: "Vedabase Quiz",
  description: "Self-study quizzes for Bhagavad Gita and Srimad Bhagavatam",
};

export const viewport = {
  width: "device-width",
  initialScale: 1,
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body
        style={{
          fontFamily:
            "system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif",
        }}
      >
        {/* Site header */}
        <div style={{ padding: "14px 16px", borderBottom: "1px solid #eee" }}>
          <a
            href="/"
            style={{ textDecoration: "none", fontWeight: 800, color: "#111" }}
          >
            Vedabase Quiz
          </a>
        </div>

        {/* Page content */}
        {children}

        {/* Minimal footer */}
        <footer
  style={{
    marginTop: 20,
    borderTop: "1px solid #eee",
  }}
>
  <div
    style={{
      maxWidth: 900,
      margin: "0 auto",
      padding: "16px 16px 20px",
      fontSize: 13,
      color: "#666",
      lineHeight: 1.6,
      textAlign: "center",
    }}
  >
    <div style={{ fontSize: 24, marginBottom: 6, opacity: 0.6 }}>
  🪷
</div>

    Grateful acknowledgment to <a href="https://vedabase.io" target="_blank" rel="noopener noreferrer" style={{ color: "#666", textDecoration: "underline" }}>Vedabase.io</a> for making the works of His Divine Grace A.C. Bhaktivedanta Swami Prabhupada freely accessible. All scriptural content, translations, purports, and cover images © Bhaktivedanta Book Trust.
    <div style={{ marginTop: 8 }}>
      Vedabase Quiz is an independent, non-commercial project.
    </div>
  </div>
</footer>

      </body>
    </html>
  );
}
