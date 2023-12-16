class Player:
    def __init__(self, name: str, id: str):
        self.id = id
        self.name = name

    def __eq__(self, other):
        return self.id == other.id if isinstance(other, Player) else False
