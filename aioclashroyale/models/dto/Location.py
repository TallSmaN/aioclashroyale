from msgspec import Struct


class Location(Struct, rename='camel'):
    localized_name: str = None
    id: int = None
    name: str = None
    is_country: bool = None
    country_code: str = None