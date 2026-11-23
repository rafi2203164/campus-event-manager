from app import create_app


def make_client(tmp_path):
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "test.db")})
    return app.test_client()


def test_register_page_loads(tmp_path):
    client = make_client(tmp_path)

    response = client.get("/register")

    assert response.status_code == 200
    assert b"Register" in response.data


def test_register_new_user_shows_success_message(tmp_path):
    client = make_client(tmp_path)

    response = client.post(
        "/register",
        data={"name": "Rafi", "email": "rafi@example.com", "password": "secret123"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Registration successful" in response.data


def test_register_duplicate_email_shows_error(tmp_path):
    client = make_client(tmp_path)
    data = {"name": "Rafi", "email": "rafi@example.com", "password": "secret123"}
    client.post("/register", data=data)

    response = client.post("/register", data=data)

    assert b"Email already registered" in response.data


def test_register_with_empty_fields_shows_error(tmp_path):
    client = make_client(tmp_path)

    response = client.post("/register", data={"name": "", "email": "", "password": ""})

    assert b"All fields are required" in response.data
