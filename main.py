import os
from openai import OpenAI
from config import Config
from audio_utils import extract_audio_from_youtube_video
from convert_audio_to_text import recognise_speech
from text_summariser import summarise
from logger import logger
from re import compile

TEMP_DIR = '/tmp'
YOUTUBE_REGEX = compile(r'^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$')


def is_youtube_url(url: str) -> bool:
    """
    Checks if the provided URL is a valid YouTube link.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if it's a YouTube URL, False otherwise.
    """

    return bool(YOUTUBE_REGEX.match(url))


def get_video_url_from_user() -> str:
    """
    Prompts the user to enter a YouTube video URL.

    Returns:
        str: The entered URL.
    """

    return input('Enter YouTube video URL: ')


def main() -> None:
    try:
        config = Config()
        client = OpenAI(api_key=config.openai_api_key)

        video_url = get_video_url_from_user()
        if not is_youtube_url(video_url):
            logger.error(f'{video_url} is not a valid YouTube link.')
            print('Error: Please enter a valid YouTube video URL.')

            return

        os.makedirs(TEMP_DIR, exist_ok=True)

        logger.info('Starting YouTube summarisation process.')
        audio_path = extract_audio_from_youtube_video(url=video_url,
                                                      output_path=TEMP_DIR,
                                                      ffmpeg_path=config.ffmpeg_path)
        logger.info('Audio extracted successfully.')

        raw_text = recognise_speech(audio_path)
        logger.info('Transcription completed.')

        os.remove(audio_path)

        summary = summarise(raw_text, client)
        logger.info(f'Summary generated')

        print(f'\n{summary}\n')
    except Exception as e:
        logger.error(f'Error occurred: {e}')
        print(f'\nError occurred: {e}')

if __name__ == '__main__':
    main()