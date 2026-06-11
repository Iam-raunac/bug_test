import pytest
from auth.login import login_user, USERS

@pytest.fixture
def test_user():
    return USERS[0]

def test_login_user_with_exact_match(test_user):
    assert login_user(test_user["email"], test_user["password"]) is not None

def test_login_user_with_uppercase_email(test_user):
    assert login_user(test_user["email"].upper(), test_user["password"]) is not None

def test_login_user_with_mixed_case_email(test_user):
    assert login_user(test_user["email"].capitalize(), test_user["password"]) is not None

def test_login_user_with_invalid_email():
    assert login_user("invalid@example.com", "password") is None

def test_login_user_with_invalid_password(test_user):
    assert login_user(test_user["email"], "invalid_password") is None

def test_login_user_with_empty_email():
    assert login_user("", test_user["password"]) is None

def test_login_user_with_empty_password(test_user):
    assert login_user(test_user["email"], "") is None