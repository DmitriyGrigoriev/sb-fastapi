from typing import Any, List, Optional, Generic, TypeVar, Type
from sqlmodel import SQLModel
from fastapi import HTTPException, status

from sb_backend.app.crud.base.base_crud import CRUDBase
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType", bound=SQLModel)
CRUDType = TypeVar("CRUDType", bound=CRUDBase)

CreateSchemaType = TypeVar("CreateSchemaType", bound=SQLModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=SQLModel)


class ServiceBase(Generic[CRUDType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, crud: Type[CRUDType]):
        """ CRUD Service """

        self.crud = crud

    # async def all(self, **kwargs) -> Optional[ModelType]:
    #     return await self.crud.all(**kwargs)

    def get(self, *, db: Session, id: Any) -> Optional[ModelType]:
        result = self.crud.get(db=db, id=id)
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{self.crud.model.__name__} not found")
        return result

    def get_multi(self, *args, order: str=None, skip=0, limit=100, **kwargs) -> List[ModelType]:
        return self.crud.get_multi(order=order, skip=skip, limit=limit, **kwargs)

    def create(self, db: Session, schema: CreateSchemaType) -> ModelType:
        return self.crud.create(db=db, schema=schema)

    def create_single(self, *args, schema: CreateSchemaType, **kwargs) -> ModelType:
        if self.crud.exists(**kwargs):
            return None
        return self.crud.create(schema=schema, **kwargs)

    def get_object(self, db: Session, **kwargs) -> Optional[ModelType]:
        return self.crud.get(db=db, **kwargs)

    def update(self, db: Session, schema: UpdateSchemaType, **kwargs) -> ModelType:
        obj = self.get_object(db=db, **kwargs)
        if obj:
            return self.crud.update(db=db, db_obj=obj, obj_in=schema)
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{self.crud.model.__name__} not found")

    def delete(self, db: Session, *args, **kwargs) -> ModelType:
        obj = self.get_object(db=db, **kwargs)
        if obj:
            return self.crud.remove(db=db, **kwargs)
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{self.crud.model.__name__} not found")

    def count(self, **kwargs) -> int:
        return self.crud.count(**kwargs)

    def exists(self, **kwargs) -> ModelType:
        return self.crud.exists(**kwargs)