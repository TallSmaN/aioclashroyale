from msgspec import Struct

from aioclashroyale.models.dto.PlayerClan import PlayerClan


class TournamentMember(Struct, rename='camel'):
    clan: PlayerClan = None
    rank: int = None
    previous_rank: int = None
    tag: str = None
    name: str = None
    score: int = None