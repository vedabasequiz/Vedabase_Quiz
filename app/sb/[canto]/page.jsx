import Link from "next/link";
import { redirect } from "next/navigation";
import { getSbAvailability, listSbCantos, listSbChaptersInCanto } from "../../../lib/quizLoader";

// Vedabase Canto titles (ASCII-only)
const SB_CANTO_TITLES = {
  1: "Creation",
  2: "The Cosmic Manifestation",
  3: "The Status Quo",
  4: "The Creation of the Fourth Order",
  5: "The Creative Impetus",
  6: "Prescribed Duties for Mankind",
  7: "The Science of God",
  8: "Withdrawal of the Cosmic Creations",
  9: "Liberation",
  10: "The Summum Bonum",
  11: "General History",
  12: "The Age of Deterioration",
};

// Small mapping (expand as you publish more)
// ASCII-only spellings.
const SB_CHAPTER_TITLES = {
  1: {
    1: "Questions by the Sages",
    2: "Divinity and Divine Service",
    3: "Krsna Is the Source of All Incarnations",
    4: "The Appearance of Sri Narada",
    5: "Narada's Instructions on Srimad-Bhagavatam for Vyasadeva",
    6: "Conversation Between Narada and Vyasadeva",
    7: "The Son of Drona Punished",
    8: "Prayers by Queen Kunti and Pariksit Saved",
    9: "The Passing Away of Bhismadeva in the Presence of Lord Krsna",
    10: "Departure of Lord Krsna for Dvaraka",
    11: "Lord Krsna's Entrance into Dvaraka",
    12: "Birth of Emperor Pariksit",
    13: "Dhritarastra Quits Home",
    14: "The Disappearance of Lord Krsna",
    15: "The Pandavas Retire Timely",
    16: "How Pariksit Received the Age of Kali",
    17: "Punishment and Reward of Kali",
    18: "Maharaja Pariksit Cursed by a Brahmana Boy",
    19: "The Appearance of Sukadeva Gosvami",
  },
};

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

  function chapterTitleFor(canto, chapter) {
    return SB_CHAPTER_TITLES[canto] && SB_CHAPTER_TITLES[canto][chapter] ? SB_CHAPTER_TITLES[canto][chapter] : "";
  }

  const cantoTitle = SB_CANTO_TITLES[cantoNum] || "";

  return (
    <main style={{ maxWidth: 900, margin: "0 auto", padding: "24px 16px" }}>
     <div style={{ marginBottom: 10, fontSize: 14, opacity: 0.75 }}>
  <Link href="/">Home</Link> <span style={{ opacity: 0.6 }}>/</span>{" "}
  <Link href={`/sb/?audience=${audience}`}>Srimad Bhagavatam</Link> <span style={{ opacity: 0.6 }}>/</span>{" "}
  <span>Canto {cantoNum}</span>
</div>

      <h1 style={{ fontSize: 28, marginBottom: 10 }}>
        Srimad Bhagavatam - Canto {cantoNum}
        {cantoTitle ? `: ${cantoTitle}` : ""}
      </h1>

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

          const title = chapterTitleFor(cantoNum, ch);

          return (
            <div key={ch} style={{ border: "1px solid #ddd", borderRadius: 10, padding: 12 }}>
              <div style={{ fontWeight: 800, marginBottom: 6 }}>Chapter {ch}</div>

              {/* Chapter title (if available in mapping) */}
              {title ? (
                <div style={{ opacity: 0.75, fontSize: 14, lineHeight: 1.25, marginBottom: 10 }}>
                  {title}
                </div>
              ) : (
                <div style={{ marginBottom: 10 }} />
              )}

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
  <Link href={`/sb/?audience=${audience}`}>
    Back to cantos
  </Link>
</div>

    </main>
  );
}
