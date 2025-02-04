from enum import Enum


class TournamentType(Enum):
    OPEN: str = 'open'
    PASSWORD_PROTECTED: str = 'passwordProtected'
    UNKNOWN: str = 'unknown'