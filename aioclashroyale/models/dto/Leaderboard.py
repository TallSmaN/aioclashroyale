from msgspec import Struct


class Leaderboard(Struct, rename='camel'):
    name: str = None
    id: int = None
