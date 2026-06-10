import time
import secrets

_sessions = {}

def create_session(user_id):
    token = secrets.token_hex(16)
    _sessions[token] = {"user_id": user_id, "expires_at": time.time() + 3600}
    return token

def get_session(token):
    return _sessions.get(token)

def destroy_session(token):
    return _sessions.pop(token, None) is not None
