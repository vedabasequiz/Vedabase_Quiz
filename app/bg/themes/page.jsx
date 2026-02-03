import Link from "next/link";

const BG_THEMES = [
  { title: "Five Topics of BG", desc: "The five foundational subjects of the Gita." },
  { title: "Bhakti Yoga", desc: "The path of devotion as taught in the Gita." },
  { title: "Three Modes of Nature", desc: "Sattva, Rajas, and Tamas explained." },
  { title: "Renunciation: Real vs False", desc: "True renunciation versus external detachment." },
  { title: "Knowledge vs Speculation", desc: "The difference between realized knowledge and mental speculation." },
];

export default function BgThemesPage({ searchParams }) {
  const audience = searchParams?.audience || "adult";
  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: "24px 16px" }}>
      {/* Breadcrumb */}
      <div style={{ fontSize: 14, opacity: 0.8, marginBottom: 10 }}>
        <Link href="/">Home</Link>
        <span style={{ opacity: 0.6 }}> / </span>
        <Link href={`/bg?audience=${audience}`}>Bhagavad Gita</Link>
        <span style={{ opacity: 0.6 }}> / </span>
        <span>{audience.charAt(0).toUpperCase() + audience.slice(1)}</span>
        <span style={{ opacity: 0.6 }}> / </span>
        <span>Themes</span>
      </div>
      <h1 style={{ fontSize: 28, margin: "0 0 10px" }}>BG Themes</h1>
      {/* Audience filter bar */}
      <div className="filterBar" style={{ marginTop: 10, marginBottom: 18 }}>
        <Link href="/bg/themes?audience=adult">
          <button className={`filterBtn ${audience === "adult" ? "filterBtnActive" : ""}`}>Adult</button>
        </Link>
        <Link href="/bg/themes?audience=teens">
          <button className={`filterBtn ${audience === "teens" ? "filterBtnActive" : ""}`}>Teens</button>
        </Link>
        <Link href="/bg/themes?audience=kids">
          <button className={`filterBtn ${audience === "kids" ? "filterBtnActive" : ""}`}>Kids</button>
        </Link>
      </div>
      {/* Card-based theme list */}
      <div className="chapterList">
        {BG_THEMES.map((theme, idx) => (
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
      <Link href={`/bg?audience=${audience}`} className="backLink">&larr; Back</Link>
    </main>
  );
}
