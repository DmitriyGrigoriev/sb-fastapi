from fastapi import APIRouter
from ..endpoints.setup import unitofmeasure, servicetype, vat, noseries, noseriesline, noseriessetup

router = APIRouter()

# setup
router.include_router(unitofmeasure.measure_router, prefix='/unitofmeasure')
router.include_router(servicetype.servicetype_router, prefix='/servicetype')
router.include_router(vat.vat_router, prefix='/vat')
router.include_router(noseries.noseries_router, prefix='/noseries')
router.include_router(noseriesline.noseriesline_router, prefix='/noseriesline')
router.include_router(noseriessetup.noseriessetup_router, prefix='/setup')
