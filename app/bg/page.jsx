import Link from "next/link";

export default function BgSelectorPage({ searchParams }) {
  const audience = searchParams?.audience || "adult";
  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: "24px 16px" }}>
      <h1 style={{ fontSize: 28, margin: "0 0 10px" }}>Bhagavad Gita</h1>
      {/* Audience filter bar */}
      <div className="filterBar" style={{ marginTop: 10, marginBottom: 18 }}>
        <Link href="/bg/?audience=adult">
          <button className={`filterBtn ${audience === "adult" ? "filterBtnActive" : ""}`}>Adult</button>
        </Link>
        <Link href="/bg/?audience=teens">
          <button className={`filterBtn ${audience === "teens" ? "filterBtnActive" : ""}`}>Teens</button>
        </Link>
        <Link href="/bg/?audience=kids">
          <button className={`filterBtn ${audience === "kids" ? "filterBtnActive" : ""}`}>Kids</button>
        </Link>
      </div>
      {/* Card-based options */}
      <div className="chapterList">
        <Link href={`/bg/themes?audience=${audience}`} className="chapterListItem">
          <div className="chapterListContent">
            <div className="chapterListHeader">Themes</div>
            <div className="chapterListTitle">Explore key themes and concepts in the Gita</div>
          </div>
        </Link>
        <Link href={`/bg/chapters?audience=${audience}`} className="chapterListItem">
          <div className="chapterListContent">
            <div className="chapterListHeader">Chapters</div>
            <div className="chapterListTitle">Browse all chapters and quizzes</div>
          </div>
        </Link>
      </div>
    </main>
  );
}
