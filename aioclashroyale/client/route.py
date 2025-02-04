from typing import Final

from aioclashroyale.types import NonRequiredParam, ParamList

__all__ = (
    'Route',
)


class Route:
    __slots__ = ('__endpoint_template',)

    BASE_URL: Final[str] = 'https://api.clashroyale.com/v1'

    def __init__(self, endpoint_template: str) -> None:
        self.__endpoint_template: str = endpoint_template

    async def build_url(self, *required_params: str | int, **optional_params: str | int) -> str:
        url: str = self.BASE_URL + self.__endpoint_template

        if required_params:
            url = url.format(*map(lambda s: s if isinstance(s, int) else s.replace('#', '%23'), required_params))

        if optional_params:
            optional_params: ParamList[NonRequiredParam] = await self.__format_non_required_args(
                **optional_params
            )

            for param in optional_params:
               url += param

        return url

    async def __format_non_required_args(self, **non_required_args: any) -> ParamList[NonRequiredParam]:
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
        parts: list[str] = key.split('_')
        return parts[0] + ''.join(part.capitalize() for part in parts[1:])

