import pytest
from fastapi.testclient import TestClient
from sb_backend.app.asgi import get_app
from sb_backend.config import settings


@pytest.fixture
def app():
    # Overriding to true in order to initialize redis client on FastAPI event
    # startup handler. It'll be needed for unit tests.
    settings.USE_REDIS = True
    app = get_app()
    with TestClient(app) as client:
        yield client
