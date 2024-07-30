import os
from yt_dlp import YoutubeDL
from datetime import datetime
import uuid


def generate_unique_file_name() -> str:
    timestamp = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
    unique_id = uuid.uuid4().hex
    return f'{timestamp}_{unique_id}'


def create_path(path: str, file_name: str) -> str:
    return os.path.join(path, file_name)


def extract_audio_from_youtube_video(url: str, output_path: str) -> str:
    try:
        unique_file_name = generate_unique_file_name()
        temp_file_path = create_path(output_path, f'{unique_file_name}.webm')
        final_wav_file_path = create_path(output_path, f'{unique_file_name}.wav')

        youtubedl_options = {'format': 'bestaudio',
                             'outtmpl': temp_file_path,
                             'postprocessors': [{'key': 'FFmpegExtractAudio',
                                                 'preferredcodec': 'wav',
                                                 'preferredquality': '192'}]}

        with YoutubeDL(youtubedl_options) as ydl:
            ydl.extract_info(url, download=True)

        return final_wav_file_path
    except Exception as initial_exception:
        raise ValueError('Failed to extract information from video') from initial_exception


output_path = '/Users/carolinakelkel/Save-time-on'
wav_file_path = extract_audio_from_youtube_video('https://www.youtube.com/watch?v=05cVgDJRW_U', output_path)
