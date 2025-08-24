from enum import Enum
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from pydantic import BaseModel, EmailStr, Field

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: int | None = Column(Integer, primary_key=True, index=True)
    username: str = Column(String, unique=True, index=True, nullable=False)
    password: str = Column(String, nullable=False)
    email: EmailStr = Column(String, unique=True, index=True, nullable=False)
    dni: str = Column(String, nullable=False)
    fullName: str = Column(String, nullable=False)
    phoneNumber: str = Column(String, nullable=False)
    status: str = Column(String, nullable=False)
