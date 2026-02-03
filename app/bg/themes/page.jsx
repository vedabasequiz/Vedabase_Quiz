import Link from "next/link";

const BG_THEMES = [
  { title: "Five Topics of BG", desc: "The five foundational subjects of the Gita." },
  { title: "Bhakti Yoga", desc: "The path of devotion as taught in the Gita." },
  { title: "Three Modes of Nature", desc: "Sattva, Rajas, and Tamas explained." },
  { title: "Renunciation: Real vs False", desc: "True renunciation versus external detachment." },
  { title: "Knowledge vs Speculation", desc: "The difference between realized knowledge and mental speculation." },
];

export default function BgThemesPage() {
  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: "24px 16px" }}>
      <h1 style={{ fontSize: 28, margin: "0 0 10px" }}>BG Themes</h1>
      <div className="themeList">
        {BG_THEMES.map((theme, idx) => (
          <div key={idx} className="themeCard themeCardDisabled">
            <div className="themeCardTitle">{theme.title}</div>
            <div className="themeCardDesc">{theme.desc}</div>
            <div className="themeCardComingSoon">Coming soon</div>
          </div>
        ))}
      </div>
      <Link href="/bg" className="backLink">&larr; Back</Link>
    </main>
  );
}
