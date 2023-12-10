from app.database.repositories.lobby_repository import LobbyRepository
from app.dtos.lobby import CreateLobbyRequest, LobbyResponse
from app.utils.lobby_utils import create_lobby_response


class LobbyService:
    def __init__(self, repository: LobbyRepository) -> None:
        self.repository = repository

    def create_lobby(self, data: CreateLobbyRequest) -> LobbyResponse:
        lobby = self.repository.create_lobby(data)
        return create_lobby_response(lobby)
