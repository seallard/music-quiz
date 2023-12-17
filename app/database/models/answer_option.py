import uuid
from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.database.database import Base


class AnswerOptionModel(Base):
    __tablename__ = "answer_option"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    text = Column(String(250), nullable=False)
    is_correct = Column(Boolean, default=False)
    question_id = Column(String(36), ForeignKey("question.id"))

    question = relationship("QuestionModel", back_populates="answer_options")
