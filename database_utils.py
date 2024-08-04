import psycopg2
from psycopg2.extensions import connection as Connection
from typing import Optional
from config import Config

DB_CONNECTION_PARAMS = {'dbname': Config.DB_NAME,
                        'user': Config.DB_USER,
                        'password': Config.DB_PASSWORD,
                        'host': Config.DB_HOST,
                        'port': Config.DB_PORT}
SELECT_SUMMARY_SQL_QUERY = """SELECT summary 
                              FROM summaries 
                              WHERE video_id = %s"""
INSERT_SUMMARY_SQL_QUERY = """INSERT INTO summaries (video_id, summary) 
                              VALUES (%s, %s) 
                              ON CONFLICT (video_id) DO NOTHING"""


def connect_to_db() -> Optional[Connection]:
    try:
        connection = psycopg2.connect(**DB_CONNECTION_PARAMS)
        return connection
    except Exception as e:
        print(f'Error while connecting to database: {e}')
    return None


def get_summary_from_database(youtube_id: str) -> Optional[str]:
    connection = connect_to_db()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute(SELECT_SUMMARY_SQL_QUERY, (youtube_id,))
                result = cursor.fetchone()
                if result:
                    return result[0]
        except Exception as e:
            print(f"Error while getting summary from database: {e}")
        finally:
            connection.close()
    return None


def add_summary_to_database(*, youtube_id: str, summary: str) -> None:
    connection = connect_to_db()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute(INSERT_SUMMARY_SQL_QUERY, (youtube_id, summary))
                connection.commit()
        except Exception as e:
            print(f'Error while adding summary to database: {e}')
        finally:
            connection.close()
    return None
