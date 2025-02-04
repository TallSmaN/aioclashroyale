from msgspec import Struct

from aioclashroyale.models.dto.ClanWarParticipant import ClanWarParticipant
from aioclashroyale.models.dto.ClanWarStanding import ClanWarStanding


class ClanWarLog(Struct, rename='camel'):
    standings: list[ClanWarStanding] = None
    season_id: int = None
    participants: list[ClanWarParticipant] = None
    created_date: str = None
