import pytest
from pydantic import ValidationError

from domain.models.user import User

from fastapi.testclient import TestClient
from entrypoints.api.main import app


def test_create_user_with_valid_data(valid_user_data):
    """Test creating a user with valid data."""
    user = User(**valid_user_data)

    assert user.id is None
    assert user.username == valid_user_data["username"]
    assert user.password == valid_user_data["password"]
    assert user.email == valid_user_data["email"]
    assert user.dni == valid_user_data["dni"]
    assert user.fullName == valid_user_data["fullName"]
    assert user.phoneNumber == valid_user_data["phoneNumber"]
    assert user.status == "POR_VERIFICAR"


def test_create_user_with_missing_fields():
    """Test creating a user with missing required fields."""
    with pytest.raises(ValidationError):
        User(username="user", password="pass")  # faltan campos obligatorios


def test_create_user_with_invalid_email(valid_user_data):
    """Test creating a user with an invalid email."""
    with pytest.raises(ValidationError):
        User(**{**valid_user_data, "email": "not-an-email"})


def test_create_user_with_empty_username(valid_user_data):
    """Test creating a user with an empty username."""
    with pytest.raises(ValidationError):
        User(**{**valid_user_data, "username": ""})


def test_create_user_with_extra_fields(valid_user_data):
    """Test creating a user with extra fields."""
    user = User(**valid_user_data, extra_field="extra")  # type: ignore

    assert not hasattr(user, "extra_field")


def test_user_model_equality():
    """Test user model equality."""
    user1 = User(
        id=1,
        username="jtapia",
        password="password123",
        email="tapia23@gmail.com",
        dni="223432345",
        fullName="Pedro Alicante",
        phoneNumber="3123452342",
    )
    user2 = User(
        id=1,
        username="jtapia",
        password="password123",
        email="tapia23@gmail.com",
        dni="223432345",
        fullName="Pedro Alicante",
        phoneNumber="3123452342",
    )

    assert user1 == user2


def test_user_model_inequality():
    """Test user model inequality."""
    user1 = User(
        id=1,
        username="jtapia",
        password="password123",
        email="tapia23@gmail.com",
        dni="223432345",
        fullName="Pedro Alicante",
        phoneNumber="3123452342",
    )
    user2 = User(
        id=2,
        username="jtapia",
        password="password123",
        email="tapia23@gmail.com",
        dni="223432345",
        fullName="Pedro Alicante",
        phoneNumber="3123452342",
    )

    assert user1 != user2


import pytest
from fastapi.testclient import TestClient
from entrypoints.api.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_users():
    client.post("/users/reset")


def test_health_check():
    response = client.get("/users/ping")
    assert response.status_code == 200
    assert response.text == "pong"


def test_create_user():
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "fullName": "Test User",
        "dni": "12345678",
        "phoneNumber": "5551234",
        "status": "POR_VERIFICAR",
        "password": "password123",
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 201
    assert "id" in response.json()


def test_get_users():
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "fullName": "Test User",
        "dni": "12345678",
        "phoneNumber": "5551234",
        "status": "POR_VERIFICAR",
        "password": "password123",
    }
    client.post("/users/", json=user_data)
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 1


def test_get_user_by_id():
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "fullName": "Test User",
        "dni": "12345678",
        "phoneNumber": "5551234",
        "status": "POR_VERIFICAR",
        "password": "password123",
    }
    create_resp = client.post("/users/", json=user_data)
    user_id = create_resp.json()["id"]
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id


def test_get_user_not_found():
    response = client.get("/users/999")
    assert response.status_code == 404


def test_patch_user_not_found():
    patch_data = {"fullName": "Patched User"}
    response = client.patch("/users/999", json=patch_data)
    assert response.status_code == 404


def test_patch_user_invalid_id():
    patch_data = {"fullName": "Patched User"}
    response = client.patch("/users/invalid_id", json=patch_data)
    assert response.status_code == 404


def test_patch_user_no_fields():
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "fullName": "Test User",
        "dni": "12345678",
        "phoneNumber": "5551234",
        "status": "POR_VERIFICAR",
        "password": "password123",
    }
    create_resp = client.post("/users/", json=user_data)
    user_id = create_resp.json()["id"]
    response = client.patch(f"/users/{user_id}", json={})
    assert response.status_code == 400


def test_delete_user():
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "fullName": "Test User",
        "dni": "12345678",
        "phoneNumber": "5551234",
        "status": "POR_VERIFICAR",
        "password": "password123",
    }
    create_resp = client.post("/users/", json=user_data)
    user_id = create_resp.json()["id"]
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    # Confirm user is deleted
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 404


def test_delete_user_not_found():
    response = client.delete("/users/999")
    assert response.status_code == 404


def test_count_users():
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "fullName": "Test User",
        "dni": "12345678",
        "phoneNumber": "5551234",
        "status": "POR_VERIFICAR",
        "password": "password123",
    }
    client.post("/users/", json=user_data)
    response = client.get("/users/count")
    assert response.status_code == 200
    assert "count" in response.json()
    assert response.json()["count"] == 1


def test_authenticate_user_missing_fields():
    auth_data = {"username": "", "password": ""}
    response = client.post("/users/auth", json=auth_data)
    assert response.status_code == 400


def test_authenticate_user_not_found():
    auth_data = {"username": "nouser", "password": "nopassword"}
    response = client.post("/users/auth", json=auth_data)
    assert response.status_code == 404


def test_get_current_user():
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "fullName": "Test User",
        "dni": "12345678",
        "phoneNumber": "5551234",
        "status": "POR_VERIFICAR",
        "password": "password123",
    }
    client.post("/users/", json=user_data)
    auth_data = {"username": "testuser", "password": "password123"}
    auth_resp = client.post("/users/auth", json=auth_data)
    token = auth_resp.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users/me", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "testuser@example.com"
    assert data["fullName"] == "Test User"
    assert data["dni"] == "12345678"
    assert data["phoneNumber"] == "5551234"
    assert data["status"] == "POR_VERIFICAR"
    assert "id" in data


def test_get_current_user_missing_token():
    response = client.get("/users/me")
    assert response.status_code == 403


def test_get_current_user_invalid_token():
    headers = {"Authorization": "Bearer invalidtoken"}
    response = client.get("/users/me", headers=headers)
    assert response.status_code == 401


def test_reset_users():
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "fullName": "Test User",
        "dni": "12345678",
        "phoneNumber": "5551234",
        "status": "POR_VERIFICAR",
        "password": "password123",
    }
    client.post("/users/", json=user_data)
    response = client.post("/users/reset")
    assert response.status_code == 200
    response = client.get("/users/count")
    assert response.json()["count"] == 0
