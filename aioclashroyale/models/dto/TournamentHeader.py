from msgspec import Struct

from aioclashroyale.models.dto.GameMode import GameMode
from aioclashroyale.models.enum.TournamentStatus import TournamentStatus
from aioclashroyale.models.enum.TournamentType import TournamentType


class TournamentHeader(Struct, rename='camel'):
    status: TournamentStatus = None
    preparation_duration: int = None
    created_time: str = None
    first_place_card_prize: int = None
    game_mode: GameMode = None
    duration: int = None
    type: TournamentType = None
    tag: str = None
    creator_tag: str = None
    name: str = None
    description: str = None
    capacity: int = None
    max_capacity: int = None
    level_cap: int = None
