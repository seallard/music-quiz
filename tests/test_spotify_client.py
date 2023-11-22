from requests_mock import Mocker

from quiz.clients.spotify_client import SpotifyAPIClient


def test_get_user_profile(
    client: SpotifyAPIClient, mock_request: Mocker, user_response: dict
):
    # GIVEN a mocked user response
    mock_request.get("https://api.spotify.com/v1/users/id", json=user_response)

    # WHEN retrieving the user profile
    user_profile = client.get_user_profile("id", "token")

    # THEN the user profile is parsed
    assert user_profile


def test_get_user_top_items(
    client: SpotifyAPIClient, mock_request: Mocker, top_items_response: dict
):
    # GIVEN a mocked top items response
    mock_request.get("https://api.spotify.com/v1/me/top/artists", json=top_items_response)

    # WHEN retrieving the user top items
    top_items = client.get_user_top_items(item_type="artists", access_token="token")

    # THEN the user top items are parsed
    assert top_items


def test_get_followed_artists(
    client: SpotifyAPIClient, mock_request: Mocker, artists_response: dict
):
    # GIVEN a mocked followed artists response
    mock_request.get("https://api.spotify.com/v1/me/following?type=artist", json=artists_response)

    # WHEN retrieving the followed artists
    artists = client.get_followed_artists("token")

    # THEN the followed artists are parsed
    assert artists
