"use client";

import React, { useState, useEffect } from "react";
import { getWeeklyStreak, getBgProgress, getSbProgress } from "../lib/quizProgress";
import Link from "next/link";

export default function WeeklyEngagement() {
  const [streak, setStreak] = useState(0);
  const [bgProgress, setBgProgress] = useState({ completed: 0, total: 18, percentage: 0 });
  const [sbProgress, setSbProgress] = useState({ completed: 0, total: 0, percentage: 0 });

  useEffect(() => {
    // Load streak and progress data
    const currentStreak = getWeeklyStreak();
    const bg = getBgProgress('adult');
    const sb = getSbProgress('adult');

    setStreak(currentStreak);
    setBgProgress(bg);
    setSbProgress(sb);
  }, []);

  return (
    <div className="weeklyEngagement">
      {/* Weekly Streak Counter */}
      {streak > 0 && (
        <div className="streakCounter">
          <span className="streakEmoji">🔥</span>
          <span className="streakText">{streak}-week streak!</span>
        </div>
      )}

      {/* Progress Trackers */}
      <div className="progressTrackers">
        {/* Bhagavad-gita Progress */}
        <Link href="/bg?audience=adult" className="progressTracker">
          <div className="progressHeader">
            <span className="progressTitle">📖 Bhagavad-gita</span>
            <span className="progressStats">
              {bgProgress.completed}/{bgProgress.total} chapters
            </span>
          </div>
          <div className="progressBarContainer">
            <div 
              className="progressBarFill"
              style={{ width: `${bgProgress.percentage}%` }}
            />
          </div>
          <div className="progressPercentage">{bgProgress.percentage}% complete</div>
        </Link>

        {/* Srimad Bhagavatam Progress */}
        <Link href="/sb?audience=adult" className="progressTracker">
          <div className="progressHeader">
            <span className="progressTitle">📚 Srimad Bhagavatam</span>
            <span className="progressStats">
              {sbProgress.completed}/{sbProgress.total} chapters
            </span>
          </div>
          <div className="progressBarContainer">
            <div 
              className="progressBarFill"
              style={{ width: `${sbProgress.percentage}%` }}
            />
          </div>
          <div className="progressPercentage">{sbProgress.percentage}% complete</div>
        </Link>
      </div>
    </div>
  );
}
