from app.models.lobby import Lobby

class LobbyService:
    def create_lobby(self, name: str, player_id: str) -> Lobby:
        return Lobby(
            name=name,
            owner_id=player_id,
        )
