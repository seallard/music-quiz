from http import HTTPMethod, HTTPStatus
from flask import Blueprint, jsonify, request

from app.dtos.lobby import CreateLobbyRequest, create_lobby_response
from app.services.lobby_service import LobbyService


def create_lobby_controller(lobby_service: LobbyService) -> Blueprint:
    controller = Blueprint("lobby_controller", __name__)

    @controller.route("/lobby", methods=[HTTPMethod.POST])
    def create_lobby():
        try:
            data = CreateLobbyRequest(**request.json)
            lobby = lobby_service.create_lobby(data)
            dto = create_lobby_response(lobby).model_dump_json()
            return dto, HTTPStatus.CREATED
        except ValueError as e:
            return jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST

    return controller
