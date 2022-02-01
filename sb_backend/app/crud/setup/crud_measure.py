from sb_backend.app.crud.base.base_crud import CRUDBase
from sb_backend.app.models.setup import unitofmeasure

class CRUDBase(CRUDBase[unitofmeasure.Measure]):
    pass

measure = CRUDBase(unitofmeasure.Measure)