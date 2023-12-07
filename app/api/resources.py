from flask import Flask

from app.services.lobby_service import LobbyService


def register_routes(app: Flask, lobby_service: LobbyService):
    from app.api.lobby_controller import create_lobby_controller

    # Controllers
    lobby_controller = create_lobby_controller(lobby_service)

    # Register routes
    app.register_blueprint(lobby_controller)
