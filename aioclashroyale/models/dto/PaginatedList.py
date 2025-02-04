from msgspec import Struct

from aioclashroyale.models.dto.Paging import Paging


class PaginatedList[T: any](Struct, rename='camel'):
    items: list[T]
    paging: Paging = None
