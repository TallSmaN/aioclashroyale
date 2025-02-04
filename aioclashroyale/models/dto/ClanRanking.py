from msgspec import Struct

from aioclashroyale.models.dto.Location import Location


class ClanRanking(Struct, rename='camel'):
    clan_scrore: int = None
    badge_id: int = None
    location: Location = None
    members: int = None
    tag: str = None
    name: str = None
    rank: int = None
    previous_rank: int = None
    badge_urls: list[str] = None