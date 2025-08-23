from domain.ports.user_repository_port import UserRepositoryPort

class CountUsersUseCase:
    def __init__(self, user_repository: UserRepositoryPort):
        self.user_repository = user_repository

    def execute(self) -> int:
        return len(self.user_repository.get_all())