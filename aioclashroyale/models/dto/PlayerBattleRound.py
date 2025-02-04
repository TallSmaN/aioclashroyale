from msgspec import Struct

from aioclashroyale.models.dto.PlayerItemLevel import PlayerItemLevel


class PlayerBattleRound(Struct, rename='camel'):
    elixir_leaked: float = None
    cards: list[PlayerItemLevel] = None
    crowns: int = None
    king_tower_hit_points: int = None
    princess_tower_hit_points: list[int] = None
