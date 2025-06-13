import pytest
from rest_framework.test import APIClient

@pytest.fixture
def client():
    return APIClient()

def test_get_workouts_empty(client):
    response = client.get('/api/workouts/')
    assert response.status_code == 200
    assert isinstance(response.data, list)
    assert len(response.data) == 0

def test_create_workout(client):
    workout = {"name": "Pushups", "description": "Do 20 pushups", "difficulty": "easy"}
    response = client.post('/api/workouts/', workout, format='json')
    assert response.status_code == 201
    assert response.data["name"] == workout["name"]
    assert response.data["description"] == workout["description"]
    assert response.data["difficulty"] == workout["difficulty"]
