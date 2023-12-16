from app.dtos.lobby import LobbyResponse
from app.models.lobby import Lobby


def create_lobby_response(lobby: Lobby):
    return LobbyResponse(
        id=lobby.id,
        name=lobby.name,
        owner_id=lobby.owner_id,
    )
