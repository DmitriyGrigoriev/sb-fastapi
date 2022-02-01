from sqlmodel import SQLModel
from sb_backend.app.service.base.base_service import ServiceBase
from sb_backend.app.crud.setup.crud_measure import CRUDBase, measure

class ServiceBase(ServiceBase[CRUDBase, SQLModel, SQLModel]):
    pass

measure_s = ServiceBase(measure)
