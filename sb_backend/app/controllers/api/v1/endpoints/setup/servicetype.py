from typing import List
from fastapi import APIRouter, Depends, Query, status

from sqlmodel import Session
from sb_backend.app import service
from sb_backend.app.db.session import get_session
from sb_backend.app.schemas import ErrorResponse
from sb_backend.app.models.setup.servicetype import (
    ServiceTypeRead, ServiceTypeUpdate, ServiceTypeCreate
)

DEFAULT_URL = "/"
DEFAULT_URL_PATH = DEFAULT_URL + "{item_id}"

servicetype_router = APIRouter(tags=['servicetype'])

@servicetype_router.post(DEFAULT_URL, status_code=status.HTTP_201_CREATED, response_model=ServiceTypeRead, responses={400: {"model": ErrorResponse}})
def create_servicetype(*, session: Session = Depends(get_session), schema: ServiceTypeCreate):
    """«Service Type» («Тип Услуги»)"""
    return service.servicetype_s.create(db=session, schema=schema)


@servicetype_router.get(DEFAULT_URL, response_model=List[ServiceTypeRead], responses={400: {"model": ErrorResponse}})
def read_servicetypes(
        *,
        session: Session = Depends(get_session),
        offset: int = 0,
        limit: int = Query(default=100, lte=100),
):
    """«Service Type» («Тип Услуги»)"""
    return service.servicetype_s.get_multi(db=session, order="code", skip=offset, limit=limit)


@servicetype_router.get(DEFAULT_URL_PATH, response_model=ServiceTypeRead)
def read_servicetype(*, session: Session = Depends(get_session), item_id: int):
    """«Service Type» («Тип Услуги»)"""
    return service.servicetype_s.get(db=session, id=item_id)


@servicetype_router.patch(DEFAULT_URL_PATH, response_model=ServiceTypeRead)
def update_servicetype(
        *, session: Session = Depends(get_session), item_id: int, schema: ServiceTypeUpdate
):
    """«Service Type» («Тип Услуги»)"""
    return service.servicetype_s.update(db=session, schema=schema, id=item_id)


@servicetype_router.delete(DEFAULT_URL_PATH)
def delete_servicetype(*, session: Session = Depends(get_session), item_id: int):
    """«Service Type» («Тип Услуги»)"""
    return service.servicetype_s.delete(db=session, id=item_id)