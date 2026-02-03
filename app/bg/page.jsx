import Link from "next/link";

export default function BgSelectorPage() {
  return (
    <div className="selectorPage">
      <h1>Bhagavad Gita</h1>
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
    </div>
  );
}
