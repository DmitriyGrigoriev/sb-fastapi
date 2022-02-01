from sb_backend.app.crud.base.base_crud import CRUDBase
from sb_backend.app.models.setup import noseries

class CRUDBase(CRUDBase[noseries.NoSeries]):
    pass

noseries = CRUDBase(noseries.NoSeries)