from msgspec import Struct
from typing import Optional

from aioclashroyale.models.dto.PlayerBattleRound import PlayerBattleRound
from aioclashroyale.models.dto.PlayerClan import PlayerClan
from aioclashroyale.models.dto.PlayerItemLevel import PlayerItemLevel


class PlayerBattleData(Struct, rename='camel'):
    elixir_leaked: float = None
    global_rank: Optional[int] = None
    clan: PlayerClan = None
    cards: list[PlayerItemLevel] = None
    support_cards: list[PlayerItemLevel] = None
    rounds: list[PlayerBattleRound] = None
    crowns: int = None
    princess_tower_hit_points: list[int] = None
    tag: str = None
    name: str = None
    starting_trophies: int = None
    trophy_change: int = None
    king_tower_hit_points: int = None

