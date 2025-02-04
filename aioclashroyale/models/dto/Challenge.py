from msgspec import Struct

from aioclashroyale.models.dto.ChallengeGameMode import ChallengeGameMode
from aioclashroyale.models.dto.SurvivalMilestoneReward import SurvivalMilestoneReward


class Challenge(Struct, rename='camel'):
    name: str = None
    description: str = None
    id: int = None
    win_mode: str = None
    casual: bool = None
    max_losses: int = None
    max_wins: int = None
    icon_url: str = None
    game_mode: ChallengeGameMode = None
    prizes: list[SurvivalMilestoneReward] = None
