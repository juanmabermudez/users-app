from pydantic import BaseModel


class TokenResponse(BaseModel):
    id: int
    token: str
    expireAt: str
