from typing import List
from fastapi import APIRouter, Depends, Query, status

from sqlmodel import Session
from sb_backend.app import service
from sb_backend.app.db.session import get_session
from sb_backend.app.schemas import ErrorResponse
from sb_backend.app.models.setup.noseriesline import (
    NoSeriesLineRead, NoSeriesLineUpdate, NoSeriesLineCreate
)

DEFAULT_URL = "/"
DEFAULT_URL_PATH = DEFAULT_URL + "{item_id}"

noseriesline_router = APIRouter(tags=['noseriesline'])

@noseriesline_router.post(DEFAULT_URL, status_code=status.HTTP_201_CREATED, response_model=NoSeriesLineRead, responses={400: {"model": ErrorResponse}})
def create_noseriesline(*, session: Session = Depends(get_session), schema: NoSeriesLineCreate):
    """«No. Series Line» («Серия Номеров Строка»)"""
    return service.noseriesline_s.create(db=session, schema=schema)


@noseriesline_router.get(DEFAULT_URL, response_model=List[NoSeriesLineRead], responses={400: {"model": ErrorResponse}})
def read_noserieslines(
        *,
        session: Session = Depends(get_session),
        offset: int = 0,
        limit: int = Query(default=100, lte=100),
):
    """«No. Series Line» («Серия Номеров Строка»)"""
    return service.noseriesline_s.get_multi(db=session, order="-starting_date", skip=offset, limit=limit)


@noseriesline_router.get(DEFAULT_URL_PATH, response_model=NoSeriesLineRead)
def read_noseriesline(*, session: Session = Depends(get_session), item_id: int):
    """«No. Series Line» («Серия Номеров Строка»)"""
    return service.noseriesline_s.get(db=session, id=item_id)


@noseriesline_router.patch(DEFAULT_URL_PATH, response_model=NoSeriesLineRead)
def update_noseriesline(
        *, session: Session = Depends(get_session), item_id: int, schema: NoSeriesLineUpdate
):
    """«No. Series Line» («Серия Номеров Строка»)"""
    return service.noseriesline_s.update(db=session, schema=schema, id=item_id)


@noseriesline_router.delete(DEFAULT_URL_PATH)
def delete_noseriesline(*, session: Session = Depends(get_session), item_id: int):
    """«No. Series Line» («Серия Номеров Строка»)"""
    return service.noseriesline_s.delete(db=session, id=item_id)