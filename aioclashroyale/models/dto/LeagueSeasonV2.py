from msgspec import Struct


class LeagueSeasonV2(Struct, rename='camel'):
    code: str = None
    unique_id: str = None
    end_time: str = None