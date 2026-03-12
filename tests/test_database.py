import pytest
from database import get_db

def test_get_db():
    db = get_db()
    assert db is not None

def test_create_todo():
    db = get_db()
    todo = db.create_todo({"title": "New Todo"})
    assert todo["title"] == "New Todo"
    assert todo["completed"] is False

def test_get_todos():
    db = get_db()
    db.create_todo({"title": "New Todo 1"})
    db.create_todo({"title": "New Todo 2"})
    todos = db.get_todos()
    assert len(todos) == 2

def test_complete_todo():
    db = get_db()
    todo = db.create_todo({"title": "New Todo"})
    db.complete_todo(todo["id"])
    completed_todo = db.get_todo(todo["id"])
    assert completed_todo["completed"] is True

def test_delete_todo():
    db = get_db()
    todo = db.create_todo({"title": "New Todo"})
    db.delete_todo(todo["id"])
    assert db.get_todo(todo["id"]) is None