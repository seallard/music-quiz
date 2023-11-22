import requests_mock

from quiz.clients.spotify_client import SpotifyAPIClient
from quiz.models.spotify_models import UserProfile


def test_get_user_profile(user_response: dict):
    # GIVEN a spotify api client
    client = SpotifyAPIClient()

    # GIVEN a user id and data
    user_id = "id"
    with requests_mock.Mocker() as m:
        m.get(f"https://api.spotify.com/v1/users/{user_id}", json=user_response)

        # WHEN retrieving the user profile
        user_profile: UserProfile = client.get_user_profile(user_id, "token")

        # THEN the user profile is parsed
        assert user_profile


def test_get_user_top_items(top_items_response: dict):
    # GIVEN a spotify api client
    client = SpotifyAPIClient()

    with requests_mock.Mocker() as m:
        m.get(
            "https://api.spotify.com/v1/me/top/artists?limit=10&offset=0",
            json=top_items_response,
        )

        # WHEN retrieving the user top items
        top_items = client.get_user_top_items(item_type="artists", access_token="token")

        # THEN the user top items are parsed
        assert top_items
