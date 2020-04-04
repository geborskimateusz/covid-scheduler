import firebase_admin
from firebase_admin import credentials, firestore
import google.cloud.exceptions

cred, db = None, None


def init_firebase():
    try:
        global cred, db
        cred = credentials.Certificate("./covid-email-notifier-firebase-adminsdk-vrr9h-3c7d66f9b8.json")
        firebase_admin.initialize_app(cred)
        db = firestore.client()
    except google.cloud.exceptions.ServerError:
        print(u'Something went wrong when initializing database')


def get_sender_email():
    try:
        return db.collection(u'emails').document(u'sender').get()
    except google.cloud.exceptions.NotFound:
        print(u'Something went wrong when obtaining sender email')


init_firebase()
get_sender_email()
