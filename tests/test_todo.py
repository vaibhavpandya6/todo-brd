from todo import Todo
from database import SessionLocal, engine

def test_todo_model():
    todo = Todo(title="New Todo")
    assert todo.title == "New Todo"

def test_todo_crud():
    db = SessionLocal()
    try:
        # Create a todo
        todo = Todo(title="New Todo")
        db.add(todo)
        db.commit()
        db.refresh(todo)

        # Read the todo
        todo_from_db = db.query(Todo).filter(Todo.id == todo.id).first()
        assert todo_from_db.title == "New Todo"

        # Update the todo
        todo.title = "Updated Todo"
        db.commit()
        db.refresh(todo)

        # Delete the todo
        db.delete(todo)
        db.commit()
    finally:
        db.close()