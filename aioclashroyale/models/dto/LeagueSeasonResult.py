from msgspec import Struct


class LeagueSeasonResult(Struct, rename='camel'):
    trophies: int = None
    rank: int = None
    best_trophies: int = None
    id: str = None

