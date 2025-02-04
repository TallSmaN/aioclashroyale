from enum import Enum


class ClanType(Enum):
    OPEN: str = 'open'
    INVITE_ONLY: str = 'inviteOnly'
    CLOSED: str = 'closed'