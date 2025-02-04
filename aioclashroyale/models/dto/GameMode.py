from msgspec import Struct


class GameMode(Struct, rename='camel'):
    id: int = None
    name: str = None