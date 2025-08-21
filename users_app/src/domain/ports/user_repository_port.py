from abc import ABC, abstractmethod
from typing import List, Optional

from domain.models.user import User


class UserRepositoryPort(ABC):
    """User repository interface."""

    @abstractmethod
    def create(self, user: User) -> User:
        """Create a new user."""
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        """Get user by ID."""
        pass

    @abstractmethod
    def get_all(self) -> List[User]:
        """Get all users."""
        pass

    @abstractmethod
    def update(self, user: User) -> User:
        """Update an existing user."""
        pass

    @abstractmethod
    def delete(self, user_id: int) -> User:
        """Delete user."""
        pass
