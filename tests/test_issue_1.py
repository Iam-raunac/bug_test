import pytest
from auth.login import login_user, find_user_by_email
from auth.login import USERS

@pytest.fixture
def test_users():
    return [
        {"email": "test@example.com", "password": "password123"},
        {"email": "TEST@example.com", "password": "password123"},
    ]

def test_login_success_with_lowercase_email():
    assert login_user("test@example.com", "password123") is not None

def test_login_success_with_uppercase_email():
    assert login_user("TEST@EXAMPLE.COM", "password123") is not None

def test_login_success_with_mixedcase_email():
    assert login_user("TeSt@ExAmPle.Com", "password123") is not None

def test_find_user_by_email_with_lowercase_email(test_users):
    USERS.extend(test_users)
    assert find_user_by_email("test@example.com") is not None

def test_find_user_by_email_with_uppercase_email(test_users):
    USERS.extend(test_users)
    assert find_user_by_email("TEST@EXAMPLE.COM") is not None

def test_find_user_by_email_with_mixedcase_email(test_users):
    USERS.extend(test_users)
    assert find_user_by_email("TeSt@ExAmPle.Com") is not None

def test_find_user_by_email_with_nonexistent_email(test_users):
    USERS.extend(test_users)
    assert find_user_by_email("nonexistent@example.com") is None

@pytest.mark.parametrize("email, expected_result", [
    ("test@example.com", True),
    ("TEST@EXAMPLE.COM", True),
    ("TeSt@ExAmPle.Com", True),
    ("nonexistent@example.com", False),
])
def test_find_user_by_email_parametrized(email, expected_result, test_users):
    USERS.extend(test_users)
    user = find_user_by_email(email)
    if expected_result:
        assert user is not None
    else:
        assert user is None