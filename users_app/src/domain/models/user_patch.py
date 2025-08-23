from pydantic import BaseModel
from typing import Optional

class UserPatch(BaseModel):
    fullName: Optional[str] = None
    phoneNumber: Optional[str] = None
    dni: Optional[str] = None
    status: Optional[str] = None