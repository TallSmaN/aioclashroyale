from typing import Optional

from aiohttp import ClientSession, ClientTimeout
from msgspec import Struct
from msgspec.json import decode

from aioclashroyale.client import Token
from aioclashroyale.exceptions import EXCEPTION_MAP

__all__ = (
    'AiohttpClient',
)


class AiohttpClient:
    __slots__ = ('session', 'timeout', '__headers')

    def __init__(self, token: Token, timeout: ClientTimeout = None, pretty_errors: bool = True) -> None:
        self.session: Optional[ClientSession] = None
        self.timeout: ClientTimeout = timeout
        self.__headers: dict = {'Authorization': f'Bearer {token}'}

        if pretty_errors:
            import pretty_errors

    async def new_request[T: Struct | list[Struct]](self, url: str, dto: type[T]) -> T:
        if not self.session:
            self.session = ClientSession(timeout=self.timeout)

        async with self.session.get(url=url, headers=self.__headers) as response:
            if response.status != 200:
                raise EXCEPTION_MAP[response.status](decode(await response.read()))

            return decode(await response.read(), type=dto)
