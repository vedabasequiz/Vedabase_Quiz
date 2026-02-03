"use client";
import { useState, useEffect } from "react";
import Link from "next/link";
import { getCantoProgress } from "../lib/quizProgress";

// Static map of available chapters for each canto and audience
const AVAILABLE_CHAPTERS = {
  1: {
    adult: [1, 2],
    teens: [1, 2],
    kids: [1, 2],
  },
  // Add more cantos as quiz files are created
};

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

const CHAPTERS_PER_CANTO = {
  1: 19,
  2: 10,
  3: 33,
  4: 31,
  5: 26,
  6: 19,
  7: 15,
  8: 24,
  9: 24,
  10: 90,
  11: 31,
  12: 13,
};

export default function SbCantoListClient({ audience }) {
  const [cantoProgress, setCantoProgress] = useState({});

  useEffect(() => {
    // Calculate progress for each canto for the selected audience
    const progress = {};
    for (let c = 1; c <= 12; c++) {
      const totalChapters = CHAPTERS_PER_CANTO[c] || 0;
      progress[c] = getCantoProgress(c, totalChapters, audience);
    }
    setCantoProgress(progress);
  }, [audience]);

  const cantos = Array.from({ length: 12 }, (_, i) => i + 1);

  return (
    <div className="chapterList">
      {cantos.map((c) => {
        const progress = cantoProgress[c] || { completed: 0, total: CHAPTERS_PER_CANTO[c] || 0 };
        const audienceLabel = audience.charAt(0).toUpperCase() + audience.slice(1);
        const available = AVAILABLE_CHAPTERS[c] && AVAILABLE_CHAPTERS[c][audience] && AVAILABLE_CHAPTERS[c][audience].length > 0;
        if (!available) {
          return (
            <div
              key={c}
              className="chapterListItem chapterListItemDisabled"
              style={{ pointerEvents: 'none', opacity: 0.6 }}
            >
              <div className="chapterListContent">
                <div className="chapterListHeader">Canto {c}</div>
                <div className="chapterListTitle">{SB_CANTO_TITLES[c] || ""}</div>
              </div>
              <div className="chapterListRight">
                <div className="chapterListComingSoon">{audienceLabel}: coming soon</div>
              </div>
            </div>
          );
        }
        // Otherwise, show enabled card with progress
        return (
          <Link
            key={c}
            href={`/sb/${c}/?audience=${audience}`}
            className={`chapterListItem ${progress.completed > 0 ? "chapterListItemCompleted" : ""}`}
          >
            <div className="chapterListContent">
              <div className="chapterListHeader">Canto {c}</div>
              <div className="chapterListTitle">{SB_CANTO_TITLES[c] || ""}</div>
            </div>
            <div className="chapterListRight">
              <div className="chapterListBadge">
                {progress.completed}/{progress.total} chapters
              </div>
            </div>
          </Link>
        );
      })}
    </div>
  );
}
