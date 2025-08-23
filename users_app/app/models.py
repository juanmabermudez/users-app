from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    salt = Column(String, nullable=False)
    token = Column(String, nullable=True)
    status = Column(String, nullable=False, default="POR_VERIFICAR")
    fullName = Column(String, nullable=True)
    phoneNumber = Column(String, nullable=True)
    dni = Column(String, nullable=True)
    expireAt = Column(DateTime, nullable=True)
    createdAt = Column(DateTime, server_default=func.now())
    updatedAt = Column(DateTime, server_default=func.now(), onupdate=func.now())
