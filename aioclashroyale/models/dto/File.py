from msgspec import Struct


class File(Struct, rename='camel'):
    file: str = None
    sha: str = None
