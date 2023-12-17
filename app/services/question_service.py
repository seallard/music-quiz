from app.clients.spotify_client import SpotifyAPIClient
from app.database.repositories.question_repository import QuestionRepository
from app.models.answer_option import AnswerOption
from app.models.question import Question


class QuestionService:
    def __init__(
        self, repository: QuestionRepository, spotify_client: SpotifyAPIClient
    ) -> None:
        self.repository = repository
        self.spotify_client = spotify_client

    def generate_question(self) -> Question:
        question = Question(text="Who listens the most to Bach?")
        options = [
            AnswerOption(text="Hilda"),
            AnswerOption(text="Herbert"),
            AnswerOption(text="Haakon"),
            AnswerOption(text="Hannah"),
        ]

        question.options = options
        return self.repository.create(question)
