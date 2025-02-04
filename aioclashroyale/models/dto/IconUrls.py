from msgspec import Struct


class IconUrls(Struct, rename='camel'):
    large: str = None
    medium: str = None
    evolution_medium: str = None