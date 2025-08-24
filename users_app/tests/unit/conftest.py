import pytest

from domain.models.user import User


@pytest.fixture
def valid_user_data():
    return {
        "username": "testuser",
        "email": "testuser@example.com",
        "fullName": "Test User",
        "dni": "12345678",
        "phoneNumber": "5551234",
        "status": "POR_VERIFICAR",
        "password": "password123"
    }


@pytest.fixture
def user_with_id(valid_user_data):
    data = valid_user_data.copy()
    data["id"] = 1
    return data
