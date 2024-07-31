import os
import psycopg2
import re
from dotenv import load_dotenv

URL = 'https://www.youtube.com/watch?v=B0VeKPwUY0c&t=1s'
SUMMARY = 'Исследование показывает, что при отмене антидепрессантов от 26 до 60% пациентов испытывают синдром отмены, ' \
          'однако значительная часть испытывают его и при отмене плацебо. Это подчеркивает важность постепенного ' \
          'снижения дозировки и грамотного подхода к лечению. Врачи должны учитывать эту информацию, ' \
          'чтобы предотвратить дискомфорт у пациентов. '


def extract_youtube_id(url: str) -> str:
    regex = re.compile(r'(?<=e/|v=|d/|v/)([A-Za-z\d]+)')
    match = regex.search(url)
    return match.group() if match else None


def connect_to_db():
    try:
        load_dotenv()
        connection = psycopg2.connect(dbname=os.getenv('DB_NAME'),
                                      user=os.getenv('DB_USER'),
                                      password=os.getenv('DB_PASSWORD'),
                                      host=os.getenv('DB_HOST'),
                                      port=os.getenv('DB_PORT'))

        return connection
    except Exception as e:
        print(f'Database Connection Error: {e}')

        return None


def add_summary(youtube_id, summary):
    connection = connect_to_db()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO summaries (video_id, summary) 
                                  VALUES (%s, %s) 
                                  ON CONFLICT (video_id) DO NOTHING""", (youtube_id, summary))
                connection.commit()
        except Exception as e:
            print(f'Error while adding summary: {e}')
        finally:
            connection.close()


video_id = extract_youtube_id(URL)
add_summary(video_id, SUMMARY)
















# # Функция для получения саммари по YouTube ID
# def get_summary(youtube_id):
#     conn = connect_to_db()
#     if conn:
#         try:
#             with conn.cursor() as cursor:
#                 cursor.execute(
#                     sql.SQL("SELECT summary FROM summaries WHERE youtube_id = %s"),
#                     [youtube_id]
#                 )
#                 result = cursor.fetchone()
#                 if result:
#                     return result[0]
#                 else:
#                     return None
#         except Exception as e:
#             print(f"Ошибка получения саммари: {e}")
#         finally:
#             conn.close()
#
# # Пример использования функций
# youtube_id = "B0VeKPwUY0c"
# summary = "This is a generated summary for the video."
#
# # Проверка наличия саммари в базе данных
# existing_summary = get_summary(youtube_id)
# if existing_summary:
#     print(f"Саммари для видео {youtube_id}: {existing_summary}")
# else:
#     print(f"Саммари для видео {youtube_id} не найдено, добавляем новое.")
#     add_summary(youtube_id, summary)
#
#
