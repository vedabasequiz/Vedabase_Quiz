import Link from "next/link";

const SB_THEMES = [
  { title: "Gajendra Moksha — Helpless Surrender", desc: "The story of Gajendra's surrender and deliverance." },
  { title: "Prahlada Maharaja — Pure Devotion vs Power & Fear", desc: "Prahlada's unwavering devotion in the face of adversity." },
  { title: "Dhruva Maharaja — From Desire to Purification", desc: "Dhruva's journey from material desire to spiritual realization." },
  { title: "Ajāmila — The Power of the Holy Name", desc: "Ajāmila's redemption through chanting the holy name." },
  { title: "Bharata Maharaja — Subtle Attachment & Fall-Down", desc: "Lessons from Bharata Maharaja's attachment and rebirth." },
  { title: "Pariksit & Sukadeva — Transformation Through Hearing", desc: "The transformative power of hearing Srimad Bhagavatam." },
];

export default function SbThemesPage({ searchParams }) {
  const audience = searchParams?.audience || "adult";
  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: "24px 16px" }}>
      <h1 style={{ fontSize: 28, margin: "0 0 10px" }}>SB Themes</h1>
      {/* Audience filter bar */}
      <div className="filterBar" style={{ marginTop: 10, marginBottom: 18 }}>
        <Link href="/sb/themes?audience=adult">
          <button className={`filterBtn ${audience === "adult" ? "filterBtnActive" : ""}`}>Adult</button>
        </Link>
        <Link href="/sb/themes?audience=teens">
          <button className={`filterBtn ${audience === "teens" ? "filterBtnActive" : ""}`}>Teens</button>
        </Link>
        <Link href="/sb/themes?audience=kids">
          <button className={`filterBtn ${audience === "kids" ? "filterBtnActive" : ""}`}>Kids</button>
        </Link>
      </div>
      {/* Card-based theme list */}
      <div className="chapterList">
        {SB_THEMES.map((theme, idx) => (
          <div key={idx} className="chapterListItem chapterListItemDisabled">
            <div className="chapterListContent">
              <div className="chapterListHeader">{theme.title}</div>
              <div className="chapterListTitle">{theme.desc}</div>
            </div>
            <div className="chapterListRight">
              <div className="chapterListComingSoon">Coming soon</div>
            </div>
          </div>
        ))}
      </div>
      <Link href={`/sb?audience=${audience}`} className="backLink">&larr; Back</Link>
    </main>
  );
}
