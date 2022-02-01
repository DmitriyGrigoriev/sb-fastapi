from pydantic_i18n import JsonLoader, PydanticI18n
from sb_backend.app.utils.constants import DEFAULT_LOCALE

__all__ = ['get_locale']

loader = JsonLoader("sb_backend/i18n")
tr = PydanticI18n(loader, default_locale=DEFAULT_LOCALE)

def get_locale(locale: str = DEFAULT_LOCALE) -> str:
    return locale