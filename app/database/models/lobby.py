from sqlalchemy import Column, Integer, String

from app.database.database import Base


class Lobby(Base):
    __tablename__ = "lobby"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    owner_id = Column(Integer)
    join_code = Column(String, unique=True)
