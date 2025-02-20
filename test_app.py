import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200

def test_video(client):
    response = client.get("/videos/sample.mp4")  # Ensure this file exists
    assert response.status_code == 200
