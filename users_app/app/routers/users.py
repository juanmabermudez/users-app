from fastapi import APIRouter, Depends, HTTPException, status, Header
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
import uuid

from .. import models, schemas
from ..database import get_db
from ..utils import security

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

# 1. Creación de usuarios
@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.UserCreatedResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Verificar si el username o email ya existen
    existing_user = db.query(models.User).filter(
        (models.User.username == user.username) | (models.User.email == user.email)
    ).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_412_PRECONDITION_FAILED, detail="Username or email already exists")

    salt = security.get_salt()
    hashed_password = security.hash_password(user.password, salt)

    new_user = models.User(
        username=user.username,
        email=user.email,
        password=hashed_password,
        salt=salt.decode('utf-8'), # Guardar la sal como string
        fullName=user.fullName,
        dni=user.dni,
        phoneNumber=user.phoneNumber
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# 2. Actualización de usuarios
@router.patch("/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: uuid.UUID, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id == user_id)
    user = user_query.first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")

    update_data = user_update.dict(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No fields to update")

    user_query.update(update_data, synchronize_session=False)
    db.commit()
    return {"msg": "el usuario ha sido actualizado"}

# 3. Generación de token
@router.post("/auth", response_model=schemas.Token)
def login_for_token(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == user_credentials.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    # La sal se guardó como string, hay que codificarla de nuevo a bytes
    salt_bytes = user.salt.encode('utf-8')
    
    if not security.verify_password(user_credentials.password, user.password, salt_bytes):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    token, expire_at = security.generate_token()
    user.token = token
    user.expireAt = expire_at
    db.commit()
    db.refresh(user)

    return {"id": user.id, "token": token, "expireAt": expire_at}

# 4. Consultar información del usuario
@router.get("/me", response_model=schemas.UserOut)
def read_users_me(authorization: Optional[str] = Header(None), db: Session = Depends(get_db)):
    if authorization is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Authorization header is missing")
    
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authentication scheme")
    except ValueError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authorization header format")

    user = db.query(models.User).filter(models.User.token == token).first()

    if not user or user.expireAt < datetime.utcnow():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")

    return user

# 5. Consultar cantidad de entidades
@router.get("/count", response_model=dict)
def get_user_count(db: Session = Depends(get_db)):
    count = db.query(models.User).count()
    return {"count": count}

# 6. Consulta de salud del servicio
@router.get("/ping")
def ping():
    return "pong"

# 7. Restablecer base de datos
@router.post("/reset", status_code=status.HTTP_200_OK)
def reset_database(db: Session = Depends(get_db)):
    db.query(models.User).delete()
    db.commit()
    return {"msg": "Todos los datos fueron eliminados"}
