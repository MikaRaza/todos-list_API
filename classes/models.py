from pydantic import BaseModel

class Todo(BaseModel):
    id: str
    title: str
    completed: bool
