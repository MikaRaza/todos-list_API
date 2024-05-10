import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def get_firestore_client():
    cred = credentials.Certificate("credentials.json")
    firebase_admin.initialize_app(cred)
    return firestore.client()
