import Link from "next/link";

export default function SbSelectorPage({ searchParams }) {
  const audience = searchParams?.audience || "adult";
  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: "24px 16px" }}>
      {/* Breadcrumb */}
      <div style={{ fontSize: 14, opacity: 0.8, marginBottom: 10 }}>
        <Link href="/">Home</Link>
        <span style={{ opacity: 0.6 }}> / </span>
        <span>Shrimad Bhagavatam</span>
        <span style={{ opacity: 0.6 }}> / </span>
        <span>{audience.charAt(0).toUpperCase() + audience.slice(1)}</span>
      </div>
      <h1 style={{ fontSize: 28, margin: "0 0 10px" }}>Shrimad Bhagavatam</h1>
      {/* Audience filter bar */}
      <div className="filterBar" style={{ marginTop: 10, marginBottom: 18 }}>
        <Link href="/sb/?audience=adult">
          <button className={`filterBtn ${audience === "adult" ? "filterBtnActive" : ""}`}>Adult</button>
        </Link>
        <Link href="/sb/?audience=teens">
          <button className={`filterBtn ${audience === "teens" ? "filterBtnActive" : ""}`}>Teens</button>
        </Link>
        <Link href="/sb/?audience=kids">
          <button className={`filterBtn ${audience === "kids" ? "filterBtnActive" : ""}`}>Kids</button>
        </Link>
      </div>
      {/* Card-based options */}
      <div className="chapterList">
        <Link href={`/sb/themes?audience=${audience}`} className="chapterListItem">
          <div className="chapterListContent">
            <div className="chapterListHeader">Themes</div>
            <div className="chapterListTitle">Explore key themes and stories in the Bhagavatam</div>
          </div>
        </Link>
        <Link href={`/sb/cantos?audience=${audience}`} className="chapterListItem">
          <div className="chapterListContent">
            <div className="chapterListHeader">Cantos</div>
            <div className="chapterListTitle">Browse all cantos and quizzes</div>
          </div>
        </Link>
      </div>
      <div style={{ marginTop: 18 }}>
        <Link href="/" className="backLink">&larr; Back</Link>
      </div>
    </main>
  );
}
