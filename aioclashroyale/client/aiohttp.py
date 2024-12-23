from typing import Any, Dict

from aiohttp import ClientSession, ClientTimeout

from . import Route
from .abc import ABCClient


class AiohttpClient(ABCClient):
    def __init__(
        self,
        session: ClientSession | None = None,
        timeout: ClientTimeout | None = None,
        **session_params: Any,
    ) -> None:
        self.session = session
        self.session_params = session_params
        self.timeout = timeout or ClientTimeout(total=0)


    async def request_raw(self, route: Route, data: Dict[str, Any]) -> Any:
        ...


