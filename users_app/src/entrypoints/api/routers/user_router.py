from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Body
from fastapi.responses import JSONResponse, PlainTextResponse

from assembly import (
    build_create_user_use_case,
    build_delete_user_use_case,
    build_get_user_use_case,
    build_get_users_use_case,
    build_update_user_use_case,
)
from domain.models.user import User
from domain.models.user_patch import UserPatch
from domain.use_cases.base_use_case import BaseUseCase
from errors import UserNotFoundError, UserAlreadyExistsError

router = APIRouter(prefix="/users")


@router.get("/ping", response_class=PlainTextResponse)
def health_check():
    """Healthcheck endpoint."""
    return "pong"


@router.post("/", response_model=User, status_code=201)
def create_user(user: User, use_case: BaseUseCase = Depends(build_create_user_use_case)):
    """Create a new user."""
    try:
        created_user = use_case.execute(user)
        created_at = datetime.utcnow()
        return JSONResponse(
            status_code=201,
            content={
                "id": created_user.id,
                "createdAt": created_at.isoformat()
            }
        )
    except UserAlreadyExistsError as err:
        return JSONResponse({"error": str(err)}, status_code=412)
    except UserNotFoundError as err:
        return JSONResponse({"error": str(err)}, status_code=404)


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, use_case: BaseUseCase = Depends(build_get_user_use_case)):
    """Get a user by ID."""
    user = use_case.execute(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/", response_model=List[User])
def get_users(use_case: BaseUseCase = Depends(build_get_users_use_case)):
    """Get all users."""
    return use_case.execute()


@router.put("/{user_id}", response_model=User)
def update_user(
    user_id: int, user: User, use_case: BaseUseCase = Depends(build_update_user_use_case)
):
    """Update user."""
    try:
        user.id = user_id
        return use_case.execute(user)
    except UserNotFoundError as err:
        return JSONResponse({"error": str(err)}, status_code=404)


@router.delete("/{user_id}", response_model=User)
def delete_user(user_id: int, use_case: BaseUseCase = Depends(build_delete_user_use_case)):
    """Delete user."""
    try:
        return use_case.execute(user_id)
    except UserNotFoundError as err:
        return JSONResponse({"error": str(err)}, status_code=404)


@router.patch("/{user_id}")
def patch_user(
    user_id: str,
    body: UserPatch = Body(...),
    use_case: BaseUseCase = Depends(build_update_user_use_case)
):
    # Intentar convertir a entero
    try:
        user_id_int = int(user_id)
    except ValueError:
        return JSONResponse(
            status_code=404,
            content={"error": "Usuario no encontrado"}
        )

    update_data = body.dict(exclude_unset=True)
    if not update_data:
        return JSONResponse(
            status_code=400,
            content={"error": "Debe enviar al menos uno de los campos esperados: fullName, phoneNumber, dni, status"}
        )
    try:
        use_case.execute(user_id_int, update_data)
        return JSONResponse(
            status_code=200,
            content={"msg": "el usuario ha sido actualizado"}
        )
    except UserNotFoundError:
        return JSONResponse(
            status_code=404,
            content={"error": "Usuario no encontrado"}
        )