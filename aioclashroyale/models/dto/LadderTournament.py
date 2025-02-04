from msgspec import Struct

from aioclashroyale.models.dto.GameMode import GameMode
from aioclashroyale.models.dto.SurvivalMilestoneReward import SurvivalMilestoneReward


class LadderTournament(Struct, rename='camel'):
    game_mode: GameMode = None
    free_tier_rewards: list[SurvivalMilestoneReward] = None
    max_losses: int = None
    min_exp_level: int = None
    tournament_level: int = None
    milestone_rewards: list[SurvivalMilestoneReward] = None
    tag: str = None
    title: str = None
    start_time: str = None
    end_time: str = None
    top_rank_reward: list[SurvivalMilestoneReward] = None
    max_top_reward_rank: int = None