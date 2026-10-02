import pytest
from auth import login as login_mod


@pytest.fixture
def isolated_users(monkeypatch):
    original_users = login_mod.USERS[:]
    test_user = {"email": "raunak@example.com", "id": 1, "name": "Raunak"}
    monkeypatch.setattr(login_mod, "USERS", [test_user])
    yield test_user
    monkeypatch.setattr(login_mod, "USERS", original_users)


@pytest.mark.parametrize(
    "email_input",
    [
        "raunak@example.com",
        "RAUNAK@EXAMPLE.COM",
        "RaUnAk@ExAmPlE.cOm",
    ],
)
def test__find_user_by_email_case_insensitive(isolated_users, email_input):
    result = login_mod.find_user_by_email(email_input)
    assert result is not None
    assert result["email"] == isolated_users["email"]


def test__find_user_by_email_not_found(isolated_users):
    result = login_mod.find_user_by_email("nonexistent@example.com")
    assert result is None