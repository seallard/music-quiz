import uuid
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.database.database import Base


class PlayerModel(Base):
    __tablename__ = "player"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    lobby_id = Column(String(36), ForeignKey("lobby.id"))

    lobby = relationship("LobbyModel", back_populates="players")
