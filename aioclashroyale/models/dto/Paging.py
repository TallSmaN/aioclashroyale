from msgspec import Struct

from aioclashroyale.models.dto.Cursors import Cursors


class Paging(Struct, rename='camel'):
    cursors: Cursors