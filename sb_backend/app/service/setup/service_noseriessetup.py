from sqlmodel import SQLModel
from sb_backend.app.service.base.base_service import ServiceBase
from sb_backend.app.crud.setup.crud_noseriessetup import CRUDBase, noseriessetup

class ServiceBase(ServiceBase[CRUDBase, SQLModel, SQLModel]):
    pass

noseriessetup_s = ServiceBase(noseriessetup)
