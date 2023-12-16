import uuid
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.database.database import Base
from app.database.models.player import PlayerModel


class LobbyModel(Base):
    __tablename__ = "lobby"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    owner_id = Column(String(36), default=lambda: str(uuid.uuid4()))

    players = relationship(PlayerModel, back_populates="lobby")
