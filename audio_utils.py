import os
import re
import uuid
from datetime import datetime
from typing import Optional
from yt_dlp import YoutubeDL

DATE_FORMAT = '%d-%m-%Y_%H-%M-%S'
YOUTUBE_ID_REGEX = re.compile(r'(?<=e/|d/|v/|v=)([A-Za-z\d]+)')
AUDIO_FORMAT = 'bestaudio'
AUDIO_CODEC = 'wav'
AUDIO_QUALITY = '192'


def generate_unique_file_name() -> str:
    timestamp = datetime.now().strftime(DATE_FORMAT)
    unique_id = uuid.uuid4().hex

    return f'{timestamp}_{unique_id}'


def create_path(*, path: str, file_name: str) -> str:
    return os.path.join(path, file_name)


def extract_audio_from_youtube_video(*, url: str, output_path: str) -> str:
    try:
        unique_file_name = generate_unique_file_name()
        temp_file_path = create_path(path=output_path, file_name=f'{unique_file_name}.webm')
        final_wav_file_path = create_path(path=output_path, file_name=f'{unique_file_name}.wav')

        youtubedl_options = {'format': AUDIO_FORMAT,
                             'outtmpl': temp_file_path,
                             'postprocessors': [{'key': 'FFmpegExtractAudio',
                                                 'preferredcodec': AUDIO_CODEC,
                                                 'preferredquality': AUDIO_QUALITY}]}

        with YoutubeDL(youtubedl_options) as ydl:
            ydl.extract_info(url, download=True)

        return final_wav_file_path
    except Exception as initial_exception:
        raise ValueError('Failed to extract information from video') from initial_exception


def extract_youtube_id(url: str) -> Optional[str]:
    match = YOUTUBE_ID_REGEX.search(url)

    return match.group() if match else None
