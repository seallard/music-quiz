from uuid import UUID

from app.database.repositories.lobby_repository import LobbyRepository
from app.dtos.lobby import (
    CreateLobbyRequest,
    LobbyJoinRequest,
    LobbyJoinResponse,
    LobbyResponse,
)
from app.models.lobby import Lobby
from app.services.exceptions import (
    LobbyNotFoundException,
    LobbyNotJoinableException,
)
from app.services.player_service import PlayerService
from app.utils.lobby_utils import create_lobby_response


class LobbyService:
    def __init__(
        self, repository: LobbyRepository, player_service: PlayerService
    ) -> None:
        self.repository = repository
        self.player_service = player_service

    def create_lobby(self, data: CreateLobbyRequest) -> LobbyResponse:
        lobby: Lobby = self.repository.create(data)
        return create_lobby_response(lobby)

    def join_lobby(self, lobby_id: UUID, data: LobbyJoinRequest) -> LobbyJoinResponse:
        lobby: Lobby | None = self.repository.get(lobby_id)
        if not lobby:
            raise LobbyNotFoundException

        if not lobby.is_joinable():
            raise LobbyNotJoinableException
        lobby: Lobby = self.repository.add_player(lobby.id, str(data.player_id))
        return LobbyJoinResponse(lobby_id=lobby.id)
