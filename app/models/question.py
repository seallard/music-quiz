from app.models.answer_option import AnswerOption


class Question:
    def __init__(self, text: str, options: list[AnswerOption]) -> None:
        self.text = text
        self.options = options
