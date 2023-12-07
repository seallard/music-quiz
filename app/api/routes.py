from flask import Flask

from app.services.lobby_service import LobbyService


def register_routes(app: Flask, lobby_service: LobbyService):
    from app.api.controllers.lobby_controller import create_lobby_controller

    lobby_controller = create_lobby_controller(lobby_service)

    app.register_blueprint(lobby_controller)
