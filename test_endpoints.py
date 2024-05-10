import pytest
import requests

@pytest.fixture
def api_url():
    return "http://localhost:8000"

def test_get_todos(api_url):
    response = requests.get(f"{api_url}/todos")
    assert response.status_code == 200
    
def test_create_todo(api_url):
    todo_data = {"title": "Pytest", "completed": False}
    response = requests.post(f"{api_url}/todos", json=todo_data)
    assert response.status_code == 200