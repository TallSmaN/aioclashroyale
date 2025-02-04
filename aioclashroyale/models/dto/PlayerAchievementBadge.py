from msgspec import Struct

from aioclashroyale.models.dto.IconUrls import IconUrls


class PlayerAchievementBadge(Struct, rename='camel'):
    icon_urls: IconUrls = None
    max_level: int = None
    progress: int = None
    level: int = None
    target: int = None
    name: str = None
