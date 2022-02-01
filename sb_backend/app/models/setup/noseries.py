from typing import List, Optional

from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import relationship
from sqlmodel import Field, Relationship, SQLModel
from sb_backend.app.models.base.base_model import TimeStampMixin


class NoSeriesBase(SQLModel):
    """«No. Series» («Серия Номеров»)"""
    code: str = Field(max_length=20, nullable=False, default="")
    description: str = Field(max_length=100)
    date_order: bool = False

    noserieslines: List["NoSeriesLine"] = Relationship(
        sa_relationship_kwargs=relationship(
            "NoSeriesLine", cascade="all, delete, delete-orphan", back_populates="series_no", passive_deletes=True
        ),
    )
    noseriessetup: List["NoSeriesSetup"] = Relationship(back_populates="setup_series_no")

class NoSeries(NoSeriesBase, TimeStampMixin, table=True):
    """«No. Series» («Серия Номеров»)"""
    __tablename__ = "no_series"
    __table_args__ = (UniqueConstraint("code"),)
    id: Optional[int] = Field(default=None, primary_key=True)

    def __repr__(self):
        return f'<NoSeries({self.code})>'

class NoSeriesCreate(NoSeriesBase):
    """«No. Series» («Серия Номеров»)"""
    code: str

class NoSeriesRead(NoSeriesBase):
    """«No. Series» («Серия Номеров»)"""
    id: int
    # noserieslines: Optional[NoSeriesLine]

class NoSeriesUpdate(SQLModel):
    """«No. Series» («Серия Номеров»)"""
    code: str
    description: Optional[str]
    date_order: Optional[bool] = False
