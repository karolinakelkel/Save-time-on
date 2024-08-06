import firebase_admin
import os
from dotenv import load_dotenv
from firebase_admin import credentials, db, initialize_app
from typing import Optional

load_dotenv()

FIREBASE_DB_CONFIG_PATH = os.getenv('FIREBASE_DB_CONFIG_PATH')
FIREBASE_DB_URL = os.getenv('FIREBASE_DB_URL')
FIREBASE_DB_NODE = 'summaries'


def connect_to_db() -> None:
    try:
        if not firebase_admin._apps:
            credential = credentials.Certificate(FIREBASE_DB_CONFIG_PATH)
            initialize_app(credential, {'databaseURL': FIREBASE_DB_URL})
    except Exception as e:
        print(f'Error while connecting to database: {e}')


def get_summary_from_database(youtube_id: str) -> Optional[str]:
    connect_to_db()
    try:
        ref = db.reference(f'{FIREBASE_DB_NODE}/{youtube_id}')
        return ref.get()
    except Exception as e:
        print(f"Error while getting summary from database: {e}")
    return None


def add_summary_to_database(*, youtube_id: str, summary: str) -> None:
    connect_to_db()
    try:
        ref = db.reference(FIREBASE_DB_NODE)
        ref.update({youtube_id: summary})
    except Exception as e:
        print(f'Error while adding summary to database: {e}')
