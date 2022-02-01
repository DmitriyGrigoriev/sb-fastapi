from sb_backend.app.crud.base.base_crud import CRUDBase
from sb_backend.app.models.setup import vat

class CRUDBase(CRUDBase[vat.VatPostingGroup]):
    pass

vat = CRUDBase(vat.VatPostingGroup)