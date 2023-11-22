import requests_mock

from quiz.clients.spotify_client import SpotifyAPIClient
from quiz.models.spotify_models import UserProfile


def test_get_user_profile(spotify_client: SpotifyAPIClient, user_response: dict):
    # GIVEN a user id and user data
    user_id = "id"
    with requests_mock.Mocker() as m:
        m.get(f"https://api.spotify.com/v1/users/{user_id}", json=user_response)

        # WHEN retrieving the user profile
        user_profile: UserProfile = spotify_client.get_user_profile(user_id, "token")

        # THEN the user profile was validated
        assert user_profile
