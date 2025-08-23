from datetime import datetime
from errors import UserNotFoundError
from domain.use_cases.authenticate_user_use_case import AuthenticateUserUseCase

class GetCurrentUserUseCase:
    def __init__(self, auth_use_case: AuthenticateUserUseCase):
        self.auth = auth_use_case  # contiene repository y tokens

    def execute(self, token: str):
        data = self.auth.tokens.get(token)
        if not data:
            raise UserNotFoundError("Token inválido")

        expire_at = datetime.fromisoformat(data["expire_at"])
        if datetime.utcnow() > expire_at:
            raise UserNotFoundError("Token expirado")

        user = self.auth.user_repository.get_by_id(data["user_id"])
        if not user:
            raise UserNotFoundError("Usuario no encontrado")
        return user
