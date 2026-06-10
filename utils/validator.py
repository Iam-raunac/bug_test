import re

def is_valid_email(email):
    return bool(re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', email))

def is_strong_password(password):
    return bool(password and len(password) >= 6)

def sanitize_email(email):
    return email.strip() if email else ""
