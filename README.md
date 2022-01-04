# hhs-vertretungsplan
Python parser for the Heinrich-Hertz-Schule, Hamburg, Vertretungsplan interface

Retrieves latest status of classes being substituted.

Usage:

```python
import aiohttp
import asyncio
from hhs_vertretungsplan_parser.vertretungsplan_parser import HHSVertretungsplanParser

async def main():
    async with aiohttp.ClientSession() as session:
        hhs = HHSVertretungsplanParser(session, user, password)
        await hhs.load_data()
        print(f"Vertretungsplan={hhs}")


if (__name__ == '__main__'):
    asyncio.run(main())
```
