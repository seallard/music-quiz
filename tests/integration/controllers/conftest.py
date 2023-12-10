from flask import Flask
from flask.testing import FlaskClient
import pytest

from app.api.app import app
from app.database.database import SESSION, setup_test_database


@pytest.fixture
def flask_app():
    yield app


@pytest.fixture
def client(flask_app: Flask) -> FlaskClient:
    return flask_app.test_client()


@pytest.fixture(autouse=True)
def transactional_session():
    # Start a savepoint
    nested = SESSION.begin_nested()

    yield

    # Rollback to the savepoint after the test
    nested.rollback()


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    setup_test_database()
    yield
