from typing import List

from users_app.src.domain.models.user import Pet
from users_app.src.domain.ports.user_repository_port import PetRepositoryPort
from domain.use_cases.base_use_case import BaseUseCase


class GetAllPetsUseCase(BaseUseCase):
    """Use case for getting all pets."""

    def __init__(self, pet_repository: PetRepositoryPort):
        self.pet_repository = pet_repository

    def execute(self) -> List[Pet]:
        return self.pet_repository.get_all()
