from auth.login import find_user_by_email
from auth.login import USERS

def test_login_with_exact_lowercase_match():
    email = "test@example.com"
    assert find_user_by_email(email) is not None

def test_login_with_exact_uppercase_match():
    email = "TEST@EXAMPLE.COM"
    assert find_user_by_email(email) is not None

def test_login_with_mixed_case_match():
    email = "TeSt@ExAmPle.Com"
    assert find_user_by_email(email) is not None

def test_login_with_non_existent_email():
    email = "nonexistent@example.com"
    assert find_user_by_email(email) is None

def test_login_with_empty_email():
    email = ""
    assert find_user_by_email(email) is None

def test_login_with_none_email():
    email = None
    assert find_user_by_email(email) is None