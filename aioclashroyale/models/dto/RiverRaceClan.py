from msgspec import Struct

from aioclashroyale.models.dto.RiverRaceParticipant import RiverRaceParticipant


class RiverRaceClan(Struct, rename='camel'):
    tag: str = None
    clan_score: int = None
    badge_id: int = None
    name: str = None
    fame: int = None
    repair_points: int = None
    finish_time: str = None
    participants: list[RiverRaceParticipant] = None
    period_points: int = None


