import sys
import os

import mock
from sb_backend.wsgi import run_wsgi


@mock.patch("sb_backend.wsgi.ApplicationLoader")
def test_run_wsgi(loader_mock):
    run_wsgi("localhost", "5555", "2")
    loader_mock.assert_called_once()
    assert sys.argv == [
        "--gunicorn",
        "-c",
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "../../sb_backend/config/gunicorn.conf.py"
            )
        ),
        "-w",
        "2",
        "-b localhost:5555",
        "sb_backend.app.asgi:application"
    ]
