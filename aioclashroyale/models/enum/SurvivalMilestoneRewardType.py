from enum import Enum

class SurvivalMilestoneRewardType(Enum):
    NONE: str = 'none'
    CARD_STACK: str = 'cardStack'
    CHEST: str = 'chest'
    CARD_STACK_RANDOM: str = 'cardStackRandom'
    RESOURCE: str = 'resource'
    TRADE_TOKEN: str = 'tradeToken'
    CONSUMABLE: str = 'consumable'