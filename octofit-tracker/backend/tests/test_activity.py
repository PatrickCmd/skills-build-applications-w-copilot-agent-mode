import pytest
from rest_framework.test import APIClient
from datetime import datetime

@pytest.fixture
def client():
    return APIClient()

def test_get_activity_empty(client):
    response = client.get('/api/activity/')
    assert response.status_code == 200
    assert isinstance(response.data, list)
    assert len(response.data) == 0

def test_create_activity(client):
    activity = {
        "user_email": "test@example.com",
        "activity_type": "run",
        "duration": 30,
        "timestamp": datetime.now().isoformat()
    }
    response = client.post('/api/activity/', activity, format='json')
    assert response.status_code == 201
    assert response.data["user_email"] == activity["user_email"]
    assert response.data["activity_type"] == activity["activity_type"]
    assert response.data["duration"] == activity["duration"]
