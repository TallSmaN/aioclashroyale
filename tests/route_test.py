import asyncio

from aioclashroyale import AioClashRoyale
from aioclashroyale.client import Token

# from tests.profiler import async_pyinstrument_profile

acr: AioClashRoyale = AioClashRoyale(token=Token.from_env(env_file='tests/.env', key='CLASH_ROYALE_TOKEN'))


# @async_pyinstrument_profile
async def main():
    a = await acr.get_tournaments(name="Apex-Army")

    for i in a.items:
        print(i)


asyncio.run(main())