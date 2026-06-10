from auth.login import login_user
from utils.validator import is_valid_email

def test_login_with_exact_lowercase_match():
    email = "test@example.com"
    password = "password"
    assert login_user(email, password) is not None

def test_login_with_uppercase_email():
    email = "Test@Example.com"
    password = "password"
    assert login_user(email, password) is not None

def test_login_with_mixed_case_email():
    email = "tEsT@ExAmPle.cOm"
    password = "password"
    assert login_user(email, password) is not None

def test_login_with_invalid_email():
    email = "invalid_email"
    password = "password"
    assert login_user(email, password) is None

def test_login_with_valid_email_and_invalid_password():
    email = "test@example.com"
    password = "wrong_password"
    assert login_user(email, password) is None

import pytest
@pytest.mark.parametrize("email", ["test@example.com", "Test@Example.com", "tEsT@ExAmPle.cOm"])
def test_login_with_different_email_cases(email):
    password = "password"
    assert login_user(email, password) is not None