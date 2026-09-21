import pytest
from auth import login as auth_login

@pytest.fixture(autouse=True)
def setup_users(monkeypatch):
    test_user = {"email": "raunak@example.com", "password": "secret"}
    monkeypatch.setattr(auth_login, "USERS", [test_user])
    return test_user

@pytest.mark.parametrize(
    "email_input",
    [
        "raunak@example.com",
        "RAUNAK@EXAMPLE.COM",
        "RaUnAk@ExAmPlE.CoM",
    ],
)
def test__find_user_by_email_case_insensitive(email_input, setup_users):
    user = auth_login.find_user_by_email(email_input)
    assert user is not None
    assert user["email"] == "raunak@example.com"

def test__find_user_by_email_non_string_returns_none():
    assert auth_login.find_user_by_email(None) is None
    assert auth_login.find_user_by_email(123) is None

def test__login_user_accepts_email_case_insensitive(setup_users):
    # Assuming login_user returns the user dict on successful authentication
    user = auth_login.login_user("RAUNAK@EXAMPLE.COM", "secret")
    assert user is not None
    assert user["email"] == "raunak@example.com"

    user = auth_login.login_user("Raunak@Example.Com", "secret")
    assert user is not None
    assert user["email"] == "raunak@example.com"

    # Wrong password should fail (return None or raise)
    result = auth_login.login_user("raunak@example.com", "wrong")
    assert result is None or result is False