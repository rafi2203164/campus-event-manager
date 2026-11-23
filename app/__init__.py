import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev-secret-change-me"
    app.config["DATABASE"] = os.path.abspath(
        os.path.join(app.root_path, "..", "events.db")
    )
    if test_config:
        app.config.update(test_config)

    from app.repositories.user_repository import UserRepository
    from app.services.user_service import UserService
    from app.routes.auth import auth_bp

    user_repository = UserRepository(app.config["DATABASE"])
    app.extensions["user_service"] = UserService(user_repository)
    app.register_blueprint(auth_bp)

    return app
