from domain.models.user import User
from domain.ports.user_repository_port import UserRepositoryPort
from domain.use_cases.base_use_case import BaseUseCase
from errors import UserNotFoundError


class UpdateUserUseCase(BaseUseCase):
    """Use case for updating a user."""

    def __init__(self, user_repository: UserRepositoryPort):
        self.user_repository = user_repository

    def execute(self, user_id: int, update_data: dict) -> None:
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise UserNotFoundError("Usuario no encontrado")
        for key, value in update_data.items():
            setattr(user, key, value)
        self.user_repository.update(user)