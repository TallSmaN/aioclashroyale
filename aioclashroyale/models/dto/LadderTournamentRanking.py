from msgspec import Struct

from aioclashroyale.models.dto.PlayerRankingClan import PlayerRankingClan


class LadderTournamentRanking(Struct, rename='camel'):
    clan: PlayerRankingClan = None
    wins: int = None
    losses: int = None
    tag: str = None
    name: str = None
    rank: int = None
    previous_rank: int = None