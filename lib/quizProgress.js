// Client-side quiz progress utilities

export function getQuizResult(slug) {
  if (typeof window === "undefined") return null;
  try {
    const results = JSON.parse(localStorage.getItem("vedabaseQuizResults") || "{}");
    return results[slug] || null;
  } catch (e) {
    return null;
  }
}

export function getAllResults() {
  if (typeof window === "undefined") return {};
  try {
    return JSON.parse(localStorage.getItem("vedabaseQuizResults") || "{}");
  } catch (e) {
    return {};
  }
}

export function getWeekNumber(date) {
  const d = new Date(date);
  d.setHours(0, 0, 0, 0);
  d.setDate(d.getDate() + 4 - (d.getDay() || 7));
  const yearStart = new Date(d.getFullYear(), 0, 1);
  const weekNo = Math.ceil((((d - yearStart) / 86400000) + 1) / 7);
  return `${d.getFullYear()}-W${String(weekNo).padStart(2, '0')}`;
}

export function getBgProgress(audience = 'adult') {
  if (typeof window === "undefined") return { completed: 0, total: 18, percentage: 0 };
  
  try {
    const results = getAllResults();
    let completed = 0;
    for (let i = 1; i <= 18; i++) {
      const slug = `bg/${i}-${audience}`;
      if (results[slug]) completed++;
    }
    return {
      completed,
      total: 18,
      percentage: Math.round((completed / 18) * 100)
    };
  } catch (e) {
    return { completed: 0, total: 18, percentage: 0 };
  }
}

export function getSbProgress(audience = 'adult') {
  if (typeof window === "undefined") return { completed: 0, total: 0, percentage: 0 };
  
  try {
    const results = getAllResults();
    const cantoChapters = [19, 34, 33, 31, 26, 19, 15, 24, 24, 90, 31, 13];
    const total = cantoChapters.reduce((sum, count) => sum + count, 0);
    
    let completed = 0;
    for (let canto = 1; canto <= 12; canto++) {
      for (let chapter = 1; chapter <= cantoChapters[canto - 1]; chapter++) {
        const slug = `sb/${canto}/${chapter}-${audience}`;
        if (results[slug]) completed++;
      }
    }
    
    return {
      completed,
      total,
      percentage: total > 0 ? Math.round((completed / total) * 100) : 0
    };
  } catch (e) {
    return { completed: 0, total: 0, percentage: 0 };
  }
}

export function getWeeklyStreak() {
  if (typeof window === "undefined") return 0;
  
  try {
    const results = getAllResults();
    const dates = Object.values(results).map(r => r.date).filter(Boolean);
    if (dates.length === 0) return 0;
    
    // Get unique weeks with activity
    const weeks = [...new Set(dates.map(d => getWeekNumber(d)))].sort().reverse();
    if (weeks.length === 0) return 0;
    
    const currentWeek = getWeekNumber(new Date());
    let streak = 0;
    
    // Check if current week has activity
    if (weeks[0] === currentWeek) {
      streak = 1;
      
      // Count consecutive previous weeks
      for (let i = 1; i < weeks.length; i++) {
        const expectedPrevWeek = getWeekNumber(new Date(new Date() - i * 7 * 24 * 60 * 60 * 1000));
        if (weeks[i] === expectedPrevWeek) {
          streak++;
        } else {
          break;
        }
      }
    }
    
    return streak;
  } catch (e) {
    return 0;
  }
}

export function getWeeklyChallenge() {
  // Deterministic: same chapter for everyone in same week
  const weekNum = getWeekNumber(new Date());
  const weekInt = parseInt(weekNum.split('-W')[1]);
  
  // Rotate through BG chapters (1-18) based on week
  const chapter = ((weekInt - 1) % 18) + 1;
  
  return {
    scripture: 'bg',
    chapter,
    slug: `bg/${chapter}-adult`,
  };
}

export function isWeeklyChallengeCompleted() {
  if (typeof window === "undefined") return false;
  
  try {
    const challenge = getWeeklyChallenge();
    const results = getAllResults();
    const result = results[challenge.slug];
    
    if (!result) return false;
    
    const currentWeek = getWeekNumber(new Date());
    const resultWeek = getWeekNumber(result.date);
    
    return currentWeek === resultWeek;
  } catch (e) {
    return false;
  }
}

