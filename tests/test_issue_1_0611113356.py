from auth.login import login_user
from auth.login import find_user_by_email

def test_login_works_with_lowercase_email():
    email = "test@example.com"
    password = "password"
    assert login_user(email, password) is not None

def test_login_works_with_uppercase_email():
    email = "TEST@EXAMPLE.COM"
    password = "password"
    assert login_user(email, password) is not None

def test_login_works_with_mixed_case_email():
    email = "TeSt@ExAmPle.Com"
    password = "password"
    assert login_user(email, password) is not None

def test_find_user_by_email_works_with_lowercase_email():
    email = "test@example.com"
    assert find_user_by_email(email) is not None

def test_find_user_by_email_works_with_uppercase_email():
    email = "TEST@EXAMPLE.COM"
    assert find_user_by_email(email) is not None

def test_find_user_by_email_works_with_mixed_case_email():
    email = "TeSt@ExAmPle.Com"
    assert find_user_by_email(email) is not None

def test_find_user_by_email_returns_none_for_nonexistent_email():
    email = "nonexistent@example.com"
    assert find_user_by_email(email) is None