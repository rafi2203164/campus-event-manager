from unittest.mock import Mock

import pytest

from app.services.user_service import UserService


def test_register_saves_user_with_hashed_password():
    repo = Mock()
    repo.find_by_email.return_value = None
    service = UserService(repo)

    user = service.register("Rafi", "rafi@example.com", "secret123")

    assert user["email"] == "rafi@example.com"
    assert user["password_hash"] != "secret123"
    repo.save.assert_called_once()


def test_register_rejects_duplicate_email():
    repo = Mock()
    repo.find_by_email.return_value = {"email": "rafi@example.com"}
    service = UserService(repo)

    with pytest.raises(ValueError):
        service.register("Rafi", "rafi@example.com", "secret123")

    repo.save.assert_not_called()
