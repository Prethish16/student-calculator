import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index_page_load(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Student Calculator" in response.data

def test_calculation(client):
    response = client.post("/", data={"marks1": "80", "marks2": "90", "marks3": "70"})
    assert response.status_code == 200
    assert b"Total Marks: 240.0" in response.data
    assert b"Average Marks: 80.0" in response.data

def test_invalid_input(client):
    response = client.post("/", data={"marks1": "abc", "marks2": "90", "marks3": "70"})
    assert response.status_code == 200
    assert b"Invalid input" in response.data

def test_out_of_bounds_input(client):
    response = client.post("/", data={"marks1": "105", "marks2": "90", "marks3": "70"})
    assert response.status_code == 200
    assert b"Marks must be between 0 and 100" in response.data
