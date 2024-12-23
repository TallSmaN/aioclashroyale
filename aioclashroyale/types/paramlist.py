from typing import TypeVar, Generic, Generator, Sequence
from aioclashroyale.types import NonRequiredParam

__all__ = (
    'ParamList',
)

T = TypeVar('T', bound=NonRequiredParam)


class ParamList(Generic[T]):
    def __init__(self, *args: T) -> None:
        self.args: Sequence[T] = args

    def __iter__(self) -> Generator:
        for index, item in enumerate(self.args):
            prefix: str = '?' if index == 0 else '&'
            yield f'{prefix}{item.key}={item.value}'

    def __repr__(self) -> str:
        return "<{}: params_count={!r}>".format(
            self.__class__.__name__,
            len(self.args),
        )
