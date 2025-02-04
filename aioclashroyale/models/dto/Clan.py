from msgspec import Struct

from aioclashroyale.models.dto.ClanMember import ClanMember
from aioclashroyale.models.dto.Location import Location
from aioclashroyale.models.enum.ClanChestStatus import ClanChestStatus
from aioclashroyale.models.enum.ClanType import ClanType


class Clan(Struct, rename='camel'):
    member_list: list[ClanMember] = None
    tag: str = None
    badge_id: int = None
    clan_chest_status: ClanChestStatus = None
    clan_chest_level: int = None
    required_trophies: int = None
    donations_per_week: int = None
    clan_score: int = None
    clan_chest_max_level: int = None
    clan_war_trophies: int = None
    name: str = None
    location: Location = None
    type: ClanType = None
    members: int = None
    description: str = None
    clan_chest_points: int = None
    badge_urls: list[str] = None
