import uuid
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.database.database import Base
from app.database.models.answer_option import AnswerOptionModel


class QuestionModel(Base):
    __tablename__ = "question"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    text = Column(String(500), nullable=False)

    options = relationship(AnswerOptionModel, back_populates="question")
