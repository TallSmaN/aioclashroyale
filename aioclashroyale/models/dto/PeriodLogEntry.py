from msgspec import Struct

from aioclashroyale.models.dto.PeriodLogEntryClan import PeriodLogEntryClan


class PeriodLogEntry(Struct, rename='camel'):
    clan: PeriodLogEntryClan = None
    points_earned: int = None
    progress_start_of_day: int = None
    progress_end_of_day: int = None
    end_of_day_rank: int = None
    progress_earned: int = None
    num_of_defenses_remaining: int = None
    progress_earned_from_defenses: int = None