import pytest

from domain.models.user import User


@pytest.fixture
def valid_pet_data():
    """Fixture providing valid pet data."""
    return {"username": "jtapia", "password": "password123", 
            "email": "tapia23@gmail.com","dni": "223432345",
            "fullName": "Pedro Alicante", "phoneNumber": "3123452342"}


@pytest.fixture
def pet_with_id():
    """Fixture providing a pet with ID."""
    return User(id=1, name="Rex", age=5, owner_name="John Doe",
                username="jtapia", password="password123",
                email="tapia23@gmail.com",dni="223432345",
                fullName="Pedro Alicante", phoneNumber="3123452342")


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
