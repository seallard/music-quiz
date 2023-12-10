from flask import Flask

from app.api.ext import setup_logger
from app.api.routes import register_routes
from app.database.database import initialize_database
from app.database.repositories.lobby_repository import LobbyRepository
from app.services.lobby_service import LobbyService

app = Flask(__name__)

setup_logger(app)
initialize_database("sqlite:///:memory:")

lobby_repository = LobbyRepository()
lobby_service = LobbyService(lobby_repository)
register_routes(app, lobby_service)

if __name__ == "__main__":
    app.run(debug=True)
