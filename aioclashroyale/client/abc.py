from abc import ABC, abstractmethod
from typing import Any, Self

__all__ = ("ABCClient",)


class ABCClient(ABC):

    @abstractmethod
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        ...

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
            self,
            exc_type: type[BaseException],
            exc_val: Any,
            exc_tb: Any,
    ) -> None:
        ...
