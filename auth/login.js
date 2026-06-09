const users = [
  { id: 1, email: "raunak@example.com", password: "secret123", role: "admin" },
  { id: 2, email: "john@example.com",   password: "pass456",   role: "user"  },
  { id: 3, email: "alice@example.com",  password: "alice789",  role: "user"  },
];

function findUserByEmail(email) {
  // BUG: case-sensitive comparison breaks login for uppercase emails
  return users.find((u) => u.email === email);
}

function validatePassword(user, inputPassword) {
  return user.password === inputPassword;
}

function loginUser(email, password) {
  if (!email || !password) {
    return { success: false, error: "Email and password are required" };
  }

  const user = findUserByEmail(email);

  if (!user) {
    return { success: false, error: "User not found" };
  }

  if (!validatePassword(user, password)) {
    return { success: false, error: "Invalid password" };
  }

  return {
    success: true,
    user: { id: user.id, email: user.email, role: user.role },
  };
}

module.exports = { loginUser, findUserByEmail, validatePassword };
