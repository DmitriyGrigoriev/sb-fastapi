from typing import Optional

from pydantic import validator
from sqlmodel import Field, SQLModel
from sqlalchemy import UniqueConstraint
from sb_backend.app.models.base.base_model import TimeStampMixin

from ..validators import to_upper

class ServiceTypeBase(SQLModel):
    """«Service Type» («Тип Услуги»)"""
    code: str = Field(max_length=20, nullable=False, default="")
    description: str = Field(max_length=50)

    # validators
    _normalize_code = validator('code', allow_reuse=True)(to_upper)

class ServiceType(ServiceTypeBase, TimeStampMixin, table=True):
    """«Service Type» («Тип Услуги»)"""
    __tablename__ = "service_type"
    __table_args__ = (UniqueConstraint("code"),)
    id: Optional[int] = Field(default=None, primary_key=True)

class ServiceTypeCreate(ServiceTypeBase):
    """«Unit of Measure» («Единица Измерения»)"""
    description: str

class ServiceTypeRead(ServiceTypeBase):
    """«Unit of Measure» («Единица Измерения»)"""
    id: int

class ServiceTypeUpdate(SQLModel):
    """«Unit of Measure» («Единица Измерения»)"""
    code: str
    description: str
