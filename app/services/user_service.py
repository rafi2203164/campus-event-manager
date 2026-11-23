from werkzeug.security import generate_password_hash


class UserService:
    def __init__(self, repository):
        self.repository = repository

    def register(self, name, email, password):
        user = {
            "name": name,
            "email": email,
            "password_hash": generate_password_hash(password),
            "role": "student",
        }
        self.repository.save(user)
        return user
