"""Application routes configuration.

In this file all application endpoints are being defined.
"""
from fastapi import APIRouter
from sb_backend.app.controllers.api.v1 import ready
from sb_backend.app.controllers.api.v1.endpoints import main

router = APIRouter(prefix="/api/v1")

router.include_router(ready.router, tags=["ready"])
router.include_router(main.router)