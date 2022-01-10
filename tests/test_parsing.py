from dataclasses import dataclass
from typing import Any
import pytest
import aiohttp
from aioresponses import aioresponses

from hhs_vertretungsplan_parser.const import BASE_URL, LOGIN_URL, KEY_ALLE
from hhs_vertretungsplan_parser.vertretungsplan_parser import HHSVertretungsplanParser

SUBST001_URL = BASE_URL + "vertretungsplan/subst_001.htm"
SUBST002_URL = BASE_URL + "vertretungsplan/subst_002.htm"
SUBST003_URL = BASE_URL + "vertretungsplan/subst_003.htm"

@pytest.mark.asyncio
async def test_parsing_with_fake_data(
    response_OnlineVertretungsplan_loggedout,
    response_OnlineVertretungsplan_loggedin,
    response_subst001,
    response_subst002,
    response_subst003
):
    """Test parsing with fake data loaded from fixture response files."""
    async with aiohttp.ClientSession() as session:
        with aioresponses() as mocked:
            mocked.get(LOGIN_URL, status=200, body=response_OnlineVertretungsplan_loggedout)
            mocked.post(LOGIN_URL, status=200, body=response_OnlineVertretungsplan_loggedin)
            mocked.get(SUBST001_URL, status=200, body=response_subst001)
            mocked.get(SUBST002_URL, status=200, body=response_subst002)
            mocked.get(SUBST003_URL, status=200, body=response_subst003)

            hhs = HHSVertretungsplanParser(session, "fakeuser", "fakepassword")
            await hhs.load_data()

            _validate_vertretung(hhs)

def _validate_vertretung(hhs: HHSVertretungsplanParser) -> None:
    """Validate Vertretung against fixture."""
    assert len(hhs.vertretungen) == 106
    assert hhs.status == "2022-01-10T07:17:00+01:00"

    """Pick one class to check details."""
    _6d_list = list(filter(lambda vertretung: vertretung.klasse == '6d', hhs.vertretungen))
    first_6d = _6d_list[0]
    assert first_6d.klasse == "6d"
    assert first_6d.stunde == "1"
    assert first_6d.vertreter == "Lor"
    assert first_6d.fach == "Sopäd DB"
    assert first_6d.raum == "A109"
    assert first_6d.nach == ""
    assert first_6d.text == ""
    assert first_6d.datum == "2022-01-10T00:00:00+01:00"

    """Check for Jahrgang."""
    total_6 = '6' + KEY_ALLE
    assert 1 == len(list(filter(lambda vertretung: vertretung.klasse == total_6, hhs.vertretungen)))

    """Check for Alle Klassen."""
    assert 1 == len(list(filter(lambda vertretung: vertretung.klasse == KEY_ALLE, hhs.vertretungen)))

