from flask import Flask
from app.services.lobby_service import LobbyService
from resources import register_routes

app = Flask(__name__)

# Services
lobby_service = LobbyService()


# Register routes
register_routes(app, lobby_service)

if __name__ == "__main__":
    app.run(debug=True)
