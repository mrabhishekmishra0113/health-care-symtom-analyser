import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from app import app as flask_app  # noqa: E402


def app(environ, start_response):
    path = environ.get("PATH_INFO", "")
    if path.startswith("/api/index"):
        environ["PATH_INFO"] = path[len("/api/index"):] or "/"
    return flask_app(environ, start_response)