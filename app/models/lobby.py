from uuid import UUID


class Lobby:
    def __init__(self, name: str, owner_id: UUID):
        self.name = name
        self.owner_id = owner_id
        self.members = [owner_id]
