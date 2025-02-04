from msgspec import Struct

class PlayerClan(Struct, rename='camel'):
    badge_id: int = None
    tag: str = None
    name: str = None
    badge_urls: list[str] = None
