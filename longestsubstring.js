//Javascript
function longestSubstringWithoutRepeatingChars(str) {
  let longest = '';
  let start = 0;
  let charMap = new Map();
  for (let end = 0; end < str.length; end++) {
    if (charMap.has(str[end])) {
      start = Math.max(start, charMap.get(str[end]) + 1);
    }
    charMap.set(str[end], end);
    let substring = str.slice(start, end + 1);
    if (substring.length > longest.length) {
      longest = substring;
    }
  }
  return longest;
}

console.log(longestSubstringWithoutRepeatingChars("abcabcbb")); // Output: "abc"