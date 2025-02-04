from msgspec import Struct

from aioclashroyale.models.dto.IconUrls import IconUrls


class Chest(Struct, rename='camel'):
    name: str = None
    index: int = None
    icon_urls: IconUrls = None
