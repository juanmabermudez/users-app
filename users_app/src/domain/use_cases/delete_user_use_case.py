from users_app.src.domain.models.user import Pet
from users_app.src.domain.ports.user_repository_port import PetRepositoryPort
from domain.use_cases.base_use_case import BaseUseCase


class DeletePetUseCase(BaseUseCase):
    """Use case for deleting a pet."""

    def __init__(self, pet_repository: PetRepositoryPort):
        self.pet_repository = pet_repository

    def execute(self, pet_id: int) -> Pet:
        return self.pet_repository.delete(pet_id)
