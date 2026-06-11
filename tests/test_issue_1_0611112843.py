import pytest
from auth.login import find_user_by_email, USERS

@pytest.fixture
def users():
    return [
        {"email": "user1@example.com", "password": "password1"},
        {"email": "user2@example.com", "password": "password2"},
    ]

def test__find_user_by_email_lowercase_match(users):
    USERS.extend(users)
    user = find_user_by_email("user1@example.com")
    assert user["email"] == "user1@example.com"

def test__find_user_by_email_uppercase_match(users):
    USERS.extend(users)
    user = find_user_by_email("USER1@EXAMPLE.COM")
    assert user["email"] == "user1@example.com"

def test__find_user_by_email_mixed_case_match(users):
    USERS.extend(users)
    user = find_user_by_email("UsEr1@ExAmPle.Com")
    assert user["email"] == "user1@example.com"

def test__find_user_by_email_no_match(users):
    USERS.extend(users)
    user = find_user_by_email("nonexistent@example.com")
    assert user is None

def test__find_user_by_email_empty_string(users):
    USERS.extend(users)
    user = find_user_by_email("")
    assert user is None

def test__find_user_by_email_none_input(users):
    USERS.extend(users)
    user = find_user_by_email(None)
    assert user is None