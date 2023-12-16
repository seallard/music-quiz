from uuid import UUID
from app.database.database import get_session
from app.database.model_converter import ModelConverter
from app.database.models.lobby import LobbyModel
from app.database.models.player import PlayerModel
from app.dtos.lobby import CreateLobbyRequest
from app.models.lobby import Lobby
from app.utils.utils import get_uuid


class LobbyRepository:
    def get(self, lobby_id: UUID) -> Lobby | None:
        with get_session() as session:
            if lobby := session.query(LobbyModel).filter_by(id=str(lobby_id)).first():
                return ModelConverter.lobby_to_domain(lobby)

    def create(self, data: CreateLobbyRequest) -> LobbyModel:
        with get_session() as session:
            lobby = LobbyModel(
                id=get_uuid(),
                name=data.name,
                owner_id=str(data.owner_id),
            )
            session.add(lobby)
        return lobby

    def add_player(self, lobby_id: str, player_id: str):
        with get_session() as session:
            lobby = session.query(LobbyModel).filter_by(id=lobby_id).first()
            player = session.query(PlayerModel).filter_by(id=player_id).first()
            lobby.players.append(player)
            session.commit()
        return ModelConverter.lobby_to_domain(lobby)
