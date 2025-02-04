from msgspec import Struct

from aioclashroyale.models.dto.IconUrls import IconUrls


class Arena(Struct, rename='camel'):
    name: str = None
    id: int = None
    icon_urls: IconUrls = None