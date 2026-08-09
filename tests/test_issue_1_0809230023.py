from auth.login import find_user_by_email, login_user
from auth.login import USERS

def test__login_with_exact_match():
    email = USERS[0]["email"]
    assert find_user_by_email(email) is not None

def test__login_with_mixed_case_email():
    email = USERS[0]["email"].swapcase()
    assert find_user_by_email(email) is not None

def test__login_with_uppercase_email():
    email = USERS[0]["email"].upper()
    assert find_user_by_email(email) is not None

def test__login_with_lowercase_email():
    email = USERS[0]["email"].lower()
    assert find_user_by_email(email) is not None

def test__login_with_non_existent_email():
    email = "non_existent_email@example.com"
    assert find_user_by_email(email) is None

import pytest
@pytest.mark.parametrize("email", [
    "TestEmail@example.com",
    "testEMAIL@example.com",
    "TESTemail@example.com",
    "tEsTeMaIl@example.com"
])
def test__login_with_various_case_emails(email):
    user_email = email.lower()
    USERS.append({"email": user_email})
    assert find_user_by_email(email) is not None
    USERS.pop()