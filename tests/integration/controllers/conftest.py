from flask import Flask
from flask.testing import FlaskClient
import pytest

from app.api.app import app
from app.database.database import SESSION, get_session, setup_test_database
from app.database.models.lobby import LobbyModel
from app.database.models.player import PlayerModel
from app.utils.utils import get_uuid


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


@pytest.fixture
def player(setup_database):
    player = PlayerModel(id=get_uuid(), name="test")
    with get_session() as session:
        session.add(player)
    return player


@pytest.fixture
def lobby(setup_database):
    lobby = LobbyModel(id=get_uuid(), name="test")
    with get_session() as session:
        session.add(lobby)
    return lobby
