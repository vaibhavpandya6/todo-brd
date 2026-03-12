from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from todo import Todo
from database import SessionLocal

app = FastAPI()

# Define the request and response models
class TodoRequest(BaseModel):
    title: str

class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool
    created_at: str

# Setup database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Implement API endpoints
@app.post("/todos", response_model=TodoResponse)
def create_todo(todo_request: TodoRequest, db: SessionLocal = Depends(get_db)):
    todo = Todo(title=todo_request.title)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

@app.patch("/todos/{id}", response_model=TodoResponse)
def update_todo(id: int, todo_request: TodoRequest, db: SessionLocal = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo.title = todo_request.title
    db.commit()
    db.refresh(todo)
    return todo

@app.delete("/todos/{id}")
def delete_todo(id: int, db: SessionLocal = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted successfully"}

@app.get("/todos", response_model=List[TodoResponse])
def get_todos(db: SessionLocal = Depends(get_db)):
    todos = db.query(Todo).all()
    return todos

# Start the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)