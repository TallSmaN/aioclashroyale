from msgspec import Struct

from aioclashroyale.models.dto.RiverRaceClan import RiverRaceClan


class RiverRaceStanding(Struct, rename='camel'):
    rank: int = None
    trophy_change: int = None
    clan: RiverRaceClan = None