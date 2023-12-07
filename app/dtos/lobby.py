from pydantic import BaseModel

from app.models.lobby import Lobby


class CreateLobbyRequest(BaseModel):
    name: str
    owner_id: str


class LobbyResponse(BaseModel):
    name: str
    owner_id: str
    join_code: str
    members: list[str]


def create_lobby_response(lobby: Lobby) -> LobbyResponse:
    return LobbyResponse(
        name=lobby.name,
        owner_id=lobby.owner_id,
        join_code=lobby.join_code,
        members=lobby.members,
    )
