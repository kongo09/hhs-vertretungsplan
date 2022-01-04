import datetime
import pytest
from hhs_vertretungsplan_parser.model.vertretung import Vertretung

@pytest.mark.asyncio
async def test_vertretung():
    vertretung = Vertretung()
    vertretung.datum = datetime.date(2021, 12, 22)
    vertretung.klasse = "5g"
    vertretung.stunde = "1 - 2"
    vertretung.vertreter = "Hz"
    vertretung.fach = "NW"
    vertretung.raum = "A201"
    vertretung.text = "--"
    vertretung.nach = "???"

    assert "Vertretung(Datum=2021-12-22, Klasse=5g, Stunde=1 - 2, Vertreter=Hz, Fach=NW, Raum=A201)" == vertretung.__str__()
    
