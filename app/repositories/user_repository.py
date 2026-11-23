import sqlite3
from contextlib import closing


class UserRepository:
    def __init__(self, db_path):
        self.db_path = db_path
        self._create_table()

    def _connect(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _create_table(self):
        with closing(self._connect()) as conn:
            with conn:
                conn.execute(
                    "CREATE TABLE IF NOT EXISTS users ("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "name TEXT NOT NULL, "
                    "email TEXT NOT NULL UNIQUE, "
                    "password_hash TEXT NOT NULL, "
                    "role TEXT NOT NULL)"
                )

    def save(self, user):
        with closing(self._connect()) as conn:
            with conn:
                conn.execute(
                    "INSERT INTO users (name, email, password_hash, role) "
                    "VALUES (?, ?, ?, ?)",
                    (user["name"], user["email"], user["password_hash"], user["role"]),
                )

    def find_by_email(self, email):
        with closing(self._connect()) as conn:
            row = conn.execute(
                "SELECT * FROM users WHERE email = ?", (email,)
            ).fetchone()
        return dict(row) if row else None
