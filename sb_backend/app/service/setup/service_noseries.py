from sqlmodel import SQLModel
from sb_backend.app.service.base.base_service import ServiceBase
from sb_backend.app.crud.setup.crud_noseries import CRUDBase, noseries

class ServiceBase(ServiceBase[CRUDBase, SQLModel, SQLModel]):
    pass

noseries_s = ServiceBase(noseries)
