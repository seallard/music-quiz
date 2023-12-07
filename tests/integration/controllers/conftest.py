from flask import Flask
from flask.testing import FlaskClient
import pytest

from app.api.app import app

@pytest.fixture
def flask_app():
    yield app


@pytest.fixture
def client(flask_app: Flask) -> FlaskClient:
    return flask_app.test_client()
