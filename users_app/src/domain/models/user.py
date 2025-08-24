from enum import Enum

from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    """User domain model."""

    id: int | None = None
    username: str = Field(min_length=1, description="Nombre de usuario")
    password: str = Field(min_length=1, description="Contraseña del usuario")
    email: EmailStr = Field(description="Correo electrónico del usuario")
    dni: str = Field(min_length=1, description="Identificación")
    fullName: str = Field(min_length=1, description="Nombre completo del usuario")
    phoneNumber: str = Field(min_length=1, description="Número de teléfono")
    status: str = Field(default="POR_VERIFICAR", description="Estado del usuario")
