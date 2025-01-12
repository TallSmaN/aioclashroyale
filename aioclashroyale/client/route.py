from typing import Any, Final, List
from urllib.parse import urlencode
from aioclashroyale.types import NonRequiredParam, ParamList

__all__ = (
    'Route',
)


class Route:
    __slots__ = ('__compiled_url',)

    BASE_URL: Final[str] = 'https://api.clashroyale.com/v1'

    def __init__(self, endpoint_template: str) -> None:
        self.__compiled_url: str = self.BASE_URL + endpoint_template

    async def build_url(self, *required_params: Any, **optional_params: Any) -> str:
        if required_params:
            self.__compiled_url = self.__compiled_url.format(*required_params)

        if optional_params:
            optional_params: ParamList[NonRequiredParam] = await self.__format_non_required_args(
                **optional_params
            )

            for param in optional_params:
                self.__compiled_url += param

        return self.__compiled_url

    @property
    async def compiled_url(self) -> str:
        return self.__compiled_url

    async def __format_non_required_args(self, **non_required_args: Any) -> ParamList[NonRequiredParam]:
        return ParamList(
            *[
                NonRequiredParam(
                    key=await self.__to_camel_case(k),
                    value=v
                )
                for k, v in non_required_args.items() if v is not None
            ]
        )

    @staticmethod
    async def __to_camel_case(key: str) -> str:
        parts: List[str] = key.split('_')
        return parts[0] + ''.join(part.capitalize() for part in parts[1:])

