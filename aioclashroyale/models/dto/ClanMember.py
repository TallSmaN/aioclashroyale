from msgspec import Struct

from aioclashroyale.models.dto.Arena import Arena
from aioclashroyale.models.enum.ClanRole import ClanRole


class ClanMember(Struct, rename='camel'):
    clan_chest_points: int = None
    last_seen: str = None
    arena: Arena = None
    tag: str = None
    name: str = None
    role: ClanRole = None
    exp_level: int = None
    trophies: int = None
    clan_rank: int = None
    previous_clan_rank: int = None
    donations: int = None
    donations_received: int = None
