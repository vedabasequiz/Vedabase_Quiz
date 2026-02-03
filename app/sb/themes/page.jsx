import Link from "next/link";

const SB_THEMES = [
  { title: "Gajendra Moksha — Helpless Surrender", desc: "The story of Gajendra's surrender and deliverance." },
  { title: "Prahlada Maharaja — Pure Devotion vs Power & Fear", desc: "Prahlada's unwavering devotion in the face of adversity." },
  { title: "Dhruva Maharaja — From Desire to Purification", desc: "Dhruva's journey from material desire to spiritual realization." },
  { title: "Ajāmila — The Power of the Holy Name", desc: "Ajāmila's redemption through chanting the holy name." },
  { title: "Bharata Maharaja — Subtle Attachment & Fall-Down", desc: "Lessons from Bharata Maharaja's attachment and rebirth." },
  { title: "Pariksit & Sukadeva — Transformation Through Hearing", desc: "The transformative power of hearing Srimad Bhagavatam." },
];

export default function SbThemesPage() {
  return (
    <div className="themeListPage">
      <h1>SB Themes</h1>
      <div className="themeList">
        {SB_THEMES.map((theme, idx) => (
          <div key={idx} className="themeCard themeCardDisabled">
            <div className="themeCardTitle">{theme.title}</div>
            <div className="themeCardDesc">{theme.desc}</div>
            <div className="themeCardComingSoon">Coming soon</div>
          </div>
        ))}
      </div>
      <Link href="/sb" className="backLink">&larr; Back</Link>
    </div>
  );
}
