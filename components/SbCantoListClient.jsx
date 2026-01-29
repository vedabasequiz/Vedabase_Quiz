"use client";
import { useState, useEffect } from "react";
import Link from "next/link";
import { getCantoProgress } from "../lib/quizProgress";

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
    // Calculate progress for each canto
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
        const hasProgress = progress.completed > 0;
        
        return (
          <Link 
            key={c} 
            href={`/sb/${c}/?audience=${audience}`} 
            className={`chapterListItem ${hasProgress ? "chapterListItemCompleted" : ""}`}
          >
            <div className="chapterListContent">
              <div className="chapterListHeader">Canto {c}</div>
              <div className="chapterListTitle">{SB_CANTO_TITLES[c] || ""}</div>
            </div>
            
            <div className="chapterListRight">
              <div className={hasProgress ? "chapterListBadge" : "chapterListHint"}>
                {progress.completed}/{progress.total} chapters
              </div>
            </div>
          </Link>
        );
      })}
    </div>
  );
}
