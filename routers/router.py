from fastapi import APIRouter, HTTPException
from classes.database1 import get_firestore_client
from classes.schemas import TodoCreate, TodoUpdate

router = APIRouter()

@router.get("/todos/")
async def read_todos():
    db = get_firestore_client()
    todos = db.collection(u'todos').stream()
    return [todo.to_dict() for todo in todos]

@router.post("/todos/")
async def create_todo(todo: TodoCreate):
    db = get_firestore_client()
    doc_ref = db.collection(u'todos').document()
    doc_ref.set(todo.dict())
    return {"id": doc_ref.id, **todo.dict()}


