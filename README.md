<img src="https://raw.githubusercontent.com/TallSmaN/aioclashroyale/master/.github/assets/logo.png"  width="200px" height="188px" align="right"></img>

# AioClashRoyale

---
[![Python](https://img.shields.io/badge/Python-^3.12-E26C66.svg)](https://www.python.org) 
[![License](https://img.shields.io/github/license/TallSmaN/aioclashroyale?color=E26C66)](LICENSE) 
![Last Commit](https://img.shields.io/github/last-commit/TallSmaN/aioclashroyale?color=E26C66)
![GitHub Release](https://img.shields.io/github/v/release/TallSmaN/aioclashroyale?color=E26C66)

--- 

Clash Royale API Wrapper

### Example usage
```python
from aioclashroyale import AioClashRoyale
from aioclashroyale.client import Token
from asyncio import run


acr: AioClashRoyale = AioClashRoyale(token=Token.from_env(env_file='.env', key='CLASH_ROYALE_TOKEN'))


async def main() -> None:
    await acr.get_player(player_tag='#2YLRGVVC')

    
if __name__ == '__main__':
    run(main())
```

### How to setup?

#### Pip
```bash
pip install aioclashroyale	
```

#### Poetry
```bash
poetry add aioclashroyale	
```
