import pytest
from pydantic import ValidationError

from domain.models.user import User


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


def test_create_user_with_id(user_with_id):
    """Test creating a user with an ID."""
    assert user_with_id.id == 1
    assert user_with_id.username == "jtapia"
    assert user_with_id.password == "password123"
    assert user_with_id.email == "tapia23@gmail.com"
    assert user_with_id.dni == "223432345"
    assert user_with_id.fullName == "Pedro Alicante"
    assert user_with_id.phoneNumber == "3123452342"
    assert user_with_id.status == "POR_VERIFICAR"


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


def test_user_model_dict_conversion(user_with_id):
    """Test user model conversion to dictionary."""
    user_dict = user_with_id.model_dump()
    assert user_dict == {
        "id": 1,
        "username": "jtapia",
        "password": "password123",
        "email": "tapia23@gmail.com",
        "dni": "223432345",
        "fullName": "Pedro Alicante",
        "phoneNumber": "3123452342",
        "status": "POR_VERIFICAR",
    }
