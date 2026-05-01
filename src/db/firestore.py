from google.cloud import firestore

class model:
    def __init__(self):
        self.db = firestore.Client(database="huehunt")

    