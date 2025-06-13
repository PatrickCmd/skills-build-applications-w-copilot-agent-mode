import pytest
from rest_framework.test import APIClient

@pytest.fixture
def client():
    return APIClient()

def test_get_teams_empty(client):
    response = client.get('/api/teams/')
    assert response.status_code == 200
    assert isinstance(response.data, list)
    assert len(response.data) == 0

def test_create_team(client):
    team = {"name": "Team A", "members": ["test@example.com"]}
    response = client.post('/api/teams/', team, format='json')
    assert response.status_code == 201
    assert response.data["name"] == team["name"]
    assert response.data["members"] == team["members"]
