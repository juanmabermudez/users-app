from domain.ports.user_repository_port import UserRepositoryPort

class ResetUsersUseCase:
    def __init__(self, user_repository: UserRepositoryPort):
        self.user_repository = user_repository

    def execute(self) -> dict:
        # Sin acceder a atributos internos del adapter.
        # Usamos únicamente el puerto: get_all + delete
        for u in list(self.user_repository.get_all()):
            self.user_repository.delete(u.id)
        return {"msg": "Todos los datos fueron eliminados"}