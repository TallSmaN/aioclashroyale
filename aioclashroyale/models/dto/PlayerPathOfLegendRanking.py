from msgspec import Struct

from aioclashroyale.models.dto.PlayerRankingClan import PlayerRankingClan


class PlayerPathOfLegendRanking(Struct, rename='camel'):
    clan: PlayerRankingClan = None
    tag: str = None
    name: str = None
    exp_level: int = None
    rank: int = None
    elo_rating: int = None