import Link from "next/link";
import { redirect } from "next/navigation";
import { getBgAvailability } from "../../lib/quizLoader";

// BG Chapter titles (ASCII-only)
const BG_CHAPTER_TITLES = {
  1: "Observing the Armies on the Battlefield of Kuruksetra",
  2: "Contents of the Gita Summarized",
  3: "Karma-yoga",
  4: "Transcendental Knowledge",
  5: "Karma-yoga - Action in Krsna Consciousness",
  6: "Dhyana-yoga",
  7: "Knowledge of the Absolute",
  8: "Attaining the Supreme",
  9: "The Most Confidential Knowledge",
  10: "The Opulence of the Absolute",
  11: "The Universal Form",
  12: "Devotional Service",
  13: "Nature, the Enjoyer and Consciousness",
  14: "The Three Modes of Material Nature",
  15: "The Yoga of the Supreme Person",
  16: "The Divine and Demoniac Natures",
  17: "The Divisions of Faith",
  18: "Conclusion - The Perfection of Renunciation",
};

function getAudienceFromSearchParams(searchParams) {
  const a = searchParams?.audience;
  const v = Array.isArray(a) ? a[0] : a;
  return v === "kids" ? "kids" : "adult"; // default adult
}

export default function BgIndex({ searchParams }) {
  // Default audience -> explicit URL
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
      {/* Breadcrumb */}
      <div style={{ marginBottom: 10, fontSize: 14, opacity: 0.75 }}>
        <Link href="/">Home</Link> <span style={{ opacity: 0.6 }}>/</span> <span>Bhagavad Gita</span>
      </div>

      <h1 style={{ fontSize: 28, marginBottom: 10 }}>Bhagavad Gita</h1>

      {/* Tabs: Adult / Kids only */}
      <div className="filterBar" style={{ marginBottom: 18 }}>
        <Link href="/bg/?audience=adult">
          <button className={`filterBtn ${audience === "adult" ? "filterBtnActive" : ""}`}>Adult</button>
        </Link>
        <Link href="/bg/?audience=kids">
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

          const title = BG_CHAPTER_TITLES[ch] || "";

          return (
            <div key={ch} style={{ border: "1px solid #ddd", borderRadius: 10, padding: 12 }}>
              <div style={{ fontWeight: 800, marginBottom: 6 }}>Chapter {ch}</div>

              {title ? (
                <div style={{ opacity: 0.75, fontSize: 14, lineHeight: 1.25, marginBottom: 10 }}>
                  {title}
                </div>
              ) : (
                <div style={{ marginBottom: 10 }} />
              )}

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
        <Link href="/">Back to home</Link>
      </div>
    </main>
  );
}
