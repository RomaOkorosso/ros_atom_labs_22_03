from sqlalchemy import Text, Column, Integer, Enum, DateTime
from .db import Base
from enum import IntEnum
from sqlalchemy.sql import func


class GenderEnum(IntEnum):
    male = 0
    female = 1


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    email = Column(Text, nullable=False, unique=True, index=True)
    age = Column(Integer)
    gender = Column(Enum(GenderEnum), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), server_onupdate=func.now())
