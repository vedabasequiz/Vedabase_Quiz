"use client";

import React, { useState, useEffect } from "react";
import { getWeeklyStreak, getWeeklyChallenge, isWeeklyChallengeCompleted } from "../lib/quizProgress";
import Link from "next/link";

export default function WeeklyEngagement() {
  const [streak, setStreak] = useState(0);
  const [challenge, setChallenge] = useState(null);
  const [challengeCompleted, setChallengeCompleted] = useState(false);

  useEffect(() => {
    // Load streak and challenge data
    const currentStreak = getWeeklyStreak();
    const weeklyChallenge = getWeeklyChallenge();
    const isCompleted = isWeeklyChallengeCompleted();

    setStreak(currentStreak);
    setChallenge(weeklyChallenge);
    setChallengeCompleted(isCompleted);
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

      {/* Weekly Challenge */}
      {challenge && (
        <div className="weeklyChallenge">
          <div className="challengeHeader">
            <span className="challengeIcon">🎯</span>
            <span className="challengeTitle">This Week's Challenge</span>
          </div>
          <Link href={`/quiz/${challenge.slug}`} className="challengeLink">
            <div className="challengeContent">
              <span className="challengeText">
                {challenge.scripture === "bg" ? "Bhagavad-gita" : "Srimad Bhagavatam"} Chapter {challenge.chapter}
              </span>
              {challengeCompleted && <span className="challengeCheck">✓ Completed!</span>}
            </div>
          </Link>
        </div>
      )}
    </div>
  );
}
