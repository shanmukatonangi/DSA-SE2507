//Javascript
function isvalidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

// Example usage
const email1 = "michael.scott@gmail.com";
const email2 = "pam.beesly_gmail.com";
console.log(isvalidEmail(email1));
console.log(isvalidEmail(email2));

// Output
