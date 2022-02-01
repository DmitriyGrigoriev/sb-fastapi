from typing import Optional
from decimal import Decimal

from pydantic import condecimal
from sqlmodel import Field, SQLModel
from sqlalchemy import UniqueConstraint
from sb_backend.app.utils import constants
from sb_backend.app.models.base.base_model import TimeStampMixin


class VatPostingGroupBase(SQLModel):
    """«VAT Posting Group» («НДС  Учетная Группа»)"""
    code: str = Field(max_length=20, nullable=False, default="")
    description: str = Field(max_length=50)
    vat: condecimal(max_digits=constants.VAT_MAX_DIGITS, decimal_places=constants.VAT_MAX_DECIMAL) = Field(default=0)
    vatextempt: bool = False

class VatPostingGroup(VatPostingGroupBase, TimeStampMixin, table=True):
    """«VAT Posting Group» («НДС  Учетная Группа»)"""
    __tablename__ = "vat_posting_group"
    __table_args__ = (UniqueConstraint("code"),)
    id: Optional[int] = Field(default=None, primary_key=True)

class VatPostingGroupCreate(VatPostingGroupBase):
    """«VAT Posting Group» («НДС  Учетная Группа»)"""
    code: str

class VatPostingGroupRead(VatPostingGroupBase):
    """«VAT Posting Group» («НДС  Учетная Группа»)"""
    id: int

class VatPostingGroupUpdate(SQLModel):
    """«VAT Posting Group» («НДС  Учетная Группа»)"""
    code: str
    description: Optional[str] = None
    vat: Decimal = 0.00
    vatextempt: Optional[bool] = False
