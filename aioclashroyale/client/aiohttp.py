from typing import Any, Optional, Dict

from aiohttp import ClientSession

from aioclashroyale.client import Token

__all__ = (
    'AiohttpClient',
)

class AiohttpClient:
    __slots__ = ('session', '__headers')

    def __init__(self, token: Token) -> None:
        self.session: Optional[ClientSession] = None
        self.__headers: Dict = {'Authorization': f'Bearer {token}'}

        print(self.__headers)

    async def request_raw(self, url: str) -> Any:
        if not self.session:
            self.session = ClientSession()

        async with self.session.get(url=url, headers=self.__headers) as response:
            a = await response.json()
            print(a)
            return await response.json()

    async def request_json(self, url: str) -> Any:
        return await self.request_raw(url=url)
