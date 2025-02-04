from msgspec import Struct

from aioclashroyale.models.dto.PeriodLogEntry import PeriodLogEntry


class PeriodLog(Struct, rename='camel'):
    items: list[PeriodLogEntry] = None
    period_index: int = None