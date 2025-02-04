from msgspec import Struct

from aioclashroyale.models.dto.RiverRaceStanding import RiverRaceStanding


class RiverRaceLog(Struct, rename='camel'):
    standings: list[RiverRaceStanding] = None
    season_id: int = None
    created_date: str = None
    section_index: int = None