import asyncio

from aioclashroyale import AioClashRoyale
from aioclashroyale.client import Token
from tests.profiler import async_pyinstrument_profile

acr: AioClashRoyale = AioClashRoyale(token=Token.from_env(env_file='tests/.env', key='CLASH_ROYALE_TOKEN'))



@async_pyinstrument_profile
async def main():
    await acr.get_clans_clan_warlog(clan_tag='%239PV2RJ00', limit=1)


asyncio.run(main())
