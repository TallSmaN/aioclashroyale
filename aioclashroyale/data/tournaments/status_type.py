from enum import Enum


class StatusType(Enum):
    IN_PREPARATION = "inPreparation"
    IN_PROGRESS = "inProgress"
    ENDED = "ended"
    UNKNOWN = "unknown"

