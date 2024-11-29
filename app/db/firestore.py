"""Database module for Firestore."""

import os

from google.cloud import firestore

from app.config.settings import BASE_DIR


db = firestore.Client.from_service_account_json(
    os.path.join(BASE_DIR, "firestore.json")
)
