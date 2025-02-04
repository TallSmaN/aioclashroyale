from msgspec import Struct

from aioclashroyale.models.dto.Arena import Arena
from aioclashroyale.models.dto.PlayerRankingClan import PlayerRankingClan


class PlayerRanking(Struct, rename='camel'):
    clan: PlayerRankingClan = None
    arena: Arena = None
    tag: str = None
    name: str = None
    exp_level: int = None
    rank: int = None
    previous_rank: int = None
    trophies: int = None