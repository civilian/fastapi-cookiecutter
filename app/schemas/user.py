from peewee import Model
from pydantic import BaseModel, EmailStr
from typing import Optional

from app.db.connector import models
from .utils import PeeweeGetterDict


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    password: str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
