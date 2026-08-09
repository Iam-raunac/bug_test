from auth.login import find_user_by_email, login_user
from auth.login import USERS

def test__login_with_exact_lowercase_match():
    user = next(u for u in USERS)
    assert find_user_by_email(user["email"]) is not None

def test__login_with_uppercase_email():
    user = next(u for u in USERS)
    assert find_user_by_email(user["email"].upper()) is not None

def test__login_with_mixed_case_email():
    user = next(u for u in USERS)
    mixed_case_email = user["email"].lower().replace("a", "A")
    assert find_user_by_email(mixed_case_email) is not None

def test__login_with_nonexistent_email():
    nonexistent_email = "nonexistent@example.com"
    assert find_user_by_email(nonexistent_email) is None

import pytest
@pytest.mark.parametrize("email_case", ["lower", "upper", "mixed"])
def test__login_with_different_email_cases(email_case):
    user = next(u for u in USERS)
    if email_case == "lower":
        email = user["email"].lower()
    elif email_case == "upper":
        email = user["email"].upper()
    else:
        email = user["email"].lower().replace("a", "A")
    assert find_user_by_email(email) is not None