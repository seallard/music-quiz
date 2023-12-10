from app.database.models.lobby import Lobby
from app.dtos.lobby import LobbyResponse


def create_lobby_response(lobby: Lobby):
    return LobbyResponse(
        id=lobby.id,
        name=lobby.name,
        owner_id=lobby.owner_id,
    )
