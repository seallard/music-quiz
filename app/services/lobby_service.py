from app.dtos.lobby import CreateLobbyRequest
from app.models.lobby import Lobby


class LobbyService:
    def create_lobby(self, data: CreateLobbyRequest) -> Lobby:
        return Lobby(name=data.name, owner_id=data.owner_id)
