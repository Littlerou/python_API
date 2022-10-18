import pytest
import app
from controllers import shows

@pytest.fixture
def api(monkeypatch):
    test_shows = [
    {'id': 1, 'name': 'Game Of Thrones', 'seasons': 8},
    {'id': 2, 'name': 'House Of The Dragon', 'seasons' : 1},
    {'id': 3, 'name': 'The Boys', 'seasons': 3},
    {'id': 4, 'name': 'Breaking Bad', 'seasons' : 5},
    {'id': 5, 'name': 'Mr Robot', 'seasons' : 4}
    ]
    monkeypatch.setattr(shows, "shows", test_shows)
    api = app.app.test_client()
    return api
