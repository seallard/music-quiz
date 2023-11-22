from quiz.models.spotify_models import TopItems, UserProfile

import requests


class SpotifyAPIClient:
    def __init__(self):
        self.base_url = "https://api.spotify.com/v1"

    def get_headers(self, access_token: str) -> dict:
        return {"Authorization": f"Bearer {access_token}"}

    def get_user_profile(self, user_id: str, access_token: str) -> UserProfile:
        url = f"{self.base_url}/users/{user_id}"
        headers = self.get_headers(access_token)
        response = requests.get(url, headers=headers)
        return UserProfile.model_validate(response.json())

    def get_user_top_items(
        self, item_type: str, access_token: str, limit: int = 10, offset: int = 0
    ) -> TopItems:
        url = f"{self.base_url}/me/top/{item_type}?limit={limit}&offset={offset}"
        headers = self.get_headers(access_token)
        response = requests.get(url, headers=headers)
        return TopItems.model_validate(response.json())
