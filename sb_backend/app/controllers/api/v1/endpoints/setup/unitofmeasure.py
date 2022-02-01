from typing import List
from fastapi import APIRouter, Depends, Query, status

from sqlmodel import Session
from sb_backend.app import service
from sb_backend.app.db.session import get_session
from sb_backend.app.schemas import ErrorResponse
from sb_backend.app.models.setup.unitofmeasure import (
    MeasureRead, MeasureUpdate, MeasureCreate
)


DEFAULT_URL = "/"
DEFAULT_URL_PATH = DEFAULT_URL + "{item_id}"

measure_router = APIRouter(tags=['measure'])

@measure_router.post(DEFAULT_URL, status_code=status.HTTP_201_CREATED, response_model=MeasureRead, responses={400: {"model": ErrorResponse}})
def create_measure(*, session: Session = Depends(get_session), schema: MeasureCreate):
    """ «Unit of Measure» («Единица Измерения») """
    return service.measure_s.create(db=session, schema=schema)


@measure_router.get(DEFAULT_URL, response_model=List[MeasureRead], responses={400: {"model": ErrorResponse}})
def read_measures(
        *,
        session: Session = Depends(get_session),
        offset: int = 0,
        limit: int = Query(default=100, lte=100),
):
    """ «Unit of Measure» («Единица Измерения») """
    return service.measure_s.get_multi(db=session, order="code", skip=offset, limit=limit)


@measure_router.get(DEFAULT_URL_PATH, response_model=MeasureRead)
def read_measure(*, session: Session = Depends(get_session), item_id: int):
    """ «Unit of Measure» («Единица Измерения») """
    return service.measure_s.get(db=session, id=item_id)


@measure_router.patch(DEFAULT_URL_PATH, response_model=MeasureRead)
def update_measure(
        *, session: Session = Depends(get_session), item_id: int, schema: MeasureUpdate
):
    """ «Unit of Measure» («Единица Измерения») """
    return service.measure_s.update(db=session, schema=schema, id=item_id)


@measure_router.delete(DEFAULT_URL_PATH)
def delete_measure(*, session: Session = Depends(get_session), item_id: int):
    """ «Unit of Measure» («Единица Измерения») """
    return service.measure_s.delete(db=session, id=item_id)