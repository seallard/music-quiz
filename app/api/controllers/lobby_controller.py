from http import HTTPMethod, HTTPStatus
import logging
from flask import Blueprint, jsonify, request

from app.dtos.lobby import CreateLobbyRequest, create_lobby_response
from app.services.lobby_service import LobbyService

logger = logging.getLogger(__name__)


def create_lobby_controller(lobby_service: LobbyService) -> Blueprint:
    controller = Blueprint("lobby_controller", __name__)

    @controller.route("/lobby", methods=[HTTPMethod.POST])
    def create_lobby():
        try:
            data = CreateLobbyRequest(**request.json)
            lobby = lobby_service.create_lobby(data)
            response = create_lobby_response(lobby).model_dump_json()
            return response, HTTPStatus.CREATED
        except ValueError as e:
            logger.error(f"Invalid request to create lobby: {request.json}, {e}")
            return jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST

    return controller
