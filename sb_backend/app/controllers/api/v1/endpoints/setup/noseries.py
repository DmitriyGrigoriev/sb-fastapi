from typing import List
from fastapi import APIRouter, Depends, Query, status

from sqlmodel import Session
from sb_backend.app import service
from sb_backend.app.db.session import get_session
from sb_backend.app.schemas import ErrorResponse
from sb_backend.app.models.setup.noseries import (
    NoSeriesRead, NoSeriesUpdate, NoSeriesCreate
)

DEFAULT_URL = "/"
DEFAULT_URL_PATH = DEFAULT_URL + "{item_id}"

noseries_router = APIRouter(tags=['noseries'])

@noseries_router.post(DEFAULT_URL, status_code=status.HTTP_201_CREATED, response_model=NoSeriesRead, responses={400: {"model": ErrorResponse}})
def create_noseries(*, session: Session = Depends(get_session), schema: NoSeriesCreate):
    """«No. Series» («Серия Номеров»)"""
    return service.noseries_s.create(db=session, schema=schema)


@noseries_router.get(DEFAULT_URL, response_model=List[NoSeriesRead], responses={400: {"model": ErrorResponse}})
def read_noserieses(
        *,
        session: Session = Depends(get_session),
        offset: int = 0,
        limit: int = Query(default=100, lte=100),
):
    """«No. Series» («Серия Номеров»)"""
    return service.noseries_s.get_multi(db=session, order="code", skip=offset, limit=limit)


@noseries_router.get(DEFAULT_URL_PATH, response_model=NoSeriesRead)
def read_noseries(*, session: Session = Depends(get_session), item_id: int):
    """«No. Series» («Серия Номеров»)"""
    return service.noseries_s.get(db=session, id=item_id)


@noseries_router.patch(DEFAULT_URL_PATH, response_model=NoSeriesRead)
def update_noseries(
        *, session: Session = Depends(get_session), item_id: int, schema: NoSeriesUpdate
):
    """«No. Series» («Серия Номеров»)"""
    return service.noseries_s.update(db=session, schema=schema, id=item_id)


@noseries_router.delete(DEFAULT_URL_PATH)
def delete_noseries(*, session: Session = Depends(get_session), item_id: int):
    """«No. Series» («Серия Номеров»)"""
    return service.noseries_s.delete(db=session, id=item_id)