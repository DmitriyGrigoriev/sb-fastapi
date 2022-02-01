from typing import Optional

from pydantic import validator
from sqlmodel import Field, SQLModel
from sqlalchemy import UniqueConstraint
from sb_backend.app.models.base.base_model import TimeStampMixin

from ..validators import to_lower


class MeasureBase(SQLModel):
    """«Unit of Measure» («Единица Измерения»)"""
    code: str = Field(max_length=20, nullable=False, default="")
    description: str = Field(max_length=50)
    okei_code: str = Field(max_length=3, nullable=True)

    # validators
    _normalize_code = validator('code', allow_reuse=True)(to_lower)

class Measure(MeasureBase, TimeStampMixin, table=True):
    """«Unit of Measure» («Единица Измерения»)"""
    __tablename__ = "measure"
    __table_args__ = (UniqueConstraint("code"),)
    id: Optional[int] = Field(default=None, primary_key=True)

class MeasureCreate(MeasureBase):
    """«Unit of Measure» («Единица Измерения»)"""
    pass

class MeasureRead(MeasureBase):
    """«Unit of Measure» («Единица Измерения»)"""
    id: int

class MeasureUpdate(SQLModel):
    """«Unit of Measure» («Единица Измерения»)"""
    code: str
    description: Optional[str]
    okei_code: Optional[str]
