from app.database.database import get_session
from app.database.model_converter import ModelConverter
from app.database.models.player import PlayerModel
from uuid import UUID

from app.models.player import Player


class PlayerRepository:
    def get(self, player_id: UUID) -> Player | None:
        with get_session() as session:
            player = session.query(PlayerModel).filter_by(id=str(player_id)).first()
            return ModelConverter.player_to_domain(player)
