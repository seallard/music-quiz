import uuid
from sqlalchemy import Column, String

from app.database.database import Base


class Lobby(Base):
    __tablename__ = "lobby"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    owner_id = Column(String(36), default=lambda: str(uuid.uuid4()))
