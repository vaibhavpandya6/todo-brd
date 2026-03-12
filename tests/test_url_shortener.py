import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_shorten_url(client):
    response = client.post(
        "/shorten",
        json={"original_url": "https://example.com"}
    )
    assert response.status_code == 200
    assert "short_url" in response.json()

def test_short_url_redirect(client):
    # assuming the shortened url is http://localhost/abc123
    response = client.post(
        "/shorten",
        json={"original_url": "https://example.com"}
    )
    short_url = response.json()["short_url"]
    short_code = short_url.split("/")[-1]
    response = client.get(f"/{short_code}")
    assert response.status_code == 301
    assert response.headers.get("location") == "https://example.com"

def test_short_url_invalid(client):
    response = client.get("/invalid")
    assert response.status_code == 404

def test_shorten_url_invalid_json(client):
    response = client.post("/shorten", json={"invalid": "field"})
    assert response.status_code == 422

def test_shorten_url_empty(client):
    response = client.post("/shorten", json={})
    assert response.status_code == 422