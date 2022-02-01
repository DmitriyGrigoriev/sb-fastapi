from sb_backend.app.crud.base.base_crud import CRUDBase
from sb_backend.app.models.setup import noseriessetup

class CRUDBase(CRUDBase[noseriessetup.NoSeriesSetup]):
    pass

noseriessetup = CRUDBase(noseriessetup.NoSeriesSetup)