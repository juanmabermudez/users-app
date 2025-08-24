from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from domain.models.user import User
from domain.ports.user_repository_port import UserRepositoryPort
from errors import UserAlreadyExistsError, UserNotFoundError


class PostgresUserRepositoryAdapter(UserRepositoryPort):
    """PostgreSQL implementation of UserRepository."""

    def __init__(self, db: Session):
        self.db = db

    def create(self, user: User) -> User:
        # Validación de username y email únicos
        exists = self.db.query(User).filter(
            (User.username == user.username) | (User.email == user.email)
        ).first()
        if exists:
            raise UserAlreadyExistsError("Username or email already exists")
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_all(self) -> List[User]:
        return self.db.query(User).all()

    def update(self, user: User) -> User:
        db_user = self.get_by_id(user.id)
        if not db_user:
            raise UserNotFoundError(f"User with id {user.id} not found")
        for field, value in user.model_dump().items():
            setattr(db_user, field, value)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete(self, user_id: int) -> User:
        db_user = self.get_by_id(user_id)
        if not db_user:
            raise UserNotFoundError(f"User with id {user_id} not found")
        self.db.delete(db_user)
        self.db.commit()
        return db_user

    def clear_all(self):
        self.db.query(User).delete()
        self.db.commit()