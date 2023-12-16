import json
import uuid
from flask.testing import FlaskClient
from http import HTTPStatus

from app.dtos.lobby import CreateLobbyRequest, LobbyJoinRequest
from app.utils.utils import generate_uuid


def test_create_lobby_success(client: FlaskClient):
    # GIVEN a valid request to create a lobby
    lobby_request = CreateLobbyRequest(name="test", owner_id=generate_uuid())
    data = lobby_request.model_dump_json()

    # WHEN the request is made
    response = client.post("/lobby", data=data, content_type="application/json")

    # THEN the response should be successful
    assert response.status_code == HTTPStatus.CREATED


def test_create_lobby_bad_request(client: FlaskClient):
    # GIVEN an invalid request to create a lobby
    data = json.dumps({})

    # WHEN the request is made
    response = client.post("/lobby", data=data, content_type="application/json")

    # THEN the response should be unsuccessful
    assert response.status_code == HTTPStatus.BAD_REQUEST
