"""HTTP exception and handler for FastAPI."""
from contextlib import contextmanager
from typing import Any, Optional, Dict, Generator, NoReturn, Type

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from starlette import status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from sb_backend.app.utils.constants import DEFAULT_LOCALE, DEFAULT_ERROR_MESSAGE
from sb_backend.i18n.translate import tr

class HTTPException(Exception):
    """Custom HTTPException class definition.

    This exception combined with exception_handler method allows you to use it
    the same manner as you'd use FastAPI.HTTPException with one difference. You
    have freedom to define returned response body, whereas in
    FastAPI.HTTPException content is returned under "detail" JSON key.

    FastAPI.HTTPException source:
    https://github.com/tiangolo/fastapi/blob/master/fastapi/exceptions.py

    """

    def __init__(
        self,
        status_code: int,
        content: Any = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Initialize HTTPException class object instance.

        Args:
            status_code(int): HTTP error status code.
            content(Any): Response body.
            headers(Optional[Dict[str, Any]]): Additional response headers.

        """
        self.status_code = status_code
        self.content = content
        self.headers = headers

    def __repr__(self):
        """Class custom __repr__ method implementation.

        Returns:
            str: HTTPException string object.

        """
        kwargs = []

        for key, value in self.__dict__.items():
            if not key.startswith("_"):
                kwargs.append(
                    "{key}={value}".format(key=key, value=repr(value))
                )

        return "{name}({kwargs})".format(
            name=self.__class__.__name__, kwargs=", ".join(kwargs)
        )


async def http_exception_handler(request: Request, exception: HTTPException):
    """Handle HTTPException globally.

    In this application custom handler is added in asgi.py while initializing
    FastAPI application. This is needed in order to handle custom HTTException
    globally.

    More details:
    https://fastapi.tiangolo.com/tutorial/handling-errors/#install-custom-exception-handlers

    Args:
        request(starlette.requests.Request): Request class object instance.
            More details: https://www.starlette.io/requests/
        exception(HTTPException): Custom HTTPException class object instance.

    Returns:
        FastAPI.response.JSONResponse class object instance initialized with
            kwargs from custom HTTPException.

    """
    return JSONResponse(
        status_code=exception.status_code,
        content=exception.content,
        headers=exception.headers,
    )


@contextmanager
def expected_exceptions(
    *except_types: Type[Exception],
    detail: Optional[str] = None,
    error_code: int = status.HTTP_400_BAD_REQUEST,
    headers: Optional[Dict[str, str]] = None,
) -> Generator[None, None, None]:
    try:
        yield
    except except_types as exc:
        _raise_api_response_error(detail, error_code, headers, exc=exc)


def _raise_api_response_error(
    detail: Optional[str], status_code: int, headers: Optional[Dict[str, str]] = None, exc: Optional[Exception] = None,
    debug: bool = False
) -> NoReturn:
    if debug and exc is not None:
        detail = str(exc)
    if detail is None:
        detail = DEFAULT_ERROR_MESSAGE


@contextmanager
def expected_integrity_error(
    session: Session, *, detail: Optional[str] = None, status_code: int = status.HTTP_409_CONFLICT, debug: bool
) -> Generator[None, None, None]:
    try:
        yield
    except IntegrityError as exc:
        session.rollback()
        _raise_api_integrity_error(detail, status_code, exc=exc, debug=debug)

def _raise_api_integrity_error(
    detail: Optional[str], status_code: int, headers: Optional[Dict[str, str]] = None, exc: Optional[Exception] = None,
    debug: bool = False
) -> NoReturn:
    if debug and exc is not None:
        detail = str(exc)
    if detail is None:
        detail = DEFAULT_ERROR_MESSAGE
    raise HTTPException(detail=detail, status_code=status_code, headers=headers)


async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    current_locale = request.query_params.get("locale", DEFAULT_LOCALE)
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": tr.translate(exc.errors(), current_locale)},
    )