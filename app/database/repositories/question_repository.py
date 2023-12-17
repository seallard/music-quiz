from app.database.database import get_session
from app.database.model_converter import ModelConverter
from app.database.models.answer_option import AnswerOptionModel
from app.database.models.question import QuestionModel
from app.models.question import Question


class QuestionRepository:
    def create(self, question: Question) -> Question:
        with get_session() as session:
            question_model = QuestionModel(text=question.text)
            for option in question.options:
                option_model = AnswerOptionModel(text=option.text)
                question_model.options.append(option_model)
            session.add(question_model)
            return ModelConverter.question_to_domain(question)
