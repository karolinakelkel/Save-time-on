import os
import uuid
from datetime import datetime
from dotenv import load_dotenv
from logger import logger
from yt_dlp import YoutubeDL

load_dotenv()

DATE_FORMAT = '%d-%m-%Y_%H-%M-%S'
AUDIO_FORMAT = 'bestaudio'
AUDIO_CODEC = 'wav'
AUDIO_QUALITY = '192'
FFMPEG_POSTPROCESSOR_KEY = 'FFmpegExtractAudio'
FFMPEG_PATH = os.getenv('FFMPEG_PATH')


def generate_unique_file_name() -> str:
    timestamp = datetime.now().strftime(DATE_FORMAT)
    unique_id = uuid.uuid4().hex

    return f'{timestamp}_{unique_id}'


def create_path(*, path: str, file_name: str) -> str:
    return os.path.join(path, file_name)


def extract_audio_from_youtube_video(*, url: str, output_path: str) -> str:
    try:
        unique_file_name = generate_unique_file_name()
        final_wav_file_path = create_path(path=output_path, file_name=f'{unique_file_name}.wav')

        youtubedl_options = {'format': AUDIO_FORMAT,
                             'outtmpl': create_path(path=output_path, file_name=f'{unique_file_name}.%(ext)s'),
                             'postprocessors': [{'key': FFMPEG_POSTPROCESSOR_KEY,
                                                 'preferredcodec': AUDIO_CODEC,
                                                 'preferredquality': AUDIO_QUALITY}],
                             'ffmpeg_location': FFMPEG_PATH}

        with YoutubeDL(youtubedl_options) as ydl:
            ydl.extract_info(url, download=True)

        logger.info(f"Audio successfully extracted and saved to: {final_wav_file_path}")

        return final_wav_file_path
    except Exception as e:
        logger.error(f"Failed to extract audio: {e}")

        raise ValueError(f'Failed to extract information from video: {e}')
