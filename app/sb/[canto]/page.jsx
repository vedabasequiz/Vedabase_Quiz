import Link from "next/link";
import { redirect } from "next/navigation";
import { getSbAvailability, listSbCantos, listSbChaptersInCanto } from "../../../lib/quizLoader";

export function generateStaticParams() {
  return listSbCantos().map((c) => ({ canto: String(c) }));
}

function getAudienceFromSearchParams(searchParams) {
  const a = searchParams?.audience;
  const v = Array.isArray(a) ? a[0] : a;
  return v === "kids" ? "kids" : "adult"; // default adult
}

export default function SbCantoPage({ params, searchParams }) {
  // UX: make default explicit in URL
  if (!searchParams?.audience) {
    redirect(`/sb/${params.canto}/?audience=adult`);
  }

  const cantoNum = Number(params.canto);
  const audience = getAudienceFromSearchParams(searchParams);
  const availability = getSbAvailability();

  // We still show a reasonable list even if many chapters aren't added yet
  const existing = listSbChaptersInCanto(cantoNum);
  const maxChapter = existing.length > 0 ? Math.max(...existing) : 5;
  const chapters = Array.from({ length: Math.max(maxChapter, 5) }, (_, i) => i + 1);

  function linkFor(chapter, aud) {
    const key = `${cantoNum}/${chapter}-${aud}`;
    const meta = availability.get(key);
    return meta ? `/quiz/${meta.slug}/` : null;
  }

  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: "24px 16px" }}>
      <h1 style={{ fontSize: 28, marginBottom: 10 }}>Srimad Bhagavatam - Canto {cantoNum}</h1>

      {/* Tabs: Adult / Kids only */}
      <div className="filterBar" style={{ marginBottom: 18 }}>
        <Link href={`/sb/${cantoNum}/?audience=adult`}>
          <button className={`filterBtn ${audience === "adult" ? "filterBtnActive" : ""}`}>Adult</button>
        </Link>
        <Link href={`/sb/${cantoNum}/?audience=kids`}>
          <button className={`filterBtn ${audience === "kids" ? "filterBtnActive" : ""}`}>Kids</button>
        </Link>
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))", gap: 12 }}>
        {chapters.map((ch) => {
          const adultUrl = linkFor(ch, "adult");
          const kidsUrl = linkFor(ch, "kids");

          const selectedUrl = audience === "kids" ? kidsUrl : adultUrl;
          const label = audience === "kids" ? "Kids quiz" : "Adult quiz";
          const comingSoon = audience === "kids" ? "Kids: coming soon" : "Adult: coming soon";

          return (
            <div key={ch} style={{ border: "1px solid #ddd", borderRadius: 10, padding: 12 }}>
              <div style={{ fontWeight: 800, marginBottom: 10 }}>Chapter {ch}</div>

              {/* Only show the selected audience */}
              {selectedUrl ? (
                <Link href={selectedUrl}>{label}</Link>
              ) : (
                <span className="comingSoonBadge">{comingSoon}</span>
              )}
            </div>
          );
        })}
      </div>

      <div style={{ marginTop: 18 }}>
        <Link href="/sb/?audience=adult">Back to cantos</Link>
      </div>
    </main>
  );
}
