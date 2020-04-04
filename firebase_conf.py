import firebase_admin
from firebase_admin import credentials, firestore
import google.cloud.exceptions

cred, db = None, None


def init_firebase():
    try:
        global cred, db
        cred = credentials.Certificate("./covid-email-notifier-firebase-adminsdk-vrr9h-3c7d66f9b8.json")

        print("Initializing Firebase connection")
        firebase_admin.initialize_app(cred)

        print("Obtaining Firebase client")
        db = firestore.client()
    except google.cloud.exceptions.ServerError:
        print(u'Something went wrong when initializing database')


def get_receiver_emails():
    try:
        print("Fetching receiver addresses")
        return db.collection(u'emails').document(u'receivers').get().to_dict().get('emails')
    except google.cloud.exceptions.NotFound:
        print(u'Something went wrong when obtaining sender email')
