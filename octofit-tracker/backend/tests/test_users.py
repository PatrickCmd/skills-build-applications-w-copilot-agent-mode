import pytest
from rest_framework.test import APIClient

@pytest.fixture
def client():
    return APIClient()

def test_get_users_empty(client):
    response = client.get('/api/users/')
    assert response.status_code == 200
    assert isinstance(response.data, list)
    assert len(response.data) == 0

def test_create_user(client):
    user = {"email": "test@example.com", "name": "Test User", "password": "pass123"}
    response = client.post('/api/users/', user, format='json')
    assert response.status_code == 201
    assert response.data["email"] == user["email"]
    assert response.data["name"] == user["name"]
    # Password should not be returned
    assert "password" not in response.data

def test_create_duplicate_user(client):
    user = {"email": "dupe@example.com", "name": "Dupe User", "password": "pass123"}
    client.post('/api/users/', user, format='json')
    response = client.post('/api/users/', user, format='json')
    assert response.status_code == 400
