from msgspec import Struct

from aioclashroyale.models.dto.Chest import Chest


class UpcomingChests(Struct, rename='camel'):
    items: list[Chest] = None