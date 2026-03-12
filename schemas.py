from pydantic import BaseModel
from typing import List

class TodoRequest(BaseModel):
    title: str

class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool
    created_at: str

class TodoListResponse(BaseModel):
    todos: List[TodoResponse]