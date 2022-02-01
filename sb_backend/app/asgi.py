# -*- coding: utf-8 -*-
"""Application Asynchronous Server Gateway Interface."""
import logging

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from sb_backend.config import router, settings
from sb_backend.app.utils import RedisClient, AiohttpClient
from sb_backend.app.exceptions import (
    HTTPException,
    http_exception_handler,
)
from sb_backend.app.db.init_db import init_db
from sb_backend.app.db.session import Session
from sb_backend.app.exceptions.http import validation_exception_handler

log = logging.getLogger(__name__)


async def on_startup():
    """Fastapi startup event handler.

    Creates RedisClient and AiohttpClient session.

    """
    log.debug("Execute FastAPI startup event handler.")
    # Initialize utilities for whole FastAPI application without passing object
    # instances within the logic.
    if settings.USE_REDIS:
        await RedisClient.open_redis_client()

    init_db(db=Session())

    AiohttpClient.get_aiohttp_client()


async def on_shutdown():
    """Fastapi shutdown event handler.

    Destroys RedisClient and AiohttpClient session.

    """
    log.debug("Execute FastAPI shutdown event handler.")
    # Gracefully close utilities.
    if settings.USE_REDIS:
        await RedisClient.close_redis_client()

    await AiohttpClient.close_aiohttp_client()


def get_app():
    """Initialize FastAPI application.

    Returns:
        app (FastAPI): Application object instance.

    """
    log.debug("Initialize FastAPI application node.")
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description="Сервис выставления финансовых документов участникам ВЭД",
        debug=settings.DEBUG,
        version=settings.VERSION,
        docs_url=settings.DOCS_URL,
        on_startup=[on_startup],
        on_shutdown=[on_shutdown],
    )
    log.debug("Add application routes.")
    app.include_router(router)
    # Register global exception handler for custom HTTPException.
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)

    return app


application = get_app()
