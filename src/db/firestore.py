from google.cloud import firestore
from google.cloud.firestore_v1.base_query import FieldFilter


class model:
    def __init__(self):
        self.db = firestore.Client(database="huehunt-db")

    def get_user(self, user_id: str) -> dict | None:
        doc = self.db.collection("users").document(user_id).get()
        return doc.to_dict() if doc.exists else None

    def get_user_by_email(self, email: str) -> tuple[str, dict] | None:
        """Returns (user_id, data) or None."""
        docs = list(
            self.db.collection("users")
            .where(filter=FieldFilter("email", "==", email))
            .limit(1)
            .stream()
        )
        if docs:
            return docs[0].id, docs[0].to_dict()
        return None

    def upsert_user(self, user_id: str, data: dict) -> None:
        self.db.collection("users").document(user_id).set(data, merge=True)
