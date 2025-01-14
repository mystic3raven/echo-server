import pytest
from server import app

@pytest.fixture
def client():
    # Set up a test client for the Flask app
    with app.test_client() as client:
        yield client

def test_echo_json(client):
    """Test the /echo endpoint with JSON input."""
    response = client.post('/echo', json={"message": "Hello, Flask!"})
    assert response.status_code == 200
    data = response.get_json()
    assert "timestamp" in data
    assert data["echo"] == {"message": "Hello, Flask!"}

def test_echo_plain_text(client):
    """Test the /echo endpoint with plain text input."""
    response = client.post('/echo', data="Hello, Plain Text!", content_type="text/plain")
    assert response.status_code == 200
    data = response.get_json()
    assert "timestamp" in data
    assert data["echo"] == "Hello, Plain Text!"

def test_no_data(client):
    """Test the /echo endpoint with no data sent."""
    response = client.post('/echo')
    assert response.status_code == 200
    data = response.get_json()
    assert "timestamp" in data
    assert data["echo"] == "No data sent"
