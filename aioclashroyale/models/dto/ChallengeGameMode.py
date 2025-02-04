from msgspec import Struct


class ChallengeGameMode(Struct, rename='camel'):
    id: int = None
    name: str = None