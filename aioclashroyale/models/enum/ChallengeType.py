from enum import Enum


class ChallengeType(Enum):
    SINGLE_CHALLENGE: str = "singleChallenge"
    CHAIN_CHALLENGE: str = "chainChallenge"