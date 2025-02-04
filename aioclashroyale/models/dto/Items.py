from msgspec import Struct

from aioclashroyale.models.dto.Item import Item


class Items(Struct, rename='camel'):
    items: list[Item] = None
    support_items: list[Item] = None