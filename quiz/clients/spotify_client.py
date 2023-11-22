from quiz.models.spotify_models import FollowedArtists, TopItems, UserProfile

import requests


class SpotifyAPIClient:
    def __init__(self):
        self.base_url = "https://api.spotify.com/v1"

    def get_headers(self, access_token: str) -> dict:
        return {"Authorization": f"Bearer {access_token}"}

    def get_user_profile(self, user_id: str, access_token: str) -> UserProfile:
        """Get public profile information about a Spotify user."""
        url = f"{self.base_url}/users/{user_id}"
        headers = self.get_headers(access_token)
        response = requests.get(url, headers)
        return UserProfile.model_validate(response.json())

    def get_user_top_items(
        self, item_type: str, access_token: str, limit: int = 10, offset: int = 0
    ) -> TopItems:
        """Get the current user's top artists or tracks based on calculated affinity."""
        url = f"{self.base_url}/me/top/{item_type}?limit={limit}&offset={offset}"
        headers = self.get_headers(access_token)
        response = requests.get(url, headers)
        return TopItems.model_validate(response.json())

    def get_followed_artists(self, access_token: str, limit: int = 10) -> FollowedArtists:
        """Get the current user's followed artists."""
        url = f"{self.base_url}/me/following?type=artist&limit={limit}"
        headers = self.get_headers(access_token)
        response = requests.get(url, headers)
        return FollowedArtists.model_validate(response.json())

    def start_playback(self, access_token: str, context_uri: str) -> None:
        """Start a new context or resume current playback on the user's active device."""
        url = f"{self.base_url}/me/player/play"
        headers = self.get_headers(access_token)
        data = {"context_uri": context_uri}
        requests.put(url, headers=headers, json=data)
