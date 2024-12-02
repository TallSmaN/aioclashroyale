from typing import Any, Final

__all__ = ("Route",)

class Route:
    __slots__ = ('path_template', '_compiled_no_args')

    BASE_URL: Final[str] = 'https://api.clashroyale.com/v1'

    def __init__(self, path_template: str) -> None:
        self._compiled_no_args: str = self.BASE_URL + path_template


    async def compile(self, **kwargs: Any) -> str:
        if kwargs:
            return self._compiled_no_args.format(**kwargs)

        return self._compiled_no_args
