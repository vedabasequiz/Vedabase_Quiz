import Link from "next/link";
import { redirect } from "next/navigation";
import { getBgAvailability } from "../../lib/quizLoader";

function getAudienceFromSearchParams(searchParams) {
  const a = searchParams?.audience;
  const v = Array.isArray(a) ? a[0] : a;
  if (v === "kids" || v === "teens" || v === "adult") return v;
  return "adult"; // default
}

export default function BgIndex({ searchParams }) {
  // Make default explicit in URL so the UI always has a selected tab
  if (!searchParams?.audience) {
    redirect("/bg/?audience=adult");
  }

  const availability = getBgAvailability();
  const audience = getAudienceFromSearchParams(searchParams);

  const chapters = Array.from({ length: 18 }, (_, i) => i + 1);

  function linkFor(chapter, aud) {
    const key = `${chapter}-${aud}`;
    const meta = availability.get(key);
    return meta ? `/quiz/${meta.slug}/` : null;
  }

  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: "24px 16px" }}>
      <h1 style={{ fontSize: 28, marginBottom: 10 }}>Bhagavad Gita</h1>

      {/* Tabs: Adult / Teens / Kids */}
      <div className="filterBar filterBarTight" style={{ marginBottom: 18 }}>
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

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))",
          gap: 12,
        }}
      >
        {chapters.map((ch) => {
          const selectedUrl = linkFor(ch, audience);
          const isAvailable = !!selectedUrl;

          const cardInner = (
            <div className={`chapterCard ${isAvailable ? "" : "chapterCardDisabled"}`}>
              <div style={{ fontWeight: 800, marginBottom: 8 }}>Chapter {ch}</div>

              {isAvailable ? (
                <div style={{ opacity: 0.8, fontSize: 14 }}>Open quiz</div>
              ) : (
                <div className="comingSoonBadge">{audience[0].toUpperCase() + audience.slice(1)}: coming soon</div>
              )}
            </div>
          );

          // Entire card clickable ONLY when quiz exists
          return isAvailable ? (
            <Link key={ch} href={selectedUrl} className="cardLink">
              {cardInner}
            </Link>
          ) : (
            <div key={ch}>{cardInner}</div>
          );
        })}
      </div>

      <div style={{ marginTop: 18 }}>
        <Link href="/">Back to home</Link>
      </div>
    </main>
  );
}
