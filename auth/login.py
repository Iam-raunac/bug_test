USERS = [
    {"id": 1, "email": "raunak@example.com", "password": "secret123", "role": "admin"},
    {"id": 2, "email": "john@example.com",   "password": "pass456",   "role": "user"},
    {"id": 3, "email": "alice@example.com",  "password": "alice789",  "role": "user"},
]

def find_user_by_email(email):
    # BUG: case-sensitive comparison breaks login for uppercase emails
    return next((u for u in USERS if u["email"] == email), None)

def validate_password(user, input_password):
    return user["password"] == input_password

def login_user(email, password):
    if not email or not password:
        return {"success": False, "error": "Email and password are required"}
    user = find_user_by_email(email)
    if not user:
        return {"success": False, "error": "User not found"}
    if not validate_password(user, password):
        return {"success": False, "error": "Invalid password"}
    return {"success": True, "user": {"id": user["id"], "email": user["email"]}}
