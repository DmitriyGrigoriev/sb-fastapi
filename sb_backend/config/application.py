# -*- coding: utf-8 -*-
"""Application configuration."""
from typing import Optional, Any, Dict
from functools import lru_cache
from pydantic import BaseSettings, PostgresDsn, EmailStr, validator
from sb_backend.version import __version__


class Application(BaseSettings):
    """Application configuration model definition.

    Constructor will attempt to determine the values of any fields not passed
    as keyword arguments by reading from the environment. Default values will
    still be used if the matching environment variable is not set.

    Environment variables:
        FASTAPI_DEBUG
        FASTAPI_PROJECT_NAME
        FASTAPI_VERSION
        FASTAPI_DOCS_URL
        FASTAPI_USE_REDIS

    Attributes:
        DEBUG(bool): FastAPI logging level. You should disable this for
            production.
        PROJECT_NAME(str): FastAPI project name.
        VERSION(str): Application version.
        DOCS_URL(str): Path where swagger ui will be served at.
        USE_REDIS(bool): Whether or not to use Redis.

    """

    DEBUG: bool = True
    PROJECT_NAME: str = "Умный Биллинг"
    VERSION: str = __version__
    DOCS_URL: str = "/"
    USE_REDIS: bool = False
    DATABASE_URL: str = "sqlite:///billing.db"
    # All your additional application configuration should go either here or in
    # separate file in this submodule.

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    FIRST_SUPERUSER: EmailStr
    FIRST_SUPERUSER_PASSWORD: str

    class Config:
        """Config sub-class needed to customize BaseSettings settings.

        More details can be found in pydantic documentation:
        https://pydantic-docs.helpmanual.io/usage/settings/

        """

        case_sensitive = True
        env_prefix = "FASTAPI_"
        env_file_encoding = 'utf-8'
        env_file = 'sb_backend/.env'


settings = Application()

@lru_cache()
def get_settings():
    return Application()