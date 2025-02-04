from typing import Optional

from msgspec import Struct

from aioclashroyale.models.dto.Item import Item
from aioclashroyale.models.enum.PlayerItemLevelRarity import PlayerItemLevelRarity
from aioclashroyale.models.enum.SurvivalMilestoneRewardResource import SurvivalMilestoneRewardResource
from aioclashroyale.models.enum.SurvivalMilestoneRewardType import SurvivalMilestoneRewardType


class SurvivalMilestoneReward(Struct, rename='camel'):
    rarity: PlayerItemLevelRarity = None
    chest: str = None
    resource: SurvivalMilestoneRewardResource = None
    type: Optional[SurvivalMilestoneRewardType] = None
    amount: int = None
    card: Item = None
    consumable_name: str = None
    wins: int = None
