from app.repositories.user_repository import UserRepository


def make_user(email="rafi@example.com"):
    return {
        "name": "Rafi",
        "email": email,
        "password_hash": "hashed",
        "role": "student",
    }


def test_save_and_find_user_by_email(tmp_path):
    repo = UserRepository(str(tmp_path / "test.db"))
    repo.save(make_user())

    found = repo.find_by_email("rafi@example.com")

    assert found["name"] == "Rafi"
    assert found["role"] == "student"


def test_find_missing_user_returns_none(tmp_path):
    repo = UserRepository(str(tmp_path / "test.db"))

    assert repo.find_by_email("nobody@example.com") is None
