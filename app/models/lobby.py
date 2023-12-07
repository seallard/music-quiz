from app.utils.lobby_utils import generate_lobby_code


class Lobby:
    def __init__(self, name: str, owner_id: int):
        self.name = name
        self.owner_id = owner_id
        self.join_code = generate_lobby_code()
        self.members = [owner_id]
