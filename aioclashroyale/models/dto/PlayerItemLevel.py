from msgspec import Struct

from aioclashroyale.models.dto.IconUrls import IconUrls
from aioclashroyale.models.enum.PlayerItemLevelRarity import PlayerItemLevelRarity


class PlayerItemLevel(Struct, rename='camel'):
    id: int = None
    rarity: PlayerItemLevelRarity = None
    count: int = None
    level: int = None
    star_level: int = None
    evolution_level: int = None
    used: bool = None
    name: str = None
    max_level: int = None
    elixir_cost: int = None
    max_evolution_level: int = None
    icon_urls: IconUrls = None