from main import app
from fastapi.testclient import TestClient
from todo import Todo
from database import SessionLocal, engine

client = TestClient(app)

def test_create_todo():
    response = client.post("/todos", json={"title": "New Todo"})
    assert response.status_code == 200
    assert response.json()["title"] == "New Todo"

def test_update_todo():
    # Create a todo
    response = client.post("/todos", json={"title": "New Todo"})
    todo_id = response.json()["id"]

    # Update the todo
    response = client.patch(f"/todos/{todo_id}", json={"title": "Updated Todo"})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Todo"

def test_delete_todo():
    # Create a todo
    response = client.post("/todos", json={"title": "New Todo"})
    todo_id = response.json()["id"]

    # Delete the todo
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 200

def test_get_todos():
    # Create multiple todos
    client.post("/todos", json={"title": "New Todo 1"})
    client.post("/todos", json={"title": "New Todo 2"})

    # Get all todos
    response = client.get("/todos")
    assert response.status_code == 200
    assert len(response.json()) == 2

# Test database connection
def test_database_connection():
    db = SessionLocal()
    try:
        db.execute("SELECT 1")
    finally:
        db.close()