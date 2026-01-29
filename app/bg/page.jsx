import { redirect } from "next/navigation";
import { getBgAvailability } from "../../lib/quizLoader";
import BgClient from "../../components/BgClient";

// Vedabase chapter headings (ASCII-only)
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
  13: "Nature, the Enjoyer, and Consciousness",
  14: "The Three Modes of Material Nature",
  15: "The Yoga of the Supreme Person",
  16: "The Divine and Demoniac Natures",
  17: "The Divisions of Faith",
  18: "Conclusion - The Perfection of Renunciation",
};

function getAudienceFromSearchParams(searchParams) {
  const a = searchParams?.audience;
  const v = Array.isArray(a) ? a[0] : a;
  if (v === "kids" || v === "teens" || v === "adult") return v;
  return "adult";
}

export default function BgIndex({ searchParams }) {
  if (!searchParams?.audience) redirect("/bg/?audience=adult");

  const availability = getBgAvailability();
  const audience = getAudienceFromSearchParams(searchParams);
  const chapters = Array.from({ length: 18 }, (_, i) => i + 1);

  return (
    <BgClient 
      chapters={chapters}
      availability={availability}
      titles={BG_CHAPTER_TITLES}
      initialAudience={audience}
    />
  );
}
