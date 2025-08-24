from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app import schemas
import uuid

# Prueba para el endpoint de salud /ping
def test_ping(client: TestClient):
    response = client.get("/users/ping")
    assert response.status_code == 200
    assert response.text == '"pong"'

# Prueba de creación de usuario exitosa
def test_create_user_success(client: TestClient):
    response = client.post(
        "/users",
        json={"username": "testuser", "email": "test@example.com", "password": "password123"}
    )
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert "createdAt" in data

# Prueba de creación de usuario con username duplicado
def test_create_user_duplicate_username(client: TestClient):
    # Crear un usuario primero
    client.post("/users", json={"username": "testuser", "email": "test@example.com", "password": "password123"})
    
    # Intentar crear otro con el mismo username
    response = client.post(
        "/users",
        json={"username": "testuser", "email": "another@example.com", "password": "password123"}
    )
    assert response.status_code == 412
    assert response.json()["detail"] == "Username or email already exists"

# Prueba de autenticación y obtención de token
def test_login_for_token(client: TestClient, db_session: Session):
    # Crear un usuario para la prueba de login
    create_response = client.post(
        "/users",
        json={"username": "loginuser", "email": "login@example.com", "password": "password123"}
    )
    assert create_response.status_code == 201

    # Intentar login
    login_response = client.post(
        "/users/auth",
        json={"username": "loginuser", "password": "password123"}
    )
    assert login_response.status_code == 200
    token_data = login_response.json()
    assert "token" in token_data
    assert "expireAt" in token_data
    return token_data["token"] # Devolver el token para usarlo en otra prueba

# Prueba para consultar información del usuario autenticado (/me)
def test_read_users_me(client: TestClient):
    # Primero, obtener un token
    token = test_login_for_token(client, None) # Pasamos None para db_session porque la función de login lo gestiona

    # Realizar la solicitud a /me con el token
    response = client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    user_data = response.json()
    assert user_data["username"] == "loginuser"
    assert user_data["email"] == "login@example.com"

# Prueba para el endpoint de conteo de usuarios
def test_get_user_count(client: TestClient):
    # Crear algunos usuarios
    client.post("/users", json={"username": "user1", "email": "user1@example.com", "password": "password123"})
    client.post("/users", json={"username": "user2", "email": "user2@example.com", "password": "password123"})
    
    response = client.get("/users/count")
    assert response.status_code == 200
    assert response.json()["count"] == 2

# Prueba para el endpoint de reseteo de la base de datos
def test_reset_database(client: TestClient):
    # Crear un usuario
    client.post("/users", json={"username": "user_to_delete", "email": "delete@example.com", "password": "password123"})
    
    # Verificar que el usuario existe
    count_before = client.get("/users/count").json()["count"]
    assert count_before > 0
    
    # Resetear la base de datos
    reset_response = client.post("/users/reset")
    assert reset_response.status_code == 200
    assert reset_response.json()["msg"] == "Todos los datos fueron eliminados"
    
    # Verificar que no hay usuarios
    count_after = client.get("/users/count").json()["count"]
    assert count_after == 0
