import Link from "next/link";

export default function SbSelectorPage() {
  return (
    <div className="selectorPage">
      <h1>Shrimad Bhagavatam</h1>
      <div className="selectorOptions">
        <Link href="/sb/themes" className="selectorCard">
          <div className="selectorCardTitle">SB Themes</div>
          <div className="selectorCardDesc">Explore key themes and stories in the Bhagavatam</div>
        </Link>
        <Link href="/sb/cantos" className="selectorCard">
          <div className="selectorCardTitle">SB Cantos</div>
          <div className="selectorCardDesc">Browse all cantos and quizzes</div>
        </Link>
      </div>
    </div>
  );
}
