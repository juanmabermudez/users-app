from domain.models.user import User
from domain.ports.user_repository_port import UserRepositoryPort
from domain.use_cases.base_use_case import BaseUseCase


class DeleteUserUseCase(BaseUseCase):
    """Use case for deleting a user."""

    def __init__(self, user_repository: UserRepositoryPort):
        self.user_repository = user_repository

    def execute(self, user_id: int) -> User:
        return self.user_repository.delete(user_id)
