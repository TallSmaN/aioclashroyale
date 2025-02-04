from msgspec import Struct

from aioclashroyale.models.dto.PeriodLog import PeriodLog
from aioclashroyale.models.dto.RiverRaceClan import RiverRaceClan
from aioclashroyale.models.enum.CurrentRiverRaceState import CurrentRiverRaceState
from aioclashroyale.models.enum.PeriodType import PeriodType


class CurrentRiverRace(Struct, rename='camel'):
    state: CurrentRiverRaceState = None
    clan: RiverRaceClan = None
    clans: list[RiverRaceClan] = None
    collection_end_time: str = None
    war_end_time: str = None
    section_index: int = None
    period_index: int = None
    period_type: PeriodType = None
    period_logs: list[PeriodLog] = None
