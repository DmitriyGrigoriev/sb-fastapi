from sqlmodel import SQLModel
from sb_backend.app.service.base.base_service import ServiceBase
from sb_backend.app.crud.setup.crud_vat import CRUDBase, vat

class ServiceBase(ServiceBase[CRUDBase, SQLModel, SQLModel]):
    pass

vat_s = ServiceBase(vat)
