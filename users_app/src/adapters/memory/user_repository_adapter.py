from typing import Dict, List, Optional

from domain.models.user import User
from domain.ports.user_repository_port import UserRepositoryPort
from errors import UserAlreadyExistsError, UserNotFoundError


class InMemoryUserRepositoryAdapter(UserRepositoryPort):
    """In memory implementation of UserRepository."""

    memory_store: Dict[int, User] = {}

    def sequence(self) -> int:
        """Generate a new sequence number."""
        return len(self.memory_store) + 1

    def create(self, user: User) -> User:
        """Create a new user."""
        # Validación de username y email únicos
        for existing_user in self.memory_store.values():
            if existing_user.username == user.username or existing_user.email == user.email:
                raise UserAlreadyExistsError("Username or email already exists")
        user.id = self.sequence()
        self.memory_store[user.id] = user
        return user

    def get_by_id(self, user_id: int) -> Optional[User]:
        """Get user by ID."""
        return self.memory_store.get(user_id)

    def get_all(self) -> List[User]:
        """Get all users."""
        return list(self.memory_store.values())

    def update(self, user: User) -> User:
        """Update an existing user."""
        if user.id not in self.memory_store:
            raise UserNotFoundError(f"User with id {user.id} not found")
        self.memory_store[user.id] = user
        return user

    def delete(self, user_id: int) -> User:
        """Delete a user."""
        if user_id not in self.memory_store:
            raise UserNotFoundError(f"User with id {user_id} not found")
        user = self.memory_store[user_id]
        del self.memory_store[user_id]
        return user
