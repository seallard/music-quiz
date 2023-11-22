import pytest
import requests_mock

from quiz.clients.spotify_client import SpotifyAPIClient


@pytest.fixture
def user_response() -> dict:
    return {
        "display_name": "string",
        "external_urls": {"spotify": "string"},
        "followers": {"href": "string", "total": 0},
        "href": "string",
        "id": "string",
        "images": [
            {
                "url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228",
                "height": 300,
                "width": 300,
            }
        ],
        "type": "user",
        "uri": "string",
    }

@pytest.fixture
def spotify_client():
    return SpotifyAPIClient()
