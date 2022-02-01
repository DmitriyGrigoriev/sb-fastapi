from typing import List
from fastapi import APIRouter, Depends, Query, status

from sqlmodel import Session
from sb_backend.app import service
from sb_backend.app.db.session import get_session
from sb_backend.app.schemas import ErrorResponse
from sb_backend.app.models.setup.noseriessetup import (
    NoSeriesSetupRead, NoSeriesSetupCreate, NoSeriesSetupUpdate
)

DEFAULT_URL = "/"
DEFAULT_URL_PATH = DEFAULT_URL + "{item_id}"

noseriessetup_router = APIRouter(tags=['noseriessetup'])

@noseriessetup_router.post(DEFAULT_URL, status_code=status.HTTP_201_CREATED, response_model=NoSeriesSetupRead, responses={400: {"model": ErrorResponse}})
def create_noseriessetup(*, session: Session = Depends(get_session), schema: NoSeriesSetupCreate):
    """«No Series Setup» («Биллинг Настройка»)"""
    return service.noseriessetup_s.create(db=session, schema=schema)


@noseriessetup_router.get(DEFAULT_URL, response_model=List[NoSeriesSetupRead], responses={400: {"model": ErrorResponse}})
def read_noseriessetups(
        *,
        session: Session = Depends(get_session),
        offset: int = 0,
        limit: int = Query(default=100, lte=100),
):
    """«No Series Setup» («Биллинг Настройка»)"""
    return service.noseriessetup_s.get_multi(db=session, skip=offset, limit=limit)


@noseriessetup_router.get(DEFAULT_URL_PATH, response_model=NoSeriesSetupRead)
def read_noseriessetup(*, session: Session = Depends(get_session), item_id: int):
    """«No Series Setup» («Биллинг Настройка»)"""
    return service.noseriessetup_s.get(db=session, id=item_id)


@noseriessetup_router.patch(DEFAULT_URL_PATH, response_model=NoSeriesSetupRead)
def update_noseriessetup(
        *, session: Session = Depends(get_session), item_id: int, schema: NoSeriesSetupUpdate
):
    """«No Series Setup» («Биллинг Настройка»)"""
    return service.noseriessetup_s.update(db=session, schema=schema, id=item_id)


@noseriessetup_router.delete(DEFAULT_URL_PATH)
def delete_noseriessetup(*, session: Session = Depends(get_session), item_id: int):
    """«No Series Setup» («Биллинг Настройка»)"""
    return service.noseriessetup_s.delete(db=session, id=item_id)