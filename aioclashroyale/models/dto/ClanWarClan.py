from msgspec import Struct

class ClanWarClan(Struct, rename='camel'):
    tag: str = None
    clan_score: int = None
    crowns: int = None
    badge_id: int = None
    name: str = None
    participants: int = None
    battles_played: int = None
    wins: int = None
