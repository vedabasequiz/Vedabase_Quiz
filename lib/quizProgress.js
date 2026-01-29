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
