//Javascript
function firstNonRepeatingChar(str) {
  const charCount = new Map();
  for (let char of str) {
    charCount.set(char, (charCount.get(char) || 0) + 1);
    console.log(charCount);
  }
  for (let char of str) {
    if (charCount.get(char) === 1) {
      return char;
    }
  }
  return null;
}

console.log(firstNonRepeatingChar("lovealmario"));