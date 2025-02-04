from enum import Enum


class CurrentRiverRaceState(Enum):
    CLAN_NOT_FOUND: str = 'clanNotFound'
    ACCESS_DENIED: str = 'accessDenied'
    MATCHMAKING: str = 'matchmaking'
    MATCHED: str = 'matched'
    FULL: str = 'full'
    ENDED: str = 'ended'