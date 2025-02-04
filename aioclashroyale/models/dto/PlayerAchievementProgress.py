from msgspec import Struct


class PlayerAchievementProgress(Struct, rename='camel'):
    stars: int = None
    value: int = None
    name: str = None
    target: int = None
    info: str = None
    completion_info: str = None