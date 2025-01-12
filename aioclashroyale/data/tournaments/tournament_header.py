from msgspec import Struct

from . import GameMode, PrivacyType, StatusType


class TournamentHeader(Struct):
    status: StatusType
    preparationDuration: int
    createdTime: str
    firstPlaceCardPrize: int
    gameMode: GameMode
    type: PrivacyType
    duration: int
    tag: str
    creatorTag: str
    name: str
    description: str
    capacity: int
    maxCapacity: int
    levelCap: int



class TournamentHeaderList(Struct):
    items: list[TournamentHeader]