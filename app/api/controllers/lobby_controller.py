from http import HTTPMethod, HTTPStatus
import logging
from flask import Blueprint, jsonify, request

from app.dtos.lobby import CreateLobbyRequest, LobbyJoinRequest
from app.services.lobby_service import LobbyService

logger = logging.getLogger(__name__)


def create_lobby_controller(lobby_service: LobbyService) -> Blueprint:
    controller = Blueprint("lobby_controller", __name__)

    @controller.route("/lobby", methods=[HTTPMethod.POST])
    def create_lobby():
        try:
            data = CreateLobbyRequest(**request.json)
            lobby = lobby_service.create_lobby(data)
            response = lobby.model_dump_json()
            return response, HTTPStatus.CREATED
        except ValueError as e:
            logger.error(f"Invalid request to create lobby: {request.json}, {e}")
            return jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST

    @controller.route("/lobby/<lobby_id>/join", methods=[HTTPMethod.POST])
    def join_lobby(lobby_id: str):
        try:
            data = LobbyJoinRequest(**request.json)
            lobby = lobby_service.join_lobby(lobby_id=lobby_id, data=data)
            response = lobby.model_dump_json()
            return response, HTTPStatus.OK
        except ValueError as e:
            logger.error(f"Invalid request to join lobby: {lobby_id}, {e}")
            return jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST

    return controller
