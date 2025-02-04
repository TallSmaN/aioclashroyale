from enum import Enum


class TournamentStatus(Enum):
    IN_PREPARATION: str = 'inPreparation'
    IN_PROGRESS: str = 'inProgress'
    ENDED: str = 'ended'
    UNKNOWN: str = 'unknown'