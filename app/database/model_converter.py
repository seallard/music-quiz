from app.database.models.answer_option import AnswerOptionModel
from app.database.models.lobby import LobbyModel
from app.database.models.player import PlayerModel
from app.database.models.question import QuestionModel
from app.models.answer_option import AnswerOption
from app.models.lobby import Lobby
from app.models.player import Player
from app.models.question import Question


class ModelConverter:
    @staticmethod
    def lobby_to_domain(lobby: LobbyModel) -> Lobby:
        return Lobby(
            id=lobby.id,
            name=lobby.name,
            owner_id=lobby.owner_id,
        )

    @staticmethod
    def player_to_domain(player: PlayerModel) -> Player:
        return Player(
            id=player.id,
            name=player.name,
        )

    @staticmethod
    def question_to_domain(question: QuestionModel) -> Question:
        answer_options: list[AnswerOption] = [
            ModelConverter.option_to_domain(option)
            for option in question.options
        ]
        return Question(text=question.text, options=answer_options)

    @staticmethod
    def option_to_domain(option: AnswerOptionModel) -> AnswerOption:
        return AnswerOption(text=option.text)
