import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def get_firestore_client():
    if not firebase_admin._apps:
        cred = credentials.Certificate("credentials.json")
        firebase_admin.initialize_app(cred, name="todo-lists")
    return firestore.client(app=firebase_admin.get_app(name="todo-lists"))