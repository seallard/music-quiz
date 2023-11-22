import pytest
import requests_mock

from quiz.clients.spotify_client import SpotifyAPIClient


@pytest.fixture
def mock_request():
    with requests_mock.Mocker() as mock:
        yield mock


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
def top_items_response() -> dict:
    return {
        "href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20",
        "limit": 20,
        "next": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
        "offset": 0,
        "previous": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
        "total": 4,
        "items": [
            {
                "external_urls": {"spotify": "string"},
                "followers": {"href": "string", "total": 0},
                "genres": ["Prog rock", "Grunge"],
                "href": "string",
                "id": "string",
                "images": [
                    {
                        "url": "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228",
                        "height": 300,
                        "width": 300,
                    }
                ],
                "name": "string",
                "popularity": 0,
                "type": "artist",
                "uri": "string",
            }
        ],
    }


@pytest.fixture
def client() -> SpotifyAPIClient:
    return SpotifyAPIClient()
