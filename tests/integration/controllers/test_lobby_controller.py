from flask.testing import FlaskClient
import json
from http import HTTPStatus


def test_create_lobby_success(client: FlaskClient):
    # GIVEN a valid request to create a lobby
    test_data = {"name": "test", "owner_id": "123"}
    request = json.dumps(test_data)

    # WHEN the request is made
    response = client.post("/lobby", data=request, content_type="application/json")

    # THEN the response should be successful
    assert response.status_code == HTTPStatus.CREATED
    assert json.loads(response.data)
