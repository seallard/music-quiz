from uuid import UUID

from app.database.repositories.player_repository import PlayerRepository
from app.models.player import Player
from app.services.exceptions import PlayerNotFoundException


class PlayerService:
    def __init__(self, player_repository: PlayerRepository):
        self.player_repository = player_repository

    def player_exists(self, player_id: UUID) -> bool:
        return bool(self.player_repository.get(player_id))
