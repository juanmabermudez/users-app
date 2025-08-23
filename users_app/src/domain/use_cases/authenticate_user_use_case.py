from uuid import uuid4
from datetime import datetime, timedelta
from domain.ports.user_repository_port import UserRepositoryPort
from domain.models.token_response import TokenResponse
from errors import UserNotFoundError

class AuthenticateUserUseCase:
    def __init__(self, user_repository: UserRepositoryPort):
        self.user_repository = user_repository
        self.tokens = {}  # Opcional: almacena tokens en memoria

    def execute(self, username: str, password: str) -> TokenResponse:
        # Busca el usuario por username
        users = self.user_repository.get_all()
        user = next((u for u in users if u.username == username and u.password == password), None)
        if not user:
            raise UserNotFoundError("Usuario no encontrado")
        token = str(uuid4())
        expire_at = (datetime.utcnow() + timedelta(hours=1)).isoformat()
        self.tokens[token] = {"user_id": user.id, "expire_at": expire_at}
        return TokenResponse(id=user.id, token=token, expireAt=expire_at)