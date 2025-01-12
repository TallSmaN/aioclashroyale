from typing import Optional

import msgspec.json
from aiohttp import ClientSession
from msgspec import Struct

from aioclashroyale.client import Token

__all__ = (
    'AiohttpClient',
)


class AiohttpClient:
    __slots__ = ('session', '__headers')

    def __init__(self, token: Token) -> None:
        self.session: Optional[ClientSession] = None
        self.__headers: dict = {'Authorization': f'Bearer {token}'}

    async def new_request[T: Struct](self, url: str, obj: type[T]) -> T:
        if not self.session:
            self.session = ClientSession()

        async with self.session.get(url=url, headers=self.__headers) as response:
            print(await response.json())
            if response.status != 200:
                raise Exception(response.status)

            return msgspec.json.decode(msgspec.json.encode(await response.json()), type=obj)
