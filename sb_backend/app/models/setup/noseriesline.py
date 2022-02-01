import datetime
from typing import Optional

from pydantic import PositiveInt
from sqlalchemy import Integer, ForeignKey
from sqlmodel import Field, Column, DateTime, Relationship, SQLModel
from sqlalchemy import UniqueConstraint
from sb_backend.app.models.base.base_model import TimeStampMixin

from sb_backend.app.models.fields import SeriesCode
from .noseries import NoSeries

class NoSeriesLineBase(SQLModel):
    """«No. Series Line» («Серия Номеров Строка»)"""
    starting_date:  datetime.datetime = Field(
      sa_column=Column(
          DateTime(timezone=True),
          nullable=False
      )
    )

    starting_no: SeriesCode
    ending_no: SeriesCode
    # starting_no: str = Field(max_length=20, nullable=False)
    # ending_no: str = Field(max_length=20, nullable=True, default='')
    last_date_used:  datetime.datetime = Field(
      sa_column=Column(
          DateTime(timezone=True),
          nullable=True
      )
    )
    warning_no: str = Field(max_length=20, nullable=True, default='')
    last_no_used: str = Field(max_length=20, nullable=True, default='')
    increment_by: PositiveInt = Field(default=1)
    blocked: bool = False

    # series_no_id:  int = Field(
    #   sa_column=Column(
    #       Integer,
    #       ForeignKey(NoSeries.id, ondelete="CASCADE"),
    #   ),
    #  nullable = False
    # )
    # ForeignKey(NoSeries.id, ondelete="RESTRICT"),

    # series_no_id: int = Field(default=None, foreign_key="no_series.id")
    series_no_id: int
    series_no: Optional[NoSeries] = Relationship(back_populates = "noserieslines")

class NoSeriesLine(NoSeriesLineBase, TimeStampMixin, table=True):
    """«No. Series Line» («Серия Номеров Строка»)"""
    __tablename__ = "no_series_line"
    __table_args__ = (UniqueConstraint("series_no_id", "starting_date"),)
    id: Optional[int] = Field(default=None, primary_key=True)
    series_no_id:  int = Field(
      sa_column=Column(
          Integer,
          ForeignKey(NoSeries.id, ondelete="RESTRICT"),
      ),
     nullable = False
    )

class NoSeriesLineCreate(NoSeriesLineBase):
    """«No. Series Line» («Серия Номеров Строка»)"""
    pass

class NoSeriesLineRead(NoSeriesLineBase):
    """«No. Series Line» («Серия Номеров Строка»)"""
    id: int

class NoSeriesLineUpdate(SQLModel):
    """«No. Series Line» («Серия Номеров Строка»)"""
    starting_date: datetime.datetime
    starting_no: SeriesCode
    ending_no: Optional[SeriesCode]
    last_date_used: datetime.datetime
    warning_no: Optional[SeriesCode]
    increment_by: Optional[PositiveInt] = 1
    blocked: Optional[bool] = False
    series_no_id: PositiveInt

    # series_no_id: Optional[int] = None