export function checkMilestone() {
  if (typeof window === "undefined") return null;
  
  try {
    const results = getAllResults();
    const achievedMilestones = JSON.parse(localStorage.getItem("achievedMilestones") || "[]");
    const completedSlugs = Object.keys(results);
    const totalQuizzes = completedSlugs.length;
    
    // First quiz
    if (totalQuizzes === 1 && !achievedMilestones.includes("first")) {
      achievedMilestones.push("first");
      localStorage.setItem("achievedMilestones", JSON.stringify(achievedMilestones));
      return { type: "first", message: "First Quiz Complete! 🎊" };
    }
    
    // 5 chapters
    if (totalQuizzes === 5 && !achievedMilestones.includes("5chapters")) {
      achievedMilestones.push("5chapters");
      localStorage.setItem("achievedMilestones", JSON.stringify(achievedMilestones));
      return { type: "5chapters", message: "5 Chapters Complete! 🎉" };
    }
    
    // 10 chapters
    if (totalQuizzes === 10 && !achievedMilestones.includes("10chapters")) {
      achievedMilestones.push("10chapters");
      localStorage.setItem("achievedMilestones", JSON.stringify(achievedMilestones));
      return { type: "10chapters", message: "10 Chapters Complete! 🌟" };
    }
    
    // BG Complete (all 18 chapters, any audience)
    const bgChapters = completedSlugs.filter(s => s.startsWith("bg/")).map(s => {
      const match = s.match(/bg\/(\d+)-/);
      return match ? parseInt(match[1]) : 0;
    });
    const uniqueBgChapters = new Set(bgChapters);
    if (uniqueBgChapters.size === 18 && !achievedMilestones.includes("bgComplete")) {
      achievedMilestones.push("bgComplete");
      localStorage.setItem("achievedMilestones", JSON.stringify(achievedMilestones));
      return { type: "bgComplete", message: "Bhagavad Gita Complete! 🏆" };
    }
    
    // Canto complete check (any canto with all chapters)
    const cantoChapters = {
      1: 19, 2: 10, 3: 33, 4: 31, 5: 26, 6: 19,
      7: 15, 8: 24, 9: 24, 10: 90, 11: 31, 12: 13
    };
    
    for (const [canto, total] of Object.entries(cantoChapters)) {
      const cantoSlugs = completedSlugs.filter(s => s.startsWith(`sb/${canto}/`));
      const chapters = cantoSlugs.map(s => {
        const match = s.match(/sb\/\d+\/(\d+)-/);
        return match ? parseInt(match[1]) : 0;
      });
      const uniqueChapters = new Set(chapters);
      
      if (uniqueChapters.size === total && !achievedMilestones.includes(`canto${canto}`)) {
        achievedMilestones.push(`canto${canto}`);
        localStorage.setItem("achievedMilestones", JSON.stringify(achievedMilestones));
        return { type: "cantoComplete", message: `Canto ${canto} Complete! 🎊` };
      }
    }
    
    return null;
  } catch (e) {
    return null;
  }
}

export function getCantoProgress(cantoNum, totalChapters, audience) {
  if (typeof window === "undefined") return { completed: 0, total: totalChapters };
  
  try {
    const results = JSON.parse(localStorage.getItem("vedabaseQuizResults") || "{}");
    let completed = 0;
    
    for (let ch = 1; ch <= totalChapters; ch++) {
      const slug = `sb/${cantoNum}/${ch}-${audience}`;
      if (results[slug]) {
        completed++;
      }
    }
    
    return { completed, total: totalChapters };
  } catch (e) {
    return { completed: 0, total: totalChapters };
  }
}

export function formatTimeAgo(isoDate) {
  if (!isoDate) return "";
  try {
    const date = new Date(isoDate);
    const now = new Date();
    const diffMs = now - date;
    const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));
    
    if (diffDays === 0) return "Today";
    if (diffDays === 1) return "Yesterday";
    if (diffDays < 7) return `${diffDays} days ago`;
    if (diffDays < 30) return `${Math.floor(diffDays / 7)} weeks ago`;
    return `${Math.floor(diffDays / 30)} months ago`;
  } catch (e) {
    return "";
  }
}
