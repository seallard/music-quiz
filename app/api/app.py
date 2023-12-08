from flask import Flask

from app.api.ext import setup_logger
from app.api.routes import register_routes
from app.services.lobby_service import LobbyService

app = Flask(__name__)

setup_logger(app)

lobby_service = LobbyService()
register_routes(app, lobby_service)

if __name__ == "__main__":
    app.run(debug=True)
