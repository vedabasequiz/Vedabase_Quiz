// update-published-date.js
// Usage: node update-published-date.js data/quizzes/sb/1/1-adult.json
// This script updates the 'publishedOn' field in the quiz JSON to the latest git commit date (US Central Time)

const fs = require('fs');
const { execSync } = require('child_process');

// Get file path from command line
const filePath = process.argv[2];
if (!filePath) {
  console.error('Usage: node update-published-date.js <path-to-json>');
  process.exit(1);
}

// Get latest git commit date for the file (ISO 8601 UTC)
let gitDate;
try {
  gitDate = execSync(`git log -1 --format=%cI -- "${filePath}"`).toString().trim();
} catch (e) {
  console.error('Error: Could not get git commit date. Is this a git repo?');
  process.exit(1);
}

// Convert to US Central Time (America/Chicago)
const date = new Date(gitDate);
const centralDate = date.toLocaleDateString('en-CA', { timeZone: 'America/Chicago' }); // YYYY-MM-DD
const centralTime = date.toLocaleTimeString('en-US', { timeZone: 'America/Chicago', hour12: false }); // HH:MM:SS
const publishedOn = `${centralDate}T${centralTime}`;

// Read and update JSON
let quiz;
try {
  quiz = JSON.parse(fs.readFileSync(filePath, 'utf8'));
} catch (e) {
  console.error('Error: Could not read or parse JSON file.');
  process.exit(1);
}
quiz.publishedOn = publishedOn;

// Write back to file (pretty print)
fs.writeFileSync(filePath, JSON.stringify(quiz, null, 2) + '\n');
console.log(`Updated publishedOn to ${publishedOn} in ${filePath}`);
