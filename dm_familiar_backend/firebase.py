import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

db.collection('persons').add({'name':'John', 'age':'40'})