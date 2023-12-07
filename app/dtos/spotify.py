from pydantic import BaseModel


class ExternalUrls(BaseModel):
    spotify: str


class Followers(BaseModel):
    href: str | None
    total: int


class Image(BaseModel):
    url: str
    height: int | None
    width: int | None


class UserProfile(BaseModel):
    display_name: str | None
    external_urls: ExternalUrls
    followers: Followers
    href: str
    id: str
    images: list[Image]
    type: str
    uri: str


class Item(BaseModel):
    external_urls: ExternalUrls
    followers: Followers
    genres: list[str]
    href: str
    id: str
    images: list[Image]
    name: str
    popularity: int
    type: str
    uri: str


class TopItems(BaseModel):
    href: str
    limit: int
    next: str | None
    offset: int
    previous: str | None
    total: int
    items: list[Item]


class Cursor(BaseModel):
    after: str
    before: str


class Artists(BaseModel):
    href: str
    limit: int
    next: str
    cursors: Cursor
    total: int
    items: list[Item]


class FollowedArtists(BaseModel):
    artists: Artists
