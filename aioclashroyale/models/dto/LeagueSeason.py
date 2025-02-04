from msgspec import Struct
from typing import Optional


class LeagueSeason(Struct, rename='camel'):
    id: Optional[str] = None