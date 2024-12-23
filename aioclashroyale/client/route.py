from typing import Any, Final, List

from aioclashroyale.types import NonRequiredParam, ParamList

__all__ = (
    'Route',
)


class Route:
    __slots__ = ('path_template', '_compiled_no_args')

    BASE_URL: Final[str] = 'https://api.clashroyale.com/v1'

    def __init__(self, path_template: str) -> None:
        self._compiled_no_args: str = self.BASE_URL + path_template

    async def compile(self, *required_params: Any, **non_required_params: Any) -> str:
        if required_params:
            self._compiled_no_args = self._compiled_no_args.format(*required_params)

        if non_required_params:
            non_required_params: ParamList[NonRequiredParam] = await self.__format_non_required_args(
                **non_required_params
            )

            for param in non_required_params:
                self._compiled_no_args += param

        return self._compiled_no_args

    @staticmethod
    async def __format_non_required_args(**non_required_args: Any) -> ParamList[NonRequiredParam]:
        async def to_camel_case(key: str) -> str:
            parts: List[str] = key.split('_')
            return parts[0] + ''.join(part.capitalize() for part in parts[1:])

        return ParamList(
            *[
                NonRequiredParam(
                    key=await to_camel_case(k),
                    value=v
                )
                for k, v in non_required_args.items() if v is not None
            ]
        )
