from typing import Optional

from pydantic import BaseModel


class UserPatch(BaseModel):
    fullName: Optional[str] = None
    phoneNumber: Optional[str] = None
    dni: Optional[str] = None
    status: Optional[str] = None
