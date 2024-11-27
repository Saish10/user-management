"""Database module for Firestore."""

import os
from pathlib import Path
from google.cloud import firestore


BASE_DIR = Path(__file__).resolve().parent.parent.parent

db = firestore.Client.from_service_account_json(
    os.path.join(BASE_DIR, "firestore.json")
)
