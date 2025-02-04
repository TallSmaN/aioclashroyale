from msgspec import Struct

from aioclashroyale.models.dto.Challenge import Challenge
from aioclashroyale.models.enum.ChallengeType import ChallengeType


class ChallengeChain(Struct, rename='camel'):
    title: str = None
    type: ChallengeType = None
    start_time: str = None
    end_time: str = None
    challanges: list[Challenge] = None