# -*- coding: utf-8 -*-
"""Part of this code get from the https://github.com/tiangolo/full-stack-fastapi-postgresql"""

from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from sqlalchemy import desc
from sqlalchemy.orm import Session
from sqlmodel import SQLModel
from sb_backend.app.exceptions.http import expected_exceptions, expected_integrity_error, _raise_api_integrity_error
from sqlalchemy.exc import IntegrityError


# from ..schemas.response import _raise_api_response_error
# from starlette import status

ModelType = TypeVar("ModelType", bound=SQLModel)
SchemaType = TypeVar("SchemaType", bound=SQLModel)


class InvalidTable(RuntimeError):
    """Raised when calling a method coupled to SQLAlchemy operations.
    It should be called only by SQLModel objects that are tables.
    """
    pass


class CRUDBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLModel model class with table=True
        * `schema`: A SQLModel model (schema) class
        """
        if self._validate_table(model):
            self.model = model

    def _is_table(self, cls) -> bool:
        base_is_table = False
        for base in cls.__bases__:
            config = getattr(base, "__config__")
            if config and getattr(config, "table", False):
                base_is_table = True
                break
        return getattr(cls.__config__, "table", False) and not base_is_table

    def _validate_table(self, cls):
        if not self._is_table(cls):
            raise InvalidTable(
                f'"{cls.__name__}" is not a table. '
                "Add the class parameter `table=True` or don't use with this object."
            )
        return True

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(
        self, db: Session, *, order: str = None, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        if order:
            if order.startswith('-'):
                desc_order = order[1:]
                result = db.query(self.model).order_by(desc(desc_order)).offset(skip).limit(limit).all()
            else:
                result = db.query(self.model).order_by(order).offset(skip).limit(limit).all()
        else:
            result = db.query(self.model).offset(skip).limit(limit).all()
        return result

    def create(self, db: Session, *, schema: SchemaType) -> ModelType:
        db_obj = self.model.from_orm(schema)
        try:
            db.add(db_obj)
        except:
            db.rollback()
        else:
            db.commit()
            db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[SchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        try:
            db.add(db_obj)
        except:
            db.rollback()
        else:
            db.commit()
            db.refresh(db_obj)

        return db_obj

    def remove(self, db: Session, *, id: int) -> ModelType:
        obj = db.query(self.model).get(id)
        db.delete(obj)

        with expected_exceptions(IntegrityError, detail="An error occured"):
            db.commit()
        # with expected_integrity_error(session=db, detail="There was a conflict with an existing user", debug=True):
        #     db.delete(obj)

        # db.commit()


        # if obj:
        #     try:
        #         db.commit()
        #     except IntegrityError as exc:
        #         _raise_api_integrity_error(detail="An error occured", status_code=400, exc=exc, debug=True)
        #     except Exception:
        #         db.rollback()
        #     else:
        #         db.commit()
        return obj

    def exists(self, db: Session, **kwargs) ->  Optional[ModelType]:
        return db.query(self.model).get_or_none(**kwargs)

    async def count(self, db: Session, **kwargs) -> int:
        return db.query(self.model).filter(**kwargs).count()
