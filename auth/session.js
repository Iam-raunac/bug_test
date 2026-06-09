const activeSessions = new Map();

function createSession(userId) {
  const token = `token_${userId}_${Date.now()}`;
  activeSessions.set(token, {
    userId,
    createdAt: new Date().toISOString(),
    expiresAt: new Date(Date.now() + 3600000).toISOString(), // 1 hour
  });
  return token;
}

function getSession(token) {
  return activeSessions.get(token) || null;
}

function destroySession(token) {
  return activeSessions.delete(token);
}

module.exports = { createSession, getSession, destroySession };
