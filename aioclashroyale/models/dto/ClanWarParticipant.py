from msgspec import Struct

class ClanWarParticipant(Struct, rename='camel'):
    tag: str = None
    name: str = None
    cards_earned: int = None
    battles_played: int = None
    wins: int = None
    collection_day_battles_played: int = None
    number_of_battles: int = None