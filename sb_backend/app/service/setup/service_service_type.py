from sqlmodel import SQLModel
from sb_backend.app.service.base.base_service import ServiceBase
from sb_backend.app.crud.setup.crud_service_type import CRUDBase, servicetype

class ServiceBase(ServiceBase[CRUDBase, SQLModel, SQLModel]):
    pass

servicetype_s = ServiceBase(servicetype)
