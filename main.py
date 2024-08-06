import os
from audio_utils import extract_audio_from_youtube_video, extract_youtube_id
from convert_audio_to_text import recognize_speech
from database_utils import add_summary_to_database, get_summary_from_database
from text_summarizer import get_summary
from config import Config

VIDEO_URL = input('Paste YouTube link: ')
OUTPUT_PATH = '/Users/carolinakelkel/Save-time-on/'
IS_SHORT_SUMMARY = False

try:
    Config.validate_environment_variables()
except ValueError as e:
    print(f"Configuration error: {e}")
    exit(1)

youtube_id = extract_youtube_id(VIDEO_URL)

summary = get_summary_from_database(youtube_id)

if summary is None:
    audio_path = extract_audio_from_youtube_video(url=VIDEO_URL, output_path=OUTPUT_PATH)

    raw_text = recognize_speech(audio_path)

    os.remove(audio_path)

    summary = get_summary(input_text=raw_text, short=IS_SHORT_SUMMARY)

    add_summary_to_database(youtube_id=youtube_id, summary=summary)

print(summary)