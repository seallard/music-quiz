from flask import Blueprint

from app.services.lobby_service import LobbyService


def create_lobby_controller(lobby_service: LobbyService) -> Blueprint:
    lobby_controller = Blueprint("lobby_controller", __name__)

    @lobby_controller.route("/lobby")
    def lobby():
        return "Hello World!"

    return lobby_controller
