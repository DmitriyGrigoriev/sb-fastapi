from typing import List
from fastapi import APIRouter, Depends, Query, status

from sqlmodel import Session
from sb_backend.app import service
from sb_backend.app.db.session import get_session
from sb_backend.app.schemas import ErrorResponse
from sb_backend.app.models.setup.vat import (
    VatPostingGroupRead, VatPostingGroupUpdate, VatPostingGroupCreate
)


DEFAULT_URL = "/"
DEFAULT_URL_PATH = DEFAULT_URL + "{item_id}"

vat_router = APIRouter(tags=['vat'])

@vat_router.post(DEFAULT_URL, status_code=status.HTTP_201_CREATED, response_model=VatPostingGroupRead, responses={400: {"model": ErrorResponse}})
def create_vat(*, session: Session = Depends(get_session), schema: VatPostingGroupCreate):
    """«VAT Posting Group» («НДС  Учетная Группа»)"""
    return service.servicetype_s.create(db=session, schema=schema)


@vat_router.get(DEFAULT_URL, response_model=List[VatPostingGroupRead], responses={400: {"model": ErrorResponse}})
def read_vats(
        *,
        session: Session = Depends(get_session),
        offset: int = 0,
        limit: int = Query(default=100, lte=100),
):
    """«VAT Posting Group» («НДС  Учетная Группа»)"""
    return service.vat_s.get_multi(db=session, order="code", skip=offset, limit=limit)


@vat_router.get(DEFAULT_URL_PATH, response_model=VatPostingGroupRead)
def read_vat(*, session: Session = Depends(get_session), item_id: int):
    """«VAT Posting Group» («НДС  Учетная Группа»)"""
    return service.vat_s.get(db=session, id=item_id)


@vat_router.patch(DEFAULT_URL_PATH, response_model=VatPostingGroupRead)
def update_vat(
        *, session: Session = Depends(get_session), item_id: int, schema: VatPostingGroupUpdate
):
    """«VAT Posting Group» («НДС  Учетная Группа»)"""
    return service.vat_s.update(db=session, schema=schema, id=item_id)


@vat_router.delete(DEFAULT_URL_PATH)
def delete_vat(*, session: Session = Depends(get_session), item_id: int):
    """«VAT Posting Group» («НДС  Учетная Группа»)"""
    return service.vat_s.delete(db=session, id=item_id)