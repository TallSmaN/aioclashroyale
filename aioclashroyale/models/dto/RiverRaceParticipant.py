from msgspec import Struct

class RiverRaceParticipant(Struct, rename='camel'):
    tag: str = None
    name: str = None
    fame: int = None
    repair_points: int = None
    boat_attacks: int = None
    decks_used: int = None
    decks_used_today: int = None
