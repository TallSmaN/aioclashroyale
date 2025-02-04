from enum import Enum

class ClanRole(Enum):
    NOT_MEMBER: str = 'notMember'
    MEMBER: str = 'member'
    LEADER: str = 'leader'
    ADMIN: str = 'admin'
    COLEADER: str = 'coLeader'
    ELDER: str = 'elder'