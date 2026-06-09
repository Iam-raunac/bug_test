function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

function isStrongPassword(password) {
  return password && password.length >= 6;
}

function sanitizeEmail(email) {
  return email ? email.trim() : "";
}

module.exports = { isValidEmail, isStrongPassword, sanitizeEmail };
