from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
import uuid

# Esquema base para la creación de un usuario
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8)
    email: EmailStr
    dni: Optional[str] = None
    fullName: Optional[str] = None
    phoneNumber: Optional[str] = None

# Esquema para la actualización de un usuario
class UserUpdate(BaseModel):
    status: Optional[str] = None
    dni: Optional[str] = None
    fullName: Optional[str] = None
    phoneNumber: Optional[str] = None

# Esquema para la respuesta al crear un usuario
class UserCreatedResponse(BaseModel):
    id: uuid.UUID
    createdAt: datetime

    class Config:
        orm_mode = True

# Esquema para la respuesta de la información del usuario
class UserOut(BaseModel):
    id: uuid.UUID
    username: str
    email: EmailStr
    fullName: Optional[str]
    dni: Optional[str]
    phoneNumber: Optional[str]
    status: str

    class Config:
        orm_mode = True

# Esquema para el cuerpo de la solicitud de autenticación
class UserLogin(BaseModel):
    username: str
    password: str

# Esquema para la respuesta del token
class Token(BaseModel):
    id: uuid.UUID
    token: str
    expireAt: datetime
