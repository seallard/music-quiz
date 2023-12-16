from app.models.player import Player
from app.services.exceptions import PlayerAlreadyInLobbyException


class Lobby:
    def __init__(self, name: str, id: str, owner_id: str):
        self.name = name
        self.id = id
        self.owner_id = owner_id
        self.players = []

    def is_joinable(self) -> bool:
        # TODO: validate that the lobby is not full etc.
        return True

    def add_player(self, player: Player):
        if player in self.players:
            raise PlayerAlreadyInLobbyException
        self.players.append(player)
