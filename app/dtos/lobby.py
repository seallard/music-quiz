from uuid import UUID
from pydantic import BaseModel


class CreateLobbyRequest(BaseModel):
    name: str
    owner_id: UUID


class LobbyResponse(BaseModel):
    id: UUID
    owner_id: UUID
    name: str
