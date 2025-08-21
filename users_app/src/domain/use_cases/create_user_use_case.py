from users_app.src.domain.models.user import User
from users_app.src.domain.ports.user_repository_port import PetRepositoryPort
from domain.use_cases.base_use_case import BaseUseCase


class CreatePetUseCase(BaseUseCase):
    """Use case for saving a pet."""

    def __init__(self, pet_repository: PetRepositoryPort):
        self.pet_repository = pet_repository

    def execute(self, pet: Pet) -> Pet:
        """Create a new pet."""
        return self.pet_repository.create(pet)
