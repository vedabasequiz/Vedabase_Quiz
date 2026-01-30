const fs = require('fs');
const path = require('path');

const bgDir = path.join(__dirname, '../data/quizzes/bg');
const files = fs.readdirSync(bgDir).filter(f => f.endsWith('.json'));

const chapterNames = {
  1: "Observing the Armies on the Battlefield of Kurukshetra",
  2: "Contents of the Gita Summarized",
  3: "Karma-yoga",
  4: "Transcendental Knowledge",
  5: "Karma-yoga—Action in Krishna Consciousness",
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
  18: "Conclusion—The Perfection of Renunciation",
};

files.forEach(file => {
  const filePath = path.join(bgDir, file);
  const content = fs.readFileSync(filePath, 'utf8');
  const quiz = JSON.parse(content);
  
  // Extract chapter number from id (e.g., "bg-1-adult" -> 1)
  const match = quiz.id.match(/bg-(\d+)-/);
  const chapterNum = match ? parseInt(match[1]) : null;
  
  if (!chapterNum) {
    console.log(`Skipping ${file} - could not parse chapter number`);
    return;
  }
  
  // Determine audience suffix
  const audienceSuffix = quiz.audience === 'kids' ? ' (Kids)' : 
                         quiz.audience === 'teens' ? ' (Teens)' : 
                         ' (Adult)';
  const questionCount = quiz.questions.length;
  
  // Update title to match SB format
  quiz.title = `Bhagavad Gita - Chapter ${chapterNum}${audienceSuffix} | ${questionCount}Q`;
  
  // Add publishedOn field (using 2026-01-28 based on git history)
  quiz.publishedOn = "2026-01-28";
  
  // Write back to file with proper formatting
  fs.writeFileSync(filePath, JSON.stringify(quiz, null, 2) + '\n', 'utf8');
  
  console.log(`✓ Updated ${file}: "${quiz.title}"`);
});

console.log(`\n✅ Updated ${files.length} BG quiz files`);
