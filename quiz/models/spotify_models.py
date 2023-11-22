from pydantic import BaseModel


class ExternalUrls(BaseModel):
    spotify: str


class Followers(BaseModel):
    href: str | None
    total: int


class ImageObject(BaseModel):
    url: str
    height: int | None
    width: int | None


class UserProfile(BaseModel):
    display_name: str | None
    external_urls: ExternalUrls
    followers: Followers
    href: str
    id: str
    images: list[ImageObject]
    type: str
    uri: str
