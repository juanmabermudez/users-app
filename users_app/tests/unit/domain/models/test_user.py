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


def test_create_user_with_id(user_with_id):
    """Test creating a user with an ID."""
    assert user_with_id.id == 1
    assert user_with_id.username == "jtapia"
    assert user_with_id.password == "password123"
    assert user_with_id.email == "tapia23@gmail.com"
    assert user_with_id.dni == "223432345"
    assert user_with_id.fullName == "Pedro Alicante"
    assert user_with_id.phoneNumber == "3123452342"


def test_create_user_with_invalid_type(valid_user_data):
    """Test creating a user with an invalid type."""
    with pytest.raises(ValidationError) as exc_info:
        User(**{**valid_user_data, "type": "invalid_type"})  # type: ignore

    assert "type" in str(exc_info.value)
    assert "Input should be" in str(exc_info.value)


def test_create_user_with_negative_age(valid_user_data):
    """Test creating a user with a negative age."""
    with pytest.raises(ValidationError) as exc_info:
        User(**{**valid_user_data, "age": -1})

    assert "age" in str(exc_info.value)
    assert "Input should be greater than 0" in str(exc_info.value)


def test_create_user_with_empty_name(valid_user_data):
    """Test creating a user with an empty name."""
    with pytest.raises(ValidationError) as exc_info:
        User(**{**valid_user_data, "name": ""})

    assert "name" in str(exc_info.value)
    assert "String should have at least 1 character" in str(exc_info.value)


def test_create_user_with_empty_owner_name(valid_user_data):
    """Test creating a user with an empty owner name."""
    with pytest.raises(ValidationError) as exc_info:
        User(**{**valid_user_data, "owner_name": ""})

    assert "owner_name" in str(exc_info.value)
    assert "String should have at least 1 character" in str(exc_info.value)


def test_create_user_with_none_values():
    """Test creating a user with None values for required fields."""
    with pytest.raises(ValidationError) as exc_info:
        User(
            name=None,  # type: ignore
            age=None,  # type: ignore
            owner_name=None,  # type: ignore
        )

    assert "name" in str(exc_info.value)
    assert "age" in str(exc_info.value)
    assert "owner_name" in str(exc_info.value)


def test_create_user_with_extra_fields(valid_user_data):
    """Test creating a user with extra fields."""
    user = User(**valid_user_data, extra_field="extra")  # type: ignore

    assert not hasattr(user, "extra_field")


def test_user_model_equality(user_with_id):
    """Test user model equality."""
    user2 = User(id=1, name="Rex", age=5, owner_name="John Doe")

    assert user_with_id == user2


def test_user_model_inequality(user_with_id):
    """Test user model inequality."""
    user2 = User(id=2, name="Rex", age=5, owner_name="John Doe")

    assert user_with_id != user2


def test_user_model_dict_conversion(user_with_id):
    """Test user model conversion to dictionary."""
    user_dict = user_with_id.model_dump()
    assert user_dict == {
        "id": 1,
        "name": "Rex",
        "age": 5,
        "owner_name": "John Doe",
    }


def test_user_model_json_conversion(user_with_id):
    """Test user model conversion to JSON."""
    user_json = user_with_id.model_dump_json()
    assert (
        user_json == '{"id":1,"name":"Rex","age":5,"owner_name":"John Doe"}'
    )
