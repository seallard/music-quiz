import json
from flask.testing import FlaskClient
from http import HTTPStatus

from app.database.models.lobby import LobbyModel
from app.database.models.player import PlayerModel
from app.dtos.lobby import CreateLobbyRequest, LobbyJoinRequest
from app.utils.utils import get_uuid


def test_create_lobby_success(client: FlaskClient):
    # GIVEN a valid request to create a lobby
    lobby_request = CreateLobbyRequest(name="test", owner_id=get_uuid())
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


def test_join_lobby_success(
    client: FlaskClient, lobby: LobbyModel, player: PlayerModel
):
    # GIVEN an existing player and lobby

    # GIVEN a request from the player to join the lobby
    join_request = LobbyJoinRequest(player_id=player.id)
    data = join_request.model_dump_json()

    # WHEN the request is made
    response = client.post(
        f"/lobby/{lobby.id}/join",
        data=data,
        content_type="application/json",
    )

    # THEN the response should be successful
    assert response.status_code == HTTPStatus.OK


def test_join_lobby_invalid_lobby_id(client: FlaskClient, player: PlayerModel):
    # GIVEN a join request for an existing player
    join_request = LobbyJoinRequest(player_id=player.id)
    data = join_request.model_dump_json()

    # WHEN trying to join a lobby that does not exists
    response = client.post(
        f"/lobby/{get_uuid()}/join",
        data=data,
        content_type="application/json",
    )

    # THEN the response should be unsuccessful
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_join_lobby_invalid_lobby_id(client: FlaskClient, lobby: LobbyModel):
    # GIVEN a join request for a non-existing player
    join_request = LobbyJoinRequest(player_id=get_uuid())
    data = join_request.model_dump_json()

    # WHEN the request is made
    response = client.post(
        f"/lobby/{lobby.id}/join",
        data=data,
        content_type="application/json",
    )

    # THEN the response should be unsuccessful
    assert response.status_code == HTTPStatus.BAD_REQUEST
