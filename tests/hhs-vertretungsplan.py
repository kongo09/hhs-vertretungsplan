import aiohttp
import asyncio
import sys
from hhs_vertretungsplan_parser.vertretungsplan_parser import HHSVertretungsplanParser

async def main(user: str, password: str):
    async with aiohttp.ClientSession() as session:
        hhs = HHSVertretungsplanParser(session, user, password)
        await hhs.load_data()
        print(f"Daten vom {hhs.status}")
        for vertretung in hhs.vertretungen:
            print(f"Klasse {vertretung.klasse} hat am {vertretung.datum} in Stunde {vertretung.stunde} im Fach {vertretung.fach} bei {vertretung.vertreter} Vertretung. Hinweise: {vertretung.text} / {vertretung.nach}")

if (__name__ == '__main__'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    if len(sys.argv) == 3:
        asyncio.run(main(sys.argv[1], sys.argv[2]))
    else:
        print(f"usage: python hhs-vertretungsplan.py <user> <password>")