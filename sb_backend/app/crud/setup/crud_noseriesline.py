from sb_backend.app.crud.base.base_crud import CRUDBase
from sb_backend.app.models.setup import noseriesline

class CRUDBase(CRUDBase[noseriesline.NoSeriesLine]):
    pass

noseriesline = CRUDBase(noseriesline.NoSeriesLine)