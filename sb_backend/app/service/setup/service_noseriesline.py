from sqlmodel import SQLModel
from sb_backend.app.service.base.base_service import ServiceBase
from sb_backend.app.crud.setup.crud_noseriesline import CRUDBase, noseriesline

class ServiceBase(ServiceBase[CRUDBase, SQLModel, SQLModel]):
    pass

noseriesline_s = ServiceBase(noseriesline)
