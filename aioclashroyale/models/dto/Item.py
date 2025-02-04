from typing import Optional

from msgspec import Struct

from aioclashroyale.models.dto.IconUrls import IconUrls
from aioclashroyale.models.enum.PlayerItemLevelRarity import PlayerItemLevelRarity


class Item(Struct, rename='camel'):
    icon_urls: IconUrls = None
    name: Optional[str] = None
    id: int = None
    rarity: Optional[PlayerItemLevelRarity] = None
    max_level: int = None
    elixir_cost: int = None
    max_evolution_level: int = None
