from typing import TypeVar, Generic, Generator, Sequence
from aioclashroyale.types import NonRequiredParam

__all__ = (
    'ParamList',
)

T = TypeVar('T', bound=NonRequiredParam)


class ParamList(Generic[T]):
    __slots__ = ('params',)

    def __init__(self, *params: T) -> None:
        self.params: Sequence[T] = params

    def __iter__(self) -> Generator:
        for index, param in enumerate(self.params):
            prefix: str = '?' if index == 0 else '&'
            yield f'{prefix}{param.key}={param.value}'

    def __repr__(self) -> str:
        return '<{}: params_count={!r}>'.format(
            self.__class__.__name__,
            len(self.params),
        )
