from msgspec import Struct

class Cursors(Struct, rename='camel'):
    after: str = None
    before: str = None
