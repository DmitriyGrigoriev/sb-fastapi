from sb_backend.app.crud.base.base_crud import CRUDBase
from sb_backend.app.models.setup import servicetype

class CRUDBase(CRUDBase[servicetype.ServiceType]):
    pass

servicetype = CRUDBase(servicetype.ServiceType)