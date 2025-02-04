from msgspec import Struct

from aioclashroyale.models.dto.ClanWarClan import ClanWarClan


class ClanWarStanding(Struct, rename='camel'):
    trophy_change: int = None
    clan: ClanWarClan = None

