import os
import uuid
from datetime import datetime
from yt_dlp import YoutubeDL
from logger import logger

DATE_FORMAT = '%d-%m-%Y_%H-%M-%S'
AUDIO_FORMAT = 'bestaudio'
AUDIO_CODEC = 'wav'
AUDIO_QUALITY = '192'
FFMPEG_POSTPROCESSOR_KEY = 'FFmpegExtractAudio'


def generate_unique_file_name() -> str:
    """
    Generates a unique filename based on the current datetime and a random UUID.

    Returns:
        str: A unique string in the format 'DD-MM-YYYY_HH-MM-SS_UUID'.
    """

    timestamp = datetime.now().strftime(DATE_FORMAT)
    unique_id = uuid.uuid4().hex

    return f'{timestamp}_{unique_id}'


def create_path(*, path: str, file_name: str) -> str:
    """
    Joins a directory path and a filename into a full file path.

    Args:
        path (str): The directory path.
        file_name (str): The name of the file.

    Returns:
        str: The combined file path.
    """

    return os.path.join(path, file_name)


def extract_audio_from_youtube_video(*, url: str, output_path: str, ffmpeg_path: str) -> str:
    """
    Downloads and extracts audio from a YouTube video using yt_dlp and FFmpeg.

    Args:
        url (str): The URL of the YouTube video.
        output_path (str): Directory where the audio file will be saved.
        ffmpeg_path (str): Path to the ffmpeg binary.

    Returns:
        str: Full path to the extracted .wav audio file.

    Raises:
        ValueError: If extraction or download fails.
    """

    unique_file_name = generate_unique_file_name()
    final_wav_file_path = create_path(path=output_path, file_name=f'{unique_file_name}.wav')

    try:
        youtubedl_options = {'format': AUDIO_FORMAT,
                             'outtmpl': create_path(path=output_path, file_name=f'{unique_file_name}.%(ext)s'),
                             'postprocessors': [{'key': FFMPEG_POSTPROCESSOR_KEY,
                                                 'preferredcodec': AUDIO_CODEC,
                                                 'preferredquality': AUDIO_QUALITY}],
                             'ffmpeg_location': ffmpeg_path}

        with YoutubeDL(youtubedl_options) as ydl:
            ydl.extract_info(url, download=True)
        logger.info(f'Audio successfully extracted and saved to: {final_wav_file_path}')

        return final_wav_file_path
    except Exception as e:
        logger.error(f'Failed to extract audio from {url} to {final_wav_file_path}: {e}')

        raise ValueError(f'Failed to extract information from video: {e}')
