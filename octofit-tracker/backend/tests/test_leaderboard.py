import pytest
from rest_framework.test import APIClient

@pytest.fixture
def client():
    return APIClient()

def test_get_leaderboard_empty(client):
    response = client.get('/api/leaderboard/')
    assert response.status_code == 200
    assert isinstance(response.data, list)
    assert len(response.data) == 0
