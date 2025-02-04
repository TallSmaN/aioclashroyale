from msgspec import Struct
from typing import Optional


class PathOfLegendSeasonResult(Struct, rename='camel'):
    trophies: int = None
    league_number: int = None
    rank: Optional[int] = None