from typing import Optional

from sqlmodel import Field, Relationship, SQLModel
from sb_backend.app.models.base.base_model import TimeStampMixin
from .noseries import NoSeries

class NoSeriesSetupBase(SQLModel):
    """«No Series Setup» («Биллинг Настройка»)"""
    setup_series_no_id: int = Field(default=None, foreign_key="no_series.id")
    setup_series_no: Optional[NoSeries] = Relationship(back_populates = "noseriessetup")

class NoSeriesSetup(NoSeriesSetupBase, TimeStampMixin, table=True):
    """«No Series Setup» («Биллинг Настройка»)"""
    __tablename__ = "noseries_setup"
    id: Optional[int] = Field(default=None, primary_key=True)

class NoSeriesSetupCreate(NoSeriesSetupBase):
    """«No Series Setup» («Биллинг Настройка»)"""
    pass


class NoSeriesSetupRead(NoSeriesSetupBase):
    """«No Series Setup» («Биллинг Настройка»)"""
    id: int

class NoSeriesSetupUpdate(SQLModel):
    """«No Series Setup» («Биллинг Настройка»)"""
    pass