from typing import Generator

__all__ = (
    'NonRequiredParam',
)


class NonRequiredParam:
    __slots__ = ('key', 'value')

    def __init__(self, key: str, value: str | int) -> None:
        self.key: str = key
        self.value: str | int = value

    @property
    async def get_value(self) -> str | int:
        return self.value

    @property
    async def get_key(self) -> str:
        return self.key

    def __iter__(self) -> Generator:
        yield self.key, self.value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, NonRequiredParam):
            return False

        return self.key == other.key and self.value == other.value

    def __repr__(self) -> str:
        return '<{}: key={!r}, value={!r}>'.format(
            self.__class__.__name__,
            self.key,
            self.value,
        )
