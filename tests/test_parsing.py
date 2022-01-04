from aiohttp import payload
import pytest
import aiohttp
from aioresponses import aioresponses

from hhs_vertretungsplan_parser.const import BASE_URL, LOGIN_URL
from hhs_vertretungsplan_parser.vertretungsplan_parser import HHSVertretungsplanParser
from hhs_vertretungsplan_parser.model.vertretung import Vertretung

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
    assert len(hhs.vertretungen) == 18