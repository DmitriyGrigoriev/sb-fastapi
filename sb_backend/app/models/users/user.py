from typing import Optional

from pydantic import EmailStr
from sqlmodel import Field, SQLModel
from sb_backend.app.models.base.base_model import TimeStampMixin

# Shared properties
class UserBase(SQLModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = Field(default=None, primary_key=True)


# Additional properties to return via API
class User(UserInDBBase, TimeStampMixin, table=True):
    __tablename__ = "user"
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
