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
            marginTop: 48,
            padding: "18px 16px",
            borderTop: "1px solid #eee",
            fontSize: 13,
            color: "#666",
            lineHeight: 1.6,
          }}
        >
          Vedabase Quiz is a quiet, non-commercial self-study project based on
          Srila Prabhupada’s translations and purports as published on Vedabase.io.
        </footer>
      </body>
    </html>
  );
}
