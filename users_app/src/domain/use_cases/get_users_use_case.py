from typing import List

from domain.models.user import User
from domain.ports.user_repository_port import UserRepositoryPort
from domain.use_cases.base_use_case import BaseUseCase


class GetAllUsersUseCase(BaseUseCase):
    """Use case for getting all users."""

    def __init__(self, user_repository: UserRepositoryPort):
        self.user_repository = user_repository

    def execute(self) -> List[User]:
        return self.user_repository.get_all()
