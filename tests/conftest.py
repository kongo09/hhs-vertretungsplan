import pytest

@pytest.fixture()
def response_OnlineVertretungsplan_loggedout():
    with open("tests/fixtures/response_OnlineVertretungsplan_loggedout.php", "r", encoding='utf-8') as mock_response:
        return mock_response.read()

@pytest.fixture()
def response_OnlineVertretungsplan_loggedin():
    with open("tests/fixtures/response_OnlineVertretungsplan_loggedin.php", "r", encoding='utf-8') as mock_response:
        return mock_response.read()

@pytest.fixture()
def response_subst001():
    with open("tests/fixtures/response_subst001.htm", "r", encoding='utf-8') as mock_response:
        return mock_response.read()

@pytest.fixture()
def response_subst002():
    with open("tests/fixtures/response_subst002.htm", "r", encoding='utf-8') as mock_response:
        return mock_response.read()

@pytest.fixture()
def response_subst003():
    with open("tests/fixtures/response_subst003.htm", "r") as mock_response:
        return mock_response.read()
