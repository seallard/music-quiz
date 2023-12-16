from app.database.models.lobby import LobbyModel
from app.database.models.player import PlayerModel
from app.models.lobby import Lobby
from app.models.player import Player


class ModelConverter:
    @staticmethod
    def lobby_to_domain(lobby_model: LobbyModel) -> Lobby:
        return Lobby(
            id=lobby_model.id,
            name=lobby_model.name,
            owner_id=lobby_model.owner_id,
        )

    @staticmethod
    def player_to_domain(player_model: PlayerModel) -> Player:
        return Player(
            id=player_model.id,
            name=player_model.name,
        )

