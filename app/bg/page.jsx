import Link from "next/link";

export default function BgSelectorPage() {
  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: "24px 16px" }}>
      <h1 style={{ fontSize: 28, margin: "0 0 10px" }}>Bhagavad Gita</h1>
      <div className="selectorOptions">
        <Link href="/bg/themes" className="selectorCard">
          <div className="selectorCardTitle">BG Themes</div>
          <div className="selectorCardDesc">Explore key themes and concepts in the Gita</div>
        </Link>
        <Link href="/bg/chapters" className="selectorCard">
          <div className="selectorCardTitle">BG Chapters</div>
          <div className="selectorCardDesc">Browse all chapters and quizzes</div>
        </Link>
      </div>
    </main>
  );
}
