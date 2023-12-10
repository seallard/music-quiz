from app.database.database import get_session
from app.database.models.lobby import Lobby
from app.dtos.lobby import CreateLobbyRequest
from app.utils.utils import generate_uuid


class LobbyRepository:
    def create_lobby(self, lobby_dto: CreateLobbyRequest) -> Lobby:
        with get_session() as session:
            lobby_dto = Lobby(
                id=generate_uuid(),
                name=lobby_dto.name,
                owner_id=str(lobby_dto.owner_id),
            )
            session.add(lobby_dto)
        return lobby_dto
