import aiohttp
import asyncio
import sys
from hhs_vertretungsplan_parser.vertretungsplan_parser import HHSVertretungsplanParser

async def main(user: str, password: str):
    async with aiohttp.ClientSession() as session:
        hhs = HHSVertretungsplanParser(session, user, password)
        await hhs.load_data()
        for vertretung in hhs.vertretungen:
            print(f"Klasse {vertretung.klasse} hat am {vertretung.datum} in Stunde {vertretung.stunde} im Fach {vertretung.fach} bei {vertretung.vertreter} Vertretung.")

if (__name__ == '__main__'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main(sys.argv[0], sys.argv[1]))