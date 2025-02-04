from msgspec import Struct

from aioclashroyale.models.dto.File import File


class FingerPrint(Struct, rename='camel'):
    sha: str = None
    version: str = None
    files: list[File] = None