from typing import Optional

from msgspec import Struct


class GameMode(Struct):
    id: int
    name: str = None