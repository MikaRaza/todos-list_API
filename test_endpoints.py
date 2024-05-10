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
    
def test_get_todo_by_id(api_url):
    task_id = "5SQj9wWVu8EQdqbeSqgP"
    response = requests.get(f"{api_url}/todos/{task_id}")
    assert response.status_code == 200