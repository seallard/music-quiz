from flask import Flask

from app.api.ext import setup_logger
from app.api.routes import register_routes
from app.database.database import initialize_database
from app.database.repositories.lobby_repository import LobbyRepository
from app.database.repositories.player_repository import PlayerRepository
from app.services.lobby_service import LobbyService
from app.services.player_service import PlayerService

app = Flask(__name__)

setup_logger(app)
initialize_database("sqlite:///:memory:")

player_repository = PlayerRepository()
player_service = PlayerService(player_repository)

lobby_repository = LobbyRepository()
lobby_service = LobbyService(repository=lobby_repository, player_service=player_service)

register_routes(app, lobby_service)

if __name__ == "__main__":
    app.run(debug=True)
